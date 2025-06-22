#include <atcoder/all>
#include <bits/stdc++.h>

using namespace std;
using i64 = long long;
using u32 = uint32_t;

// --- rep マクロ（0‥n-1 ループ）---
#define rep(i, n) for (int i = 0; (i) < int(n); ++(i))

// --- デバッグ用マクロ（LOCAL 定義時のみ有効）---
#ifdef DEFINED_ONLY_IN_LOCAL
#include "cpp-dump.hpp"
#include <atcoder/modint>
namespace cpp_dump::_detail {
template <int m>
inline std::string
export_var(const atcoder::static_modint<m> &mint, const std::string &indent,
           std::size_t last_line_length, std::size_t current_depth,
           bool fail_on_newline, const export_command &command) {
    return export_var(mint.val(), indent, last_line_length, current_depth,
                      fail_on_newline, command);
}
template <int m>
inline std::string
export_var(const atcoder::dynamic_modint<m> &mint, const std::string &indent,
           std::size_t last_line_length, std::size_t current_depth,
           bool fail_on_newline, const export_command &command) {
    return export_var(mint.val(), indent, last_line_length, current_depth,
                      fail_on_newline, command);
}
} // namespace cpp_dump::_detail
#define dump(...) cpp_dump(__VA_ARGS__)
namespace cp = cpp_dump;
CPP_DUMP_SET_OPTION_GLOBAL(max_line_width, 80);
CPP_DUMP_SET_OPTION_GLOBAL(log_label_func, cp::log_label::filename());
CPP_DUMP_SET_OPTION_GLOBAL(enable_asterisk, true);
#else
#define dump(...)
#define CPP_DUMP_SET_OPTION(...)
#define CPP_DUMP_SET_OPTION_GLOBAL(...)
#define CPP_DUMP_DEFINE_EXPORT_OBJECT(...)
#define CPP_DUMP_DEFINE_EXPORT_ENUM(...)
#define CPP_DUMP_DEFINE_EXPORT_OBJECT_GENERIC(...)
#endif

// ──────────────────────────────
//   0. 乱数ユーティリティ（xorshift32）
// ──────────────────────────────
namespace rnd {
inline u32 xorshift32() {
    static u32 y = 2463534242u;
    y ^= y << 13;
    y ^= y >> 17;
    return y ^= y << 5;
}
inline int uniform_int(int l, int r) {
    return l + int(xorshift32() % u32(r - l + 1));
}
inline double uniform01() { return double(xorshift32()) / 4294967296.0; }
inline double uniform_real(double L, double R) {
    return L + (R - L) * uniform01();
}
} // namespace rnd

// ──────────────────────────────
//  1. 経過時間管理クラス
// ──────────────────────────────
class TimeKeeper {
    using Clock = chrono::high_resolution_clock;
    const Clock::time_point start;
    const double limit_ms; // 制限時間[ms]
    double now_ms = 0;     // 現在経過時間[ms]
  public:
    explicit TimeKeeper(double ms) : start(Clock::now()), limit_ms(ms) {}
    void update() {
        auto d = Clock::now() - start;
        now_ms = chrono::duration_cast<chrono::microseconds>(d).count() * 1e-3;
    }
    double now() const { return now_ms; }
    bool over() const { return now_ms >= limit_ms; }
};

constexpr int N = 20;
constexpr int MAX_TURN = N * N * N * 2;

// ──────────────────────────────
//  2. 入力
// ──────────────────────────────
struct Input {
    int n;
    array<array<int, N>, N> w;
    array<array<int, N>, N> d;
    void input() {
        cin >> n;
        rep(i, N) rep(j, N) cin >> w[i][j];
        rep(i, N) rep(j, N) cin >> d[i][j];
    }
};

// ──────────────────────────────
//  3. 箱束管理
// ──────────────────────────────
struct Boxes {
    int n = 0;
    vector<int> ws, ds;
    static int dis(int sx, int sy, int tx, int ty) {
        return abs(sx - tx) + abs(sy - ty);
    }

    bool can_add(int w, int d, int sx, int sy, int tx, int ty) {
        int sum = 0;
        int d1 = dis(sx, sy, tx, ty);
        int d2 = tx + ty;
        for (int i = n - 1; i >= 0; --i) {
            int need_d = d1 * sum + d2 * (sum + w);
            if (ds[i] <= need_d)
                return false;
            sum += ws[i];
        }
        return true;
    }
    void move(int cnt) {
        int sum = 0;
        for (int i = n - 1; i >= 0; --i) {
            ds[i] -= cnt * sum;
            sum += ws[i];
        }
    }
    void add(int w, int d) { ++n, ws.push_back(w), ds.push_back(d); }
    void clear() { n = 0, ws.clear(), ds.clear(); }
};

// ──────────────────────────────
//  4. ソルバー
// ──────────────────────────────
struct Solver {
    const Input &in;
    TimeKeeper &tk;
    vector<string> ans;

    Solver(const Input &input, TimeKeeper &tk_) : in(input), tk(tk_) {
        ans.reserve(MAX_TURN);
    }

    static int dis(int sx, int sy, int tx, int ty) {
        return abs(sx - tx) + abs(sy - ty);
    }

    static vector<string> get_route(int sx, int sy, int tx, int ty) {
        vector<string> res;
        res.reserve(dis(sx, sy, tx, ty));
        rep(_, sx - tx) res.emplace_back("U");
        rep(_, tx - sx) res.emplace_back("D");
        rep(_, sy - ty) res.emplace_back("L");
        rep(_, ty - sy) res.emplace_back("R");
        return res;
    }

    vector<pair<int, int>> make_init_order() const {
        vector<pair<int, int>> order;
        order.reserve(N * N);
        rep(i, N) rep(j, N) if (i || j) order.emplace_back(i, j);
        return order;
    }

    vector<string> make_ans(const vector<pair<int, int>> &order) const {
        Boxes boxes;
        int x = 0, y = 0, turn = 0;
        vector<string> out;
        out.reserve(MAX_TURN);
        for (auto [tx, ty] : order) {
            if (boxes.can_add(in.w[tx][ty], in.d[tx][ty], x, y, tx, ty)) {
                auto r = get_route(x, y, tx, ty);
                out.insert(out.end(), r.begin(), r.end());
                out.emplace_back("1");
                boxes.move(dis(x, y, tx, ty));
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += dis(x, y, tx, ty);
                tie(x, y) = tie(tx, ty);
            } else {
                auto r1 = get_route(x, y, 0, 0);
                out.insert(out.end(), r1.begin(), r1.end());
                auto r2 = get_route(0, 0, tx, ty);
                out.insert(out.end(), r2.begin(), r2.end());
                out.emplace_back("1");
                boxes.clear();
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += x + y + tx + ty;
                tie(x, y) = tie(tx, ty);
            }
        }
        auto r = get_route(x, y, 0, 0);
        out.insert(out.end(), r.begin(), r.end());
        if ((int)out.size() > MAX_TURN)
            out.resize(MAX_TURN);
        return out;
    }

    int evaluate(const vector<pair<int, int>> &order) const {
        static Boxes boxes;
        boxes.clear();
        int x = 0, y = 0, turn = 0;
        for (auto [tx, ty] : order) {
            if (boxes.can_add(in.w[tx][ty], in.d[tx][ty], x, y, tx, ty)) {
                boxes.move(dis(x, y, tx, ty));
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += dis(x, y, tx, ty);
            } else {
                boxes.clear();
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += x + y + tx + ty;
            }
            tie(x, y) = tie(tx, ty);
        }
        return turn + x + y;
    }

    // ---- 焼きなまし：time_limit_ms だけ回す ----
    vector<pair<int, int>> sa(vector<pair<int, int>> order,
                              double time_limit_ms) {
        tk.update();
        const double start = tk.now();

        int n = order.size();
        int curr_turn = evaluate(order);
        int best_turn = curr_turn;
        auto curr_order = order;
        auto best_order = curr_order;

        constexpr double T0 = 1.0, T1 = 1e-3;
        double temp = T0;

        while (true) {
            // 時間管理
            static int iter = 0;
            if ((iter++ & 15) == 0) {
                tk.update();
                double t = tk.now() - start;
                if (t >= time_limit_ms)
                    break;
                temp = T0 + (T1 - T0) * (t / time_limit_ms);
            }

            int mode = rnd::xorshift32() % 2; // 0:swap,1:insert
            int i = rnd::xorshift32() % n;
            int j = rnd::xorshift32() % n;
            if (i == j)
                continue;

            if (mode == 0) {
                swap(curr_order[i], curr_order[j]);
                int new_turn = evaluate(curr_order);
                int diff = curr_turn - new_turn;
                if (diff >= 0 || exp(double(diff) / temp) > rnd::uniform01()) {
                    curr_turn = new_turn;
                    if (new_turn < best_turn) {
                        best_turn = new_turn;
                        best_order = curr_order;
                    }
                } else
                    swap(curr_order[i], curr_order[j]);
            } else {
                auto tmp = curr_order[i];
                curr_order.erase(curr_order.begin() + i);
                curr_order.insert(curr_order.begin() + j, tmp);
                int new_turn = evaluate(curr_order);
                int diff = curr_turn - new_turn;
                if (diff >= 0 || exp(double(diff) / temp) > rnd::uniform01()) {
                    curr_turn = new_turn;
                    if (new_turn < best_turn) {
                        best_turn = new_turn;
                        best_order = curr_order;
                    }
                } else {
                    auto tmp2 = curr_order[j];
                    curr_order.erase(curr_order.begin() + j);
                    curr_order.insert(curr_order.begin() + i, tmp2);
                }
            }
        }
        return best_order;
    }

    // ---- 複数回 SA を走らせ最良を採用 ----
    void solve() {
        const int REP = 4;           // 試行回数
        const double ONE_MS = 450.0; // 1 回あたり 450ms

        const auto base = make_init_order();
        vector<pair<int, int>> best_order;
        int best_score = INT_MAX;

        for (int r = 0; r < REP; ++r) {
            // 初期順序をランダムシャッフル
            auto init = base;
            for (int i = init.size() - 1; i > 0; --i) {
                int j = rnd::xorshift32() % (i + 1);
                swap(init[i], init[j]);
            }

            auto order = sa(std::move(init), ONE_MS);
            int score = evaluate(order);
            if (score < best_score) {
                best_score = score;
                best_order = std::move(order);
            }
            tk.update();
            if (tk.over())
                break; // 時間切れ安全策
        }
        ans = make_ans(best_order);
    }

    void print() const {
        for (auto &c : ans)
            cout << c << '\n';
    }
};

// ──────────────────────────────
//  5. main
// ──────────────────────────────
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    TimeKeeper tk(1900.0); // 全体で 1.9 秒
    Input in;
    in.input();

    Solver solver(in, tk);
    solver.solve();
    solver.print();
    return 0;
}

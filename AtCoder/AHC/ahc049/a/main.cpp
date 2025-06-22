#include <atcoder/all>
#include <bits/stdc++.h>

using namespace std;
using i64 = long long;
using u32 = uint32_t;

//--- rep マクロ（0‥n-1 ループ）---
#define rep(i, n) for (int i = 0; (i) < int(n); ++(i))

//--- デバッグ用マクロ（LOCAL 定義時のみ有効）---
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
constexpr array<pair<int, int>, 4> dxy = {{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}};
vector<string> UDLR = {"U", "D", "L", "R"};
constexpr int N = 20;
constexpr int MAX_TURN = N * N * N * 2;
struct Input {
    int n;
    array<array<int, N>, N> w;
    array<array<int, N>, N> d;
    void input() {
        cin >> n;
        rep(i, N) {
            rep(j, N) { cin >> w[i][j]; }
        }
        rep(i, N) {
            rep(j, N) { cin >> d[i][j]; }
        }
    }
};
struct Boxes {
    int n = 0;
    vector<int> ws;
    vector<int> ds;
    int dis(int sx, int sy, int tx, int ty) {
        return abs(sx - tx) + abs(sy - ty);
    }
    bool can_add(int w, int d, int sx, int sy, int tx, int ty) {
        // (sx,sy) -> (tx,ty) -> (0,0)を達成可能か
        int sum = 0;
        int d1 = dis(sx, sy, tx, ty);
        int d2 = (tx + ty);
        for (int i = n - 1; i >= 0; i--) {
            int need_d = 0;
            need_d += d1 * sum;
            need_d += d2 * (sum + w);
            if (ds[i] <= need_d) {
                return false;
            }
            sum += ws[i];
        }
        return true;
    }
    void move(int cnt) {
        int sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            ds[i] -= cnt * sum;
            sum += ws[i];
        }
    }
    void add(int w, int d) {
        // box追加
        n++;
        ws.push_back(w);
        ds.push_back(d);
    }
    void clear() {
        n = 0;
        ws.clear();
        ds.clear();
    }
};
struct Solver {
    int dis(int sx, int sy, int tx, int ty) {
        return abs(sx - tx) + abs(sy - ty);
    }
    vector<string> get_route(int sx, int sy, int tx, int ty) {
        vector<string> res;
        res.reserve(dis(sx, sy, tx, ty));
        rep(i, sx - tx) { res.push_back("U"); }
        rep(i, tx - sx) { res.push_back("D"); }
        rep(i, sy - ty) { res.push_back("L"); }
        rep(i, ty - sy) { res.push_back("R"); }
        return res;
    }

    const Input in;
    TimeKeeper tk;
    vector<string> ans;
    Solver(const Input &input, TimeKeeper tk) : in(input), tk(tk) {
        ans.reserve(MAX_TURN);
    }

    vector<pair<int, int>> make_init_order() {
        vector<pair<int, int>> order;
        order.reserve(N * N);
        rep(i, N) {
            rep(j, N) {
                if (i == 0 and j == 0)
                    continue;
                order.push_back({i, j});
            }
        }
        return order;
    }
    vector<string> make_ans(const vector<pair<int, int>> &order) {
        Boxes boxes;
        int x = 0;
        int y = 0;
        int turn = 0;
        vector<string> ans;
        ans.reserve(MAX_TURN);
        for (auto &[tx, ty] : order) {
            if (boxes.can_add(in.w[tx][ty], in.d[tx][ty], x, y, tx, ty)) {
                auto tmp = get_route(x, y, tx, ty);
                for (auto c : tmp) {
                    ans.push_back(c);
                }
                ans.push_back("1");
                boxes.move(dis(x, y, tx, ty));
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += dis(x, y, tx, ty);
                x = tx;
                y = ty;
            } else {
                auto tmp = get_route(x, y, 0, 0);
                for (auto c : tmp) {
                    ans.push_back(c);
                }
                tmp = get_route(0, 0, tx, ty);
                for (auto c : tmp) {
                    ans.push_back(c);
                }
                ans.push_back("1");
                boxes.clear();
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += x + y + tx + ty;
                x = tx;
                y = ty;
            }
        }
        auto tmp = get_route(x, y, 0, 0);
        for (auto c : tmp) {
            ans.push_back(c);
        }
        rep(i, (int)ans.size() - MAX_TURN) { ans.pop_back(); }
        return ans;
    }
    int evaluate(const vector<pair<int, int>> &order) {
        static Boxes boxes;
        boxes.clear();
        int x = 0;
        int y = 0;
        int turn = 0;
        for (auto &[tx, ty] : order) {
            if (boxes.can_add(in.w[tx][ty], in.d[tx][ty], x, y, tx, ty)) {
                boxes.move(dis(x, y, tx, ty));
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += dis(x, y, tx, ty);
                x = tx;
                y = ty;
            } else {
                boxes.clear();
                boxes.add(in.w[tx][ty], in.d[tx][ty]);
                turn += x + y + tx + ty;
                x = tx;
                y = ty;
            }
        }
        turn += x + y;
        return turn;
    }
    vector<pair<int, int>> sa(const vector<pair<int, int>> &order) {
        int iter = 0;
        double T0 = 1;
        double T1 = 1e-3;
        tk.update();
        double temp = T0 + (T1 - T0) * (tk.now() / 1900.0);

        int min_turn = evaluate(order);
        int curr_turn = min_turn;
        vector<pair<int, int>> best_order = order;
        vector<pair<int, int>> curr_order = order;
        int n = (N * N) - 1;
        vector<int> modes = {0, 1, 2};
        int modes_size = modes.size();
        while (1) {
            if (iter % 10 == 0) {
                cerr << iter << " " << curr_turn << '\n';
                tk.update();
                if (tk.over()) {
                    break;
                }
                temp = T0 + (T1 - T0) * (tk.now() / 1900.0);
            }
            iter++;
            int mode = modes[rnd::xorshift32() % modes_size];
            if (mode == 0) {
                // スワップ
                int i = rnd::xorshift32() % n;
                int j = rnd::xorshift32() % n;
                if (i == j) {
                    continue;
                }
                swap(curr_order[i], curr_order[j]);
                int new_turn = evaluate(curr_order);
                int d = curr_turn - new_turn;
                if (d >= 0 or exp((double)d / temp) > rnd::uniform01()) {
                    curr_turn = new_turn;
                    if (new_turn < min_turn) {
                        min_turn = new_turn;
                        best_order = curr_order;
                    }
                } else {
                    swap(curr_order[i], curr_order[j]);
                }

            } else if (mode == 1) {
                // 挿入
                int i = rnd::xorshift32() % n;
                int j = rnd::xorshift32() % n;
                if (i == j) {
                    continue;
                }
                auto tmp = curr_order[i];
                curr_order.erase(curr_order.begin() + i);
                curr_order.insert(curr_order.begin() + j, tmp);
                int new_turn = evaluate(curr_order);
                int d = curr_turn - new_turn;
                if (d >= 0 or exp((double)d / temp) > rnd::uniform01()) {
                    curr_turn = new_turn;
                    if (new_turn < min_turn) {
                        min_turn = new_turn;
                        best_order = curr_order;
                    }
                } else {
                    auto tmp = curr_order[j];
                    curr_order.erase(curr_order.begin() + j);
                    curr_order.insert(curr_order.begin() + i, tmp);
                }
            } else if (mode == 2) {
                // 隣接スワップ
                int i = rnd::xorshift32() % (n - 1);
                int j = i + 1;
                swap(curr_order[i], curr_order[j]);
                int new_turn = evaluate(curr_order);
                int d = curr_turn - new_turn;
                if (d >= 0 or exp((double)d / temp) > rnd::uniform01()) {
                    curr_turn = new_turn;
                    if (new_turn < min_turn) {
                        min_turn = new_turn;
                        best_order = curr_order;
                    }
                } else {
                    swap(curr_order[i], curr_order[j]);
                }
            }
        }
        return best_order;
    }
    void solve() {
        // 運び出す順番を焼きなます
        // 操作2は使わない
        //  運び出す順に移動し，次の目標まで取りにいってから出入り口まで破壊せずに戻れるなら取りに行く．無理ならその時点で出入口まで引き返す．
        // 初期解は(0,1),(0,2)...(n-1,n-1)の順に運ぶとする
        // 近傍は二点スワップと挿入
        auto init_order = make_init_order();
        auto sa_order = sa(init_order);
        ans = make_ans(sa_order);
    }
    void print() const {
        for (auto c : ans) {
            cout << c << '\n';
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    TimeKeeper tk(1900);
    Input input;
    input.input();

    Solver solver(input, tk);
    solver.solve();
    solver.print();

    return 0;
}

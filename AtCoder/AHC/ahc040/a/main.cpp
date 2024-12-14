#include <bits/stdc++.h>
using namespace std;
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

inline uint32_t xorshift() {
    static uint32_t y = 2463534242;
    y = y ^ (y << 13);
    y = y ^ (y >> 17);
    return y = y ^ (y << 5);
}
// 時間をDouble型で管理し、経過時間も取り出せるクラス
class TimeKeeperDouble {
  private:
    std::chrono::high_resolution_clock::time_point start_time_;
    double now_time_ = 0;

  public:
    double time_threshold_;
    // 時間制限をミリ秒単位で指定してインスタンスをつくる。
    TimeKeeperDouble(const double time_threshold)
        : start_time_(std::chrono::high_resolution_clock::now()),
          time_threshold_(time_threshold) {}

    // 経過時間をnow_time_に格納する。
    void setNowTime() {
        auto diff =
            std::chrono::high_resolution_clock::now() - this->start_time_;
        this->now_time_ =
            std::chrono::duration_cast<std::chrono::microseconds>(diff)
                .count() *
            1e-3; // ms
    }

    // 経過時間をnow_time_に取得する。
    double getNowTime() const { return this->now_time_; }

    // インスタンス生成した時から指定した時間制限を超過したか判定する。
    bool isTimeOver() const { return now_time_ >= time_threshold_; }
};
TimeKeeperDouble time_keeper(2900);
struct Init {
    Init() {
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
} init;
#define ll long long
#define vi vector<int>
#define vl vector<long long>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define elif else if
#define rep(i, n) for (int i = 0; i < static_cast<int>(n); i++)
#define all(v) (v).begin(), (v).end()
#define rall(x) x.rbegin(), x.rend()
#define el '\n'
#define Yes cout << "Yes" << el
#define No cout << "No" << el
#define YES cout << "YES" << el
#define NO cout << "NO" << el

const double pi = 3.141592653589793238;
const int inf = 1073741823;
const ll infl = 1LL << 60;
const string ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string abc = "abcdefghijklmnopqrstuvwxyz";
const int MOD = 998244353;
const array<int, 8> dx = {0, 0, -1, 1, -1, -1, 1, 1};
const array<int, 8> dy = {-1, 1, 0, 0, -1, 1, -1, 1};
template <typename T1, typename T2> inline bool chmax(T1 &a, T2 b) {
    bool compare = a < b;
    if (compare)
        a = b;
    return compare;
}
template <typename T1, typename T2> inline bool chmin(T1 &a, T2 b) {
    bool compare = a > b;
    if (compare)
        a = b;
    return compare;
}
template <typename T> void vin(vector<T> &v) {
    for (auto &element : v) {
        cin >> element;
    }
}
template <typename T> T mod_pow(T x, T n, const T &p) {
    T ret = 1;
    while (n > 0) {
        if (n & 1)
            (ret *= x) %= p;
        (x *= x) %= p;
        n >>= 1;
    }
    return ret;
}
template <typename T> T ipow(T x, T n) {
    T ret = 1;
    while (n > 0) {
        if (n & 1)
            ret *= x;
        x *= x;
        n >>= 1;
    }
    return ret;
}
constexpr double TIME_LIMIT = 2900;
int N, T, Sig;
int best_len;
const array<string, 2> UL = {"U", "L"};
struct Input {
    vector<pii> wh;
    void input() {
        cin >> N >> T >> Sig;
        wh.resize(N);
        rep(i, N) {
            int w, h;
            cin >> w >> h;
            wh[i] = {w, h};
        }
    }
};
struct Action_ {
    int p;
    int r;
    string d;
    int b;
    Action_(int p, int r, string d, int b) : p(p), r(r), d(d), b(b) {};
    bool operator==(const Action_ &other) const {
        return (p == other.p and r == other.r and d == other.d and
                b == other.b);
    }
};
struct Output {
    pair<int, int> query(const vector<Action_> &actions) {
        int size = actions.size();
        cout << size << el;
        rep(i, size) {
            if (i == size - 1) {
                cout << actions[i].p << ' ' << actions[i].r << ' '
                     << actions[i].d << ' ' << actions[i].b << endl;
            } else {
                cout << actions[i].p << ' ' << actions[i].r << ' '
                     << actions[i].d << ' ' << actions[i].b << el;
            }
        }
        int w, h;
        cin >> w >> h;
        return {w, h};
    }
};

struct Nodo_horizon {
    int l;
    int r;
    int d;
    Nodo_horizon(int l, int r, int d) : l(l), r(r), d(d) {}
    bool operator<(const Nodo_horizon &other) const {
        if (l != other.l) {
            return l < other.l;
        } else {
            return r < other.r;
        }
    }
};
string seed;
struct Solver {
    Input input;
    Output output;
    vector<pair<int, int>> wh;
    vector<Action_> actions;
    int sqrt_;
    ll sum_s;
    Solver(const Input &input) : input(input) {
        wh = input.wh;
        sum_s = 0;
        for (auto [w, h] : input.wh) {
            sum_s += (ll)w * (ll)h;
        }
        best_len = sqrt(sum_s / 0.9);
    }
    void make_init_sol() {
        sqrt_ = (int)ceil(sqrt(N));
        actions.reserve(N);
        rep(i, N) {
            if (i % sqrt_ == 0) {
                actions.emplace_back(i, 0, "U", -1);
            } else {
                actions.emplace_back(i, 0, "U", i - 1);
            }
        }
    }

    pair<int, int> evaluate(int lim, const vector<pair<int, int>> &wh,
                            const vector<vector<int>> &state_l,
                            const vector<vector<int>> &state_r) {
        int s = state_l.size();
        int W = 0;
        int H = 0;
        rep(i, s) {
            int w = 0;
            int prev = -1;
            for (auto j : state_l[i]) {
                actions[j].b = prev;
                prev = j;
                if (actions[j].r == 0) {
                    w += wh[j].first;
                } else {
                    w += wh[j].second;
                }
            }
            for (auto j : state_r[i]) {
                actions[j].b = prev;
                prev = j;
                if (actions[j].r == 0) {
                    w += wh[j].first;
                } else {
                    w += wh[j].second;
                }
            }
            chmax(W, w);
        }

        static vector<Nodo_horizon> horizon;
        static vector<int> r_vec;
        static int max_ = 1000000000;
        horizon.reserve(N);
        horizon.clear();
        r_vec.clear();
        horizon.emplace_back(0, max_, 0);

        vector<Nodo_horizon>::iterator l_;
        vector<Nodo_horizon>::iterator r_;
        vector<Nodo_horizon>::iterator it;
        rep(i, N) {
            auto [w, h] = wh[i];
            if (actions[i].r == 1) {
                swap(w, h);
            }
            int l, r, u, d;

            u = 0;
            if (actions[i].b == -1) {
                l = 0;
                r = l + w;
                l_ = horizon.begin();
            } else {
                l = r_vec[actions[i].b];
                r = l + w;
                l_ = prev(
                    lower_bound(all(horizon), Nodo_horizon(l, 1000000001, 0)));
            }

            auto l_l = *l_;
            r_ = l_;
            while (r_ != horizon.end() and r_->l < r) {
                r_++;
            }
            auto r_r = *prev(r_);

            for (auto it = l_; it != r_; it++) {
                chmax(u, it->d);
            }

            d = u + h;
            int cnt = 1 + (l_l.l < l) + (r < r_r.r);
            it = l_;
            if (distance(l_, r_) >= cnt) {
                horizon.erase(next(l_, cnt), r_);
                if (l_l.l < l) {
                    *it = {l_l.l, l, l_l.d};
                    it++;
                }
                *it = Nodo_horizon(l, r, d);
                it++;
                if (r < r_r.r) {
                    *it = {r, r_r.r, r_r.d};
                }
            } else {
                horizon.erase(next(l_), r_);
                *it = {l, r, d};
                if (l_l.l < l) {
                    it = horizon.insert(it, {l_l.l, l, l_l.d});
                    it++;
                }
                if (r < r_r.r) {
                    horizon.insert(next(it), {r, r_r.r, r_r.d});
                }
            }
            r_vec.emplace_back(r);
            chmax(H, d);

            if (W + H > lim) {
                return {W, H};
            }
        }
        return {W, H};
    }

    pair<int, int> sa(TimeKeeperDouble tk, const vector<pair<int, int>> &wh,
                      vector<vector<int>> &state_l,
                      vector<vector<int>> &state_r) {
        int cnt = 0;
        double start_temp = 7000;
        double end_temp = 0.0;
        double now_temp = -1.0;
        auto [W, H] = evaluate(1000000000, wh, state_l, state_r);
        int now_score = W + H;
        int diff_lim = 0;
        int s = state_l.size();
        static int max_cycle = N * 20;
        int cycle_cnt = 0;
        while (true) {
            cycle_cnt++;

            if (cycle_cnt > max_cycle) {
                break;
            }
            if ((cnt & 63) == 0) {
                tk.setNowTime();
                if (tk.isTimeOver()) {
                    break;
                }
                double t = tk.getNowTime();
                double N = tk.time_threshold_;
                double numerator = log(N + 1) - log(t + 1);
                double denominator = log(N + 1);
                now_temp = end_temp +
                           (start_temp - end_temp) * (numerator / denominator);
                diff_lim =
                    -ceil(now_temp * log(xorshift() / double(1Ull << 32)));
            }
            cnt++;
            int mode = xorshift() % 15;
            if (mode >= 6) {
                // 一個を回転
                int index = xorshift() % N;
                actions[index].r ^= 1;
                int lim = now_score + diff_lim;
                auto [newW, newH] = evaluate(lim, wh, state_l, state_r);
                int new_score = newW + newH;
                if (newW + newH <= lim) {
                    if (new_score < now_score) {
                        cycle_cnt = 0;
                    }
                    W = newW;
                    H = newH;
                    now_score = new_score;
                } else {
                    actions[index].r ^= 1;
                }
            } else if (mode <= 3) {
                // スワップ追加
                int index = xorshift() % (s - 1);
                if (state_r[index].size() == 0 or
                    state_l[index + 1].size() == 0) {
                    continue;
                }
                int i1 = xorshift() % state_r[index].size();
                int i2 = xorshift() % state_l[index + 1].size();
                int v1 = state_r[index][i1];
                int v2 = state_l[index + 1][i2];
                state_r[index].erase(state_r[index].begin() + i1);
                state_l[index + 1].erase(state_l[index + 1].begin() + i2);
                auto it1 = state_r[index].begin();
                auto it2 = state_l[index + 1].begin();

                while (it2 != state_l[index + 1].end() and *it2 < v1) {
                    it2++;
                }
                while (it1 != state_r[index].end() and *it1 < v2) {
                    it1++;
                }
                it2 = state_l[index + 1].insert(it2, v1);
                it1 = state_r[index].insert(it1, v2);

                int r1 = xorshift() % 2;
                int r2 = xorshift() % 2;
                actions[v1].r ^= r1;
                actions[v2].r ^= r2;

                int lim = now_score + diff_lim;
                auto [newW, newH] = evaluate(lim, wh, state_l, state_r);
                int new_score = newW + newH;
                if (newW + newH <= lim) {
                    if (new_score < now_score) {
                        cycle_cnt = 0;
                    }
                    W = newW;
                    H = newH;
                    now_score = new_score;
                } else {
                    state_r[index].erase(it1);
                    state_l[index + 1].erase(it2);
                    auto it1 = state_r[index].begin() + i1;
                    auto it2 = state_l[index + 1].begin() + i2;
                    state_l[index + 1].insert(it2, v2);
                    state_r[index].insert(it1, v1);
                    actions[v1].r ^= r1;
                    actions[v2].r ^= r2;
                }
            } else if (mode == 4) {
                // 下に移動
                int index = xorshift() % (s - 1);
                if (state_r[index].size() == 0) {
                    continue;
                }
                int i1 = xorshift() % state_r[index].size();
                int v1 = state_r[index][i1];
                state_r[index].erase(state_r[index].begin() + i1);
                auto it2 = state_l[index + 1].begin();
                while (it2 != state_l[index + 1].end() and *it2 < v1) {
                    it2++;
                }
                it2 = state_l[index + 1].insert(it2, v1);

                int r1 = xorshift() % 2;
                actions[v1].r ^= r1;

                int lim = now_score + diff_lim;
                auto [newW, newH] = evaluate(lim, wh, state_l, state_r);
                int new_score = newW + newH;
                if (newW + newH <= lim) {
                    if (new_score < now_score) {
                        cycle_cnt = 0;
                    }
                    W = newW;
                    H = newH;
                    now_score = new_score;
                } else {
                    state_l[index + 1].erase(it2);
                    auto it1 = state_r[index].begin() + i1;
                    state_r[index].insert(it1, v1);
                    actions[v1].r ^= r1;
                }
            } else if (mode == 5) {
                // 上へ移動
                int index = xorshift() % (s - 1);
                if (state_l[index + 1].size() == 0) {
                    continue;
                }
                int i2 = xorshift() % state_l[index + 1].size();
                int v2 = state_l[index + 1][i2];
                state_l[index + 1].erase(state_l[index + 1].begin() + i2);
                auto it1 = state_r[index].begin();
                while (it1 != state_r[index].end() and *it1 < v2) {
                    it1++;
                }
                it1 = state_r[index].insert(it1, v2);
                int r2 = xorshift() % 2;
                actions[v2].r ^= r2;
                int lim = now_score + diff_lim;
                auto [newW, newH] = evaluate(lim, wh, state_l, state_r);
                int new_score = newW + newH;
                if (newW + newH <= lim) {
                    if (new_score < now_score) {
                        cycle_cnt = 0;
                    }
                    W = newW;
                    H = newH;
                    now_score = new_score;
                } else {
                    state_r[index].erase(it1);
                    auto it2 = state_l[index + 1].begin() + i2;
                    state_l[index + 1].insert(it2, v2);
                    actions[v2].r ^= r2;
                }
            }
        }

        rep(i, s) {
            int prev = -1;
            for (auto j : state_l[i]) {
                actions[j].b = prev;
                prev = j;
            }
            for (auto j : state_r[i]) {
                actions[j].b = prev;
                prev = j;
            }
        }
        return {W, H};
    }
    void solve() {
        vector<vector<Action_>> queryes;
        queryes.reserve(T);
        vector<tuple<int, int, int>> results;
        results.reserve(T);

        vector<vector<pair<int, int>>> tmp_wh_vec(N);
        rep(i, N) { tmp_wh_vec[i].emplace_back(wh[i]); }
        int num;
        num = 20;
        rep(i, T - num) {
            int j = (-i % N + N) % N;
            auto tmp = output.query({Action_(j, 0, "U", -1)});
            tmp_wh_vec[j].emplace_back(tmp);
            queryes.push_back({Action_(j, 0, "U", -1)});
            results.emplace_back(1000000000, 1000000000, results.size());
        }
        vector<pair<int, int>> tmp_wh(N);
        rep(i, N) {
            for (auto [w, h] : tmp_wh_vec[i]) {
                tmp_wh[i].first += w;
                tmp_wh[i].second += h;
            }
            tmp_wh[i].first /= tmp_wh_vec[i].size();
            tmp_wh[i].second /= tmp_wh_vec[i].size();
            chmin(tmp_wh[i].first, 100000);
            chmax(tmp_wh[i].first, 10000);
            chmin(tmp_wh[i].second, 100000);
            chmax(tmp_wh[i].second, 10000);
        }

        wh = tmp_wh;
        // denug----------------
        vector<pair<int, int>> sig0_wh(N);
        ifstream file("in/" + seed + ".txt");
        {
            if (!file) { // ファイルが開けない場合のエラーチェック
                cerr << "Error: Could not open the file!" << el;
                return;
            }
            int n, t, sig;
            file >> n >> t >> sig;
            int x, y;
            rep(i, N) { file >> x >> y; }
            rep(i, N) { file >> sig0_wh[i].first >> sig0_wh[i].second; }
        }
        wh = sig0_wh;
        // denug--------------------

        int size = 150;
        make_init_sol();
        int time = TIME_LIMIT / size;
        vector<vector<Action_>> cands;
        vector<tuple<int, int, int>> scores;
        cands.reserve(size);
        vector<int> tmp(N / sqrt_, sqrt_);
        rep(i, N % (N / sqrt_)) { tmp[xorshift() % (N / sqrt_)] += 1; }
        vector<int> sp1;
        sp1.emplace_back(0);
        for (auto i : tmp) {
            sp1.emplace_back(*(sp1.rbegin()) + i);
        }
        vector<double> p = {0.65, 0.8, 0.95};
        int i = 0;
        vector<vector<int>> state_l;
        vector<vector<int>> state_r;
        while (true) {
            rep(i, N) {
                actions[i].r = xorshift() & 1;
                actions[i].b = i - 1;
            }
            int height = 0;
            if ((xorshift() & 1) == 0) {
                height = 0;
                for (auto i : sp1) {
                    if (i < N) {
                        actions[i].b = -1;
                        height++;
                    }
                }
            } else {
                int r = 0;
                height = 1;
                int best_wh = sqrt(sum_s / p[xorshift() % 3]);
                rep(i, N) {
                    if (actions[i].r == 0) {
                        if (r + wh[i].first <= best_wh) {
                            r += wh[i].first;
                        } else {
                            height++;
                            actions[i].b = -1;
                            r = wh[i].first;
                        }
                    } else {
                        if (r + wh[i].second <= best_wh) {
                            r += wh[i].second;
                        } else {
                            height++;
                            actions[i].b = -1;
                            r = wh[i].second;
                        }
                    }
                }
            }

            int j = -1;
            // 左半分(少し大きめ)
            // 右半分
            // i行目の右半分と、i+1行目の左半分は交換可能とする
            state_l.assign(height, vector<int>());
            state_r.assign(height, vector<int>());
            int sum_w = 0;
            int prev_ = 0;
            rep(i, N) {
                if (actions[i].b == -1) {
                    int tmp = 0;
                    for (int k = prev_; k < i; k++) {
                        if (actions[k].r == 1) {
                            tmp += wh[k].second;
                        } else {
                            tmp += wh[k].first;
                        }
                        if (tmp < sum_w * 0.6 and j > 0) {
                            state_l[j].push_back(k);
                        } else {
                            state_r[j].push_back(k);
                        }
                    }
                    j++;
                    sum_w = 0;
                    prev_ = i;
                }
                if (actions[i].r == 1) {
                    sum_w += wh[i].second;
                } else {
                    sum_w += wh[i].first;
                }
            }
            for (int i = prev_; i < N; i++) {
                state_l[j].push_back(i);
            }
            int max_ = (int)(sqrt(N) / 2);
            rep(i, height - 1) {
                int cnt = xorshift() % max(1, max_);
                rep(j, cnt) {
                    swap(state_r[i][xorshift() % state_r[i].size()],
                         state_l[i + 1][xorshift() % state_l[i + 1].size()]);
                }
                sort(all(state_r[i]));
                sort(all(state_l[i + 1]));
            }
            auto tk = TimeKeeperDouble(time);
            auto [W, H] = sa(tk, wh, state_l, state_r);
            cands.emplace_back(actions);
            scores.emplace_back(W, H, scores.size());
            i++;
            time_keeper.setNowTime();
            if (time_keeper.isTimeOver()) {
                break;
            }
        }
        sort(all(scores));
        sort(all(scores), [](tuple<int, int, int> a, tuple<int, int, int> b) {
            return (get<0>(a) + get<1>(a) < get<0>(b) + get<1>(b));
        });

        rep(i, size) {
            if (i > 0 and get<0>(scores[i]) == get<0>(scores[i - 1]) and
                get<1>(scores[i]) == get<1>(scores[i - 1])) {
                continue;
            }
            pair<int, int> tmp = output.query(cands[get<2>(scores[i])]);
            queryes.emplace_back(cands[get<2>(scores[i])]);
            results.emplace_back(tmp.first, tmp.second, results.size());

            if ((int)queryes.size() >= T) {
                break;
            }
        }
    }
};

int main(int argc, char *argv[]) {
    seed = argv[1];
    time_keeper = TimeKeeperDouble(TIME_LIMIT);
    Input input;
    input.input();
    Solver solver(input);
    solver.solve();
    return 0;
}
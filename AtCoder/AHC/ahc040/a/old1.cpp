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
namespace xorshift64 {

inline static uint64_t a = 12345;

uint64_t next() {
    uint64_t x = a;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    return a = x;
}

} // namespace xorshift64

// 時間をDouble型で管理し、経過時間も取り出せるクラス
class TimeKeeperDouble {
  private:
    std::chrono::high_resolution_clock::time_point start_time_;
    double time_threshold_;

    double now_time_ = 0;

  public:
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
struct Action {
    int p;
    int r;
    string d;
    int b;
    array<int, 4> udlr;
    Action(int p, int r, string d, int b) : p(p), r(r), d(d), b(b) {};
    bool operator==(const Action &other) const {
        return (p == other.p and r == other.r and d == other.d and
                b == other.b);
    }
};
struct Output {
    pair<int, int> query(const vector<Action> &actions) {
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

uint32_t xorshift() {
    static uint32_t y = 2463534242;
    y = y ^ (y << 13);
    y = y ^ (y >> 17);
    return y = y ^ (y << 15);
}
struct Solver {
    Input input;
    Output output;
    vector<pair<int, int>> wh;
    vector<Action> actions;
    vector<int> split;
    int id = 0;
    Solver(const Input &input) : input(input) {
        wh = input.wh;
        split = vector<int>(N, 0);
    }
    void make_init_sol() {
        int sqrt_ = (int)ceil(sqrt(N));
        actions.reserve(N);
        rep(i, sqrt_) {
            if (i * sqrt_ < N) {
                split[i * sqrt_] = 1;
            }
        }
        rep(i, N) {
            if (i % sqrt_ == 0) {
                actions.emplace_back(i, 0, "U", -1);
            } else {
                actions.emplace_back(i, 0, "U", i - 1);
            }
        }
    }
    int evaluate(int lim) {
        static map<pair<int, int>, int> horizon;
        static vector<int> rs;
        int max_ = 1000000000;
        horizon.clear();
        rs.clear();
        horizon[{0, max_}] = 0;
        // int prev_ = 0;
        int W = 0;
        int H = 0;
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
            } else {
                l = rs[actions[i].b];
                r = l + w;
            }
            pair<pair<int, int>, int> l_l = {{0, 0}, 0};
            pair<pair<int, int>, int> r_r = {{max_, max_}, 0};

            auto l_ = horizon.lower_bound({l, l});
            l_l = *l_;
            auto r_ = horizon.lower_bound({r, r});
            r_r = *prev(r_);

            for (auto it = l_; it != r_; it++) {
                chmax(u, (*it).second);
            }

            d = u + h;
            horizon.erase(l_, r_);
            if (l_l.first.first < l) {
                horizon[{l_l.first.first, l}] = l_l.second;
            }
            horizon[{l, r}] = d;
            if (r < r_r.first.second) {
                horizon[{r, r_r.first.second}] = r_r.second;
            }
            // prev_ = r;
            rs.emplace_back(r);
            chmax(W, r);
            chmax(H, d);
            if (W + H > lim) {
                return W + H;
            }
        }
        return W + H;
    }
    void sa() {
        int cnt = 0;
        double start_temp = 0;
        double end_temp = 0.0;
        double now_temp = -1.0;
        int now_score = inf;
        int diff_lim = 0;
        while (true) {
            if ((cnt & 31) == 0) {
                time_keeper.setNowTime();
                now_temp = start_temp + (end_temp - start_temp) *
                                            time_keeper.getNowTime() /
                                            TIME_LIMIT;
                diff_lim = ceil(now_temp * log(xorshift() / double(1ll << 32)));
                if (time_keeper.isTimeOver()) {
                    break;
                }
            }
            int mode = xorshift() % 10;
            if (mode <= 1) {
                int index = xorshift() % (N - 1) + 1;
                // if (actions[index].b == -1 and mode == 0) {
                //     //  改行位置スライド
                //     int pm = xorshift() & 1;
                //     if (pm == 0) {
                //         pm = -1;
                //     }
                //     if (index + pm < 0 or index + pm >= N) {
                //         continue;
                //     }
                //     memo =
                //     actions[index].b = xorshift() % (index + 1) - 1;
                //     // split[index] = 0;
                //     // bool memo = split[index + pm];
                //     // split[index + pm] = 1;
                //     int lim = now_score + diff_lim;
                //     int new_score = evaluate(lim);
                //     if (new_score <= lim) {
                //         if (new_score < now_score) {
                //             cerr << time_keeper.getNowTime() << " " <<
                //             new_score
                //                  << el;
                //         }
                //         now_score = new_score;
                //     } else {
                //         // split[index] = 1;
                //         // split[index + pm] = memo;
                //     }
                // } else {
                // split[index] ^= 1;
                int memo = actions[index].b;
                int j = xorshift() % (index + 1) - 1;
                actions[index].b = j;
                int lim = now_score + diff_lim;
                int new_score = evaluate(lim);
                if (new_score <= lim) {
                    if (new_score < now_score) {
                        cerr << time_keeper.getNowTime() << " " << new_score
                             << el;
                    }
                    now_score = new_score;
                } else {
                    // split[index] ^= 1;
                    actions[index].b = memo;
                }
            }
            // }
            else {
                int index = xorshift() % N;
                actions[index].r ^= 1;
                int lim = now_score + diff_lim;
                int new_score = evaluate(lim);
                if (new_score <= lim) {
                    if (new_score < now_score) {
                        cerr << time_keeper.getNowTime() << " " << new_score
                             << el;
                    }
                    now_score = new_score;
                } else {
                    actions[index].r ^= 1;
                }
            }
            cnt++;
        }
        dump(cnt);
    }
    void solve() {
        make_init_sol();
        vector<vector<pair<int, int>>> wh_tmp(N, vector<pair<int, int>>());
        rep(i, N) { wh_tmp[i].emplace_back(wh[i]); }
        rep(i, T - 1) {
            auto wh = output.query({Action(i % N, 0, "U", -1)});
            wh_tmp[i % N].emplace_back(wh);
        }
        rep(i, N) {
            int w = 0;
            int h = 0;
            for (auto [p, q] : wh_tmp[i]) {
                w += p;
                h += q;
            }
            wh[i].first = w / (int)wh_tmp[i].size();
            wh[i].second = h / (int)wh_tmp[i].size();
        }
        sa();
        // rep(i, N) {
        //     if (split[i] == 1) {
        //         actions[i].b = -1;
        //     } else {
        //         actions[i].b = i - 1;
        //     }
        // }

        output.query(actions);
    }
};
int main() {
    time_keeper = TimeKeeperDouble(TIME_LIMIT);
    Input input;
    input.input();
    Solver solver(input);
    solver.solve();
    return 0;
}
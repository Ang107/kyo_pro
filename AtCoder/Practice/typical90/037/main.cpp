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
// #include <atcoder/all>
// using namespace atcoder;
struct Init {
    Init() {
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
} init;
#define ll long long
#define vi vector<int>
#define vl vector<long long>
#define vvi vector<vector<int>>
#define vvl vector<vector<long long>>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define elif else if
#define rep(i, n) for (int i = 0; i < (n); i++)
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
int main() {
    // code
    int w, n;
    cin >> w >> n;
    vi l(n), r(n), v(n);
    rep(i, n) { cin >> l[i] >> r[i] >> v[i]; }
    vl dp(w + 1, -infl);
    dp[0] = 0;
    vector<vector<pll>> ndp(w + 1, vector<pll>(0));
    rep(i, n) {
        rep(j, w + 1) {
            if (dp[j] == -infl) {
                continue;
            }
            int l_ = l[i];
            int r_ = r[i];
            int v_ = v[i];
            ndp[j].emplace_back(1, dp[j]);
            if (j + 1 < w + 1) {
                ndp[j + 1].emplace_back(-1, dp[j]);
            }
            if (j + l_ < w + 1) {
                ndp[j + l_].emplace_back(1, dp[j] + v_);
                if (j + r_ + 1 < w + 1) {
                    ndp[j + r_ + 1].emplace_back(-1, dp[j] + v_);
                }
            }
        }
        multiset<ll> cand;
        rep(j, w + 1) {
            for (auto [io, k] : ndp[j]) {
                if (io > 0) {
                    cand.insert(k);
                } else {
                    cand.erase(cand.find(k));
                }
            }
            if (!cand.empty()) {
                dp[j] = *prev(cand.end());
            } else {
                dp[j] = -infl;
            }
        }
        ndp = vector<vector<pll>>(w + 1, vector<pll>());
    }
    if (dp[w] != -infl) {
        cout << dp[w] << el;
    } else {
        cout << -1 << el;
    }
    return 0;
}
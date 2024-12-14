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

void f(int c, int n, int k, ll &ans, vector<pll> &xy, vector<vector<int>> &g,
       int max_size) {
    int cnt = 0;
    rep(i, k) { cnt += !g[i].empty(); }
    if (cnt + (n - c) < k) {
        return;
    }
    if (c == n) {
        int ok = 1;
        rep(i, k) { ok &= !g[i].empty(); }

        if (ok) {
            ll res = 0;
            for (auto &i : g) {
                int size = i.size();
                rep(j, size) {
                    for (int l = j + 1; l < size; l++) {
                        auto [ux, uy] = xy[i[j]];
                        auto [vx, vy] = xy[i[l]];
                        chmax(res,
                              (ux - vx) * (ux - vx) + (uy - vy) * (uy - vy));
                    }
                }
            }
            // dump(g, ok, res);
            chmin(ans, res);
        }
        return;
    }
    int sum_ = 0;
    rep(i, k) {
        sum_ += g[i].size();
        if (n - sum_ < k - i) {
            continue;
        }
        if (g[i].empty()) {
            g[i].push_back(c);
            f(c + 1, n, k, ans, xy, g, max_size);
            g[i].pop_back();
            break;
        } else if (g[i].size() + 1 <= max_size) {
            g[i].push_back(c);
            f(c + 1, n, k, ans, xy, g, max_size);
            g[i].pop_back();
        }
    }
}
int main() {
    // code
    ll ans = infl;
    vector<vector<int>> g;
    int n, k;
    cin >> n >> k;
    g = vector<vector<int>>(k);
    vector<pll> xy(n);
    int max_size = 1 + n - k;
    rep(i, n) { cin >> xy[i].first >> xy[i].second; }
    f(0, n, k, ans, xy, g, max_size);
    cout << ans << el;
    return 0;
}
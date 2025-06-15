#include <bits/stdc++.h>
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
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
ll get(const vector<vector<int>> &imos, int a, int b, int c, int d) {
    ll res = (ll)0;
    res += (ll)imos[c + 1][d + 1];
    res += (ll)imos[a][b];
    res -= (ll)imos[a][d + 1];
    res -= (ll)imos[c + 1][b];
    return res;
}
int main() {
    int t;
    cin >> t;
    rep(_, t) {
        int h, w;
        cin >> h >> w;
        vector<vector<string>> s(h, vector<string>(w));
        rep(i, h) {
            string tmp;
            cin >> tmp;
            rep(j, w) { s[i][j] = tmp[j]; }
        }
        vector<vector<string>> ns(w, vector<string>(h));
        rep(i, h) {
            rep(j, w) { ns[j][i] = s[i][j]; }
        }
        if (h > w) {
            s = ns;
            swap(h, w);
        }
        vector<vector<int>> imos(h + 1, vector<int>(w + 1));
        rep(i, h) {
            rep(j, w) {
                if (s[i][j] == ".")
                    imos[i + 1][j + 1] = 1;
                else
                    imos[i + 1][j + 1] = -1;
            }
        }
        // dump(s);
        rep(i, h + 1) {
            rep(j, w) { imos[i][j + 1] += imos[i][j]; }
        }
        rep(i, h) {
            rep(j, w + 1) { imos[i + 1][j] += imos[i][j]; }
        }
        // dump(imos);
        ll ans = 0;
        rep(i, h) {
            for (int j = i; j < h; j++) {
                // unordered_map<int, int> cnt;
                vector<int> cnt;
                cnt.reserve(w + 1);
                // cnt[0] += 1;
                cnt.push_back(0);
                rep(k, w) {
                    // int res = get(imos, i, 0, j, k);
                    // ans += cnt[res];
                    // cnt[res]++;
                    cnt.push_back(get(imos, i, 0, j, k));
                }
                sort(all(cnt));
                int now = cnt[0];
                ll c = 1;
                rep(k, w) {
                    if (cnt[k + 1] == now) {
                        c += 1;
                    } else {
                        ans += c * (c - 1) / 2;
                        c = 1;
                        now = cnt[k + 1];
                    }
                }
                ans += c * (c - 1) / 2;
                // for (auto [k, v] : cnt) {
                //     // cout << k << " " << v << el;
                //     ans += (ll)v * (ll)(v - 1) / (ll)2;
                // }
            }
        }
        cout << ans << el;
    }
}
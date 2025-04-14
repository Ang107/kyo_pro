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
int n;
vector<ll> a;
vector<vector<ll>> g;
unordered_set<ll> ans;
void f(int x) {
    if (x == n) {
        ll res = 0;
        rep(i, g.size()) {
            ll tmp = 0;
            for (auto j : g[i]) {
                tmp += j;
            }
            res ^= tmp;
        }
        ans.insert(res);
    } else {
        rep(i, g.size()) {
            g[i].push_back(a[x]);
            f(x + 1);
            g[i].pop_back();
        }
        g.push_back({a[x]});
        f(x + 1);
        g.pop_back();
    }
}
vector<ll> get_p(ll n) {
    vector<int> is_prime(n + 1, 1);
    is_prime[0] = 0;
    is_prime[1] = 0;
    vector<ll> primes;
    for (ll i = 2; i <= n; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (ll j = i * 2; j <= n; j++) {
                is_prime[j] = 0;
            }
        }
    }
    return primes;
}
int main() {
    int q;
    cin >> q;
    auto primes = get_p(1000000);
    int n = primes.size();
    vector<pair<ll, ll>> cand;
    for (auto i : primes) {
        for (ll j = 2; j < 64; j += 2) {
            if (ipow(i, j) > ipow(10, 12)) {
                break;
            }
            cand.push_back({ipow(i, j), i});
        }
    }
    sort(all(cand));
    rep(t, q) {
        ll a;
        cin >> a;
        ll ans = 0;
        for (auto i : primes) {
            if (i * i * i * i > a) {
                break;
            }
            for (ll p = 2; p < 64; p += 2) {
                ll tmp = ipow(i, p);
                if (tmp * i * i >= a) {
                    break;
                }
                auto q = make_pair(a / tmp, (ll)infl);
                auto it = prev(upper_bound(all(cand), q));
                while (true) {
                    if ((*it).second != i) {
                        ans = max(ans, tmp * (*it).first);
                        break;
                    }
                    if (it == cand.begin()) {
                        break;
                    }
                    it--;
                }
            }
        }
        cout << ans << el;
    }
}
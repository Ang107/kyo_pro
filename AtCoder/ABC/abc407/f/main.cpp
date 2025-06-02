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
// https://mugen1337.github.io/procon/DataStructure/RangeSet.hpp
//  閉区間の範囲を管理
template <typename T> struct RangeSet {
    set<pair<T, T>> st;
    T TINF;

    RangeSet() {
        TINF = numeric_limits<T>::max() / 2;
        st.emplace(TINF, TINF);
        st.emplace(-TINF, -TINF);
    }
    // [l,r] covered?
    bool covered(T l, T r) {
        assert(l <= r);
        auto ite = prev(st.lower_bound({l + 1, l + 1}));
        return ite->first <= l and r <= ite->second;
    }
    bool covered(T x) { return covered(x, x); }
    // [l, r]がカバーされているなら，その区間を返す.
    // されていないなら[-TINF,-TINF]を返す
    pair<T, T> covered_by(T l, T r) {
        assert(l <= r);
        auto ite = prev(st.lower_bound({l + 1, l + 1}));
        if (ite->first <= l and r <= ite->second)
            return *ite;
        return make_pair(-TINF, -TINF);
    }
    pair<T, T> covered_by(T x) { return covered_by(x, x); }
    // insert[l,r], 増加量を返す
    T insert(T l, T r) {
        assert(l <= r);
        auto ite = prev(st.lower_bound({l + 1, l + 1}));
        if (ite->first <= l and r <= ite->second)
            return T(0);
        T sum_erased = T(0);
        if (ite->first <= l and l <= ite->second + 1) {
            l = ite->first;
            sum_erased += ite->second - ite->first + 1;
            ite = st.erase(ite);
        } else
            ite = next(ite);
        while (r > ite->second) {
            sum_erased += ite->second - ite->first + 1;
            ite = st.erase(ite);
        }
        if (ite->first - 1 <= r and r <= ite->second) {
            sum_erased += ite->second - ite->first + 1;
            r = ite->second;
            st.erase(ite);
        }
        st.emplace(l, r);
        return r - l + 1 - sum_erased;
    }
    T insert(T x) { return insert(x, x); }
    // erase [l,r], 減少量を返す
    T erase(T l, T r) {
        assert(l <= r);
        auto ite = prev(st.lower_bound({l + 1, l + 1}));
        if (ite->first <= l and r <= ite->second) {
            // 完全に1つの区間に包含されている
            if (ite->first < l)
                st.emplace(ite->first, l - 1);
            if (r < ite->second)
                st.emplace(r + 1, ite->second);
            st.erase(ite);
            return r - l + 1;
        }

        T ret = T(0);
        if (ite->first <= l and l <= ite->second) {
            ret += ite->second - l + 1; // 消えた
            if (ite->first < l)
                st.emplace(ite->first, l - 1);
            ite = st.erase(ite); // 次へ
        } else
            ite = next(ite);
        while (ite->second <= r) {
            ret += ite->second - ite->first + 1;
            ite = st.erase(ite);
        }
        // 右端が区間の間にあるか
        if (ite->first <= r and r <= ite->second) {
            ret += r - ite->first + 1;
            if (r < ite->second)
                st.emplace(r + 1, ite->second);
            st.erase(ite);
        }
        return ret;
    }
    T erase(T x) { return erase(x, x); }
    // number of range
    int size() { return (int)st.size() - 2; }
    // mex [x,~)
    T mex(T x = 0) {
        auto ite = prev(st.lower_bound({x + 1, x + 1}));
        if (ite->first <= x and x <= ite->second)
            return ite->second + 1;
        else
            return x;
    }
    void output() {
        cout << "RangeSet : ";
        for (auto &p : st) {
            if (p.first == -TINF or p.second == TINF)
                continue;
            cout << "[" << p.first << ", " << p.second << "] ";
        }
        cout << "\n";
    }
};
int main() {
    int n;
    cin >> n;
    vl a(n);
    vin(a);
    vector<pair<ll, int>> tmp;
    rep(i, n) { tmp.push_back({a[i], i}); }
    sort(tmp.rbegin(), tmp.rend());
    vector<ll> ans(n);

    rep(i, n) {
        RangeSet<int> rs;
        for (auto [v, j] : tmp) {
            if (rs.covered(0, n - i - 1)) {
                break;
            }
            ll add = rs.insert(max(0, j - i), min(j, n - i - 1));
            // dump(i, v, j, add);
            ans[i] += add * v;
        }
    }
    rep(i, n) { cout << ans[i] << "\n"; }
    return 0;
}
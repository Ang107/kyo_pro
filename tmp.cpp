// https://atcoder.jp/contests/abc404/submissions/65464932
#include <bits/stdc++.h>
// #include <atcoder/all> // AtCoder
using namespace std;
// using namespace atcoder; // AtCoder
using uint = unsigned int;
using ll = long long;
using ull = unsigned long long;
using ld = long double;
// using mint = modint998244353; // AtCoder
using vll = vector<long long>;
using vvll = vector<vector<long long>>;
using vvvll = vector<vector<vector<long long>>>;
using vvvvll = vector<vector<vector<vector<long long>>>>;
using dll = deque<long long>;
using ddll = deque<deque<long long>>;
using dddll = deque<deque<deque<long long>>>;
using ddddll = deque<deque<deque<deque<long long>>>>;
using pll = pair<long long, long long>;
using vpll = vector<pair<long long, long long>>;
using vvpll = vector<vector<pair<long long, long long>>>;
#define overload2(_1, _2, name, ...) name
#define overload4(_1, _2, _3, _4, name, ...) name
#define rep1(n) for (ll i = 0; i < n; i++)
#define rep2(i, n) for (ll i = 0; i < n; i++)
#define rep3(i, a, b) for (ll i = a; i < b; i++)
#define rep4(i, a, b, c) for (ll i = a; i < b; i += c)
#define rep(...) overload4(__VA_ARGS__, rep4, rep3, rep2, rep1)(__VA_ARGS__)
#define reps1(n) for (ll i = 1; i <= n; i++)
#define reps2(i, n) for (ll i = 1; i <= n; i++)
#define reps(...) overload2(__VA_ARGS__, reps2, reps1)(__VA_ARGS__)
#define rrep1(n) for (int i = n - 1; i >= 0; i--)
#define rrep2(i, n) for (int i = n - 1; i >= 0; i--)
#define rrep3(i, a, b) for (int i = b - 1; i >= a; i--)
#define rrep4(i, a, b, c) for (int i = b - 1; i >= a; i -= c)
#define rrep(...)                                                              \
    overload4(__VA_ARGS__, rrep4, rrep3, rrep2, rrep1)(__VA_ARGS__)
#define rreps1(n) for (long long i = n; i >= 1; i--)
#define rreps2(i, n) for (long long i = n; i >= 1; i--)
#define rreps(...) overload2(__VA_ARGS__, rreps2, rreps1)(__VA_ARGS__)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define PI acos(-1.0)
#define YES printf("YES\n"), exit(0)
#define NO printf("NO\n"), exit(0)
#define Yes printf("Yes\n"), exit(0)
#define No printf("No\n"), exit(0)
#define MINUS printf("-1\n"), exit(0)
#define cuot cout // typo
#define endk endl // typo
constexpr char ln = '\n';
constexpr long long MOD = 998244353LL;
constexpr long long LINF = 0x1fffffffffffffff; // 4倍までOK 10^18より大きい
constexpr int INF = 0x3fffffff;                // 2倍までOK 10^9より大きい
template <class T> void setcout(T n) { cout << setprecision(n) << fixed; }
template <class... T> constexpr auto min(T... a) {
    return min(initializer_list<common_type_t<T...>>{a...});
}
template <class... T> constexpr auto max(T... a) {
    return max(initializer_list<common_type_t<T...>>{a...});
}
template <class T> bool chmax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return 1;
    }
    return 0;
}
template <class T> bool chmin(T &a, const T &b) {
    if (b < a) {
        a = b;
        return 1;
    }
    return 0;
}
template <class T> long long acc(const T &a) { return accumulate(all(a), 0LL); }
template <class T> long double accl(const T &a) {
    return accumulate(all(a), 0.0L);
}
template <class T> vector<T> mrui(const vector<T> &a) {
    vector<T> ret(a.size() + 1);
    for (int i = 0; i < a.size(); i++) {
        ret[i + 1] = ret[i] + a[i];
    }
    return ret;
}
template <class T> vector<vector<T>> mrui2(const vector<vector<T>> &a) {
    vector<vector<T>> ret(a.size() + 1, vector<T>(a.front().size() + 1));
    for (int i = 0; i < (int)a.size(); i++) {
        for (int j = 0; j < (int)a.front().size(); j++) {
            ret[i + 1][j + 1] =
                ret[i][j + 1] + ret[i + 1][j] - ret[i][j] + a[i][j];
        }
    }
    return ret;
}

inline void in() {}
template <class Head, class... Tail> inline void in(Head &head, Tail &...tail) {
    cin >> head;
    in(tail...);
}

#define INT(...)                                                               \
    int __VA_ARGS__;                                                           \
    in(__VA_ARGS__)
#define LL(...)                                                                \
    ll __VA_ARGS__;                                                            \
    in(__VA_ARGS__)
#define ULL(...)                                                               \
    ull __VA_ARGS__;                                                           \
    in(__VA_ARGS__)
#define STR(...)                                                               \
    string __VA_ARGS__;                                                        \
    in(__VA_ARGS__)
#define CHR(...)                                                               \
    char __VA_ARGS__;                                                          \
    in(__VA_ARGS__)
#define DBL(...)                                                               \
    double __VA_ARGS__;                                                        \
    in(__VA_ARGS__)
#define LD(...)                                                                \
    ld __VA_ARGS__;                                                            \
    in(__VA_ARGS__)
#define vec(type, name, ...) vector<type> name(__VA_ARGS__)
#define VEC(type, name, size)                                                  \
    vector<type> name(size);                                                   \
    in(name)
#define vv(type, name, h, ...)                                                 \
    vector<vector<type>> name(h, vector<type>(__VA_ARGS__))
#define VV(type, name, h, ...)                                                 \
    vector<vector<type>> name(h, vector<type>(__VA_ARGS__));                   \
    in(name)
#define vvv(type, name, h, w, ...)                                             \
    vector<vector<vector<type>>> name(                                         \
        h, vector<vector<type>>(w, vector<type>(__VA_ARGS__)))

template <class T1, class T2>
ostream &operator<<(ostream &os, const pair<T1, T2> &p); // prototype

template <class T1, class T2>
istream &operator>>(istream &is, pair<T1, T2> &p); // prototype

template <class T>
ostream &operator<<(ostream &os, const vector<T> &v); // prototype

template <class T>
ostream &operator<<(ostream &os, const vector<vector<T>> &v); // prototype

template <class T>
ostream &operator<<(ostream &os,
                    const vector<vector<vector<T>>> &v); // prototype

template <class T> istream &operator>>(istream &is, vector<T> &v); // prototype

template <class T, class S>
ostream &operator<<(ostream &os, const map<T, S> &mp); // prototype

template <class T>
ostream &operator<<(ostream &os, const set<T> &st); // prototype

template <class T>
ostream &operator<<(ostream &os, const multiset<T> &st); // prototype

template <class T> ostream &operator<<(ostream &os, queue<T> q); // prototype

template <class T> ostream &operator<<(ostream &os, deque<T> q); // prototype

template <class T> ostream &operator<<(ostream &os, stack<T> st); // prototype

template <class T, class Container, class Compare>
ostream &operator<<(ostream &os,
                    priority_queue<T, Container, Compare> pq); // prototype

// ostream &operator<<(ostream &os, const mint &i); //atcoder // prototype

// ostream &operator<<(ostream &os, const vector<mint> &v); //atcoder //
// prototype

// ostream &operator<<(ostream &os, const modint &i); //atcoder // prototype

// ostream &operator<<(ostream &os, const vector<modint> &v); //atcoder //
// prototype

template <class T1, class T2>
ostream &operator<<(ostream &os, const pair<T1, T2> &p) {
    os << "(" << p.first << "," << p.second << ")";
    return os;
}

template <class T1, class T2>
istream &operator>>(istream &is, pair<T1, T2> &p) {
    is >> p.first >> p.second;
    return is;
}

template <class T> ostream &operator<<(ostream &os, const vector<T> &v) {
    for (int i = 0; i < (int)v.size(); i++) {
        os << v[i] << (i + 1 != (int)v.size() ? " " : "");
    }
    return os;
}

template <class T>
ostream &operator<<(ostream &os, const vector<vector<T>> &v) {
    for (int i = 0; i < (int)v.size(); i++) {
        os << v[i] << endl;
    }
    return os;
}

template <class T>
ostream &operator<<(ostream &os, const vector<vector<vector<T>>> &v) {
    for (int i = 0; i < (int)v.size(); i++) {
        os << "i = " << i << endl;
        os << v[i];
    }
    return os;
}

template <class T> istream &operator>>(istream &is, vector<T> &v) {
    for (T &in : v) {
        is >> in;
    }
    return is;
}

template <class T, class S>
ostream &operator<<(ostream &os, const map<T, S> &mp) {
    for (auto &[key, val] : mp) {
        os << key << ": " << val << " ";
    }
    return os;
}

template <class T> ostream &operator<<(ostream &os, const set<T> &st) {
    auto itr = st.begin();
    for (int i = 0; i < (int)st.size(); i++) {
        os << *itr << (i + 1 != (int)st.size() ? " " : "");
        itr++;
    }
    return os;
}

template <class T> ostream &operator<<(ostream &os, const multiset<T> &st) {
    auto itr = st.begin();
    for (int i = 0; i < (int)st.size(); i++) {
        os << *itr << (i + 1 != (int)st.size() ? " " : "");
        itr++;
    }
    return os;
}

template <class T> ostream &operator<<(ostream &os, queue<T> q) {
    while (q.size()) {
        os << q.front() << " ";
        q.pop();
    }
    return os;
}

template <class T> ostream &operator<<(ostream &os, deque<T> q) {
    while (q.size()) {
        os << q.front() << " ";
        q.pop_front();
    }
    return os;
}

template <class T> ostream &operator<<(ostream &os, stack<T> st) {
    while (st.size()) {
        os << st.top() << " ";
        st.pop();
    }
    return os;
}

template <class T, class Container, class Compare>
ostream &operator<<(ostream &os, priority_queue<T, Container, Compare> pq) {
    while (pq.size()) {
        os << pq.top() << " ";
        pq.pop();
    }
    return os;
}

/*ostream &operator<<(ostream &os, const mint &i) { //AtCoder
        os << i.val();
        return os;
}*/

/*ostream &operator<<(ostream &os, const vector<mint> &v) { //AtCoder
        for (int i = 0; i < (int)v.size(); i++) {
                os << v[i].val() << (i + 1 != (int)v.size() ? " " : "");
        }
        return os;
}*/

/*ostream &operator<<(ostream &os, const modint &i) { //AtCoder
        os << i.val();
        return os;
}*/

/*ostream &operator<<(ostream &os, const vector<modint> &v) { //AtCoder
        for (int i = 0; i < (int)v.size(); i++) {
                os << v[i].val() << (i + 1 != (int)v.size() ? "" : "");
        }
        return os;
}*/

// bit全探索っぽい
// 動物園ごとになんの動物を持っているのかを配列として持つ必要

#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

int main() {
    ll n, m;
    cin >> n >> m;
    vll c(n);
    cin >> c;
    vvll a(m);
    vvll b(n); // 各動物園がなんの動物を持っているのかの配列
    rep(i, m) {
        ll k;
        cin >> k;
        a[i].resize(k);
        rep(j, k) cin >> a[i][j], a[i][j]--;
        rep(j, k) b[a[i][j]].push_back(i);
    }
    ll ans = LINF;
    rep(bits, 1LL << (2 * n)) { // どの動物園に入場するかbit全探索
        ll p = 0;
        rep(i, 2 * n) p += ((bits >> i & 1LL) == 1) * c[i / 2];
        vll w(m); // 各動物を何回見たか
        rep(i, 2 * n) {
            if ((bits >> i & 1LL) == 0)
                continue;
            rep(j, b[i / 2].size()) w[b[i / 2][j]]++;
        }
        bool ok = 1;
        rep(i, m) ok &= (w[i] >= 2);
        if (ok)
            chmin(ans, p);
    }
    cout << ans << endl;
}
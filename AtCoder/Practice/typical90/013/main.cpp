#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define vl vector<long long>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define elif else if
#define rep(i, n) for (int i = 0; i < (n); i++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
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
template <typename T> using min_heap = priority_queue<T, vector<T>, greater<T>>;
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
template <typename T1, typename T2>
std::ostream &operator<<(std::ostream &os, std::pair<T1, T2> p) {
    os << "{" << p.first << "," << p.second << "}";
    return os;
}
template <typename T>
inline void print_vec(const vector<T> &v, bool split_line = false) {
    if (v.empty()) {
        cout << "This vector is empty." << el;
        return;
    }
    constexpr bool isValue = is_integral<T>::value;
    for (int i = 0; i < (int)v.size(); i++) {
        if constexpr (isValue) {
            if ((v[i] == inf) || (v[i] == infl))
                cout << 'x' << " \n"[split_line || i + 1 == (int)v.size()];
            else
                cout << v[i] << " \n"[split_line || i + 1 == (int)v.size()];
        } else
            cout << v[i] << " \n"[split_line || i + 1 == (int)v.size()];
    }
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
    // to do
    int n, m;
    cin >> n >> m;
    vector<vector<pii>> g(n);
    rep(i, m) {
        int a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        g[a].push_back(make_pair(c, b));
        g[b].push_back(make_pair(c, a));
    }
    min_heap(pii) heap;
    vi dis_from_1(n, inf);
    vi dis_from_n(n, inf);
    dis_from_1[0] = 0;
    dis_from_n[n - 1] = 0;
    heap.push(make_pair(0, 0));
    while (!heap.empty()) {
        auto [d, v] = heap.top();
        heap.pop();
        if (d > dis_from_1[v]) {
            continue;
        }

        for (auto [w, next] : g[v]) {
            if (d + w < dis_from_1[next]) {
                dis_from_1[next] = d + w;
                heap.push(make_pair(d + w, next));
            }
        }
    }
    heap = priority_queue<pii, vector<pii>, greater<pii>>();
    heap.push(make_pair(0, n - 1));
    while (!heap.empty()) {
        auto [d, v] = heap.top();
        heap.pop();
        if (d > dis_from_n[v]) {
            continue;
        }
        for (auto [w, next] : g[v]) {
            if (d + w < dis_from_n[next]) {
                dis_from_n[next] = d + w;
                heap.push(make_pair(d + w, next));
            }
        }
    }
    rep(i, n) { cout << dis_from_1[i] + dis_from_n[i] << el; }
}
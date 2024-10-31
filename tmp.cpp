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
const double pi = 3.141592653589793238;
const int inf = 1073741823;
const ll infl = 1LL << 60;
const string ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string abc = "abcdefghijklmnopqrstuvwxyz";

template <typename T> void vin(vector<T> &v) {
    for (auto &element : v) {
        cin >> element;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    vector<vi> a(n, vi(n));
    rep(i, n) { vin(a[i]); }
    unordered_map<int, pii> to_index;
    rep(i, n) {
        rep(j, n) { to_index[a[i][j]] = pii{i, j}; }
    }
    int q;
    cin >> q;
    vector<vi> bingo(n, vi(n, 0));

    rep(i, q) {
        int m;
        cin >> m;
        if (to_index.find(m) != to_index.end()) {
            int p = to_index[m].first;
            int q = to_index[m].second;
            bingo[p][q] = 1;
            int ok = 1;
            rep(k, n) { ok &= bingo[k][q]; }
            if (ok) {
                cout << i + 1 << '\n';
                return 0;
            }
            ok = 1;
            rep(k, n) { ok &= bingo[p][k]; }
            if (ok) {
                cout << i + 1 << '\n';
                return 0;
            }
            if (p == q) {
                int ok = 1;
                rep(k, n) { ok &= bingo[k][k]; }
                if (ok) {
                    cout << i + 1 << '\n';
                    return 0;
                }
            }
            if (p + q == n - 1) {
                int ok = 1;
                rep(k, n) { ok &= bingo[k][n - 1 - k]; }
                if (ok) {
                    cout << i + 1 << '\n';
                    return 0;
                }
            }
        }
    }
    cout << -1 << '\n';
    return 0;
}
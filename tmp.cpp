#include <bits/stdc++.h>
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
using namespace std;
#define ll long long
#define vi vector<int>
#define vl vector<long long>
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

int main() {
    // to do
    std::chrono::system_clock::time_point start, end; // 型は auto で可
    start = std::chrono::system_clock::now();         // 計測開始時間
    int q;
    int delled = -1;
    cin >> q;
    vl tree;
    rep(i, q) {
        int type;
        cin >> type;
        if (type == 1) {
            tree.push_back(0);
        } else if (type == 2) {
            ll t;
            cin >> t;
            for (size_t i = delled + 1; i < tree.size(); i++) {
                tree[i] += t;
            }
        } else if (type == 3) {
            ll h;
            int ans = 0;
            cin >> h;
            for (size_t i = delled + 1; i < tree.size(); i++) {
                if (tree[i] >= h) {
                    ans++;
                    delled++;
                }
            }
            cout << ans << el;
        }
    }
    end = std::chrono::system_clock::now(); // 計測終了時間
    double elapsed =
        std::chrono::duration_cast<std::chrono::milliseconds>(end - start)
            .count(); // 処理に要した時間をミリ秒に変換
    cout << elapsed << el;
}
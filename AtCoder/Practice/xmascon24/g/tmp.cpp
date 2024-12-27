#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int M = 500500;
vector<int> grundy(M);

void solve(int A, int B, int C, int D) {
    int N;
    cin >> N;
    vector<int> X(N);
    vector<int> G(N);
    for (int i = 0; i < N; i++)
        cin >> X[i];
    if (A == 4 && C == 1 && D == 0) {
        bool f = 0;
        for (int i = 0; i < N; i++) {
            if (X[i] == 1)
                f = 1;
        }
        if (f)
            cout << "White" << endl;
        else
            cout << "Black" << endl;
        return;
    }
    int sum = 0;
    for (int i = 0; i < N; i++) {
        if (A == 1)
            G[i] = X[i] % 4;
        else if (A == 2)
            G[i] = grundy[X[i]];
        else if (A == 3)
            G[i] = grundy[X[i] % 34];
        else
            G[i] = X[i];
    }
    for (int i = 0; i < N; i++) {
        sum ^= G[i];
    }
    if (B == 1 && C == 0 && D == 0) {
        for (int i = 0; i < N; i++) {
            if (G[i] > 0) {
                cout << "Black" << endl;
                return;
            }
        }
        cout << "White" << endl;
        return;
    }
    if (D == 1) {
        bool f = 0;
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            if (G[i] >= 2)
                f = 1;
            if (G[i] >= 1)
                cnt++;
        }
        if (!f) {
            if (cnt % 2 == 0)
                cout << "Black" << endl;
            else
                cout << "White" << endl;
        } else {
            if (sum == 0)
                cout << "White" << endl;
            else
                cout << "Black" << endl;
        }
        return;
    }
    if (sum == 0)
        cout << "White" << endl;
    else
        cout << "Black" << endl;
}

int main() {
    int A, B, C, D, T;
    cin >> A >> B >> C >> D >> T;
    if (A == 0 && B == 1 && D == 0) {
        for (int i = 0; i < T; i++) {
            cout << "Black" << endl;
        }
        return 0;
    }
    if (A == 0 && C == 1 && D == 0) {
        for (int i = 0; i < T; i++) {
            cout << "Black" << endl;
        }
        return 0;
    }
    if (A == 0 && B == 1 && D == 1) {
        for (int i = 0; i < T; i++) {
            int n;
            cin >> n;
            vector<int> x(n);
            for (int i = 0; i < n; i++) {
                cin >> x[i];
            }
            if (n == 1 and x[0] == 1) {
                cout << "White" << '\n';
            } else {
                cout << "Black" << '\n';
            }
        }
        return 0;
    }
    if (A == 2) {
        for (int i = 0; i < M; i++) {
            if (i % 2 == 0)
                grundy[i] = i / 2;
            else
                grundy[i] = grundy[i / 2];
        }
    }
    if (A == 3) {
        for (int i = 0; i < 17; i++)
            grundy[i] = i % 3;
        grundy[17] = 0;
        for (int i = 18; i < 34; i++) {
            if (i % 3 == 0)
                grundy[i] = 2;
            else if (i % 3 == 1)
                grundy[i] = 1;
            else
                grundy[i] = 0;
        }
        grundy[34] = 0;
    }
    while (T--) {
        solve(A, B, C, D);
    }
}

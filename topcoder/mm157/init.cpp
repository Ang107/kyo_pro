// C++17
#include <iostream>
#include <list>
using namespace std;

int main() {
    int N;
    int C;
    int K;
    cin >> N >> C >> K;

    int grid[N][N];
    int target[N][N];
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++)
            cin >> grid[r][c];

    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++)
            cin >> target[r][c];
    cout << "2\n"; // Two moves, one will place a block and the other slide a
                   // ball down
    for (int i = 0; i < N * N; i++) {
        int r = i % N;
        int c = i / N;
        if (grid[r][c] == 0 && target[r][c] == 0) {
            cout << r << " " << c << " B" << endl;
            cout.flush();
            grid[r][c] = -1;
            break;
        }
    }
    for (int i = 0; i < N * N; i++) {
        int r = i % N;
        int c = i / N;
        if (grid[r][c] > 0 && r + 1 < N && grid[r + 1][c] == 0) {
            cout << r << " " << c << " D" << endl;
            cout.flush();
            break;
        }
    }
}

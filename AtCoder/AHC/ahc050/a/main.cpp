#pragma GCC optimize("O3,unroll-loops,fast-math,omit-frame-pointer")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>
using namespace std;

// ───────────────────────────────────────────
//   基本型・定数
// ───────────────────────────────────────────
using i64 = long long;
constexpr int MAXN = 40;
constexpr int MAXE = MAXN * MAXN; // =1600

const int DX[4] = {-1, 1, 0, 0};
const int DY[4] = {0, 0, -1, 1};

// ───────────────────────────────────────────
//   軽量乱数（xorshift32）
// ───────────────────────────────────────────
static uint32_t xs = 2463534242u;
inline uint32_t xor32() {
    xs ^= xs << 13;
    xs ^= xs >> 17;
    return xs ^= xs << 5;
}
inline int randint(int l, int r) {
    return l + int(xor32() % uint32_t(r - l + 1));
}

// ───────────────────────────────────────────
//   時間計測
// ───────────────────────────────────────────
struct Timer {
    using C = chrono::high_resolution_clock;
    const C::time_point start;
    const double limit_ms;
    Timer(double ms) : start(C::now()), limit_ms(ms) {}
    inline bool over() const {
        return chrono::duration<double, std::milli>(C::now() - start).count() >=
               limit_ms;
    }
};

// ───────────────────────────────────────────
//   盤面クラス（リンク付き）
// ───────────────────────────────────────────
struct Board {
    int N;
    bool rock[MAXN][MAXN]{};
    bool avail[MAXN][MAXN]{};

    int L[MAXN][MAXN], R[MAXN][MAXN], U[MAXN][MAXN], D[MAXN][MAXN];

    inline void buildLinks() {
        for (int x = 0; x < N; ++x) {
            int last = -1;
            for (int y = 0; y < N; ++y) {
                if (rock[x][y])
                    last = y;
                L[x][y] = last;
            }
            last = N;
            for (int y = N - 1; y >= 0; --y) {
                if (rock[x][y])
                    last = y;
                R[x][y] = last;
            }
        }
        for (int y = 0; y < N; ++y) {
            int last = -1;
            for (int x = 0; x < N; ++x) {
                if (rock[x][y])
                    last = x;
                U[x][y] = last;
            }
            last = N;
            for (int x = N - 1; x >= 0; --x) {
                if (rock[x][y])
                    last = x;
                D[x][y] = last;
            }
        }
    }

    inline void addRock(int x, int y) {
        rock[x][y] = true;
        avail[x][y] = false;

        for (int j = y - 1; j >= 0 && R[x][j] > y; --j)
            R[x][j] = y;
        for (int j = y + 1; j < N && L[x][j] < y; ++j)
            L[x][j] = y;
        for (int i = x - 1; i >= 0 && D[i][y] > x; --i)
            D[i][y] = x;
        for (int i = x + 1; i < N && U[i][y] < x; ++i)
            U[i][y] = x;

        L[x][y] = R[x][y] = y;
        U[x][y] = D[x][y] = x;
    }

    inline pair<int, int> slide(int x, int y, int d) const {
        switch (d) {
        case 0:
            return {U[x][y] + 1, y};
        case 1:
            return {D[x][y] - 1, y};
        case 2:
            return {x, L[x][y] + 1};
        default:
            return {x, R[x][y] - 1};
        }
    }
};

// ───────────────────────────────────────────
//   1 回の貪欲＋乱択生成
// ───────────────────────────────────────────
struct Generator {
    const int N, E; // E = empty cell count(≤1600)
    const vector<pair<int, int>> &empties;
    bool rock0[MAXN][MAXN]; // 初期配置

    // 盤面・インデックス変換
    Board bd;
    int idxOf[MAXN][MAXN];  // [x][y]→idx (初期岩は -1)
    int xs[MAXE], ys[MAXE]; // idx→座標
    bool aliveIdx[MAXE];    // まだ岩で潰されていないマスか

    // 確率 DP 用
    double probA[MAXE]{}, probB[MAXE]{};

    // 出力
    vector<pair<int, int>> answer;

    Generator(int N_, const vector<pair<int, int>> &empties_,
              const bool rock_init[MAXN][MAXN])
        : N(N_), E((int)empties_.size()), empties(empties_) {

        // 座標⇔インデックス
        memset(idxOf, -1, sizeof(idxOf));
        for (int idx = 0; idx < E; ++idx) {
            auto [x, y] = empties[idx];
            xs[idx] = x;
            ys[idx] = y;
            idxOf[x][y] = idx;
        }
        memcpy(rock0, rock_init, sizeof(rock0));
    }

    double run() {
        // 盤面初期化
        bd.N = N;
        for (int i = 0; i < N; ++i) {
            memcpy(bd.rock[i], rock0[i], N * sizeof(bool));
            for (int j = 0; j < N; ++j)
                bd.avail[i][j] = !bd.rock[i][j];
        }
        bd.buildLinks();
        fill(aliveIdx, aliveIdx + E, true);

        // 確率初期化
        double *cur = probA, *nxt = probB;
        constexpr double EPS = 1e-15;
        constexpr double EPS2 = 1e-15;
        const double p0 = 1.0 / E;

        for (int idx = 0; idx < E; ++idx)
            cur[idx] = p0;

        double life = 1.0, score = 0.0;

        answer.clear();
        answer.reserve(E);

        // ターンループ
        for (int step = 0; step < E; ++step) {
            memset(nxt, 0, sizeof(double) * E);

            // 拡散
            for (int idx = 0; idx < E; ++idx) {
                double p = cur[idx];
                if (p == 0.0)
                    continue;
                int x = xs[idx], y = ys[idx];

                auto [a1, b1] = bd.slide(x, y, 0);
                nxt[idxOf[a1][b1]] += p * 0.25;
                auto [a2, b2] = bd.slide(x, y, 1);
                nxt[idxOf[a2][b2]] += p * 0.25;
                auto [a3, b3] = bd.slide(x, y, 2);
                nxt[idxOf[a3][b3]] += p * 0.25;
                auto [a4, b4] = bd.slide(x, y, 3);
                nxt[idxOf[a4][b4]] += p * 0.25;
            }

            // 最小確率 & tie-break
            static pair<int, int> cand[1600];
            int candCnt = 0;
            double bestP = 1e100;
            double bestNg = -1.0;

            for (int idx = 0; idx < E; ++idx)
                if (aliveIdx[idx]) {
                    double p = nxt[idx];
                    // 近傍最大 ×2
                    double ng = 0.0;
                    int x = xs[idx], y = ys[idx];
                    for (int d = 0; d < 4; ++d) {
                        int nx = x + DX[d], ny = y + DY[d];
                        if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                            int idn = idxOf[nx][ny];
                            if (idn != -1)
                                ng = max(ng, nxt[idn]);
                        }
                    }
                    ng *= 2.0;

                    bool better = false, equal = false;
                    if (p < bestP - EPS)
                        better = true;
                    else if (fabs(p - bestP) <= EPS) {
                        if (ng > bestNg + EPS2)
                            better = true;
                        else if (fabs(ng - bestNg) <= EPS2)
                            equal = true;
                    }

                    if (better) {
                        bestP = p;
                        bestNg = ng;
                        candCnt = 0;
                        cand[candCnt++] = {idx, 0};
                    } else if (equal) {
                        cand[candCnt++] = {idx, 0};
                    }
                }

            int chooseIdx = cand[randint(0, candCnt - 1)].first;
            int bx = xs[chooseIdx], by = ys[chooseIdx];

            double lost = nxt[chooseIdx];
            life -= lost;
            score += life;

            nxt[chooseIdx] = 0.0;
            aliveIdx[chooseIdx] = false;
            bd.addRock(bx, by);

            answer.emplace_back(bx, by);
            if (life <= 1e-12)
                break;

            // ポインタスワップ
            swap(cur, nxt);
        }
        return score;
    }
};

// ───────────────────────────────────────────
//   main
// ───────────────────────────────────────────
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M; // N==40
    vector<string> S(N);
    for (auto &row : S)
        cin >> row;

    bool rock_init[MAXN][MAXN]{};
    vector<pair<int, int>> empties;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) {
            rock_init[i][j] = (S[i][j] == '#');
            if (!rock_init[i][j])
                empties.emplace_back(i, j);
        }

    Timer tm(1900.0); // 1.9 秒走らせる
    Generator gen(N, empties, rock_init);

    double bestScore = -1.0;
    vector<pair<int, int>> bestAns;
    int iter = 0;
    while (!tm.over()) {
        double sc = gen.run();
        iter++;
        if (sc > bestScore) {
            bestScore = sc;
            bestAns = gen.answer;
        }
    }
    cerr << "iter: " << iter << '\n';

    for (auto [x, y] : bestAns)
        cout << x << ' ' << y << '\n';
    return 0;
}

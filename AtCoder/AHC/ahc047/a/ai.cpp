// Faster heuristic solver for "Lovely Language Model" (AtCoder HH)
// ------------------------------------------------------------------
//  * L1  In-place mutations + rollback
//  * L2  π warm-start 50 iter
//  * Row 近傍 Δ は progress に応じて線形 (DELTA_START → DELTA_END)
//  * progress = 経過時間 / 時間制限
//  * 文字変更は progress < 0.33 の間のみ許可
//  * プールサイズ 4 の multi-start Simulated Annealing
// ------------------------------------------------------------------
#include <bits/stdc++.h>
using namespace std;

/******************************* パラメータ ********************************/
constexpr int DELTA_START = 30; // 序盤の最大確率移動量 (%)
constexpr int DELTA_END = 10;   // 終盤の目標移動量   (%)
constexpr int DELTA_MIN = 1;    // これ以下にはしない (%)

/******************************* 乱数 **************************************/
static uint32_t xorshift() {
    static uint32_t y = 2463534242u;
    y ^= y << 13;
    y ^= y >> 17;
    return y ^= y << 5;
}
inline int randint(int l, int r) {
    return l + int(xorshift() % uint32_t(r - l + 1));
}
inline double rand01() { return double(xorshift()) / 4294967296.0; }

/******************************* 時間計測 **********************************/
class TimeKeeper {
    using Clock = chrono::high_resolution_clock;
    const Clock::time_point st_;
    const double lim_;
    double now_ = 0;

  public:
    explicit TimeKeeper(double ms) : st_(Clock::now()), lim_(ms) {}
    void update() {
        auto d = Clock::now() - st_;
        now_ = chrono::duration_cast<chrono::microseconds>(d).count() * 1e-3;
    }
    double now() const { return now_; }
    bool over() const { return now_ >= lim_; }
};

/************************** 定数と型エイリアス *****************************/
constexpr int N = 36, M = 12;
constexpr long long L = 1'000'000;
using Vec = array<double, M>;
using Mat = array<array<double, M>, M>;

/************************** ステーショナリ分布 *****************************/
static void stationary_iter(const Mat &P, Vec &v, int iters) {
    for (int it = 0; it < iters; ++it) {
        Vec nxt{};
        for (int i = 0; i < M; ++i) {
            double vi = v[i];
            if (vi == 0)
                continue;
            for (int j = 0; j < M; ++j)
                nxt[j] += vi * P[i][j];
        }
        double s = 0;
        for (double x : nxt)
            s += x;
        for (double &x : nxt)
            x /= s;
        v = nxt;
    }
}

/****************************** 出現確率 **********************************/
static double pattern_prob(const string &S, const array<char, M> &C,
                           const Mat &P, const Vec &pi) {
    array<double, M> cur{};
    for (int s = 0; s < M; ++s)
        if (C[s] == S[0])
            cur[s] = pi[s];

    for (size_t k = 1; k < S.size(); ++k) {
        array<double, M> nxt{};
        char ch = S[k];
        for (int s = 0; s < M; ++s)
            if (cur[s] > 0) {
                double vs = cur[s];
                for (int t = 0; t < M; ++t)
                    if (C[t] == ch)
                        nxt[t] += vs * P[s][t];
            }
        cur = nxt;
    }
    double sum = 0;
    for (double x : cur)
        sum += x;
    return sum;
}

/****************************** 構造体 *************************************/
struct Problem {
    array<string, N> S;
    array<int, N> P;
};
struct State {
    array<char, M> C;
    array<array<int, M>, M> A;
};

/****************************** 評価 ***************************************/
static double score(const Problem &pr, const array<char, M> &C, const Mat &P,
                    const Vec &pi) {
    double tot = 0;
    for (int i = 0; i < N; ++i) {
        double p = pattern_prob(pr.S[i], C, P, pi);
        double lambda = (L - int(pr.S[i].size()) + 1) * p;
        tot += pr.P[i] * (1.0 - exp(-lambda));
    }
    return tot;
}

/***************************** 近傍操作 ************************************/
struct DeltaLetter {
    int pos;
    char old, neu;
};
struct DeltaRow {
    int r, c1, c2, d;
};

static void apply_letter(State &s, DeltaLetter &d) {
    d.pos = randint(0, M - 1);
    d.old = s.C[d.pos];
    do
        d.neu = 'a' + randint(0, 5);
    while (d.neu == d.old);
    s.C[d.pos] = d.neu;
}
static void undo_letter(State &s, const DeltaLetter &d) { s.C[d.pos] = d.old; }

static void apply_row(State &s, DeltaRow &d, double progress) {
    d.r = randint(0, M - 1);
    d.c1 = randint(0, M - 1);
    do
        d.c2 = randint(0, M - 1);
    while (d.c2 == d.c1);

    int target = int(DELTA_START + (DELTA_END - DELTA_START) * progress + .5);
    int maxDelta = max(DELTA_MIN, target);
    maxDelta = min(maxDelta, s.A[d.r][d.c1]);
    if (maxDelta == 0) {
        d.d = 0;
        return;
    }
    d.d = randint(1, maxDelta);
    s.A[d.r][d.c1] -= d.d;
    s.A[d.r][d.c2] += d.d;
}
static void undo_row(State &s, const DeltaRow &d) {
    if (d.d == 0)
        return;
    s.A[d.r][d.c1] += d.d;
    s.A[d.r][d.c2] -= d.d;
}

/***************************************************************************
 *  焼きなましを関数化: run_sa(State init, double ms, const Problem&)
 ***************************************************************************/
struct SAResult {
    State st;
    double score;
    long long iter;
};

static SAResult run_sa(State cur, double limit_ms, const Problem &prob) {
    Mat P;
    for (int i = 0; i < M; ++i)
        for (int j = 0; j < M; ++j)
            P[i][j] = cur.A[i][j] * 0.01;
    Vec pi;
    pi.fill(1.0 / M);
    stationary_iter(P, pi, 200);

    double curScore = score(prob, cur.C, P, pi);
    State best = cur;
    double bestScore = curScore;

    constexpr double T0 = 1e3, T1 = 1e-1;
    TimeKeeper tk(limit_ms);
    tk.update();
    long long iter = 0;

    while (!tk.over()) {
        ++iter;
        if ((iter & 511) == 0)
            tk.update(); // 256 手ごとに時刻確認
        double prog = tk.now() / limit_ms;
        bool allowL = prog < 0.33;
        bool isLetter = allowL && (rand01() < 0.5);

        DeltaLetter dl;
        DeltaRow dr;
        Vec pi_new;
        if (isLetter) {
            apply_letter(cur, dl);
        } else {
            apply_row(cur, dr, prog);
            if (dr.d == 0)
                continue;
            P[dr.r][dr.c1] -= dr.d * 0.01;
            P[dr.r][dr.c2] += dr.d * 0.01;
            pi_new = pi;
            stationary_iter(P, pi_new, 50);
        }

        double nxt = isLetter ? score(prob, cur.C, P, pi)
                              : score(prob, cur.C, P, pi_new);
        double delta = nxt - curScore;
        double T = T0 * pow(T1 / T0, prog);
        bool acc = (delta >= 0) || (exp(delta / T) > rand01());

        if (acc) {
            curScore = nxt;
            if (!isLetter)
                pi = pi_new;
            if (curScore > bestScore) {
                best = cur;
                bestScore = curScore;
            }
        } else {
            if (isLetter)
                undo_letter(cur, dl);
            else {
                undo_row(cur, dr);
                P[dr.r][dr.c1] += dr.d * 0.01;
                P[dr.r][dr.c2] -= dr.d * 0.01;
            }
        }
    }
    return {best, bestScore, iter};
}

/******************************* main **************************************/
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    /* ---------- 入力 ---------- */
    int n, m;
    long long l;
    cin >> n >> m >> l; // 36 12 1e6 固定
    Problem prob;
    for (int i = 0; i < N; ++i) {
        cin >> prob.S[i] >> prob.P[i];
        prob.P[i] = pow(prob.P[i], 1.3);
    }
    /* ---------- overlap table (suffix/prefix 最大一致長) ---------- */
    int ov[36][36];
    for (int a = 0; a < N; ++a)
        for (int b = 0; b < N; ++b) {
            int mx = min(prob.S[a].size(), prob.S[b].size());
            ov[a][b] = 0;
            for (int t = 1; t <= mx; ++t)
                if (prob.S[a].substr(prob.S[a].size() - t) ==
                    prob.S[b].substr(0, t))
                    ov[a][b] = t;
        }

    /* ---------- 得点順インデックス top ---------- */
    vector<int> idx(N);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(),
         [&](int a, int b) { return prob.P[a] > prob.P[b]; });

    const int s1 = idx[0], s2 = idx[1], s3 = idx[2], s4 = idx[3], s5 = idx[4];

    /* ---------- 周期列ビルダ ---------- */
    auto build_peri = [&](int aIdx, int bIdx) -> string {
        string peri = prob.S[aIdx];
        int ol = ov[aIdx][bIdx];
        string tail = prob.S[bIdx].substr(ol);
        for (char c : tail) {
            if (peri.size() == 13)
                break;
            peri.push_back(c);
        }
        while (peri.size() < 13)
            peri.push_back("abcdef"[peri.size() % 6]);
        return peri;
    };

    /* ---------- make_state : 主枝100% 決定遷移モデル ---------- */
    auto make_state = [&](const string &peri) -> State {
        State st;
        int len = peri.size();
        for (int i = 0; i < M; ++i) {
            st.C[i] = peri[i % len];
            st.A[i].fill(0);
            st.A[i][(i + 1) % M] = 100;
        }
        return st;
    };

    /* ---------- プール (10 個) ---------- */
    const int POOL = 10;
    vector<pair<int, int>> combo = {{s1, s2}, {s2, s1}, {s1, s3}, {s3, s1},
                                    {s1, s4}, {s1, s5}, {s2, s3}, {s3, s2},
                                    {s2, s4}, {s2, s5}};
    vector<State> pool;
    pool.reserve(POOL);
    for (auto [a, b] : combo) {
        string peri = build_peri(a, b);
        pool.push_back(make_state(peri));
    }

    /* ---------- 1st stage : 0.1 s × 10 本 ---------- */
    const double SLICE_FIRST = 150.0; // ms
    vector<double> poolScore(POOL);
    vector<long long> poolIter(POOL);

    for (int k = 0; k < POOL; ++k) {
        SAResult res = run_sa(pool[k], SLICE_FIRST, prob);
        pool[k] = res.st;
        poolScore[k] = res.score;
        poolIter[k] = res.iter;
    }

    /* ---------- best 個体を 1.0 s 追加焼き ---------- */
    int bestIdx1 = int(max_element(poolScore.begin(), poolScore.end()) -
                       poolScore.begin());
    State bestState = pool[bestIdx1];
    cerr << combo[bestIdx1].first << " " << combo[bestIdx1].second << "\n";
    SAResult finalRes = run_sa(bestState, 450.0, prob); // 1 秒
    bestState = finalRes.st;
    long long totalIter =
        accumulate(poolIter.begin(), poolIter.end(), 0LL) + finalRes.iter;

    /* ---------- 出力 ---------- */
    for (int i = 0; i < M; ++i) {
        cout << bestState.C[i];
        for (int j = 0; j < M; ++j)
            cout << ' ' << bestState.A[i][j];
        cout << '\n';
    }

    cerr << "Total annealing iterations: " << totalIter << '\n';
    return 0;
}

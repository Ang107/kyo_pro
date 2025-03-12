#include <atcoder/dsu>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
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

uint64_t xorshift64() {
    static uint64_t y = 88172645463325252ULL;
    y ^= y << 13;
    y ^= y >> 7;
    y ^= y << 17;
    return y;
}
uint32_t xorshift() {
    static uint32_t y = 2463534242;
    y = y ^ (y << 13);
    y = y ^ (y >> 17);
    return y = y ^ (y << 5);
}
// 時間をDouble型で管理し、経過時間も取り出せるクラス
class TimeKeeperDouble {
  private:
    std::chrono::high_resolution_clock::time_point start_time_;
    double time_threshold_;

    double now_time_ = 0;

  public:
    // 時間制限をミリ秒単位で指定してインスタンスをつくる。
    TimeKeeperDouble(const double time_threshold)
        : start_time_(std::chrono::high_resolution_clock::now()),
          time_threshold_(time_threshold) {}

    // 経過時間をnow_time_に格納する。
    void setNowTime() {
        auto diff =
            std::chrono::high_resolution_clock::now() - this->start_time_;
        this->now_time_ =
            std::chrono::duration_cast<std::chrono::microseconds>(diff)
                .count() *
            1e-3; // ms
    }

    // 経過時間をnow_time_に取得する。
    double getNowTime() const { return this->now_time_; }

    // インスタンス生成した時から指定した時間制限を超過したか判定する。
    bool isTimeOver() const { return now_time_ >= time_threshold_; }
};
struct Init {
    Init() {
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
} init;
#define ll long long
#define vi vector<int>
#define vl vector<long long>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define elif else if
#define rep(i, n) for (int i = 0; i < static_cast<int>(n); i++)
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
//--------------------------------------
constexpr double TIME_LIMIT = 1900;
TimeKeeperDouble time_keeper(TIME_LIMIT);
//--------------------------------------
int N;
int M;
int H;
struct Input {
    vector<int> A;
    vector<pair<int, int>> Edge;
    vector<vector<int>> G;
    void input() {
        cin >> N >> M >> H;
        A = vector<int>(N);
        Edge = vector<pair<int, int>>(M);
        G = vector<vector<int>>(N, vector<int>());
        rep(i, N) { cin >> A[i]; }
        rep(i, M) {
            int u, v;
            cin >> u >> v;
            Edge[i] = {u, v};
            G[u].push_back(v);
            G[v].push_back(u);
        }
    }
};

struct Output {
    vector<int> p;
    void output() {
        rep(i, N - 1) { cout << p[i] << " "; }
        cout << p[N - 1] << el;
    }
};

struct Solver {
    Input input;
    Output output;

    Solver(const Input &input) : input(input) {}
    int bfs(int s, vector<int> &visited, vector<int> &p,
            vector<vector<int>> &child) {
        static deque<int> deq;
        deq.clear();
        deq.push_front(s);
        visited[s] = 1;
        p[s] = -1;
        int score = 0;
        score += input.A[s] * visited[s];
        while (!deq.empty()) {
            int v = deq.front();
            deq.pop_front();
            for (auto next : input.G[v]) {
                if (visited[next] == 0) {
                    visited[next] = visited[v] + 1;
                    score += input.A[next] * visited[next];
                    p[next] = v;
                    child[v].push_back(next);
                    if (visited[next] <= 10) {
                        deq.push_back(next);
                    }
                }
            }
        }
        return score;
    }
    tuple<int, vector<int>, vector<int>, vector<vector<int>>>
    evaluate(int root, int new_p, vector<int> p, vector<int> height,
             vector<vector<int>> child) {
        static mt19937 g(1);
        static deque<int> deq;
        static vector<int> free;
        int dis = height[new_p] + 1 - height[root];
        int diff = input.A[root] * dis;
        deq.clear();
        free.clear();

        if (p[root] != -1) {
            dump(root, p[root], child[p[root]]);
            child[p[root]].erase(find(all(child[p[root]]), root));
        }
        child[new_p].push_back(root);
        p[root] = new_p;
        height[root] = height[new_p] + 1;

        deq.push_back(root);
        while (!deq.empty()) {
            int v = deq.front();
            deq.pop_front();
            int dell_child = 0;
            rep(i, child[v].size() - 1) {
                dump(height[child[v][i]], height[child[v][i + 1]]);
                assert(height[child[v][i]] == height[child[v][i + 1]]);
            }
            for (auto next : child[v]) {
                if (height[next] + dis > 11) {
                    diff -= height[next] * input.A[next];
                    p[next] = -1;
                    height[next] = 1;
                    dell_child = 1;
                    free.push_back(next);
                } else {
                    height[next] = height[next] + dis;
                    diff += input.A[next] * dis;
                }
                deq.push_back(next);
            }
            if (dell_child == 1) {
                child[v].clear();
            }
        }
        vector<int> tmp(N);
        rep(i, N) { tmp[i] = i; }
        sort(all(tmp), [&](int a, int b) { return height[a] > height[b]; });
        for (auto s : tmp) {
            if (height[s] >= 11) {
                continue;
            }
            deque<int> deq;
            deq.push_back(s);
            while (!deq.empty()) {
                int v = deq.front();
                deq.pop_front();
                for (auto next : input.G[v]) {
                    if (height[v] < 11 and p[next] == -1 and
                        child[next].empty()) {
                        p[next] = v;
                        child[v].push_back(next);
                        height[next] = height[v] + 1;
                        deq.push_back(next);
                    }
                }
            }
        }
        return {diff, p, height, child};
    }

    void sa(int score, vector<vector<int>> &child, vector<int> &height) {
        // SA用パラメータ
        double startTemp = 1000.0; // 初期温度
        double endTemp = 0.0;      // 終了時温度

        // ベスト解を保持するなら初期化
        int bestScore = score;
        auto bestP = output.p;
        auto bestHeight = height;
        auto bestChild = child;

        // 開始時間 & 制限時間を取得（例）
        time_keeper.setNowTime();
        double startTime = time_keeper.getNowTime(); // 実際に必要な実装を行う
        double limitTime = TIME_LIMIT; // 合計実行可能時間(秒)など
        // または:
        //   double startTime = time_keeper.getNowTime();
        //   double limitTime = 2.95;  // 3秒制限なら、といった設定でもOK

        // イテレーションカウンタ
        int iteration = 0;

        vector<int> cand;
        while (true) {
            // 時間切れチェック
            time_keeper.setNowTime();
            if (time_keeper.isTimeOver()) {
                break;
            }

            // 経過時間の割合 progress = 経過時間 / 制限時間 (0～1)
            double nowTime = time_keeper.getNowTime(); // 現在の時刻
            double elapsed = nowTime - startTime;      // 経過時間
            double progress = elapsed / limitTime;
            if (progress > 1.0)
                progress = 1.0; // 上限クリップ

            // 今回の温度(線形スケジュールの例)
            double temperature = startTemp  (endTemp - startTemp) * progress;
            // あるいは幾何的に下げたい場合は:
            //   double temperature = startTemp * pow(endTemp / startTemp,
            //   progress);
            // などでも可

            iteration++;

            // 1. ランダムにrootを選ぶ
            int root = xorshift() % N;
            cand.clear();

            // 2. 候補を集める
            for (auto next : input.G[root]) {
                if (std::find(child[root].begin(), child[root].end(), next) ==
                        child[root].end() &&
                    height[next] < 11) {
                    cand.emplace_back(next);
                }
            }
            if (cand.empty()) {
                continue;
            }
            // 3. 候補から1つ選ぶ
            int new_p = cand[xorshift() % cand.size()];

            // 4. 高さ条件チェック
            // if (height[new_p] + 1 <= height[root]) {
            //     continue;
            // }

            // 5. 評価 (差分計算)
            auto [diff, np, nheight, nchild] =
                evaluate(root, new_p, output.p, height, child);

            // 6. SAの受理判定
            if (diff >= 0) {
                // 改善 or 同等なら常に受理
                score += diff;
                output.p = np;
                height = nheight;
                child = nchild;
            } else {
                // 悪化の場合は温度に応じて確率的に受理
                double prob = std::exp(double(diff) / temperature);
                double r = (xorshift() & 0xFFFF) / double(0x10000);
                if (r < prob) {
                    score += diff;
                    output.p = np;
                    height = nheight;
                    child = nchild;
                }
            }

            // 7. ベスト解の更新 (お好みで)
            if (score > bestScore) {
                bestScore = score;
                bestP = output.p;
                bestHeight = height;
                bestChild = child;
            }
        }

        // 終了後、ベスト解を戻す
        output.p = bestP;
        height = bestHeight;
        child = bestChild;
    }
    void solve() {
        int cnt = 0;
        vector<int> order(N);
        rep(i, N) { order[i] = i; }
        std::mt19937 g(1);
        vector<int> visited(N);
        vector<int> p(N);
        vector<int> height(N);
        int best_score = 0;
        vector<vector<int>> best_child(N, vector<int>());
        vector<vector<int>> child(N, vector<int>());
        rep(i, N) {
            sort(all(input.G[i]),
                 [&](int a, int b) { return input.A[a] < input.A[b]; });
        }

        while (1) {
            cnt++;
            if (cnt % 10 == 0) {
                time_keeper.setNowTime();
                if (time_keeper.getNowTime() > 500) {
                    break;
                }
            }
            shuffle(all(order), g);

            rep(i, N) {
                visited[i] = 0;
                child[i].clear();
            }
            int score = 0;
            rep(i, N) {
                if (visited[order[i]] == 0) {
                    score += bfs(order[i], visited, p, child);
                }
            }
            // cerr << "score: " << score << el;
            if (chmax(best_score, score)) {
                output.p = p;
                best_child = child;
                height = visited;
            }
        }
        // cerr << "cnt: " << cnt << el;
        // cerr << "best_score: " << best_score << el;
        sa(best_score, best_child, height);
        output.output();
        // rep(i, N) {
        //     if (output.p[i] != -1) {
        //         cerr << i << " " << output.p[i] << el;
        //     }
        // }
    }
};

int main(int argc, char *argv[]) {
    // seed = argv[1];
    time_keeper = TimeKeeperDouble(TIME_LIMIT);
    Input input;
    input.input();
    Solver solver(input);
    solver.solve();
    return 0;
}
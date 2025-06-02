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
#define CPP_DUMP_SET_OPTION_GLOBAL(...) /**/
#else
#define dump(...)
#define CPP_DUMP_SET_OPTION(...)
#define CPP_DUMP_SET_OPTION_GLOBAL(...)
#define CPP_DUMP_DEFINE_EXPORT_OBJECT(...)
#define CPP_DUMP_DEFINE_EXPORT_ENUM(...)
#define CPP_DUMP_DEFINE_EXPORT_OBJECT_GENERIC(...)
#endif

// --------------------------- 初期化 --------------------------------
struct Init {
    Init() {
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
} init;

// ------------------------- 型エイリアス ----------------------------
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

// ------------------------- 乱数ツール -----------------------------
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
inline double randReal(double L, double R) { return L + (R - L) * rand01(); }

// ----------------------- 時間計測クラス ---------------------------
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

// ------------------------- 色ベクトル構造体 -------------------------
struct Color {
    double C, M, Y;
    Color() : C(0), M(0), Y(0) {}
    Color(double _C, double _M, double _Y) : C(_C), M(_M), Y(_Y) {}
    Color operator-(const Color &o) const {
        return Color(C - o.C, M - o.M, Y - o.Y);
    }
    Color operator*(double t) const { return Color(C * t, M * t, Y * t); }
    Color operator+(const Color &o) const {
        return Color(C + o.C, M + o.M, Y + o.Y);
    }
};
inline double dot(const Color &a, const Color &b) {
    return a.C * b.C + a.M * b.M + a.Y * b.Y;
}
inline double norm2(const Color &a) { return dot(a, a); }

// ------------------------ 入力読み込み構造体 ------------------------
struct Input {
    int N, K, H, T, D;
    vector<Color> tubes;
    vector<Color> targets;
    void input() {
        cin >> N >> K >> H >> T >> D;
        tubes.resize(K);
        targets.resize(H);
        rep(i, K) { cin >> tubes[i].C >> tubes[i].M >> tubes[i].Y; }
        rep(i, H) { cin >> targets[i].C >> targets[i].M >> targets[i].Y; }
    }
};

// ------------------ 現在の調合ウェルの状態計算 ----------------------
struct ColorState {
    double _C, _M, _Y;
    double amount_sum;
    ColorState(double C, double M, double Y, double amount)
        : _C(C), _M(M), _Y(Y), amount_sum(amount) {}
    void add_paint(double C, double M, double Y, double amount) {
        if (amount == 0.0)
            return;
        _C = (_C * amount_sum + C * amount) / (amount_sum + amount);
        _M = (_M * amount_sum + M * amount) / (amount_sum + amount);
        _Y = (_Y * amount_sum + Y * amount) / (amount_sum + amount);
        amount_sum += amount;
    }
    double calc_error(Color target) {
        return sqrt((target.C - _C) * (target.C - _C) +
                    (target.M - _M) * (target.M - _M) +
                    (target.Y - _Y) * (target.Y - _Y)) *
               10000.0;
    }
};

// ----------------------- 操作の表現構造体 --------------------------
struct Action {
    int tube_index;
    bool add_tube;
    double amount;
    int block_cnt;
    Action() : tube_index(0), add_tube(false), amount(0), block_cnt(0) {}
    Action(int tube_index, bool add_tube, double amount, int block_cnt)
        : tube_index(tube_index), add_tube(add_tube), amount(amount),
          block_cnt(block_cnt) {}
};

// ----------------------- パレット管理クラス ------------------------
struct Palette {
    int tube_index, si, sj, lines, block_cnt;
    double amount;
    vector<pair<int, int>> coordinates;
    Palette() : tube_index(0), si(0), sj(0), lines(0), amount(0) {}
    Palette(int index, int i, int j, int lines, int amount)
        : tube_index(index), si(i), sj(j), lines(lines), amount(amount) {
        block_cnt = lines * 19;
    }
    void setup() {
        block_cnt = lines * 19;
        rep(i, lines) {
            if (i % 2 == 0) {
                for (int j = 0; j < 19; j++) {
                    coordinates.push_back({si + i, sj + j});
                }
            } else {
                for (int j = 18; j >= 0; j--) {
                    coordinates.push_back({si + i, sj + j});
                }
            }
        }
    }
    vector<int> get_sep_ans(int bl) {
        if (block_cnt == bl) {
            return {};
        } else {
            return {
                4,
                coordinates[bl - 1].first,
                coordinates[bl - 1].second,
                coordinates[bl].first,
                coordinates[bl].second,
            };
        }
    }
    vector<int> get_open_close_ans() { return {4, si, sj - 1, si, sj}; }
    Action discretization(double am, int mode = 1) {
        Action res;
        res.tube_index = tube_index;
        assert(mode == 1 or mode == -1);
        if (mode == -1) {
            if (am <= amount) {
                res.add_tube = false;
                res.block_cnt = floor(am / (amount / (double)block_cnt));
                res.amount = (amount / (double)block_cnt) * res.block_cnt;
            } else {
                res.add_tube = true;
                res.block_cnt = floor(am / ((amount + 1) / (double)block_cnt));
                res.amount = ((amount + 1) / (double)block_cnt) * res.block_cnt;
            }
        } else {
            if (am <= amount) {
                res.add_tube = false;
                res.block_cnt = ceil(am / (amount / (double)block_cnt));
                res.amount = (amount / (double)block_cnt) * res.block_cnt;
            } else {
                res.add_tube = true;
                res.block_cnt = ceil(am / ((amount + 1) / (double)block_cnt));
                res.amount = ((amount + 1) / (double)block_cnt) * res.block_cnt;
            }
        }
        return res;
    }
};

// ------------------------ Solver クラス ----------------------------
struct Solver {
    const Input input;
    vector<vector<int>> ans;
    vector<Palette> palettes;
    int max_colors;
    int tubes_cnt = 0;
    int err_sum = 0;

    Solver(const Input &input) : input(input) {}

    bool normalization(vector<double> &coefficients) {
        double sum_ = 0;
        for (auto a : coefficients)
            sum_ += a;
        if (sum_ == 0.0)
            return false;
        for (auto &a : coefficients)
            a /= sum_;
        return true;
    }
    vector<Action> discretization(vector<double> &coefficients) {
        vector<Action> res;
        rep(i, input.K) {
            if (coefficients[i] == 0.0)
                continue;
            Action d = palettes[i].discretization(coefficients[i]);
            coefficients[i] = d.amount;
            res.push_back(d);
        }
        return res;
    }
    double get_cost(Color target, const vector<double> &coefficients) {
        ColorState s(0, 0, 0, 0);
        double amount_sum = 0;
        rep(i, input.K) {
            auto tube = input.tubes[i];
            double amount = coefficients[i];
            s.add_paint(tube.C, tube.M, tube.Y, amount);
            amount_sum += amount;
        }
        double res = 0;
        res += s.calc_error(target);
        res += (amount_sum - 1.0) * input.D;
        return res;
    }
    double get_err(Color target, const vector<double> &coefficients) {
        ColorState s(0, 0, 0, 0);
        rep(i, input.K) {
            auto tube = input.tubes[i];
            double amount = coefficients[i];
            s.add_paint(tube.C, tube.M, tube.Y, amount);
        }
        double res = 0;
        res += s.calc_error(target);
        return res;
    }

    // --- 乱択＋hill climb 部分（元の実装）---
    pair<vector<double>, vector<Action>> random(Color target) {
        double min_cost = inf;
        vector<double> best_coefficients(input.K, 0.0);
        vector<Action> best_actions;

        TimeKeeper tk(1.7);
        int iter = 0;
        while (true) {
            iter++;
            if (iter % 100 == 0) {
                tk.update();
                if (tk.over()) {
                    cerr << "random iter: " << iter << el;
                    break;
                }
            }
            int choose_num = randint(1, min(input.K, max_colors));
            vector<double> coefficients(input.K, 0.0);
            rep(cnt, choose_num) {
                coefficients[xorshift() % input.K] += rand01();
            }
            normalization(coefficients);
            vector<Action> actions = discretization(coefficients);
            double res = get_cost(target, coefficients);
            if (res < min_cost) {
                min_cost = res;
                best_coefficients = coefficients;
                best_actions = actions;
            }
        }
        return {best_coefficients, best_actions};
    }

    // hill climb 部分（元の実装）
    // pair<vector<double>, vector<Action>>
    // clime(Color target, const vector<double> &coefficients,
    //       const vector<Action> &actions) {
    //     double min_cost = get_cost(target, coefficients);
    //     vector<double> best_coefficients = coefficients;
    //     vector<Action> best_actions = actions;
    //     int cnt = 0;
    //     rep(i, input.K) {
    //         if (best_coefficients[i] > 0)
    //             cnt++;
    //     }
    //     TimeKeeper tk(1);
    //     int iter = 0;
    //     while (true) {
    //         iter++;
    //         if (iter % 100 == 0) {
    //             tk.update();
    //             if (tk.over())
    //                 break;
    //         }
    //         int index = xorshift() % input.K;
    //         double diff = randReal(-0.2, 0.2);
    //         if (diff < 0 && best_coefficients[index] == 0.0)
    //             continue;
    //         if (diff > 0 && cnt == max_colors &&
    //             best_coefficients[index] == 0.0)
    //             continue;
    //         vector<double> tmp = best_coefficients;
    //         if (tmp[index] == 0 && diff > 0)
    //             cnt++;
    //         tmp[index] += diff;
    //         if (tmp[index] < 0.0) {
    //             tmp[index] = 0.0;
    //             cnt--;
    //         }
    //         normalization(tmp);
    //         vector<Action> nxt = discretization(tmp);
    //         double res = get_cost(target, tmp);
    //         if (res < min_cost) {
    //             min_cost = res;
    //             swap(best_coefficients, tmp);
    //             swap(best_actions, nxt);
    //         }
    //     }
    //     return {best_coefficients, best_actions};
    // }
    pair<vector<double>, vector<Action>>
    clime(Color target, const vector<double> &init_coeffs,
          const vector<Action> &init_actions) {
        // ─────────────────────────────────────────────
        // 1) 初期設定
        double best_cost = get_cost(target, init_coeffs);
        vector<double> best_coeffs = init_coeffs;
        vector<Action> best_actions = init_actions;

        // 現在の解 (current) とそのコスト
        vector<double> curr_coeffs = init_coeffs;
        vector<Action> curr_actions = init_actions;
        double curr_cost = best_cost;

        // 係数に非ゼロ要素が何本あるかを数えておく
        int curr_cnt = 0;
        rep(i, input.K) if (curr_coeffs[i] > 0.0) curr_cnt++;

        // 2) 温度スケジューリングの準備
        //    - 初期温度 T0 = 1.0 とし、終了直前 T_end ≈ 1e-3 まで下げる
        const double T0 = 1.0;
        const double T_end = 1e-3;

        TimeKeeper tk(1); // 1 ミリ秒だけ焼きなましに使う（時間制限）
        int iter = 0;

        while (true) {
            iter++;
            if (iter % 50 == 0) {
                tk.update();
                if (tk.over())
                    break;
            }

            // 3) 温度を現在時刻に応じて線形・反比例的に下げる
            //    - 残り時間が減るほど温度 T が小さくなる
            double elapsed = tk.now();               // 経過〔ms〕
            double limit = 1.0;                      // 制限時間 1.0 ms
            double frac = min(1.0, elapsed / limit); // [0,1]
            // 単純に線形減衰: T = T0 * (1 - frac) + T_end * frac
            double T = T0 * (1.0 - frac) + T_end * frac;

            // 4) 更新候補をつくる
            //    - 元 hill climb と同様に 1 つの係数をランダムに +- 乱数で振る
            //    - ただし「非ゼロ本数 cnt」が max_colors を超えないように制約
            int idx = xorshift() % input.K;
            double diff = randReal(-0.2, 0.2);

            // 「減少方向 diff<0 なのにすでに 0 ならスキップ」
            if (diff < 0.0 && curr_coeffs[idx] == 0.0) {
                continue;
            }
            // 「増加方向 diff>0 なのに max_colors 本まで達していて、かつ idx が
            // 0 ならスキップ」
            if (diff > 0.0 && curr_cnt == max_colors &&
                curr_coeffs[idx] == 0.0) {
                continue;
            }

            // 5) 探索点をつくる（tmp系）
            vector<double> tmp_coeffs = curr_coeffs;
            int tmp_cnt = curr_cnt;
            if (tmp_coeffs[idx] == 0.0 && diff > 0.0) {
                tmp_cnt++; // 新たに非ゼロ本数が増える
            }
            tmp_coeffs[idx] += diff;
            if (tmp_coeffs[idx] < 0.0) {
                tmp_coeffs[idx] = 0.0;
                tmp_cnt--;
            }
            // 6) 正規化して和＝1 に
            normalization(tmp_coeffs);

            // 7) tmp 値から Action を作る
            vector<Action> tmp_actions = discretization(tmp_coeffs);
            //    └── ここまでで「新しい候補点(tmp)」が完成

            // 8) 候補のコストを計算
            double tmp_cost = get_cost(target, tmp_coeffs);

            // 9) 受容判定：改善するなら無条件、悪化するなら確率 accept_prob
            // で受け入れ
            if (tmp_cost < curr_cost) {
                // 改善なら確実に受け入れ
                curr_coeffs = tmp_coeffs;
                curr_actions = tmp_actions;
                curr_cost = tmp_cost;
                curr_cnt = tmp_cnt;
            } else {
                // 悪化する場合、確率 p = exp(-(tmp_cost - curr_cost)/T)
                // で受け入れ
                double delta = tmp_cost - curr_cost;
                double p_accept = exp(-delta / max(T, 1e-9));
                if (rand01() < p_accept) {
                    curr_coeffs = tmp_coeffs;
                    curr_actions = tmp_actions;
                    curr_cost = tmp_cost;
                    curr_cnt = tmp_cnt;
                }
            }

            // 10) 全体最良解との比較
            if (curr_cost < best_cost) {
                best_cost = curr_cost;
                best_coeffs = curr_coeffs;
                best_actions = curr_actions;
            }
        }

        // 11) 結果を返す (最良解)
        return {best_coeffs, best_actions};
    }
    // --- 2本・3本混色解析解（max_colors 本以下に制限）---
    vector<double> solveByProjection(const Color &target, int max_c) {
        int K = input.K;
        vector<double> bestCoeffs(K, 0.0);
        double bestErr2 = 1e300;

        // 3本混色 (max_c >= 3)
        if (max_c >= 3) {
            rep(i, K) for (int j = i + 1; j < K; j++) for (int k = j + 1; k < K;
                                                           k++) {
                Color pi = input.tubes[i];
                Color pj = input.tubes[j];
                Color pk = input.tubes[k];
                Color ei = Color(pi.C - pk.C, pi.M - pk.M, pi.Y - pk.Y);
                Color ej = Color(pj.C - pk.C, pj.M - pk.M, pj.Y - pk.Y);
                Color v =
                    Color(target.C - pk.C, target.M - pk.M, target.Y - pk.Y);

                double m00 = dot(ei, ei);
                double m01 = dot(ei, ej);
                double m11 = dot(ej, ej);
                double b0 = dot(ei, v);
                double b1 = dot(ej, v);
                double det = m00 * m11 - m01 * m01;
                if (det == 0.0)
                    continue;

                double alpha = (b0 * m11 - b1 * m01) / det;
                double beta = (m00 * b1 - m01 * b0) / det;
                double gamma = 1.0 - alpha - beta;
                if (alpha >= 0.0 && beta >= 0.0 && gamma >= 0.0) {
                    Color mix =
                        Color(pi.C * alpha + pj.C * beta + pk.C * gamma,
                              pi.M * alpha + pj.M * beta + pk.M * gamma,
                              pi.Y * alpha + pj.Y * beta + pk.Y * gamma);
                    Color diff = Color(mix.C - target.C, mix.M - target.M,
                                       mix.Y - target.Y);
                    double err2 = norm2(diff);
                    if (err2 < bestErr2) {
                        bestErr2 = err2;
                        fill(bestCoeffs.begin(), bestCoeffs.end(), 0.0);
                        bestCoeffs[i] = alpha;
                        bestCoeffs[j] = beta;
                        bestCoeffs[k] = gamma;
                    }
                }
            }
        }

        // 2本混色 (max_c >= 2)
        if (max_c >= 2) {
            rep(i, K) for (int j = i + 1; j < K; j++) {
                Color p = input.tubes[i];
                Color q = input.tubes[j];
                Color d = Color(q.C - p.C, q.M - p.M, q.Y - p.Y);
                Color tp =
                    Color(target.C - p.C, target.M - p.M, target.Y - p.Y);

                double dd = norm2(d);
                if (dd == 0.0)
                    continue;
                double u = dot(tp, d) / dd;
                u = (u < 0.0 ? 0.0 : (u > 1.0 ? 1.0 : u));
                Color mix =
                    Color(p.C * u + q.C * (1.0 - u), p.M * u + q.M * (1.0 - u),
                          p.Y * u + q.Y * (1.0 - u));
                Color diff =
                    Color(mix.C - target.C, mix.M - target.M, mix.Y - target.Y);
                double err2 = norm2(diff);
                if (err2 < bestErr2) {
                    bestErr2 = err2;
                    fill(bestCoeffs.begin(), bestCoeffs.end(), 0.0);
                    bestCoeffs[i] = u;
                    bestCoeffs[j] = 1.0 - u;
                }
            }
        }

        // 1本最近似 (max_c >= 1)
        if (max_c >= 1) {
            double bestErr1 = 1e300;
            int bestIdx = 0;
            rep(i, K) {
                Color diff = Color(input.tubes[i].C - target.C,
                                   input.tubes[i].M - target.M,
                                   input.tubes[i].Y - target.Y);
                double err2 = norm2(diff);
                if (err2 < bestErr1) {
                    bestErr1 = err2;
                    bestIdx = i;
                }
            }
            if (bestErr1 < bestErr2) {
                fill(bestCoeffs.begin(), bestCoeffs.end(), 0.0);
                bestCoeffs[bestIdx] = 1.0;
            }
        }

        return bestCoeffs;
    }

    // ─────── rantaku を条件分岐＋比較付きに書き換え ───────
    pair<vector<double>, vector<Action>> rantaku(Color target) {
        // vector<double> proj_coeffs = solveByProjection(target, max_colors);
        // vector<Action> proj_actions = discretization(proj_coeffs);
        // double proj_cost = get_cost(target, proj_coeffs);
        // auto [clim_coeffs, clime_actions] =
        //     clime(target, proj_coeffs, proj_actions);
        // return {clim_coeffs, clime_actions};
        // １）乱択＋hill climb でベースライン取得
        auto [random_coeffs, random_actions] = random(target);
        double random_cost = get_cost(target, random_coeffs);

        // ２）解析解（max_colors 本まで）を取得
        vector<double> proj_coeffs = solveByProjection(target, max_colors);
        vector<Action> proj_actions = discretization(proj_coeffs);
        double proj_cost = get_cost(target, proj_coeffs);

        // ３）低コスト側を採用
        if (proj_cost < random_cost) {
            auto [clim_coeffs, clime_actions] =
                clime(target, proj_coeffs, proj_actions);
            return {clim_coeffs, clime_actions};
        } else {
            auto [clim_coeffs, clime_actions] =
                clime(target, random_coeffs, random_actions);
            return {clim_coeffs, clime_actions};
        }
    }

    void setup() {
        palettes = vector<Palette>(input.K);
        rep(i, 20) palettes[i % input.K].lines += 1;
        int now = 0;
        rep(i, input.K) {
            palettes[i].tube_index = i;
            palettes[i].si = now;
            palettes[i].sj = 1;
            now += palettes[i].lines;
            palettes[i].setup();
        }
        // 縦仕切り (v_{i,j})
        rep(i, 20) {
            cout << "1";
            rep(j, 18) cout << " 0";
            cout << "\n";
        }
        // 横仕切り (h_{i,j})
        rep(i, input.K) {
            Palette &palette = palettes[i];
            rep(j, palette.lines - 1) {
                cout << "0 ";
                if (j % 2 == 0) {
                    rep(k, 18) cout << "1 ";
                    cout << "0\n";
                } else {
                    cout << "0";
                    rep(k, 18) cout << " 1";
                    cout << "\n";
                }
            }
            if (i != input.K - 1) {
                cout << "0 ";
                rep(k, 19) {
                    cout << "1";
                    if (k == 18)
                        cout << "\n";
                    else
                        cout << " ";
                }
            }
        }
    }

    void update(Color target, const vector<double> &coefficients,
                const vector<Action> &actions) {
        double min_cost = inf;
        pair<int, int> best_pair;
        rep(i, input.K) {
            for (int j = i + 1; j < input.K; j++) {
                ColorState c(0, 0, 0, 0);
                c.add_paint(input.tubes[i].C, input.tubes[i].M,
                            input.tubes[i].Y, 0.5);
                c.add_paint(input.tubes[j].C, input.tubes[j].M,
                            input.tubes[j].Y, 0.5);
                int new_cost = c.calc_error(target) + input.D;
                if (new_cost < min_cost) {
                    min_cost = new_cost;
                    best_pair = {i, j};
                }
            }
        }
        double err = get_err(target, coefficients);
        err_sum += err;
        if (min_cost < get_cost(target, coefficients)) {
            ans.push_back({1, 0, 0, best_pair.first});
            ans.push_back({1, 0, 0, best_pair.second});
            ans.push_back({2, 0, 0});
            ans.push_back({3, 0, 0});
            tubes_cnt += 2;
            return;
        }
        vector<vector<int>> sep;
        int cnt = 0;
        int index = -1;
        rep(i, input.K) {
            if (coefficients[i] > 0) {
                cnt += 1;
                index = i;
            }
        }
        if (actions.size() == 1) {
            Action action = actions[0];
            ans.push_back({1, 0, 0, action.tube_index});
            ans.push_back({2, 0, 0});
            tubes_cnt += 1;
            return;
        }
        rep(i, actions.size()) {
            Action action = actions[i];
            Palette &palette = palettes[action.tube_index];
            if (action.add_tube) {
                palette.amount += 1.0;
                ans.push_back({1, palette.si, palette.sj, palette.tube_index});
                tubes_cnt += 1;
            }
            vector<int> tmp = palette.get_sep_ans(action.block_cnt);
            dump(tmp);

            if (!tmp.empty()) {
                ans.push_back(tmp);
                sep.push_back(tmp);
            }
            palette.amount -= action.amount;
            tmp = palette.get_open_close_ans();
            ans.push_back(tmp);
            sep.push_back(tmp);
        }
        ans.push_back({2, 0, 0});
        ans.push_back({3, 0, 0});
        reverse(all(sep));
        for (const auto &s : sep) {
            ans.push_back(s);
        }
    }

    void print() {
        for (const auto &row : ans) {
            for (size_t i = 0; i < row.size(); ++i) {
                cout << row[i];
                if (i + 1 < row.size())
                    cout << ' ';
            }
            cout << '\n';
        }
    }

    void solve() {
        setup();
        rep(i, input.H) {
            auto target_color = input.targets[i];
            int remains_T = input.T - ans.size() - (input.H - i) * 3 - input.H;
            max_colors = max(1, int(floor(remains_T / (4.0 * (input.H - i)))));
            auto [coefficients, actions] = rantaku(target_color);
            update(target_color, coefficients, actions);
        }
        cerr << ans.size() << " / " << input.T << el;
        cerr << "D: " << input.D << " err_cost: " << err_sum
             << " tubes_cost: " << (tubes_cnt - input.H) * input.D
             << " tubes_cnt: " << tubes_cnt << el;
        if (ans.size() <= input.T) {
            print();
            cerr << input.T << " " << ans.size() << el;
        }
    }
};

// ----------------------------- main --------------------------------
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Input input;
    input.input();
    Solver solver(input);
    solver.solve();
    return 0;
}

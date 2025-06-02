#include <bits/stdc++.h>

// ────────────────────────────────────────────────────────────
//   カラーミキサ・ソルバー（リファクタリング版／和訳コメント）
//   ・アルゴリズムは元実装と同一。
//   ・読みやすさ・保守性を重視して構造体と命名を整理。
//   ・「using namespace std;」「rep マクロ」を許可。
// ────────────────────────────────────────────────────────────

using namespace std;
using i64 = long long;
using u32 = uint32_t;

//--- rep マクロ（0‥n-1 ループ）---
#define rep(i, n) for (int i = 0; (i) < int(n); ++(i))

//--- デバッグ用マクロ（LOCAL 定義時のみ有効）---
#ifdef LOCAL
#include "cpp-dump.hpp"
#define DEBUG(...) cpp_dump(__VA_ARGS__)
#else
#define DEBUG(...) (void)0
#endif

// ──────────────────────────────
//   0. 乱数ユーティリティ（xorshift32）
// ──────────────────────────────
namespace rnd {
inline u32 xorshift32() {
    static u32 y = 2463534242u;
    y ^= y << 13;
    y ^= y >> 17;
    return y ^= y << 5;
}
inline int uniform_int(int l, int r) {
    return l + int(xorshift32() % u32(r - l + 1));
}
inline double uniform01() { return double(xorshift32()) / 4294967296.0; }
inline double uniform_real(double L, double R) {
    return L + (R - L) * uniform01();
}
} // namespace rnd

// ──────────────────────────────
//  1. 経過時間管理クラス
// ──────────────────────────────
class TimeKeeper {
    using Clock = chrono::high_resolution_clock;
    const Clock::time_point start;
    const double limit_ms; // 制限時間[ms]
    double now_ms = 0;     // 現在経過時間[ms]
  public:
    explicit TimeKeeper(double ms) : start(Clock::now()), limit_ms(ms) {}
    void update() {
        auto d = Clock::now() - start;
        now_ms = chrono::duration_cast<chrono::microseconds>(d).count() * 1e-3;
    }
    double now() const { return now_ms; }
    bool over() const { return now_ms >= limit_ms; }
};

// ──────────────────────────────
//  2. 基本色構造体・演算
// ──────────────────────────────
struct Color {
    double c, m, y; // シアン, マゼンタ, イエロー
    Color(double _c = 0, double _m = 0, double _y = 0) : c(_c), m(_m), y(_y) {}
    Color operator+(const Color &o) const {
        return {c + o.c, m + o.m, y + o.y};
    }
    Color operator-(const Color &o) const {
        return {c - o.c, m - o.m, y - o.y};
    }
    Color operator*(double t) const { return {c * t, m * t, y * t}; }
};
inline double dot(const Color &a, const Color &b) {
    return a.c * b.c + a.m * b.m + a.y * b.y;
}
inline double norm2(const Color &a) { return dot(a, a); } // 二乗ノルム

// ──────────────────────────────
//  3. 調合中ウェルの状態
// ──────────────────────────────
struct MixState {
    double c = 0, m = 0, y = 0; // 現在色
    double amt = 0;             // 総量
    void add(double dc, double dm, double dy, double da) {
        if (da == 0)
            return;
        c = (c * amt + dc * da) / (amt + da);
        m = (m * amt + dm * da) / (amt + da);
        y = (y * amt + dy * da) / (amt + da);
        amt += da;
    }
    double error(const Color &tgt) const {
        double d2 = (tgt.c - c) * (tgt.c - c) + (tgt.m - m) * (tgt.m - m) +
                    (tgt.y - y) * (tgt.y - y);
        return sqrt(d2) * 10000.0;
    }
};

// ──────────────────────────────
//  4. パレット上の 1 チューブ管理
// ──────────────────────────────
struct Action {           // 操作1回分
    int tube_idx = 0;     // チューブ番号
    bool add_new = false; // 新規チューブ設置か？
    double real_amt = 0;  // 実量
    int use_blocks = 0;   // 分子
    int blocks = 0;       // 分母
};

struct Palette {
    int tube_idx = 0;
    int si = 0, sj = 0; // 左上座標
    int ti = 0,
        tj = 0;          // 一番後ろの座標(絵具を入れる場所)
    int lines = 0;       // 行数(=高さ)
    double cap = 0;      // 保有量
    int used_blocks = 0; // 絵具が入っているマスの数(分母の最小値)
    int blocks = 0;      // 使えるマスのMax(分母の最大値)

    vector<pair<int, int>> path; // ハミルトン経路(行→列ジグザグ)

    // path, ti, tj, blocksを初期化する
    void build() {
        blocks = lines * 19;
        path.reserve(blocks);
        rep(i, lines) {
            if (i % 2 == 0) {
                rep(j, 19) path.emplace_back(si + i, sj + j);
            } // →
            else {
                for (int j = 18; j >= 0; --j)
                    path.emplace_back(si + i, sj + j);
            } // ←
        }
        ti = path[blocks - 1].first;
        tj = path[blocks - 1].second;
    }

    // ブロック分割指令
    vector<int> cmd_sep(int bl) const {
        if (bl == int(path.size()))
            return {};
        return {4, path[bl - 1].first, path[bl - 1].second, path[bl].first,
                path[bl].second};
    }
    // 絵具追加指令
    vector<int> cmd_add_tube() const { return {1, ti, tj}; }

    // 開閉指令
    vector<int> cmd_openclose() const { return {4, si, sj - 1, si, sj}; }

    // 連続量 → ブロック量 へ丸め込む
    Action discretise(double amt, int use_blocks, int mode = 1) const {
        assert(mode == 0 or mode == 1);
        Action a;
        a.tube_idx = tube_idx;
        a.blocks = use_blocks;
        double unit0 = cap / use_blocks;         // 既存チューブ
        double unit1 = (cap + 1.0) / use_blocks; // 新規追加後
        bool leq = (amt <= cap);
        if (mode == 0) { // floor 相当
            a.add_new = !leq;
            double unit = leq ? unit0 : unit1;
            a.use_blocks = int(floor(amt / unit));
        } else { // ceil 相当
            a.add_new = !leq;
            double unit = leq ? unit0 : unit1;
            a.use_blocks = int(ceil(amt / unit));
        }
        double unit = a.add_new ? unit1 : unit0;
        a.real_amt = unit * a.use_blocks;
        return a;
    }
};

// ──────────────────────────────
//  5. 入力
// ──────────────────────────────
struct Input {
    int N = 0, K = 0, H = 0, T = 0, D = 0;
    vector<Color> tubes;
    vector<Color> targets;
    void read() {
        cin >> N >> K >> H >> T >> D;
        tubes.resize(K);
        targets.resize(H);
        rep(i, K) cin >> tubes[i].c >> tubes[i].m >> tubes[i].y;
        rep(i, H) cin >> targets[i].c >> targets[i].m >> targets[i].y;
    }
};

// ──────────────────────────────
//  6. ソルバー本体
// ──────────────────────────────
class Solver {
    const Input &in;
    vector<Palette> palettes;
    vector<vector<int>> cmds; // 出力コマンド蓄積

    int max_colors = 0;
    int tubes_used = 0;
    double err_sum = 0;
    int random_iter = 0;
    int anneal_iter = 0;
    double eps = 1e-6;

  public:
    Solver(const Input &_in) : in(_in) {}

    //----------------------------------
    void solve() {
        init_palettes();
        rep(h, in.H) {
            Color tgt = in.targets[h];
            int remains = in.T - cmds.size() - (in.H - h) * 3 - in.H;
            max_colors = max(1, int(floor(remains / (4.0 * (in.H - h)))));
            auto coef = find_mix(tgt);
            auto acts = discretise(tgt, coef);
            commit(tgt, acts);
        }
        if (cmds.size() <= size_t(in.T))
            print();
        cerr_report();
    }

  private:
    //----------------------------------
    void init_palettes() {
        palettes.assign(in.K, {});
        rep(i, 20) palettes[i % in.K].lines++;
        int row = 0;
        rep(k, in.K) {
            auto &p = palettes[k];
            p.tube_idx = k;
            p.si = row;
            p.sj = 1;
            row += p.lines;
            p.build();
        }
        // 縦仕切り
        rep(i, 20) {
            cout << "1";
            rep(j, 18) cout << " 0";
            cout << "\n";
        }
        // 横仕切り
        rep(k, in.K) {
            auto &p = palettes[k];
            rep(j, p.lines - 1) {
                cout << "0 ";
                if (j % 2 == 0) {
                    rep(x, 18) cout << "1 ";
                    cout << "0\n";
                } else {
                    cout << "0";
                    rep(x, 18) cout << " 1";
                    cout << "\n";
                }
            }
            if (k + 1 < in.K) {
                cout << "0 ";
                rep(x, 19) cout << "1" << (x == 18 ? '\n' : ' ');
            }
        }
    }

    //----------------------------------
    static bool normalise(vector<double> &v) {
        double sum = accumulate(v.begin(), v.end(), 0.0);
        if (sum == 0)
            return false;
        for (double &x : v)
            x /= sum;
        return true;
    }

    vector<Action> discretise(const Color &tgt, const vector<double> &coef) {
        vector<Action> best_acts;
        double min_cost = 1e100;
        vector<pair<Action, Action>> nearest_acts;
        rep(i, in.K) {
            if (coef[i] == 0.0) {
                continue;
            }
            double amt = coef[i];
            Action best_l, best_r;
            best_l.real_amt = 1e100;
            best_r.real_amt = 1e100;
            Palette &p = palettes[i];
            for (int b = p.used_blocks; b <= p.blocks; b++) {
                Action new_l = p.discretise(amt, b, 0);
                if (abs(new_l.real_amt - amt) < abs(best_l.real_amt - amt)) {
                    best_l = new_l;
                }
                Action new_r = p.discretise(amt, b, 1);
                if (abs(new_r.real_amt - amt) < abs(best_r.real_amt - amt)) {
                    best_r = new_r;
                }
            }
            nearest_acts.push_back({best_l, best_r});
        }
        rep(mask, 1 << nearest_acts.size()) {
            double amt_sum = 0.0;
            vector<Action> new_acts;
            new_acts.reserve(nearest_acts.size());
            rep(i, nearest_acts.size()) {
                if (mask >> i & 1) {
                    amt_sum += nearest_acts[i].second.real_amt;
                    new_acts.push_back(nearest_acts[i].second);
                } else {
                    amt_sum += nearest_acts[i].first.real_amt;
                    new_acts.push_back(nearest_acts[i].first);
                }
            }
            if (amt_sum < 1.0 - eps) {
                continue;
            }
            double new_cost = cost(tgt, new_acts);
            if (new_cost < min_cost) {
                min_cost = new_cost;
                best_acts = new_acts;
            }
        }
        return best_acts;
    }

    double cost(const Color &tgt, const vector<double> &coef) const {
        MixState s;
        double total = 0;
        rep(i, in.K) {
            s.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, coef[i]);
            total += coef[i];
        }
        return s.error(tgt) + max(0.0, (total - 1.0)) * in.D;
    }

    double cost(const Color &tgt, const vector<Action> &actions) const {
        MixState s;
        double total = 0;
        for (const auto &a : actions) {
            int tube_idx = a.tube_idx;
            s.add(in.tubes[tube_idx].c, in.tubes[tube_idx].m,
                  in.tubes[tube_idx].y, a.real_amt);
            total += a.real_amt;
        }
        return s.error(tgt) + max(0.0, (total - 1.0)) * in.D;
    }

    double error_only(const Color &tgt, const vector<double> &coef) const {
        MixState s;
        rep(i, in.K)
            s.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, coef[i]);
        return s.error(tgt);
    }

    double error_only(const Color &tgt, const vector<Action> &actions) const {
        MixState s;
        for (const auto &a : actions) {
            int tube_idx = a.tube_idx;
            s.add(in.tubes[tube_idx].c, in.tubes[tube_idx].m,
                  in.tubes[tube_idx].y, a.real_amt);
        }
        return s.error(tgt);
    }

    //----------------------------------
    vector<double> random_search(const Color &tgt) {
        double best = 1e100;
        vector<double> best_c(in.K, 0);
        TimeKeeper tk(1.7);
        int it = 0;
        while (true) {
            ++it;
            ++random_iter;
            if (it % 100 == 0) {
                tk.update();
                if (tk.over())
                    break;
            }
            int choose = rnd::uniform_int(1, min(in.K, max_colors));
            vector<double> coef(in.K, 0);
            rep(k, choose) coef[rnd::xorshift32() % in.K] += rnd::uniform01();
            normalise(coef);
            double c = error_only(tgt, coef);
            if (c < best) {
                best = c;
                best_c = coef;
            }
        }
        return best_c;
    }

    //----------------------------------
    vector<double> anneal(const Color &tgt, const vector<double> &init_c) {
        vector<double> best_c = init_c, curr_c = init_c;
        double best_cost = cost(tgt, best_c), curr_cost = best_cost;
        // vector<Action> best_a = init_a, curr_a = init_a;
        int curr_nz = count_if(curr_c.begin(), curr_c.end(),
                               [](double v) { return v > 0; });
        const double T0 = 1.0, Tend = 1e-3;
        TimeKeeper tk(1.0);
        int it = 0;
        while (true) {
            ++it;
            ++anneal_iter;
            if (it % 50 == 0) {
                tk.update();
                if (tk.over())
                    break;
            }
            double frac = min(1.0, tk.now() / 1.0);
            double T = T0 * (1 - frac) + Tend * frac;
            int idx = rnd::xorshift32() % in.K;
            double diff = rnd::uniform_real(-0.2, 0.2);
            if ((diff < 0 && curr_c[idx] == 0) ||
                (diff > 0 && curr_nz == max_colors && curr_c[idx] == 0))
                continue;
            auto nxt_c = curr_c;
            int nxt_nz = curr_nz;
            if (nxt_c[idx] == 0 && diff > 0)
                ++nxt_nz;
            nxt_c[idx] += diff;
            if (nxt_c[idx] < 0) {
                nxt_c[idx] = 0;
                --nxt_nz;
            }
            normalise(nxt_c);
            double nxt_cost = error_only(tgt, nxt_c);
            double d = nxt_cost - curr_cost;
            bool accept =
                (d < 0) || (exp(-d / max(T, 1e-9)) > rnd::uniform01());
            if (accept) {
                curr_c.swap(nxt_c);
                curr_cost = nxt_cost;
                curr_nz = nxt_nz;
                if (curr_cost < best_cost) {
                    best_cost = curr_cost;
                    best_c = curr_c;
                }
            }
        }
        return best_c;
    }

    //----------------------------------
    vector<double> projection(const Color &tgt, int lim) const {
        int K = in.K;
        vector<double> best(K, 0);
        double best_e2 = 1e300;
        // 3本
        if (lim >= 3) {
            rep(i, K) for (int j = i + 1; j < K; ++j) for (int k = j + 1; k < K;
                                                           ++k) {
                Color pi = in.tubes[i], pj = in.tubes[j], pk = in.tubes[k];
                Color ei = pi - pk, ej = pj - pk, v = tgt - pk;
                double m00 = dot(ei, ei), m01 = dot(ei, ej), m11 = dot(ej, ej),
                       b0 = dot(ei, v), b1 = dot(ej, v),
                       det = m00 * m11 - m01 * m01;
                if (det == 0)
                    continue;
                double a = (b0 * m11 - b1 * m01) / det,
                       b = (m00 * b1 - m01 * b0) / det, g = 1 - a - b;
                if (a >= 0 && b >= 0 && g >= 0) {
                    Color mix = pi * a + pj * b + pk * g;
                    double e2 = norm2(mix - tgt);
                    if (e2 < best_e2) {
                        best_e2 = e2;
                        fill(best.begin(), best.end(), 0);
                        best[i] = a;
                        best[j] = b;
                        best[k] = g;
                    }
                }
            }
        }
        // 2本
        if (lim >= 2) {
            rep(i, K) for (int j = i + 1; j < K; ++j) {
                Color p = in.tubes[i], q = in.tubes[j], d = q - p, tp = tgt - p;
                double dd = norm2(d);
                if (dd == 0)
                    continue;
                double u = dot(tp, d) / dd;
                u = clamp(u, 0.0, 1.0);
                Color mix = p * u + q * (1 - u);
                double e2 = norm2(mix - tgt);
                if (e2 < best_e2) {
                    best_e2 = e2;
                    fill(best.begin(), best.end(), 0);
                    best[i] = u;
                    best[j] = 1 - u;
                }
            }
        }
        // 1本
        if (lim >= 1) {
            double best1 = 1e300;
            int idx = 0;
            rep(i, K) {
                double e2 = norm2(in.tubes[i] - tgt);
                if (e2 < best1) {
                    best1 = e2;
                    idx = i;
                }
            }
            if (best1 < best_e2) {
                fill(best.begin(), best.end(), 0);
                best[idx] = 1;
            }
        }
        return best;
    }

    //----------------------------------
    vector<double> find_mix(const Color &tgt) {
        auto rand_c = random_search(tgt);
        double rand_cost = error_only(tgt, rand_c);
        auto proj_c = projection(tgt, max_colors);
        // auto proj_a = discretise(proj_c);
        double proj_cost = error_only(tgt, proj_c);
        if (proj_cost < rand_cost)
            return anneal(tgt, proj_c);
        return anneal(tgt, rand_c);
    }

    //----------------------------------
    void commit(const Color &tgt, const vector<Action> &acts) {
        // todo
        // 0.5+0.5 2本近似の特例
        double pair_cost = 1e100;
        pair<int, int> bestp{0, 1};
        rep(i, in.K) for (int j = i + 1; j < in.K; ++j) {
            MixState s;
            s.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, 0.5);
            s.add(in.tubes[j].c, in.tubes[j].m, in.tubes[j].y, 0.5);
            double c = s.error(tgt) + in.D;
            if (c < pair_cost) {
                pair_cost = c;
                bestp = {i, j};
            }
        }
        double orig_cost = cost(tgt, acts);
        err_sum += error_only(tgt, acts);
        if (pair_cost < orig_cost) {
            cmds.push_back({1, 0, 0, bestp.first});
            cmds.push_back({1, 0, 0, bestp.second});
            cmds.push_back({2, 0, 0});
            cmds.push_back({3, 0, 0});
            tubes_used += 2;
            return;
        }

        vector<vector<int>> sep;
        if (acts.size() == 1) {
            cmds.push_back({1, 0, 0, acts[0].tube_idx});
            cmds.push_back({2, 0, 0});
            tubes_used++;
            return;
        }
        double amt_sum = 0;
        for (auto a : acts) {
            auto &p = palettes[a.tube_idx];
            if (a.add_new) {
                p.cap += 1.0;
                auto s = p.cmd_add_tube();
                cmds.push_back(s);
                tubes_used++;
            }
            // 左を閉じる(分母を決める)
            auto s = p.cmd_sep(p.blocks - a.blocks);
            if (!s.empty() and p.used_blocks != a.blocks) {
                cmds.push_back(s);
                // sep.push_back(s);
            }
            // 区切りを空ける
            s = p.cmd_sep(p.blocks - p.used_blocks);
            if (!s.empty() and p.used_blocks != a.blocks) {
                cmds.push_back(s);
                // sep.push_back(s);
            }
            // 区切りを閉める
            s = p.cmd_sep(p.blocks - (a.blocks - a.use_blocks));
            if (!s.empty()) {
                cmds.push_back(s);
                // sep.push_back(s);
            }
            p.used_blocks = a.blocks - a.use_blocks;

            p.cap -= a.real_amt;
            amt_sum += a.real_amt;
            auto oc = p.cmd_openclose();
            cmds.push_back(oc);
            sep.push_back(oc);
        }
        cmds.push_back({2, 0, 0});
        if (amt_sum > 1.0) {
            cmds.push_back({3, 0, 0});
        }
        reverse(sep.begin(), sep.end());
        for (auto &v : sep)
            cmds.push_back(v);
    }

    //----------------------------------
    void cerr_report() {
        cerr << "Cost: " << (long long)(err_sum + (tubes_used - in.H) * in.D)
             << '\n';
        cerr << "Err: " << (long long)err_sum << '\n';
        cerr << "Tube: " << (tubes_used - in.H) * in.D << '\n';
        cerr << "Random_iter: " << random_iter << '\n';
        cerr << "Anneal_iter: " << anneal_iter << '\n';
    }
    void print() const {
        for (auto &v : cmds) {
            rep(i, v.size()) {
                cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
            }
        }
    }
};

// ──────────────────────────────
//  7. main()
// ──────────────────────────────
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Input in;
    in.read();
    Solver sol(in);
    sol.solve();
    return 0;
}

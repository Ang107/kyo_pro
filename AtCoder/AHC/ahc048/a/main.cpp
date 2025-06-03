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

struct Vec3 {
    double x, y, z;
    Vec3() = default;
    Vec3(double x, double y, double z) : x(x), y(y), z(z) {}
    Vec3 operator+(const Vec3 &o) const { return {x + o.x, y + o.y, z + o.z}; }
    Vec3 operator-(const Vec3 &o) const { return {x - o.x, y - o.y, z - o.z}; }
    Vec3 operator*(double k) const { return {x * k, y * k, z * k}; }
};

inline Vec3 cross(const Vec3 &a, const Vec3 &b) {
    return {a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x};
}

inline double dot(const Vec3 &a, const Vec3 &b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

struct Plane {
    Vec3 n;   // 外向き法線
    double d; // ax+by+cz+d=0
};

vector<Plane> build_convex_hull_faces(const vector<Vec3> &v,
                                      double eps = 1e-12) {
    const int n = v.size();
    Vec3 centroid(0, 0, 0);
    for (auto &p : v)
        centroid = centroid + p;
    centroid = centroid * (1.0 / n);

    vector<Plane> faces;
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            for (int k = j + 1; k < n; ++k) {
                Vec3 nrm = cross(v[j] - v[i], v[k] - v[i]);
                double norm2 = dot(nrm, nrm);
                if (norm2 < eps)
                    continue; // ほぼ共線
                // 向きを決める
                if (dot(nrm, centroid - v[i]) > 0)
                    nrm = nrm * -1;
                // 他の頂点がすべて同じ側か確認
                bool pos = false, neg = false;
                for (int t = 0; t < n; ++t)
                    if (t != i && t != j && t != k) {
                        double s = dot(nrm, v[t] - v[i]);
                        if (s > eps)
                            pos = true;
                        if (s < -eps)
                            neg = true;
                    }
                if (pos && neg)
                    continue; // 平面が内部を分割→面ではない
                // 面確定（重複回避は必要に応じて）
                faces.push_back({nrm, -dot(nrm, v[i])});
            }
    return faces;
}

// 内部判定
bool inside(const Vec3 &p, const vector<Plane> &faces, double eps = 1e-9) {
    for (auto &pl : faces) {
        if (dot(pl.n, p) + pl.d > -eps)
            return false; // 外か境界
    }
    return true; // 厳密に内側
}
// 内部点を除外し、外殻（境界）に乗っている頂点だけを返す
std::vector<int> removeInteriorPoints(const std::vector<Vec3> &pts,
                                      double eps = 1e-9) {
    // ① 凸包面を列挙
    auto faces =
        build_convex_hull_faces(pts, eps * 1e-3); // 面生成は少し厳しめで OK

    // ② 内部かどうか判定してフィルタ
    std::vector<int> result;
    rep(i, pts.size()) {
        const auto &p = pts[i];
        // for (const auto &p : pts) {
        if (!inside(p, faces,
                    eps)) { // true ＝外殻 (境界含む)／false ＝純内部
            result.push_back(i);
        }
    }
    return result;
}

// ──────────────────────────────
//  2. 基本色構造体・演算
// ──────────────────────────────
struct Color {
    double c, m, y; // シアン, マゼンタ, イエロー
    Color(double _c = 0, double _m = 0, double _y = 0) : c(_c), m(_m), y(_y) {}
    Color operator+(const Color &o) const {
        return {c + o.c, m + o.m, y + o.y};
    }
    Color &operator+=(const Color &o) {
        c += o.c;
        m += o.m;
        y += o.y;
        return *this;
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
    double amt = 0;
    MixState() : c(0), m(0), y(0), amt(0) {} // 総量
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
    double error_if_add(double dc, double dm, double dy, double da,
                        const Color &tgt) {
        if (da == 0) {
            return error(tgt);
        }
        if (amt <= -da) {
            MixState ms;
            return ms.error(tgt);
        }
        double new_amt = amt + da;

        double new_c = (c * amt + dc * da) / new_amt;
        double new_m = (m * amt + dm * da) / new_amt;
        double new_y = (y * amt + dy * da) / new_amt;

        double dc_err = tgt.c - new_c;
        double dm_err = tgt.m - new_m;
        double dy_err = tgt.y - new_y;
        double d2 = dc_err * dc_err + dm_err * dm_err + dy_err * dy_err;
        return sqrt(d2) * 10000.0;
    }
    void clear() {
        c = 0;
        m = 0;
        y = 0;
        amt = 0;
    }
};

// ──────────────────────────────
//  4. パレット上の 1 チューブ管理
// ──────────────────────────────
struct Action {          // 操作1回分
    int tube_idx = 0;    // チューブ番号
    int add_new = 0;     // 新規チューブを設置する個数
    double real_amt = 0; // 実量
    int use_blocks = 0;  // 分子
    int blocks = 0;      // 分母
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
        path.reserve(blocks + 1);
        path.push_back({si, sj - 1});
        rep(i, lines) {
            if (i % 2 == 0) {
                rep(j, 19) path.emplace_back(si + i, sj + j);
            } // →
            else {
                for (int j = 18; j >= 0; --j)
                    path.emplace_back(si + i, sj + j);
            } // ←
        }
        ti = path[blocks].first;
        tj = path[blocks].second;
    }

    // ブロック分割指令
    vector<int> cmd_sep(int bl) const {
        if (bl == int(path.size()) - 1)
            return {};
        assert(0 <= bl);
        return {4, path[bl].first, path[bl].second, path[bl + 1].first,
                path[bl + 1].second};
    }
    // 絵具追加指令
    vector<int> cmd_add_tube() const { return {1, ti, tj, tube_idx}; }

    // 開閉指令
    vector<int> cmd_openclose() const { return {4, si, sj - 1, si, sj}; }

    // 連続量 → ブロック量 へ丸め込む
    Action discretise(double amt, int use_blocks, int mode = 1) const {
        assert(mode == 0 or mode == 1);
        assert(use_blocks > 0);
        Action a;
        a.tube_idx = tube_idx;
        a.blocks = use_blocks;
        double new_cap = cap;
        while (new_cap < amt) {
            new_cap += 1.0;
            a.add_new++;
        }
        double unit = new_cap / use_blocks;
        if (mode == 0) { // floor 相当
            a.use_blocks = int(floor(amt / unit));
        } else { // ceil 相当
            a.use_blocks = int(ceil(amt / unit));
        }
        a.real_amt = new_cap * a.use_blocks / use_blocks;
        return a;
    }
};

// ──────────────────────────────
//  5. 入力
// ──────────────────────────────
struct Input {
    int N = 0, K = 0, H = 0, T = 0, D = 0, Q = 0;
    vector<Color> tubes;
    vector<Color> targets;
    vector<int> need_idxs;
    void read() {
        cin >> N >> K >> H >> T >> D;
        tubes.resize(K);
        targets.resize(H);
        rep(i, K) cin >> tubes[i].c >> tubes[i].m >> tubes[i].y;
        rep(i, H) cin >> targets[i].c >> targets[i].m >> targets[i].y;
    }
};
struct MixStateWithAction {
    double c = 0, m = 0, y = 0; // 現在色
    double amt = 0;
    vector<int> actions;
    MixStateWithAction() : c(0), m(0), y(0), amt(0) {
        actions = vector<int>();
    } // 総量
    void add(double dc, double dm, double dy, double da, int tube_idx) {
        if (da == 0)
            return;
        c = (c * amt + dc * da) / (amt + da);
        m = (m * amt + dm * da) / (amt + da);
        y = (y * amt + dy * da) / (amt + da);
        actions.push_back(tube_idx);
        amt += da;
    }
    double error(const Color &tgt) const {
        double d2 = (tgt.c - c) * (tgt.c - c) + (tgt.m - m) * (tgt.m - m) +
                    (tgt.y - y) * (tgt.y - y);
        return sqrt(d2) * 10000.0;
    }
};
struct Well {
    int i, j;       // 代表の座標
    double amt;     // 絵具の量
    double cap;     // ウェルの大きさ
    double c, m, y; // 色
    bool is_clear = true;
    void add(const MixStateWithAction &action) {
        double da = action.amt;
        double dc = action.c;
        double dm = action.m;
        double dy = action.y;
        if (da == 0)
            return;
        is_clear = false;
        da = min(da, cap - amt);
        c = (c * amt + dc * da) / (amt + da);
        m = (m * amt + dm * da) / (amt + da);
        y = (y * amt + dy * da) / (amt + da);
        amt += da;
    }
    double error(const Color &tgt) {
        double d2 = (tgt.c - c) * (tgt.c - c) + (tgt.m - m) * (tgt.m - m) +
                    (tgt.y - y) * (tgt.y - y);
        return sqrt(d2) * 10000.0;
    }
    double error_if_add(const Color &tgt,
                        const MixStateWithAction &action) const {
        double da = action.amt;
        double dc = action.c;
        double dm = action.m;
        double dy = action.y;
        da = min(da, cap - amt);
        double _c = (c * amt + dc * da) / (amt + da);
        double _m = (m * amt + dm * da) / (amt + da);
        double _y = (y * amt + dy * da) / (amt + da);
        double d2 = (tgt.c - _c) * (tgt.c - _c) + (tgt.m - _m) * (tgt.m - _m) +
                    (tgt.y - _y) * (tgt.y - _y);
        return sqrt(d2) * 10000.0;
    }
    void use_color() {
        assert(amt > 1 - 1e-6);
        amt -= 1.0;
        if (amt == 0.0) {
            clear();
        }
    }
    void clear() {
        is_clear = true;
        amt = 0.0;
        c = 0.0;
        m = 0.0;
        y = 0.0;
    }
};
// ──────────────────────────────
//  6. Tが小さいときのための特殊ソルバー
// ──────────────────────────────
class Small_T_Solver {
    const Input &in;
    int tubes_used = 0;
    double err_sum = 0;
    double eps = 1e-6;
    int max_turn = 0;
    int max_well = 100;
    int max_iter = 1000;
    vector<Well> used_wells;
    vector<Well> clean_wells;
    vector<vector<MixStateWithAction>> actions =
        vector<vector<MixStateWithAction>>(5, vector<MixStateWithAction>(0));
    vector<vector<int>> cmds; // 出力コマンド蓄積
    vector<string> sep_v;
    vector<string> sep_h;

  public:
    int final_cost = 0;
    Small_T_Solver(const Input &_in) : in(_in) {}
    void solve() {
        init_wells();
        init_palettes();
        init_actions();
        rep(h, in.H) {
            Color tgt = in.targets[h];
            int remains = in.T - cmds.size();
            max_turn = max(1, int(floor(remains / (in.H - h))));
            auto [well_idx, is_dump, action] = calc_best_action(tgt);
            commit(tgt, well_idx, is_dump, action);
        }
        final_cost = (int)(err_sum + (tubes_used - in.H) * in.D);
    }
    void print() {
        for (auto s : sep_v) {
            cout << s;
        }
        for (auto s : sep_h) {
            cout << s;
        }
        for (auto &v : cmds) {
            rep(i, v.size()) {
                cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
            }
        }
    }
    void cerr_report() {
        cerr << "Small_T Solve: \n";
        cerr << "Cost: " << (long long)(err_sum + (tubes_used - in.H) * in.D)
             << '\n';
        cerr << "Err: " << (long long)err_sum << '\n';
        cerr << "Tube: " << (tubes_used - in.H) * in.D << '\n';
        cerr << "Used_Tubes: " << tubes_used << '\n';
        cerr << "Used_Turn: " << cmds.size() << " / " << in.T << '\n';
    }

  private:
    void commit(const Color &tgt, int well_idx, bool is_dump,
                const MixStateWithAction &action) {
        Well &well =
            (well_idx == -1 ? clean_wells.back() : used_wells[well_idx]);
        // 捨てる
        if (is_dump) {
            rep(cnt, (int)ceil(well.amt)) {
                cmds.push_back({3, well.i, well.j});
            }
            well.clear();
        }
        // 絵具を入れる
        well.add(action);
        for (int tube_idx : action.actions) {
            cmds.push_back({1, well.i, well.j, tube_idx});
            tubes_used++;
        }
        err_sum += well.error(tgt);
        // 渡す
        well.use_color();
        cmds.push_back({2, well.i, well.j});
        // 事後処理
        if (well.is_clear) {
            if (well_idx == -1) {
            } else {
                clean_wells.push_back(well);
                used_wells.erase(used_wells.begin() + well_idx);
            }
        } else {
            if (well_idx == -1) {
                used_wells.push_back(well);
                clean_wells.pop_back();
            } else {
            }
        }
    }
    tuple<int, bool, MixStateWithAction> calc_best_action(const Color &tgt) {
        double min_cost = 1e100;
        int best_well_idx;
        MixStateWithAction best_action;
        double min_amt = 1e100;
        int dump_well_idx = 0;
        bool is_dump = false;
        rep(well_idx, used_wells.size()) {
            const auto &well = used_wells[well_idx];
            if (min_amt < well.amt) {
                min_amt = well.amt;
                dump_well_idx = well_idx;
            }
            rep(i, min(5, max_turn + 1)) {
                if (actions[i].size() > 1000) {
                    rep(_, max_iter) {
                        MixStateWithAction &action =
                            actions[i][rnd::xorshift32() % actions[i].size()];
                        if (well.amt + action.amt < 1.0 - eps) {
                            continue;
                        }
                        double cost = 0;
                        if (tubes_used > 1000) {
                            cost += (action.actions.size() - 1.0) * in.D;
                        }
                        cost +=
                            max(0.0, well.amt + action.amt - well.cap) * in.D;
                        cost += well.error_if_add(tgt, action);
                        if (cost < min_cost) {
                            min_cost = cost;
                            best_well_idx = well_idx;
                            best_action = action;
                        }
                    }
                } else {
                    for (const auto &action : actions[i]) {
                        if (well.amt + action.amt < 1.0 - eps) {
                            continue;
                        }
                        double cost = 0;
                        if (tubes_used > 1000) {
                            cost += (action.actions.size() - 1.0) * in.D;
                        }
                        cost +=
                            max(0.0, well.amt + action.amt - well.cap) * in.D;
                        cost += well.error_if_add(tgt, action);
                        if (cost < min_cost) {
                            min_cost = cost;
                            best_well_idx = well_idx;
                            best_action = action;
                        }
                    }
                }
            }
        }
        if (clean_wells.empty()) {
            Well well;
            rep(i, min(5, (int)(max_turn + 1 -
                                ceil(used_wells[dump_well_idx].amt)))) {
                for (const auto &action : actions[i]) {
                    if (well.amt + action.amt < 1.0 - eps) {
                        continue;
                    }
                    double cost = 0;
                    if (tubes_used > 1000) {
                        cost += (action.actions.size() - 1.0) * in.D;
                    }
                    cost += max(0.0, well.amt + action.amt - well.cap) * in.D;
                    cost += ceil(used_wells[dump_well_idx].amt) * in.D;
                    cost += well.error_if_add(tgt, action);
                    if (cost < min_cost) {
                        is_dump = true;
                        min_cost = cost;
                        best_well_idx = dump_well_idx;
                        best_action = action;
                    }
                }
            }
        } else {
            Well well = clean_wells.back();
            rep(i, min(5, max_turn + 1)) {
                for (const auto &action : actions[i]) {
                    if (well.amt + action.amt < 1.0 - eps) {
                        continue;
                    }
                    double cost = 0;
                    if (tubes_used > 1000) {
                        cost += (action.actions.size() - 1.0) * in.D;
                    }
                    cost += max(0.0, well.amt + action.amt - well.cap) * in.D;
                    cost += well.error_if_add(tgt, action);
                    if (cost < min_cost) {
                        min_cost = cost;
                        best_well_idx = -1;
                        best_action = action;
                    }
                }
            }
        }

        return {best_well_idx, is_dump, best_action};
    }

    void init_wells() {
        used_wells.reserve(max_well);
        clean_wells.reserve(max_well);
        for (int i = 0; i < in.N; i += 2) {
            for (int j = 0; j < in.N; j += 2) {
                Well well;
                well.amt = 0;
                well.i = i;
                well.j = j;
                well.cap = 400.0 / max_well;
                clean_wells.push_back(well);
            }
        }
    }
    void init_palettes() {
        sep_v = vector<string>(in.N);
        sep_h = vector<string>(in.N - 1);
        rep(i, in.N) {
            rep(j, in.N - 1) {
                if (j % 2 == 0) {
                    sep_v[i] += "0";
                    if (j == in.N - 2) {
                        sep_v[i] += '\n';
                    } else {
                        sep_v[i] += ' ';
                    }
                } else {
                    sep_v[i] += "1 ";
                }
            }
        }
        rep(i, in.N - 1) {
            rep(j, in.N) {
                if (i % 2 == 0) {
                    sep_h[i] += "0 ";
                } else {
                    sep_h[i] += "1";
                    if (j == in.N - 1) {
                        sep_h[i] += '\n';
                    } else {
                        sep_h[i] += ' ';
                    }
                }
            }
        }
    }
    void init_actions() {
        actions[0].push_back(MixStateWithAction());
        for (int i = 0; i < in.K; i++) {
            MixStateWithAction action;
            action.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, 1.0, i);
            actions[1].push_back(action);
            for (int j = i; j < in.K; j++) {
                MixStateWithAction action;
                action.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, 1.0, i);
                action.add(in.tubes[j].c, in.tubes[j].m, in.tubes[j].y, 1.0, j);
                actions[2].push_back(action);
                for (int k = j; k < in.K; k++) {
                    MixStateWithAction action;
                    action.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, 1.0,
                               i);
                    action.add(in.tubes[j].c, in.tubes[j].m, in.tubes[j].y, 1.0,
                               j);
                    action.add(in.tubes[k].c, in.tubes[k].m, in.tubes[k].y, 1.0,
                               k);
                    actions[3].push_back(action);
                    for (int l = k; l < in.K; l++) {
                        MixStateWithAction action;
                        action.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y,
                                   1.0, i);
                        action.add(in.tubes[j].c, in.tubes[j].m, in.tubes[j].y,
                                   1.0, j);
                        action.add(in.tubes[k].c, in.tubes[k].m, in.tubes[k].y,
                                   1.0, k);
                        action.add(in.tubes[l].c, in.tubes[l].m, in.tubes[l].y,
                                   1.0, l);
                        actions[4].push_back(action);
                    }
                }
            }
        }
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
    vector<string> sep_v;
    vector<string> sep_h;
    // double random_tl = 500;
    // double anneal_tl;
    double discretise_tl;
    TimeKeeper tk;
    // vector<vector<double>> init_coefs;

  public:
    int final_cost;

    Solver(const Input &_in, TimeKeeper tk) : in(_in), tk(tk) {}

    //----------------------------------
    void solve() {
        vector<vector<double>> coefs;
        coefs.reserve(in.T);
        int used_turn = 0;
        max_colors = max(1, int((ceil(in.T - 3 * in.H) / (4.0 * in.H))));
        // make_init_coef();
        rep(h, in.H) {
            // tk.update();
            // anneal_tl = (2600.0 - tk.now()) / (in.H - h);
            Color tgt = in.targets[h];
            int remains = in.T - used_turn - (in.H - h) * 3;
            max_colors = max(1, int(floor(remains / (4.0 * (in.H - h)))));
            auto coef = find_mix(tgt, h);
            coefs.push_back(coef);
            used_turn += 3;
            rep(i, in.K) {
                if (coef[i] > eps) {
                    used_turn += 4;
                }
            }
        }
        vector<int> used_tube_cnt(in.K);
        for (const auto &coef : coefs) {
            rep(i, in.K) {
                if (coef[i] > eps) {
                    used_tube_cnt[i]++;
                }
            }
        }
        for (int idx : in.need_idxs) {
            used_tube_cnt[idx]++;
        }
        vector<int> lines_size = calc_lines_size(used_tube_cnt);
        init_palettes(lines_size);
        err_sum = 0;
        tubes_used = 0;
        rep(h, in.H) {
            // tk.update();
            // anneal_tl = (2600.0 - tk.now()) / (in.H - h);
            Color tgt = in.targets[h];
            int remains = in.T - cmds.size() - (in.H - h) * 3;
            if (h < 500)
                max_colors = max(1, int(ceil(remains / (4.0 * (in.H - h)))));
            else
                max_colors = max(1, int(floor(remains / (4.0 * (in.H - h)))));

            cerr << "Max_Colors: " << h + 1 << " " << max_colors << '\n';
            auto coef = find_mix(tgt, h);
            auto acts = discretise(tgt, coef);
            cerr << "連続値のエラー: " << error_only(tgt, coef)
                 << " 離散値のエラー: " << error_only(tgt, acts) << '\n';
            commit(tgt, acts);
        }
        while (cmds.size() > in.T) {
            cmds.pop_back();
        }
        final_cost = (int)(err_sum + (tubes_used - in.H) * in.D);
    }
    void print() const {
        for (auto s : sep_v) {
            cout << s;
        }
        for (auto s : sep_h) {
            cout << s;
        }
        for (auto &v : cmds) {
            rep(i, v.size()) {
                cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
            }
        }
    }
    //----------------------------------
    void cerr_report() {
        cerr << "Main Solve: \n";
        cerr << "Cost: " << (long long)(err_sum + (tubes_used - in.H) * in.D)
             << '\n';
        cerr << "Err: " << (long long)err_sum << '\n';
        cerr << "Tube: " << (tubes_used - in.H) * in.D << '\n';
        cerr << "Used_Tubes: " << tubes_used << '\n';
        cerr << "Random_iter: " << random_iter << '\n';
        cerr << "Anneal_iter: " << anneal_iter << '\n';
        cerr << "Used_Turn: " << cmds.size() << " / " << in.T << '\n';
        // cerr << "Used_Tube_Cnt: \n";
        // for (int i = 0; i < (int)used_tube_cnt.size(); ++i) {
        //     cerr << used_tube_cnt[i]
        //          << (i + 1 == (int)used_tube_cnt.size() ? '\n' : ' ');
        // }
    }

  private:
    //----------------------------------
    vector<int> calc_lines_size(vector<int> used_tube_cnt) {
        int total_lines = 20;
        int K = in.K;

        // まず、used_tube_cnt[i] > 0 なら必ず 1 行を確保
        int count_pos = 0;
        for (int i = 0; i < K; ++i) {
            if (used_tube_cnt[i] > 0) {
                count_pos++;
            }
        }
        // 確保分が total_lines を超えないように仮定
        // （もし count_pos > total_lines
        // になりうるなら別途エラーハンドリングを入れてください）
        int remaining = total_lines - count_pos;

        vector<int> lines_size(K, 0);
        for (int i = 0; i < K; ++i) {
            if (used_tube_cnt[i] > 0) {
                lines_size[i] = 1; // 最低 1 行
            }
        }

        // used_tube_cnt[i] > 0 の合計値を計算
        int sum_pos = 0;
        for (int i = 0; i < K; ++i) {
            if (used_tube_cnt[i] > 0) {
                sum_pos += used_tube_cnt[i];
            }
        }
        if (sum_pos == 0) {
            return lines_size;
        }

        // 「残り remaining 行」を比率 exact に基づいて floor 割り振り
        int current_sum = 0;
        vector<pair<double, int>> frac_with_index; // (小数部分, index)

        for (int i = 0; i < K; ++i) {
            if (used_tube_cnt[i] > 0) {
                double exact = double(used_tube_cnt[i]) * remaining / sum_pos;
                int add = int(floor(exact));
                lines_size[i] += add;
                current_sum += add;
                frac_with_index.emplace_back(exact - add, i);
            }
        }

        // 足りない分を、小数部分の大きい順に +1 して埋める
        int to_add = remaining - current_sum; // 余り行数
        sort(frac_with_index.rbegin(), frac_with_index.rend());
        for (int t = 0; t < to_add; ++t) {
            int idx = frac_with_index[t].second;
            lines_size[idx]++;
        }

        return lines_size;
    }
    void init_palettes(const vector<int> &lines_size) {
        palettes.assign(in.K, {});
        rep(i, in.K) palettes[i].lines = lines_size[i];

        sep_v = vector<string>(in.N);
        sep_h = vector<string>(in.N - 1);
        // 縦仕切り
        rep(i, 20) {
            sep_v[i] += "1";
            rep(j, 18) sep_v[i] += " 0";
            sep_v[i] += "\n";
        }

        int row = 0;
        rep(k, in.K) {
            if (row < in.N)
                sep_v[row][0] = '0';
            auto &p = palettes[k];
            p.tube_idx = k;
            p.si = row;
            p.sj = 1;
            row += p.lines;
            p.build();
        }

        // 横仕切り
        row = 0;
        rep(k, in.K) {
            auto &p = palettes[k];
            if (p.lines == 0 or row == in.N - 1)
                continue;
            rep(j, p.lines - 1) {
                sep_h[row] += "0 ";
                if (j % 2 == 0) {
                    rep(x, 18) sep_h[row] += "1 ";
                    sep_h[row] += "0\n";
                    row++;
                } else {
                    sep_h[row] += "0";
                    rep(x, 18) sep_h[row] += " 1";
                    sep_h[row] += "\n";
                    row++;
                }
            }
            if (row < in.N - 1) {
                sep_h[row] += "0 ";
                rep(x, 19) {
                    sep_h[row] += '1';
                    sep_h[row] += (x == 18 ? '\n' : ' ');
                }
                row++;
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
        vector<Action> new_acts;
        new_acts.reserve(in.K);
        vector<pair<Action, Action>> nearest_acts;
        vector<double> new_coef(in.K);

        for (double alp = 1.0; alp < 5.0; alp += 0.1) {
            nearest_acts.clear();
            fill(new_coef.begin(), new_coef.end(), 0.0);
            rep(i, in.K) { new_coef[i] = alp * coef[i]; }
            rep(i, in.K) {
                if (new_coef[i] < 1e-9) {
                    continue;
                }
                double amt = new_coef[i];
                Action best_l, best_r;
                best_l.real_amt = 1e100;
                best_r.real_amt = 1e100;
                Palette &p = palettes[i];
                assert(p.used_blocks <= p.blocks);
                assert(p.blocks > 0);
                for (int b = p.used_blocks; b <= p.blocks; b++) {
                    if (b == 0)
                        continue;
                    Action new_l = p.discretise(amt, b, 0);
                    if (abs(new_l.real_amt - amt) <
                        abs(best_l.real_amt - amt)) {
                        best_l = new_l;
                    }
                    Action new_r = p.discretise(amt, b, 1);
                    if (abs(new_r.real_amt - amt) <
                        abs(best_r.real_amt - amt)) {
                        best_r = new_r;
                    }
                }
                nearest_acts.push_back({best_l, best_r});
            }
            rep(mask, 1 << nearest_acts.size()) {
                double amt_sum = 0.0;
                new_acts.clear();
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
        }
        return best_acts;
    }

    double cost(const Color &tgt, const vector<double> &coef) const {
        static MixState s;
        s.clear();
        double total = 0;
        rep(i, in.K) {
            s.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, coef[i]);
            total += coef[i];
        }
        return s.error(tgt) + max(0.0, (total - 1.0)) * in.D;
    }

    double cost(const Color &tgt, const vector<Action> &actions) const {
        static MixState s;
        s.clear();
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
        static MixState s;
        s.clear();
        rep(i, in.K)
            s.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, coef[i]);
        return s.error(tgt);
    }

    double error_only(const Color &tgt, const vector<Action> &actions) const {
        static MixState s;
        s.clear();
        for (const auto &a : actions) {
            int tube_idx = a.tube_idx;
            s.add(in.tubes[tube_idx].c, in.tubes[tube_idx].m,
                  in.tubes[tube_idx].y, a.real_amt);
        }
        return s.error(tgt);
    }

    //----------------------------------
    // void make_init_coef() {
    //     vector<double> coef(in.K, 0);
    //     init_coefs = vector<vector<double>>(in.H);
    //     vector<double> best_costs(in.H, 1e100);
    //     TimeKeeper tk(random_tl);
    //     int it = 0;
    //     MixState ms;
    //     while (true) {
    //         ++it;
    //         ++random_iter;
    //         if (it % 100 == 0) {
    //             tk.update();
    //             if (tk.over())
    //                 break;
    //         }
    //         int choose = min(in.K, max_colors);
    //         fill(coef.begin(), coef.end(), 0.0);
    //         ms.clear();
    //         rep(k, choose) {
    //             int idx = in.need_idxs[rnd::xorshift32() % in.Q];
    //             double am = rnd::uniform01();
    //             coef[idx] += am;
    //             ms.add(in.tubes[idx].c, in.tubes[idx].m, in.tubes[idx].y,
    //             am);
    //         }
    //         rep(i, in.H) {
    //             const Color &tgt = in.targets[i];
    //             double c = ms.error(tgt);
    //             if (c < best_costs[i]) {
    //                 best_costs[i] = c;
    //                 init_coefs[i] = coef;
    //             }
    //         }
    //     }
    //     rep(i, in.H) { normalise(init_coefs[i]); }
    // }

    //----------------------------------
    // vector<double> anneal(const Color &tgt, const vector<double> &init_c) {
    //     vector<double> best_c = init_c, curr_c = init_c;
    //     double best_cost = cost(tgt, best_c), curr_cost = best_cost;
    //     int curr_nz = count_if(curr_c.begin(), curr_c.end(),
    //                            [](double v) { return v > 0; });
    //     const double T0 = 100.0, Tend = 1e-3;
    //     TimeKeeper tk(anneal_tl);
    //     int it = 0;
    //     MixState ms;
    //     rep(i, in.K) {
    //         if (init_c[i] > 1e-9) {
    //             ms.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y,
    //             init_c[i]);
    //         }
    //     }
    //     while (true and best_cost > 1.0) {
    //         ++it;
    //         ++anneal_iter;
    //         if (it % 50 == 0) {
    //             normalise(curr_c);
    //             ms.clear();
    //             rep(i, in.K) {
    //                 if (curr_c[i] > 1e-9) {
    //                     ms.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y,
    //                            curr_c[i]);
    //                 }
    //             }
    //             tk.update();
    //             if (tk.over())
    //                 break;
    //         }
    //         double frac = min(1.0, tk.now() / anneal_tl);
    //         double T = T0 * (1 - frac) + Tend * frac;
    //         int idx = in.need_idxs[rnd::xorshift32() % in.Q];
    //         double diff = rnd::uniform_real(-0.2, 0.2);
    //         if ((diff < 0 && curr_c[idx] == 0) ||
    //             (diff > 0 && curr_nz == max_colors && curr_c[idx] == 0))
    //             continue;

    //         // 変化した後のコスト
    //         double nxt_cost;
    //         if (diff < 0) {
    //             diff = max(diff, -curr_c[idx]);
    //             nxt_cost = ms.error_if_add(in.tubes[idx].c, in.tubes[idx].m,
    //                                        in.tubes[idx].y, diff, tgt);
    //         } else {
    //             nxt_cost = ms.error_if_add(in.tubes[idx].c, in.tubes[idx].m,
    //                                        in.tubes[idx].y, diff, tgt);
    //         }
    //         double d = nxt_cost - curr_cost;
    //         bool accept =
    //             (d < 0) || (exp(-d / max(T, 1e-9)) > rnd::uniform01());
    //         if (accept) {
    //             ms.add(in.tubes[idx].c, in.tubes[idx].m, in.tubes[idx].y,
    //             diff); if (curr_c[idx] == 0 && diff > 0)
    //                 ++curr_nz;
    //             curr_c[idx] += diff;
    //             curr_cost = nxt_cost;
    //             if (curr_c[idx] <= 0) {
    //                 curr_c[idx] = 0;
    //                 --curr_nz;
    //             }
    //             if (curr_cost < best_cost) {
    //                 best_cost = curr_cost;
    //                 best_c = curr_c;
    //             }
    //         }
    //     }
    //     normalise(best_c);
    //     return best_c;
    // }

    std::vector<double> projection_subset4(const Color &tgt,
                                           const std::vector<int> &need_idxs,
                                           int lim) const {
        int K = in.K;
        std::vector<double> best(K, 0.0);
        double best_e2 = 1e300;

        int M = (int)need_idxs.size();
        // ――――――――――――――――――――――――――――――――――――
        //  1) 四色混合 (lim >= 4)
        // ――――――――――――――――――――――――――――――――――――
        if (lim >= 4 && M >= 4) {
            for (int xi = 0; xi < M; ++xi) {
                int i = need_idxs[xi];
                for (int xj = xi + 1; xj < M; ++xj) {
                    int j = need_idxs[xj];
                    for (int xk = xj + 1; xk < M; ++xk) {
                        int k = need_idxs[xk];
                        for (int xl = xk + 1; xl < M; ++xl) {
                            int l = need_idxs[xl];

                            // 基準色 4 点を取り出す
                            Color pi = in.tubes[i];
                            Color pj = in.tubes[j];
                            Color pk = in.tubes[k];
                            Color pl = in.tubes[l];

                            // pl を原点にシフト
                            Color ei = pi - pl;
                            Color ej = pj - pl;
                            Color ek = pk - pl;
                            Color v = tgt - pl;

                            // 3×3 行列 M の要素
                            double m00 = dot(ei, ei);
                            double m01 = dot(ei, ej);
                            double m02 = dot(ei, ek);
                            double m10 = m01; // dot(ej,ei)
                            double m11 = dot(ej, ej);
                            double m12 = dot(ej, ek);
                            double m20 = m02; // dot(ek,ei)
                            double m21 = m12; // dot(ek,ej)
                            double m22 = dot(ek, ek);

                            // 右辺ベクトル b
                            double b0 = dot(ei, v);
                            double b1 = dot(ej, v);
                            double b2 = dot(ek, v);

                            // 行列式 det(M)
                            double det = m00 * (m11 * m22 - m12 * m21) -
                                         m01 * (m10 * m22 - m12 * m20) +
                                         m02 * (m10 * m21 - m11 * m20);
                            if (std::abs(det) < 1e-12)
                                continue;

                            // Cramer's rule で a, b, c を求める
                            double det_a = b0 * (m11 * m22 - m12 * m21) -
                                           m01 * (b1 * m22 - m12 * b2) +
                                           m02 * (b1 * m21 - m11 * b2);

                            double det_b = m00 * (b1 * m22 - m12 * b2) -
                                           b0 * (m10 * m22 - m12 * m20) +
                                           m02 * (m10 * b2 - b1 * m20);

                            double det_c = m00 * (m11 * b2 - b1 * m21) -
                                           m01 * (m10 * b2 - b1 * m20) +
                                           b0 * (m10 * m21 - m11 * m20);

                            double a = det_a / det;
                            double b = det_b / det;
                            double c = det_c / det;
                            double d = 1.0 - a - b - c;

                            // 非負条件 (バリセンターが四面体内部)
                            if (a >= 0 && b >= 0 && c >= 0 && d >= 0) {
                                Color mix = pi * a;
                                mix += pj * b;
                                mix += pk * c;
                                mix += pl * d;

                                double e2 = norm2(mix - tgt);
                                if (e2 < best_e2) {
                                    best_e2 = e2;
                                    std::fill(best.begin(), best.end(), 0.0);
                                    best[i] = a;
                                    best[j] = b;
                                    best[k] = c;
                                    best[l] = d;
                                }
                            }
                        }
                    }
                }
            }
        }

        // ――――――――――――――――――――――――――――――――――――
        //  2) 三色混合 (lim >= 3)
        // ――――――――――――――――――――――――――――――――――――
        if (lim >= 3 && M >= 3) {
            for (int xi = 0; xi < M; ++xi) {
                int i = need_idxs[xi];
                for (int xj = xi + 1; xj < M; ++xj) {
                    int j = need_idxs[xj];
                    for (int xk = xj + 1; xk < M; ++xk) {
                        int k = need_idxs[xk];

                        Color pi = in.tubes[i];
                        Color pj = in.tubes[j];
                        Color pk = in.tubes[k];

                        Color ei = pi - pk;
                        Color ej = pj - pk;
                        Color v = tgt - pk;

                        double m00 = dot(ei, ei);
                        double m01 = dot(ei, ej);
                        double m11 = dot(ej, ej);
                        double b0 = dot(ei, v);
                        double b1 = dot(ej, v);
                        double det2 = m00 * m11 - m01 * m01;
                        if (std::abs(det2) < 1e-12)
                            continue;

                        double a = (b0 * m11 - b1 * m01) / det2;
                        double b = (m00 * b1 - m01 * b0) / det2;
                        double g = 1.0 - a - b;

                        if (a >= 0 && b >= 0 && g >= 0) {
                            Color mix = pi * a;
                            mix += pj * b;
                            mix += pk * g;

                            double e2 = norm2(mix - tgt);
                            if (e2 < best_e2) {
                                best_e2 = e2;
                                std::fill(best.begin(), best.end(), 0.0);
                                best[i] = a;
                                best[j] = b;
                                best[k] = g;
                            }
                        }
                    }
                }
            }
        }

        // ――――――――――――――――――――――――――――――――――――
        //  3) 二色混合 (lim >= 2)
        // ――――――――――――――――――――――――――――――――――――
        if (lim >= 2 && M >= 2) {
            for (int xi = 0; xi < M; ++xi) {
                int i = need_idxs[xi];
                for (int xj = xi + 1; xj < M; ++xj) {
                    int j = need_idxs[xj];

                    Color p = in.tubes[i];
                    Color q = in.tubes[j];
                    Color dcol = q - p;
                    Color tp = tgt - p;

                    double dd = norm2(dcol);
                    if (dd < 1e-12)
                        continue;

                    double u = dot(tp, dcol) / dd;
                    u = clamp(u, 0.0, 1.0);

                    Color mix = p * u;
                    mix += q * (1.0 - u);

                    double e2 = norm2(mix - tgt);
                    if (e2 < best_e2) {
                        best_e2 = e2;
                        std::fill(best.begin(), best.end(), 0.0);
                        best[i] = u;
                        best[j] = 1.0 - u;
                    }
                }
            }
        }

        // ――――――――――――――――――――――――――――――――――――
        //  4) 単色 (lim >= 1)
        // ――――――――――――――――――――――――――――――――――――
        if (lim >= 1 && M >= 1) {
            double best1 = 1e300;
            int bestIdx = -1;
            for (int xi = 0; xi < M; ++xi) {
                int i = need_idxs[xi];
                double e2 = norm2(in.tubes[i] - tgt);
                if (e2 < best1) {
                    best1 = e2;
                    bestIdx = i;
                }
            }
            if (bestIdx >= 0 && best1 < best_e2) {
                std::fill(best.begin(), best.end(), 0.0);
                best[bestIdx] = 1.0;
            }
        }

        return best;
    }
    //----------------------------------

    vector<double> find_mix(const Color &tgt, int idx) {
        // auto rand_c = init_coefs[idx];
        // double rand_cost = error_only(tgt, rand_c);
        auto proj_c = projection_subset4(tgt, in.need_idxs, max_colors);
        return proj_c;
        // double proj_cost = error_only(tgt, proj_c);
        // if (proj_cost < rand_cost) {
        //     auto anneal_c = anneal(tgt, proj_c);
        //     double anneal_cost = error_only(tgt, anneal_c);
        //     cerr << "random: " << rand_cost << " proj: " << proj_cost
        //          << " anneal: " << anneal_cost << '\n';
        //     return anneal_c;
        // } else {
        //     auto anneal_c = anneal(tgt, rand_c);
        //     double anneal_cost = error_only(tgt, anneal_c);
        //     cerr << "random: " << rand_cost << " proj: " << proj_cost
        //          << " anneal: " << anneal_cost << '\n';
        //     return anneal_c;
        // }
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
            if (a.use_blocks == 0) {
                continue;
            }
            // used_tube_cnt[a.tube_idx]++;
            auto &p = palettes[a.tube_idx];
            // 分母の変更
            if (p.used_blocks != a.blocks) {
                // 左を閉じる(分母を決める)
                auto s = p.cmd_sep(p.blocks - a.blocks);
                if (!s.empty()) {
                    cmds.push_back(s);
                    // sep.push_back(s);
                }
                // 区切りを空ける
                s = p.cmd_sep(p.blocks - p.used_blocks);
                if (!s.empty()) {
                    cmds.push_back(s);
                    // sep.push_back(s);
                }
            }
            rep(_, a.add_new) {
                p.cap += 1.0;
                p.cap = min(p.cap, (double)a.blocks);
                auto ad = p.cmd_add_tube();
                cmds.push_back(ad);
                tubes_used++;
            }
            // 分子の変更
            // 区切りを閉める
            auto s = p.cmd_sep(p.blocks - (a.blocks - a.use_blocks));
            if (!s.empty() and (a.blocks - a.use_blocks) != 0) {
                cmds.push_back(s);
                // sep.push_back(s);
            }
            // 左を開ける
            s = p.cmd_sep(p.blocks - a.blocks);
            if (!s.empty()) {
                // cmds.push_back(s);
                sep.push_back(s);
            }
            p.used_blocks = a.blocks - a.use_blocks;
            p.cap = p.cap * p.used_blocks / a.blocks;
            // p.cap -= a.real_amt;
            amt_sum += a.real_amt;
            // auto oc = p.cmd_openclose();
            // cmds.push_back(oc);
            // sep.push_back(oc);
        }
        for (auto &v : sep)
            cmds.push_back(v);
        cmds.push_back({2, 0, 0});
        while (amt_sum > 1.0 - eps) {
            cmds.push_back({3, 0, 0});
            amt_sum -= 1.0;
        }
        reverse(sep.begin(), sep.end());
    }
};

// ──────────────────────────────
//  7. main()
// ──────────────────────────────
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    TimeKeeper tk(2900);
    Input in;
    in.read();
    vector<Vec3> xyzs;
    rep(i, in.K) {
        xyzs.push_back(Vec3(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y));
    }
    auto need_idxs = removeInteriorPoints(xyzs);
    in.need_idxs = need_idxs;
    in.Q = need_idxs.size();
    if (in.T < 17000) {
        Small_T_Solver sol(in);
        sol.solve();
        tk.update();
        if (tk.now() < 2000.0) {
            Solver sol2(in, tk);
            sol2.solve();
            sol.cerr_report();
            sol2.cerr_report();
            if (sol.final_cost < sol2.final_cost) {
                sol.print();
            } else {
                sol2.print();
            }
        } else {
            sol.cerr_report();
            sol.print();
        }
    } else {
        tk.update();
        Solver sol(in, tk);
        sol.solve();
        sol.cerr_report();
        sol.print();
    }
    return 0;
}

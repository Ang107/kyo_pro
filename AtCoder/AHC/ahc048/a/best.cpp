#include <atcoder/all>
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
inline double d2(const Color &a, const Color &b) {
    return (a.c - b.c) * (a.c - b.c) + (a.m - b.m) * (a.m - b.m) +
           (a.y - b.y) * (a.y - b.y);
}
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
    void add(const Color &color, double da, double cap = 1e100) {
        if (amt + da > cap) {
            da = cap - amt;
        }
        if (da == 0.0)
            return;
        c = (c * amt + color.c * da) / (amt + da);
        m = (m * amt + color.m * da) / (amt + da);
        y = (y * amt + color.y * da) / (amt + da);
        amt += da;
    }
    void dump() {
        amt -= 1.0;
        if (amt <= 0.0) {
            amt = 0.0;
            clear();
        }
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
    uint64_t hash() const {
        uint64_t h_c = round(c * 10000);
        uint64_t h_m = round(m * 10000);
        uint64_t h_y = round(y * 10000);
        uint64_t hash = (h_c << 28) | (h_m << 14) | (h_y);
        return hash;
    }
};

// ──────────────────────────────
//  4. パレット上の 1 チューブ管理
// ──────────────────────────────
struct Action {                   // 操作1回分
    int tube_idx = 0;             // チューブ番号
    int primary_or_secandary = 0; // 1: プライマリー 2 セカンダリー
    int i = 0, j = 0;             // 追加する場所
    int add_new = 0;              // 新規チューブを設置する個数
    double real_amt = 0;          // 実量
    int use_blocks = 0;           // 分子
    int blocks = 0;               // 分母
};

struct Palette {
    int tube_idx = -1;
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
struct PaletteControler {
    int tube_idx;
    Palette primary;
    Palette secondary;
    // 連続量 → ブロック量 へ丸め込む(切り落とし，切り上げ双方で)
    // プライマリー，セカンダリーの単体を用いる
    pair<Action, Action> discretise_one(double amt, bool not_add) const {
        assert(primary.tube_idx != -1 or secondary.tube_idx != -1);

        Action best_l, best_r;
        best_l.tube_idx = -1;
        best_r.tube_idx = -1;
        best_l.real_amt = 1e100;
        best_r.real_amt = 1e100;

        Action a;
        if (primary.tube_idx != -1) {
            if (!not_add or primary.cap >= amt) {
                auto [l, r] = discretise_primary(amt);
                if (abs(amt - l.real_amt) < abs(best_l.real_amt - amt)) {
                    best_l = l;
                }
                if (abs(amt - r.real_amt) < abs(best_r.real_amt - amt)) {
                    best_r = r;
                }
            }
        }
        if (secondary.tube_idx != -1) {
            if (!not_add or secondary.cap >= amt) {
                auto [l, r] = discretise_secondary(amt);
                if (abs(amt - l.real_amt) < abs(best_l.real_amt - amt)) {
                    best_l = l;
                }
                if (abs(amt - r.real_amt) < abs(best_r.real_amt - amt)) {
                    best_r = r;
                }
            }
        }
        return {best_l, best_r};
    }
    pair<Action, Action> discretise_primary(double amt) const {
        Action best_l, best_r;
        best_l.tube_idx = -1;
        best_r.tube_idx = -1;
        best_l.real_amt = 1e100;
        best_r.real_amt = 1e100;
        if (primary.tube_idx == -1) {
            return {best_l, best_r};
        }
        assert(primary.tube_idx != -1);

        Action a;
        if (primary.tube_idx != -1) {
            a.i = primary.ti;
            a.j = primary.tj;
            a.primary_or_secandary = 1;
            for (int use_blocks = primary.used_blocks;
                 use_blocks <= primary.blocks; use_blocks++) {
                if (use_blocks == 0) {
                    continue;
                }
                a.add_new = 0;
                a.tube_idx = tube_idx;
                a.blocks = use_blocks;
                double new_cap = primary.cap;
                while (new_cap < amt) {
                    new_cap += 1.0;
                    a.add_new++;
                }

                double unit = new_cap / use_blocks;
                a.use_blocks = int(floor(amt / unit));
                a.real_amt = new_cap * a.use_blocks / use_blocks;
                if (abs(a.real_amt - amt) < abs(best_l.real_amt - amt)) {
                    best_l = a;
                }

                a.use_blocks = int(ceil(amt / unit));
                a.real_amt = new_cap * a.use_blocks / use_blocks;
                if (abs(a.real_amt - amt) < abs(best_r.real_amt - amt)) {
                    best_r = a;
                }
            }
        }
        return {best_l, best_r};
    }
    pair<Action, Action> discretise_secondary(double amt) const {
        Action best_l, best_r;
        best_l.tube_idx = -1;
        best_r.tube_idx = -1;
        best_l.real_amt = 1e100;
        best_r.real_amt = 1e100;
        if (secondary.tube_idx == -1) {
            return {best_l, best_r};
        }
        Action a;
        assert(secondary.tube_idx != -1);
        if (secondary.tube_idx != -1) {
            a.i = secondary.ti;
            a.j = secondary.tj;
            a.primary_or_secandary = 2;
            for (int use_blocks = secondary.used_blocks;
                 use_blocks <= secondary.blocks; use_blocks++) {
                if (use_blocks == 0) {
                    continue;
                }
                a.add_new = 0;
                a.tube_idx = tube_idx;
                a.blocks = use_blocks;
                double new_cap = secondary.cap;
                while (new_cap < amt) {
                    new_cap += 1.0;
                    a.add_new++;
                }

                double unit = new_cap / use_blocks;
                a.use_blocks = int(floor(amt / unit));
                a.real_amt = new_cap * a.use_blocks / use_blocks;
                if (abs(a.real_amt - amt) < abs(best_l.real_amt - amt)) {
                    best_l = a;
                }

                a.use_blocks = int(ceil(amt / unit));
                a.real_amt = new_cap * a.use_blocks / use_blocks;
                if (abs(a.real_amt - amt) < abs(best_r.real_amt - amt)) {
                    best_r = a;
                }
            }
        }
        return {best_l, best_r};
    }
    // 連続量 → ブロック量 へ丸め込む(切り落とし，切り上げ双方で)
    // プライマリー，セカンダリーの双方の和として用いる
    pair<pair<Action, Action>, pair<Action, Action>>
    discretise_two(double amt, bool almost_end) const {
        // assert(primary.tube_idx != -1 and secondary.tube_idx != -1);
        bool can_add = true;
        if (almost_end) {
            double sum_amt = 0;
            if (primary.tube_idx >= 0) {
                sum_amt += primary.cap;
            }
            if (secondary.tube_idx >= 0) {
                sum_amt += secondary.cap;
            }
            if (sum_amt >= amt) {
                can_add = false;
            }
        }
        pair<Action, Action> best_l, best_r;
        best_l.first.tube_idx = -1;
        best_l.second.tube_idx = -1;
        best_r.first.tube_idx = -1;
        best_r.second.tube_idx = -1;
        best_l.first.real_amt = 1e100;
        best_l.second.real_amt = 1e100;
        best_r.first.real_amt = 1e100;
        best_r.second.real_amt = 1e100;
        if (primary.tube_idx == -1) {
            auto [l, r] = discretise_secondary(amt);
            best_l.first = l;
            best_r.first = r;
            return {best_l, best_r};
        } else if (secondary.tube_idx == -1) {
            auto [l, r] = discretise_primary(amt);
            best_l.first = l;
            best_r.first = r;
            return {best_l, best_r};
        }
        double min_diff_l = 1e100;
        double min_diff_r = 1e100;
        Action none_action;
        none_action.tube_idx = -1;
        none_action.real_amt = 1e100;
        if (rnd::xorshift32() & 1) {
            for (int blocks = primary.used_blocks; blocks <= primary.blocks;
                 blocks++) {
                if (blocks == 0) {
                    continue;
                }
                for (int use_blocks = 0; use_blocks <= blocks; use_blocks++) {
                    if (min_diff_l < 1e-5 and min_diff_r < 1e-5) {
                        return {best_l, best_r};
                    }
                    Action primary_l_action;
                    double primary_use_amt;
                    double need_amt;
                    if (can_add and primary.cap < 0.2 and primary.cap < amt) {
                        primary_l_action.add_new = 1;
                        primary_use_amt =
                            (primary.cap + 1) * use_blocks / blocks;
                        need_amt = amt - primary_use_amt;
                        if (secondary.cap < need_amt and almost_end) {
                            continue;
                        }
                    } else {
                        primary_use_amt = primary.cap * use_blocks / blocks;
                        need_amt = amt - primary_use_amt;
                    }

                    if (can_add == false and secondary.cap < need_amt) {
                        continue;
                    }
                    primary_l_action.i = primary.ti;
                    primary_l_action.j = primary.tj;
                    primary_l_action.tube_idx = tube_idx;
                    primary_l_action.blocks = blocks;
                    primary_l_action.use_blocks = use_blocks;
                    primary_l_action.real_amt = primary_use_amt;
                    primary_l_action.primary_or_secandary = 1;
                    if (need_amt <= 0) {
                        if (can_add and
                            abs(primary_use_amt - amt) < min_diff_r) {
                            min_diff_r = abs(primary_use_amt - amt);
                            best_r.first = primary_l_action;
                            best_r.second = none_action;
                        }
                        break;
                    }
                    auto [secondary_l_action, secondary_r_action] =
                        discretise_secondary(need_amt);
                    if (abs(amt - primary_use_amt -
                            secondary_l_action.real_amt) < min_diff_l) {
                        min_diff_l = abs(amt - primary_use_amt -
                                         secondary_l_action.real_amt);
                        best_l = {primary_l_action, secondary_l_action};
                    }
                    if (abs(amt - primary_use_amt -
                            secondary_r_action.real_amt) < min_diff_r) {
                        min_diff_r = abs(amt - primary_use_amt -
                                         secondary_r_action.real_amt);
                        best_r = {primary_l_action, secondary_r_action};
                    }
                }
            }
        } else {
            for (int blocks = secondary.used_blocks; blocks <= secondary.blocks;
                 blocks++) {
                if (blocks == 0) {
                    continue;
                }
                for (int use_blocks = 0; use_blocks <= blocks; use_blocks++) {
                    if (min_diff_l < 1e-5 and min_diff_r < 1e-5) {
                        return {best_l, best_r};
                    }

                    Action secondary_l_action;
                    double secondary_use_amt;
                    double need_amt;
                    if (can_add and secondary.cap < 0.2 and
                        secondary.cap < amt) {
                        secondary_l_action.add_new = 1;
                        secondary_use_amt =
                            (secondary.cap + 1) * use_blocks / blocks;
                        need_amt = amt - secondary_use_amt;
                        if (primary.cap < need_amt and almost_end) {
                            continue;
                        }
                    } else {
                        secondary_use_amt = secondary.cap * use_blocks / blocks;
                        need_amt = amt - secondary_use_amt;
                    }
                    if (can_add == false and primary.cap < need_amt) {
                        continue;
                    }
                    secondary_l_action.i = secondary.ti;
                    secondary_l_action.j = secondary.tj;
                    secondary_l_action.tube_idx = tube_idx;
                    secondary_l_action.blocks = blocks;
                    secondary_l_action.use_blocks = use_blocks;
                    secondary_l_action.real_amt = secondary_use_amt;
                    secondary_l_action.primary_or_secandary = 2;
                    if (need_amt <= 0) {
                        if (can_add and
                            abs(secondary_use_amt - amt) < min_diff_r) {
                            min_diff_r = abs(secondary_use_amt - amt);
                            best_r.first = none_action;
                            best_r.second = secondary_l_action;
                        }
                        break;
                    }
                    auto [primary_l_action, primary_r_action] =
                        discretise_primary(need_amt);
                    if (abs(amt - secondary_use_amt -
                            primary_l_action.real_amt) < min_diff_l) {
                        min_diff_l = abs(amt - secondary_use_amt -
                                         primary_l_action.real_amt);
                        best_l = {primary_l_action, secondary_l_action};
                    }
                    if (abs(amt - secondary_use_amt -
                            primary_r_action.real_amt) < min_diff_r) {
                        min_diff_r = abs(amt - secondary_use_amt -
                                         primary_r_action.real_amt);
                        best_r = {primary_r_action, secondary_l_action};
                    }
                }
            }
        }
        return {best_l, best_r};
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
struct Well2 {
    int i, j;    // 代表の座標
    double cap;  // 絵具の上限
    MixState ms; // 色とか量とか
};

// ──────────────────────────────
//  6. Tが小さいときのための特殊ソルバー
// ──────────────────────────────
class Small_T_Solver {
    const Input &in;
    int tubes_used = 0;
    double err_sum = 0;
    double eps = 1e-6;
    int well_w = 1;
    int well_h = 4;
    double well_cap = well_w * well_h;
    int well_num = in.N / well_w * in.N / well_h;
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
            rep(i, min(2, max_turn + 1)) {
                if (i + well.amt > well.cap) {
                    break;
                }
                if (false and actions[i].size() > 1000) {
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
                        // cost +=
                        //     max(0.0, well.amt + action.amt - well.cap) *
                        //     in.D;
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
                        // if (tubes_used > 1000) {
                        //     cost += (action.actions.size() - 1.0) * in.D;
                        // }
                        // cost +=
                        //     max(0.0, well.amt + action.amt - well.cap) *
                        //     in.D;
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
                if (i + well.amt > well.cap) {
                    break;
                }
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
                if (i + well.amt > well.cap) {
                    break;
                }
                for (const auto &action : actions[i]) {
                    if (well.amt + action.amt < 1.0 - eps) {
                        continue;
                    }
                    double cost = 0;
                    // if (tubes_used > 1000) {
                    //     cost += (action.actions.size() - 1.0) * in.D;
                    // }
                    // cost += max(0.0, well.amt + action.amt - well.cap) *
                    // in.D;
                    cost += well.error_if_add(tgt, action);
                    if (cost < min_cost) {
                        min_cost = cost;
                        best_well_idx = -1;
                        best_action = action;
                    }
                }
            }
        }
        cerr << "min_cost: " << min_cost << '\n';
        return {best_well_idx, is_dump, best_action};
    }

    void init_wells() {
        used_wells.reserve(max_well);
        clean_wells.reserve(max_well);
        for (int i = 0; i < in.N; i += well_h) {
            for (int j = 0; j < in.N; j += well_w) {
                Well well;
                well.amt = 0;
                well.i = i;
                well.j = j;
                well.cap = well_cap;
                clean_wells.push_back(well);
            }
        }
    }
    void init_palettes() {
        sep_v = vector<string>(in.N);
        sep_h = vector<string>(in.N - 1);
        rep(i, in.N) {
            rep(j, in.N - 1) {
                if (j % well_w != well_w - 1) {
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
                if (i % well_h != well_h - 1) {
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
    vector<PaletteControler> palettes;
    vector<vector<int>> cmds; // 出力コマンド蓄積

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
    vector<vector<vector<double>>> best_coefs;
    vector<vector<double>> best_coefs_err;
    // vector<vector<double>> init_coefs;
    int max_palettes;
    int MODE_THRESHOLD = 27000;

  public:
    int final_cost;

    Solver(const Input &_in, TimeKeeper tk) : in(_in), tk(tk) {
        make_best_coefs();
    }

    //----------------------------------
    void solve() {
        // dpで各ターンの使用色数を暫定計算
        vector<int> can_use_colors = calc_use_colors();
        vector<int> used_tube_cnt(in.K);
        rep(h, in.H) {
            const vector<double> &coef = best_coefs[can_use_colors[h]][h];
            rep(i, in.K) {
                if (coef[i] > 0.0) {
                    used_tube_cnt[i]++;
                }
            }
        }
        // 色の使用頻度に合わせて行数を調整
        for (int idx : in.need_idxs) {
            used_tube_cnt[idx]++;
        }
        for (auto &c : used_tube_cnt) {
            c = sqrt(c);
        }

        vector<int> lines_size = calc_lines_size(used_tube_cnt);
        init_palettes(lines_size);
        err_sum = 0;
        tubes_used = 0;

        rep(h, in.H) {
            const Color &tgt = in.targets[h];
            int colors = can_use_colors[h];
            max_palettes =
                (in.T - cmds.size() - 3 * (in.H - h)) / (4 * (in.H - h));
            colors = max(colors, max_palettes);
            colors = min(colors, 4);
            cerr << "Use_Colors: " << h + 1 << " " << colors << '\n';
            auto coef = best_coefs[colors][h];
            tk.update();
            double disc_tl = (2800 - tk.now()) / (in.H - h + 1);
            auto acts = discretise(tgt, coef, disc_tl, h);
            cerr << "連続値のエラー: " << error_only(tgt, coef)
                 << " 離散値のエラー: " << error_only(tgt, acts) << '\n';
            double sum = 0;
            for (const auto &p : palettes) {
                if (p.primary.tube_idx >= 0) {
                    sum += p.primary.cap;
                }
                if (p.secondary.tube_idx >= 0) {
                    sum += p.secondary.cap;
                }
            }
            cerr << "turn: " << h << "sum: " << sum << '\n';

            if (sum >= (double)(in.H - h)) {
                if (sum >= 1 - eps) {
                    tk.update();
                    double disc_tl = (2800 - tk.now()) / (in.H - h + 1);
                    auto tmp_coef = optimize_continuous(tgt);
                    int cnt = 0;
                    for (auto c : tmp_coef) {
                        if (c > 1e-9) {
                            cnt++;
                        }
                    }
                    vector<Action> tmp_acts;
                    bool ok = true;
                    if (cnt <= 6) {
                        tmp_acts = discretise(tgt, tmp_coef, disc_tl, h);
                    } else {
                        tie(ok, tmp_acts) = discretise_fast(tgt, tmp_coef, h);
                    }
                    if (ok) {
                        double cost = error_only(tgt, acts);
                        double tmp_cost = error_only(tgt, tmp_acts);
                        {
                            int add_tube = 0;
                            for (const auto &a : acts) {
                                add_tube += a.add_new;
                            }
                            cost += add_tube * in.D;
                        }
                        {
                            int add_tube = 0;
                            for (const auto &a : tmp_acts) {
                                add_tube += a.add_new;
                            }
                            tmp_cost += add_tube * in.D;
                        }
                        cerr << "old_cost: " << cost
                             << " new_cost: " << tmp_cost << '\n';
                        if (tmp_cost < cost) {
                            acts = tmp_acts;
                        }
                    }
                }
            }
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
    }

  private:
    vector<int> calc_use_colors() {
        // dpで各ターンに使用すべき絵具の本数を計算する
        if (in.T >= 20000) {
            return vector<int>(in.H, 4);
        }
        // i個目の目標まででjターン使用した場合の(エラーの合計の最小値,
        // iターン目に使用するターン数)
        int can_use_turn = (in.T - 3000) / 4;
        vector<vector<pair<double, int>>> dp(
            in.H + 1,
            vector<pair<double, int>>(can_use_turn + 1, make_pair(1e100, -1)));
        dp[0][0] = {0.0, -1};
        rep(i, in.H) {
            rep(j, can_use_turn) {
                if (dp[i][j].first == 1e100) {
                    continue;
                }
                for (int k = 1; k <= 4; k++) {
                    if (j + k > can_use_turn) {
                        break;
                    }
                    if (dp[i][j].first + best_coefs_err[k][i] <
                        dp[i + 1][j + k].first) {
                        dp[i + 1][j + k].first =
                            dp[i][j].first + best_coefs_err[k][i];
                        dp[i + 1][j + k].second = k;
                    }
                }
            }
        }
        pair<double, int> best_pair = {1e100, -1};
        int now_turn;
        rep(i, can_use_turn + 1) {
            if (dp[in.H][i].first < best_pair.first) {
                best_pair = dp[in.H][i];
                now_turn = i;
            }
        }
        vector<int> res(in.H);
        for (int i = in.H; i > 0; i--) {
            res[i - 1] = dp[i][now_turn].second;
            now_turn -= dp[i][now_turn].second;
        }
        return res;
    }
    //----------------------------------
    vector<int> calc_lines_size(vector<int> used_tube_cnt) {
        // todo used_tube_cnt はsqrtとっても良いかも
        int total_lines = 20;
        int K = in.K;

        // まず、used_tube_cnt[i] > 0 なら必ず 1 行を確保
        int count_pos = 0;
        for (int i = 0; i < K; ++i) {
            if (used_tube_cnt[i] > 0) {
                count_pos++;
            }
        }

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
        if (MODE_THRESHOLD <= in.T) {
            // 分割型
            rep(i, in.K) {
                palettes[i].tube_idx = i;
                palettes[i].primary.lines =
                    lines_size[i] / 2 + lines_size[i] % 2;
                palettes[i].secondary.lines =
                    lines_size[i] - palettes[i].primary.lines;
            }
        } else {
            // 既存の
            rep(i, in.K) {
                palettes[i].tube_idx = i;
                palettes[i].primary.lines = lines_size[i];
            }
        }

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
            if (palettes[k].primary.lines > 0) {
                auto &p = palettes[k].primary;
                p.tube_idx = k;
                p.si = row;
                p.sj = 1;
                row += p.lines;
                p.build();
            }
            if (row < in.N)
                sep_v[row][0] = '0';
            if (palettes[k].secondary.lines > 0) {
                auto &p = palettes[k].secondary;
                p.tube_idx = k;
                p.si = row;
                p.sj = 1;
                row += p.lines;
                p.build();
            }
        }

        // 横仕切り
        row = 0;
        rep(k, in.K) {
            if (palettes[k].primary.lines > 0) {
                auto &p = palettes[k].primary;
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
            if (palettes[k].secondary.lines > 0) {
                auto &p = palettes[k].secondary;
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
    pair<bool, vector<Action>> discretise_fast(const Color &tgt,
                                               const vector<double> &coef,
                                               int now_turn) {
        // プライマリ or セカンダリ
        vector<pair<Action, Action>> nearest_acts;
        // 併用
        vector<pair<pair<Action, Action>, pair<Action, Action>>>
            nearest_acts_pair;

        nearest_acts.clear();
        nearest_acts_pair.clear();
        rep(i, in.K) {
            if (coef[i] < 1e-9) {
                continue;
            }
            double amt = coef[i];
            auto [best_l, best_r] = palettes[i].discretise_one(
                amt, now_turn >= 980 and max_palettes >= 8 and
                         in.T >= MODE_THRESHOLD);
            nearest_acts.push_back({best_l, best_r});
            if (in.T >= MODE_THRESHOLD) {
                auto [best_l, best_r] =
                    palettes[i].discretise_two(amt, now_turn >= 980);
                nearest_acts_pair.push_back({best_l, best_r});
            }
        }

        vector<Action> acts;
        rep(i, nearest_acts.size()) {
            const auto &a = nearest_acts[i];
            const auto &p = nearest_acts_pair[i];
            if (a.second.tube_idx >= 0) {
                acts.push_back(a.second);
            } else if (p.second.first.tube_idx >= 0 or
                       p.second.second.tube_idx >= 0) {
                if (p.second.first.tube_idx >= 0) {
                    acts.push_back(p.second.first);
                }
                if (p.second.second.tube_idx >= 0) {
                    acts.push_back(p.second.second);
                }
            } else {
                return {false, {}};
            }
        }
        if (max_palettes < acts.size()) {
            return {false, acts};
        }
        return {true, acts};
    }
    vector<Action> discretise(const Color &tgt, const vector<double> &coef,
                              double tl, int now_turn) {
        vector<Action> best_acts;
        double min_cost = 1e100;
        vector<Action> new_acts;
        new_acts.reserve(in.K);
        // プライマリ or セカンダリ
        vector<pair<Action, Action>> nearest_acts;
        // 併用
        vector<pair<pair<Action, Action>, pair<Action, Action>>>
            nearest_acts_pair;
        vector<double> new_coef(in.K);
        double best_alph = -1;
        // cerr << "now palette" << '\n';
        // for (const auto &p : palettes) {
        //     if (p.primary.tube_idx >= 0) {
        //         cerr << p.tube_idx << ' ' << p.primary.tube_idx << ' '
        //              << p.primary.cap << ' ' << '\n';
        //     }
        //     if (p.secondary.tube_idx >= 0) {
        //         cerr << p.tube_idx << ' ' << p.secondary.tube_idx << ' '
        //              << p.secondary.cap << ' ' << '\n';
        //     }
        // }
        int iter = 0;
        TimeKeeper tk(tl);
        double alp = 1.0;
        while (true) {
            if (iter > 0) {
                alp = 1.0 + rnd::uniform_real(
                                0.0, 0.5 * (double)(10000 - in.D) / 10000.0);
            }
            iter++;
            if (iter % 3 == 0) {
                tk.update();
                if (tk.over()) {
                    cerr << "iter: " << iter << '\n';
                    break;
                }
            }
            nearest_acts.clear();
            nearest_acts_pair.clear();
            rep(i, in.K) { new_coef[i] = alp * coef[i]; }
            rep(i, in.K) {
                if (new_coef[i] < 1e-9) {
                    continue;
                }
                double amt = new_coef[i];
                auto [best_l, best_r] = palettes[i].discretise_one(
                    amt, now_turn >= 980 and max_palettes >= 8 and
                             in.T >= MODE_THRESHOLD);
                nearest_acts.push_back({best_l, best_r});
                if (in.T >= MODE_THRESHOLD) {
                    auto [best_l, best_r] =
                        palettes[i].discretise_two(amt, now_turn >= 980);
                    nearest_acts_pair.push_back({best_l, best_r});
                }
            }
            if (in.T < MODE_THRESHOLD) {
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
                        best_alph = alp;
                    }
                }
            } else {
                // cerr << "now_turn: " << now_turn << '\n';
                // vector<double> tmp1_coef(in.K, 0.0);
                // vector<double> tmp2_coef(in.K, 0.0);
                // for (auto &p : nearest_acts_pair) {
                //     if (p.second.first.tube_idx >= 0) {
                //         cerr << p.second.first.tube_idx << ' '
                //              << p.second.first.primary_or_secandary << ' '
                //              << p.second.first.real_amt << ' '
                //              << p.second.first.add_new << '\n';
                //         tmp1_coef[p.second.first.tube_idx] +=
                //             p.second.first.real_amt;
                //     }
                //     if (p.second.second.tube_idx >= 0) {
                //         cerr << p.second.second.tube_idx << ' '
                //              << p.second.second.primary_or_secandary << ' '
                //              << p.second.second.real_amt << ' '
                //              << p.second.second.add_new << '\n';
                //         tmp1_coef[p.second.second.tube_idx] +=
                //             p.second.second.real_amt;
                //     }
                // }

                // rep(i, in.K) {
                //     cerr << new_coef[i] << ((i < in.K - 1) ? " " : "\n");
                // }
                // rep(i, in.K) {
                //     cerr << tmp1_coef[i] << ((i < in.K - 1) ? " " : "\n");
                // }

                rep(mask, 1 << (nearest_acts.size() * 2)) {
                    double amt_sum = 0.0;
                    new_acts.clear();
                    bool valid = true;
                    rep(i, nearest_acts.size()) {
                        if (max_palettes < new_acts.size()) {
                            break;
                        }
                        if ((mask >> (2 * i) & 3) == 0) {
                            // l 単数
                            if (nearest_acts[i].first.tube_idx == -1)
                                continue;
                            amt_sum += nearest_acts[i].first.real_amt;
                            new_acts.push_back(nearest_acts[i].first);
                        } else if ((mask >> (2 * i) & 3) == 1) {
                            // l 複数
                            if (nearest_acts_pair[i].first.first.tube_idx >=
                                0) {
                                amt_sum +=
                                    nearest_acts_pair[i].first.first.real_amt;
                                new_acts.push_back(
                                    nearest_acts_pair[i].first.first);
                            }
                            if (nearest_acts_pair[i].first.second.tube_idx >=
                                0) {
                                amt_sum +=
                                    nearest_acts_pair[i].first.second.real_amt;
                                new_acts.push_back(
                                    nearest_acts_pair[i].first.second);
                            }

                        } else if ((mask >> (2 * i) & 3) == 2) {
                            // r 単数
                            if (nearest_acts[i].second.tube_idx == -1)
                                continue;
                            amt_sum += nearest_acts[i].second.real_amt;
                            new_acts.push_back(nearest_acts[i].second);
                        } else if ((mask >> (2 * i) & 3) == 3) {
                            // r 複数
                            if (nearest_acts_pair[i].second.first.tube_idx >=
                                0) {
                                amt_sum +=
                                    nearest_acts_pair[i].second.first.real_amt;
                                new_acts.push_back(
                                    nearest_acts_pair[i].second.first);
                            }
                            if (nearest_acts_pair[i].second.second.tube_idx >=
                                0) {
                                amt_sum +=
                                    nearest_acts_pair[i].second.second.real_amt;
                                new_acts.push_back(
                                    nearest_acts_pair[i].second.second);
                            }
                        }
                    }
                    if (amt_sum < 1.0 - eps) {
                        continue;
                    }
                    if (max_palettes < new_acts.size()) {
                        continue;
                    }
                    double new_cost = cost(tgt, new_acts);
                    if (new_cost < min_cost) {
                        // vector<double> tmp1_coef(in.K, 0.0);
                        // vector<double> tmp2_coef(in.K, 0.0);
                        // for (auto &a : new_acts) {
                        //     cerr << a.tube_idx << ' ' <<
                        //     a.primary_or_secandary
                        //          << ' ' << a.real_amt << " " << a.add_new
                        //          << '\n';
                        //     tmp1_coef[a.tube_idx] += a.real_amt;
                        // }

                        // rep(i, in.K) {
                        //     cerr << new_coef[i]
                        //          << ((i < in.K - 1) ? " " : "\n");
                        // }
                        // rep(i, in.K) {
                        //     cerr << tmp1_coef[i]
                        //          << ((i < in.K - 1) ? " " : "\n");
                        // }
                        min_cost = new_cost;
                        best_acts = new_acts;
                        best_alph = alp;
                    }
                }
            }
        }
        cerr << "best_acts_size: " << best_acts.size() << '\n';
        cerr << "best_alp: " << best_alph << '\n';
        return best_acts;
    }

    vector<double> optimize_continuous(const Color &tgt,
                                       int max_iters = 10000) {
        int K = in.K;
        vector<double> coef(K, 0.0), best_coef(K, 0.0), max_coef(K, 0.0);
        double sum = 0.0;

        // 上限を設定しつつ初期coefにキャパを足してsumを計算
        rep(i, K) {
            double cap = 0;
            if (palettes[i].primary.tube_idx >= 0)
                cap += palettes[i].primary.cap;
            if (palettes[i].secondary.tube_idx >= 0)
                cap += palettes[i].secondary.cap;
            max_coef[i] = cap;
            coef[i] = cap;
            sum += cap;
        }
        assert(sum >= 1 - 1e-6);

        double best_cost = error_only(tgt, coef);
        best_coef = coef;

        // 温度スケジュール: t = 1.0 -> 0.001
        for (int it = 0; it < max_iters; ++it) {
            double t = 100.0 - double(it) / max_iters;
            if (t < 0.001)
                t = 0.001;

            int idx = rnd::xorshift32() % K;
            double diff = rnd::uniform_real(-0.3, 0.3);

            if (coef[idx] + diff < 0 || coef[idx] + diff > max_coef[idx] ||
                sum + diff < 1 - 1e-6) {
                continue;
            }

            coef[idx] += diff;
            sum += diff;
            double new_cost = error_only(tgt, coef);

            if (new_cost < best_cost ||
                rnd::uniform_real(0.0, 1.0) < exp((best_cost - new_cost) / t)) {
                best_cost = new_cost;
                best_coef = coef;
            } else {
                coef[idx] -= diff;
                sum -= diff;
            }
        }

        return best_coef;
    }

    double cost(const Color &tgt, const vector<double> &coef) const {
        static MixState s;
        s.clear();
        double total = 0;
        rep(i, in.K) {
            s.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, coef[i]);
            total += coef[i];
        }
        if (total < 1 - 1e-6) {
            return 1e100;
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
        if (total < 1 - 1e-6) {
            return 1e100;
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

    void make_best_coefs() {
        best_coefs = vector<vector<vector<double>>>(5);
        best_coefs_err = vector<vector<double>>(5);

        int M = (int)in.need_idxs.size();
        rep(tgt_index, in.H) {
            int K = in.K;
            std::vector<double> best(K, 0.0);
            double best_e2 = 1e300;
            const Color &tgt = in.targets[tgt_index];
            // ――――――――――――――――――――――――――――――――――――
            //  1) 単色 (lim >= 1)
            // ――――――――――――――――――――――――――――――――――――
            if (M >= 1) {
                double best1 = 1e300;
                int bestIdx = -1;
                for (int xi = 0; xi < M; ++xi) {
                    int i = in.need_idxs[xi];
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
            best_coefs[1].push_back(best);
            best_coefs_err[1].push_back(sqrt(best_e2) * 10000.0);
            // ――――――――――――――――――――――――――――――――――――
            //  2) 二色混合 (lim >= 2)
            // ――――――――――――――――――――――――――――――――――――
            if (M >= 2) {
                for (int xi = 0; xi < M; ++xi) {
                    int i = in.need_idxs[xi];
                    for (int xj = xi + 1; xj < M; ++xj) {
                        int j = in.need_idxs[xj];

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
            best_coefs[2].push_back(best);
            best_coefs_err[2].push_back(sqrt(best_e2) * 10000.0);
            // ――――――――――――――――――――――――――――――――――――
            //  3) 三色混合 (lim >= 3)
            // ――――――――――――――――――――――――――――――――――――
            if (M >= 3) {
                for (int xi = 0; xi < M; ++xi) {
                    int i = in.need_idxs[xi];
                    for (int xj = xi + 1; xj < M; ++xj) {
                        int j = in.need_idxs[xj];
                        for (int xk = xj + 1; xk < M; ++xk) {
                            int k = in.need_idxs[xk];

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
            best_coefs[3].push_back(best);
            best_coefs_err[3].push_back(sqrt(best_e2) * 10000.0);
            // ――――――――――――――――――――――――――――――――――――
            //  4) 四色混合 (lim >= 4)
            // ――――――――――――――――――――――――――――――――――――
            if (M >= 4) {
                for (int xi = 0; xi < M; ++xi) {
                    int i = in.need_idxs[xi];
                    for (int xj = xi + 1; xj < M; ++xj) {
                        int j = in.need_idxs[xj];
                        for (int xk = xj + 1; xk < M; ++xk) {
                            int k = in.need_idxs[xk];
                            for (int xl = xk + 1; xl < M; ++xl) {
                                int l = in.need_idxs[xl];

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
                                        std::fill(best.begin(), best.end(),
                                                  0.0);
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
            best_coefs[4].push_back(best);
            best_coefs_err[4].push_back(sqrt(best_e2) * 10000.0);
        }
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
            auto &p = a.primary_or_secandary == 1
                          ? palettes[a.tube_idx].primary
                          : palettes[a.tube_idx].secondary;
            // 分母の変更
            if (p.used_blocks != a.blocks) {
                // 左を閉じる(分母を決める)
                auto s = p.cmd_sep(p.blocks - a.blocks);
                if (!s.empty()) {
                    cmds.push_back(s);
                }
                // 区切りを空ける
                s = p.cmd_sep(p.blocks - p.used_blocks);
                if (!s.empty()) {
                    cmds.push_back(s);
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
            }
            // 左を開ける
            s = p.cmd_sep(p.blocks - a.blocks);
            if (!s.empty()) {
                sep.push_back(s);
            }
            p.used_blocks = a.blocks - a.use_blocks;
            p.cap = p.cap * p.used_blocks / a.blocks;
            amt_sum += a.real_amt;
        }
        for (auto &v : sep)
            cmds.push_back(v);
        cmds.push_back({2, 0, 0});
        while (amt_sum > 1.0 - eps) {
            cmds.push_back({3, 0, 0});
            amt_sum -= 1.0;
        }
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
    if (in.T < 19000) {
        Small_T_Solver sol(in);
        // AddTubeSolver sol(in);
        sol.solve();
        tk.update();
        if (tk.now() < 2000.0 and 12000 <= in.T) {
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

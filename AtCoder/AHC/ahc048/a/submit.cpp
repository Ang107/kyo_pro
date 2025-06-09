#include <atcoder/all>
#include <bits/stdc++.h>
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
    MixState(double c, double m, double y, double amt)
        : c(c), m(m), y(y), amt(amt) {} // 総量
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
        if (amt < 1.0 - 1e-6) {
            amt = 0.0;
            clear();
        } else {
            amt -= 1.0;
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
        if (amt == 0.0) {
            return 0;
        }
        uint64_t h_c = round(c * 10000);
        uint64_t h_m = round(m * 10000);
        uint64_t h_y = round(y * 10000);
        uint64_t hash = (h_c << 28) | (h_m << 14) | (h_y);
        return hash;
    }
};

namespace fraction {

struct Fraction {
    int numerator;   // 分子
    int denominator; // 分母
    double decimal;  // 分子 / 分母の計算結果
    Fraction(int numerator, int denominator)
        : numerator(numerator), denominator(denominator),
          decimal((double)numerator / (double)denominator) {}
    bool operator==(const Fraction &other) const {
        return numerator * other.denominator == other.numerator * denominator;
    }
    bool operator!=(const Fraction &other) const {
        return numerator * other.denominator != other.numerator * denominator;
    }
    bool operator<(const Fraction &other) const {
        if (numerator * other.denominator != other.numerator * denominator) {
            // 単純な大きさで比較

            return numerator * other.denominator <
                   other.numerator * denominator;
        } else {
            // 等しいならば、分子同士の大きさで比較
            return numerator < other.numerator;
        }
    }
    bool operator<(double amt) const { return decimal < amt; }
    friend bool operator<(double amt, const Fraction &f) {
        return amt < f.decimal;
    }
};
// 分母の最小値が i で最大値が j のときの構成可能な実数の一覧(0~1)
array<array<vector<Fraction>, 401>, 401> fractions;

const vector<Fraction> &get_fractions(int min_denominator,
                                      int max_denominator) {
    if (fractions[min_denominator][max_denominator].size() == 0) {
        // assert(min_denominator > 0 and max_denominator > 0);
        assert(min_denominator <= max_denominator);
        assert(max_denominator <= 400);
        // 構築
        vector<Fraction> tmp;
        tmp.reserve(max_denominator * max_denominator);
        for (int denominator = min_denominator; denominator <= max_denominator;
             denominator++) {
            if (denominator == 0) {
                continue;
            }
            for (int numerator = 0; numerator <= denominator; numerator++) {
                tmp.push_back(Fraction(numerator, denominator));
            }
        }
        // ソート
        sort(tmp.begin(), tmp.end());
        // 重複除去
        vector<Fraction> duplicate_removal;
        duplicate_removal.reserve(tmp.size());
        assert(tmp.size() > 0);
        duplicate_removal.push_back(tmp[0]);
        for (int idx = 1; idx < tmp.size(); idx++) {
            if (tmp[idx] != duplicate_removal.back()) {
                duplicate_removal.push_back(tmp[idx]);
            }
        }
        fractions[min_denominator][max_denominator] = duplicate_removal;
    }
    return fractions[min_denominator][max_denominator];
}
// value以下のもので最大を返す。存在しなければfalse
pair<bool, Fraction> le(const vector<Fraction> &fractions, double value) {
    auto it = upper_bound(fractions.begin(), fractions.end(), value);
    if (it == fractions.begin()) {
        return {false, Fraction(0, 1)};
    }
    it--;
    return {true, *it};
}

// value以上のもので最小を返す。存在しなければfalse
pair<bool, Fraction> ge(const vector<Fraction> &fractions, double value) {
    auto it = lower_bound(fractions.begin(), fractions.end(), value);
    if (it == fractions.end()) {
        return {false, Fraction(0, 1)};
    }
    return {true, *it};
}
}; // namespace fraction
// ──────────────────────────────
//  4. パレット上の 1 チューブ管理
// ──────────────────────────────
struct Action {                   // 操作1回分
    int tube_idx = 0;             // チューブ番号
    int primary_or_secondary = 0; // 1: プライマリー 2 セカンダリー
    int i = 0, j = 0;             // 追加する場所
    int add_new = 0;              // 新規チューブを設置する個数
    double real_amt = 0;          // 実量
    int use_blocks = 0;           // 分子
    int blocks = 0;               // 分母
    Action()
        : tube_idx(-1), primary_or_secondary(0), i(0), j(0), add_new(0),
          real_amt(0), use_blocks(0), blocks(0) {}
    Action(int tube_idx, int primary_or_secondary, int i, int j, int add_new,
           double real_amt, int use_blocks, int blocks)
        : tube_idx(tube_idx), primary_or_secondary(primary_or_secondary), i(i),
          j(j), add_new(add_new), real_amt(real_amt), use_blocks(use_blocks),
          blocks(blocks) {}
};

struct Palette {
    int tube_idx = -1;
    int si = 0, sj = 0; // 左上座標
    int ti = 0,
        tj = 0;          // 一番後ろの座標(絵具を入れる場所)
    int lines = 0;       // 行数(=高さ)
    double cap = 0;      // 保有量
    int used_blocks = 1; // 絵具が入っているマスの数(分母の最小値)
    int blocks = 1;      // 使えるマスのMax(分母の最大値)

    vector<pair<int, int>> path; // ハミルトン経路(行→列ジグザグ)

    // path, ti, tj, blocksを初期化する
    void build() {
        blocks = lines * 19;
        used_blocks = 1;
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
        // 現状は余裕がある場合追加はしない実装
        // 余裕がある場合でも追加した方が精度上がるならそっちを選ぶような実装もあり
        Action best_l, best_r;
        best_l = Action(-1, 1, primary.ti, primary.tj, 0, 1e100, 0, 0);
        best_r = Action(-1, 1, primary.ti, primary.tj, 0, 1e100, 0, 0);
        if (primary.tube_idx == -1) {
            return {best_l, best_r};
        }
        const auto &fractions =
            fraction::get_fractions(primary.used_blocks, primary.blocks);

        if (amt > primary.cap) {
            {
                const auto &[is_exist, frc_l] =
                    fraction::le(fractions, amt / (primary.cap + 1.0));
                if (is_exist) {
                    best_l.tube_idx = tube_idx;
                    best_l.add_new = 1;
                    best_l.blocks = frc_l.denominator;
                    best_l.use_blocks = frc_l.numerator;
                    best_l.real_amt = (primary.cap + 1.0) * frc_l.decimal;
                }
            }
            {
                const auto &[is_exist, frc_r] =
                    fraction::ge(fractions, amt / (primary.cap + 1.0));
                if (is_exist) {
                    best_r.tube_idx = tube_idx;
                    best_r.add_new = 1;
                    best_r.blocks = frc_r.denominator;
                    best_r.use_blocks = frc_r.numerator;
                    best_r.real_amt = (primary.cap + 1.0) * frc_r.decimal;
                }
            }
            {
                if (abs(primary.cap - amt) < abs(best_l.real_amt - amt)) {
                    best_l.tube_idx = tube_idx;
                    best_l.add_new = 0;
                    best_l.blocks = primary.used_blocks;
                    best_l.use_blocks = primary.used_blocks;
                    best_l.real_amt = primary.cap;
                }
            }
        } else {
            {
                const auto &[is_exist, frc_l] =
                    fraction::le(fractions, amt / primary.cap);
                if (is_exist) {
                    best_l.tube_idx = tube_idx;
                    best_l.add_new = 0;
                    best_l.blocks = frc_l.denominator;
                    best_l.use_blocks = frc_l.numerator;
                    best_l.real_amt = primary.cap * frc_l.decimal;
                }
            }
            {
                const auto &[is_exist, frc_r] =
                    fraction::ge(fractions, amt / primary.cap);
                if (is_exist) {
                    best_r.tube_idx = tube_idx;
                    best_r.add_new = 0;
                    best_r.blocks = frc_r.denominator;
                    best_r.use_blocks = frc_r.numerator;
                    best_r.real_amt = primary.cap * frc_r.decimal;
                }
            }
        }
        return {best_l, best_r};
    }
    pair<Action, Action> discretise_secondary(double amt) const {
        Action best_l, best_r;
        best_l = Action(-1, 2, secondary.ti, secondary.tj, 0, 1e100, 0, 0);
        best_r = Action(-1, 2, secondary.ti, secondary.tj, 0, 1e100, 0, 0);
        if (secondary.tube_idx == -1) {
            return {best_l, best_r};
        }
        const auto &fractions =
            fraction::get_fractions(secondary.used_blocks, secondary.blocks);

        if (amt > secondary.cap) {
            {
                const auto &[is_exist, frc_l] =
                    fraction::le(fractions, amt / (secondary.cap + 1.0));
                if (is_exist) {
                    best_l.tube_idx = tube_idx;
                    best_l.add_new = 1;
                    best_l.blocks = frc_l.denominator;
                    best_l.use_blocks = frc_l.numerator;
                    best_l.real_amt = (secondary.cap + 1.0) * frc_l.decimal;
                }
            }
            {
                const auto &[is_exist, frc_r] =
                    fraction::ge(fractions, amt / (secondary.cap + 1.0));
                if (is_exist) {
                    best_r.tube_idx = tube_idx;
                    best_r.add_new = 1;
                    best_r.blocks = frc_r.denominator;
                    best_r.use_blocks = frc_r.numerator;
                    best_r.real_amt = (secondary.cap + 1.0) * frc_r.decimal;
                }
            }
            {
                if (abs(secondary.cap - amt) < abs(best_l.real_amt - amt)) {
                    best_l.tube_idx = tube_idx;
                    best_l.add_new = 0;
                    best_l.blocks = secondary.used_blocks;
                    best_l.use_blocks = secondary.used_blocks;
                    best_l.real_amt = secondary.cap;
                }
            }
        } else {
            {
                const auto &[is_exist, frc_l] =
                    fraction::le(fractions, amt / secondary.cap);
                if (is_exist) {
                    best_l.tube_idx = tube_idx;
                    best_l.add_new = 0;
                    best_l.blocks = frc_l.denominator;
                    best_l.use_blocks = frc_l.numerator;
                    best_l.real_amt = secondary.cap * frc_l.decimal;
                }
            }
            {
                const auto &[is_exist, frc_r] =
                    fraction::ge(fractions, amt / secondary.cap);
                if (is_exist) {
                    best_r.tube_idx = tube_idx;
                    best_r.add_new = 0;
                    best_r.blocks = frc_r.denominator;
                    best_r.use_blocks = frc_r.numerator;
                    best_r.real_amt = secondary.cap * frc_r.decimal;
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
        bool add = true;
        // 両方の絵具を合わせたら足りる場合は追加を行わない
        double sum_amt = 0;
        if (primary.tube_idx >= 0) {
            sum_amt += primary.cap;
        }
        if (secondary.tube_idx >= 0) {
            sum_amt += secondary.cap;
        }
        if (sum_amt >= amt) {
            add = false;
        }
        pair<Action, Action> best_l;
        pair<Action, Action> best_r;
        best_l.first = Action(-1, 1, primary.ti, primary.tj, 0, 1e100, 0, 0);
        best_l.second =
            Action(-1, 2, secondary.ti, secondary.tj, 0, 1e100, 0, 0);
        best_r.first = Action(-1, 1, primary.ti, primary.tj, 0, 1e100, 0, 0);
        best_r.second =
            Action(-1, 2, secondary.ti, secondary.tj, 0, 1e100, 0, 0);

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
        const auto &fr_pr =
            fraction::get_fractions(primary.used_blocks, primary.blocks);
        const auto &fr_se =
            fraction::get_fractions(secondary.used_blocks, secondary.blocks);
        if (add) {
            // いずれかに追加
            {
                // primaryに追加する場合
                double new_primary_cap = primary.cap + 1.0;
                int j = fr_se.size() - 1;
                for (const auto &[num, den, dec] : fr_pr) {
                    while (j >= 0 and new_primary_cap * dec +
                                              secondary.cap * fr_se[j].decimal >
                                          amt) {
                        j--;
                    }
                    if (j >= 0) {
                        double l = new_primary_cap * dec +
                                   secondary.cap * fr_se[j].decimal;
                        if (abs(l - amt) < min_diff_l) {
                            min_diff_l = abs(l - amt);
                            best_l.first.add_new = 1;
                            best_l.first.tube_idx = primary.tube_idx;
                            best_l.first.real_amt = new_primary_cap * dec;
                            best_l.first.blocks = den;
                            best_l.first.use_blocks = num;

                            best_l.second.add_new = 0;
                            best_l.second.tube_idx = secondary.tube_idx;
                            best_l.second.real_amt =
                                secondary.cap * fr_se[j].decimal;
                            best_l.second.blocks = fr_se[j].denominator;
                            best_l.second.use_blocks = fr_se[j].numerator;
                        }
                    }
                    if (j + 1 < fr_se.size()) {
                        double r = new_primary_cap * dec +
                                   secondary.cap * fr_se[j + 1].decimal;
                        if (abs(r - amt) < min_diff_r) {
                            min_diff_r = abs(r - amt);
                            best_r.first.add_new = 1;
                            best_r.first.tube_idx = primary.tube_idx;
                            best_r.first.real_amt = new_primary_cap * dec;
                            best_r.first.blocks = den;
                            best_r.first.use_blocks = num;

                            best_r.second.add_new = 0;
                            best_r.second.tube_idx = secondary.tube_idx;
                            best_r.second.real_amt =
                                secondary.cap * fr_se[j + 1].decimal;
                            best_r.second.blocks = fr_se[j + 1].denominator;
                            best_r.second.use_blocks = fr_se[j + 1].numerator;
                        }
                    }
                    if (new_primary_cap * dec > amt) {
                        break;
                    }
                }
            }
            { // secondaryに追加する場合
                double new_secondary_cap = secondary.cap + 1.0;
                int j = fr_se.size() - 1;
                for (const auto &[num, den, dec] : fr_pr) {
                    while (j >= 0 and primary.cap * dec + new_secondary_cap *
                                                              fr_se[j].decimal >
                                          amt) {
                        j--;
                    }
                    if (j >= 0) {
                        double l = primary.cap * dec +
                                   new_secondary_cap * fr_se[j].decimal;
                        if (abs(l - amt) < min_diff_l) {
                            min_diff_l = abs(l - amt);
                            best_l.first.add_new = 0;
                            best_l.first.tube_idx = primary.tube_idx;
                            best_l.first.real_amt = primary.cap * dec;
                            best_l.first.blocks = den;
                            best_l.first.use_blocks = num;

                            best_l.second.add_new = 1;
                            best_l.second.tube_idx = secondary.tube_idx;
                            best_l.second.real_amt =
                                new_secondary_cap * fr_se[j].decimal;
                            best_l.second.blocks = fr_se[j].denominator;
                            best_l.second.use_blocks = fr_se[j].numerator;
                        }
                    }
                    if (j + 1 < fr_se.size()) {
                        double r = primary.cap * dec +
                                   new_secondary_cap * fr_se[j + 1].decimal;
                        if (abs(r - amt) < min_diff_r) {
                            min_diff_r = abs(r - amt);
                            best_r.first.add_new = 0;
                            best_r.first.tube_idx = primary.tube_idx;
                            best_r.first.real_amt = primary.cap * dec;
                            best_r.first.blocks = den;
                            best_r.first.use_blocks = num;

                            best_r.second.add_new = 1;
                            best_r.second.tube_idx = secondary.tube_idx;
                            best_r.second.real_amt =
                                new_secondary_cap * fr_se[j + 1].decimal;
                            best_r.second.blocks = fr_se[j + 1].denominator;
                            best_r.second.use_blocks = fr_se[j + 1].numerator;
                        }
                    }
                    if (primary.cap * dec > amt) {
                        break;
                    }
                }
            }
        } else {
            // 追加しない
            int j = fr_se.size() - 1;
            for (const auto &[num, den, dec] : fr_pr) {
                while (j >= 0 and
                       primary.cap * dec + secondary.cap * fr_se[j].decimal >
                           amt) {
                    j--;
                }
                if (j >= 0) {
                    double l =
                        primary.cap * dec + secondary.cap * fr_se[j].decimal;
                    if (abs(l - amt) < min_diff_l) {
                        min_diff_l = abs(l - amt);
                        best_l.first.tube_idx = primary.tube_idx;
                        best_l.first.real_amt = primary.cap * dec;
                        best_l.first.blocks = den;
                        best_l.first.use_blocks = num;

                        best_l.second.tube_idx = secondary.tube_idx;
                        best_l.second.real_amt =
                            secondary.cap * fr_se[j].decimal;
                        best_l.second.blocks = fr_se[j].denominator;
                        best_l.second.use_blocks = fr_se[j].numerator;
                    }
                }
                if (j + 1 < fr_se.size()) {
                    double r = primary.cap * dec +
                               secondary.cap * fr_se[j + 1].decimal;
                    if (abs(r - amt) < min_diff_r) {
                        min_diff_r = abs(r - amt);
                        best_r.first.tube_idx = primary.tube_idx;
                        best_r.first.real_amt = primary.cap * dec;
                        best_r.first.blocks = den;
                        best_r.first.use_blocks = num;

                        best_r.second.tube_idx = secondary.tube_idx;
                        best_r.second.real_amt =
                            secondary.cap * fr_se[j + 1].decimal;
                        best_r.second.blocks = fr_se[j + 1].denominator;
                        best_r.second.use_blocks = fr_se[j + 1].numerator;
                    }
                }
                if (primary.cap * dec > amt) {
                    break;
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
    int i, j;                   // 代表の座標
    double amt = 0;             // 絵具の量
    double cap;                 // ウェルの大きさ
    double c = 0, m = 0, y = 0; // 色
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
    double error(const Color &tgt) const {
        double d2 = (tgt.c - c) * (tgt.c - c) + (tgt.m - m) * (tgt.m - m) +
                    (tgt.y - y) * (tgt.y - y);
        return sqrt(d2) * 10000.0;
    }
    tuple<double, double, double, double>
    error_if_add(const Color &tgt, const MixStateWithAction &action) const {
        double da = action.amt;
        double dc = action.c;
        double dm = action.m;
        double dy = action.y;
        da = min(da, cap - amt);
        if (amt + da == 0.0) {
            return {1e300, 0, 0, 0};
        }
        double _c = (c * amt + dc * da) / (amt + da);
        double _m = (m * amt + dm * da) / (amt + da);
        double _y = (y * amt + dy * da) / (amt + da);
        double d2 = (tgt.c - _c) * (tgt.c - _c) + (tgt.m - _m) * (tgt.m - _m) +
                    (tgt.y - _y) * (tgt.y - _y);
        return {sqrt(d2) * 10000.0, _c, _m, _y};
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

namespace beam_search {

// ビームサーチの設定
struct Config {
    int max_turn;
    size_t beam_width;
    size_t tour_capacity;
    uint32_t hash_map_capacity;
};

// 連想配列
// Keyにハッシュ関数を適用しない
// open addressing with linear probing
// unordered_mapよりも速い
// nは格納する要素数よりも16倍ほど大きくする
template <class Key, class T> struct HashMap {
  public:
    explicit HashMap(uint32_t n) {
        if (n % 2 == 0) {
            ++n;
        }
        n_ = n;
        valid_.resize(n_, false);
        data_.resize(n_);
    }

    // 戻り値
    // - 存在するならtrue、存在しないならfalse
    // - index
    pair<bool, int> get_index(Key key) const {
        Key i = key % n_;
        while (valid_[i]) {
            if (data_[i].first == key) {
                return {true, i};
            }
            if (++i == n_) {
                i = 0;
            }
        }
        return {false, i};
    }

    // 指定したindexにkeyとvalueを格納する
    void set(int i, Key key, T value) {
        valid_[i] = true;
        data_[i] = {key, value};
    }

    // 指定したindexのvalueを返す
    T get(int i) const {
        assert(valid_[i]);
        return data_[i].second;
    }

    void clear() { fill(valid_.begin(), valid_.end(), false); }

  private:
    uint32_t n_;
    vector<bool> valid_;
    vector<pair<Key, T>> data_;
};

using Hash = uint64_t;

// 状態遷移を行うために必要な情報
// メモリ使用量をできるだけ小さくしてください
struct Action {
    int well_idx;
    int action_idx;
    int action_cnt;
    MixState before;
    MixState after;
    Action(int well_idx, int action_idx, int action_cnt, MixState before,
           MixState after)
        : well_idx(well_idx), action_idx(action_idx), action_cnt(action_cnt),
          before(before), after(after) {}
    Action()
        : well_idx(-1), action_idx(-1), action_cnt(-1), before(MixState()),
          after(MixState()) {}
    bool operator==(const Action &other) const {
        return well_idx == other.well_idx and action_idx == other.action_idx and
               action_cnt == other.action_cnt;
    }
};

using Cost = double;

// 状態のコストを評価するための構造体
// メモリ使用量をできるだけ小さくしてください
struct Evaluator {
    Cost cost;
    Evaluator() : cost(0) {}
    Evaluator(Cost cost) : cost(cost) {}

    // 低いほどよい
    Cost evaluate() const { return cost; }
};

// 展開するノードの候補を表す構造体
struct Candidate {
    Action action;
    Evaluator evaluator;
    Hash hash;
    int parent;

    Candidate(Action action, Evaluator evaluator, Hash hash, int parent)
        : action(action), evaluator(evaluator), hash(hash), parent(parent) {}
};

// ノードの候補から実際に追加するものを選ぶクラス
// ビーム幅の個数だけ、評価がよいものを選ぶ
// ハッシュ値が一致したものについては、評価がよいほうのみを残す
class Selector {
  public:
    explicit Selector(const Config &config)
        : hash_to_index_(config.hash_map_capacity) {
        beam_width = config.beam_width;
        candidates_.reserve(beam_width);
        full_ = false;

        costs_.resize(beam_width);
        for (size_t i = 0; i < beam_width; ++i) {
            costs_[i] = {0, i};
        }
    }

    // 候補を追加する
    // ターン数最小化型の問題で、candidateによって実行可能解が得られる場合にのみ
    // finished = true とする ビーム幅分の候補をCandidateを追加したときにsegment
    // treeを構築する
    void push(const Candidate &candidate, bool finished) {
        if (finished) {
            finished_candidates_.emplace_back(candidate);
            return;
        }
        Cost cost = candidate.evaluator.evaluate();
        if (full_ && cost >= st_.all_prod().first) {
            // 保持しているどの候補よりもコストが小さくないとき
            return;
        }
        auto [valid, i] = hash_to_index_.get_index(candidate.hash);

        if (valid) {
            int j = hash_to_index_.get(i);
            if (candidate.hash == candidates_[j].hash) {
                // ハッシュ値が等しいものが存在しているとき
                if (full_) {
                    // segment treeが構築されている場合
                    if (cost < st_.get(j).first) {
                        candidates_[j] = candidate;
                        st_.set(j, {cost, j});
                    }
                } else {
                    // segment treeが構築されていない場合
                    if (cost < costs_[j].first) {
                        candidates_[j] = candidate;
                        costs_[j].first = cost;
                    }
                }
                return;
            }
        }
        if (full_) {
            // segment treeが構築されている場合
            int j = st_.all_prod().second;
            hash_to_index_.set(i, candidate.hash, j);
            candidates_[j] = candidate;
            st_.set(j, {cost, j});
        } else {
            // segment treeが構築されていない場合
            int j = candidates_.size();
            hash_to_index_.set(i, candidate.hash, j);
            candidates_.emplace_back(candidate);
            costs_[j].first = cost;

            if (candidates_.size() == beam_width) {
                // 保持している候補がビーム幅分になったときにsegment
                // treeを構築する
                full_ = true;
                st_ = MaxSegtree(costs_);
            }
        }
    }

    // 選んだ候補を返す
    const vector<Candidate> &select() const { return candidates_; }

    // 実行可能解が見つかったか
    bool have_finished() const { return !finished_candidates_.empty(); }

    // 実行可能解に到達するCandidateを返す
    vector<Candidate> get_finished_candidates() const {
        return finished_candidates_;
    }

    // 最もよいCandidateを返す
    Candidate calculate_best_candidate() const {
        if (full_) {
            size_t best = 0;
            for (size_t i = 0; i < beam_width; ++i) {
                if (st_.get(i).first < st_.get(best).first) {
                    best = i;
                }
            }
            return candidates_[best];
        } else {
            size_t best = 0;
            for (size_t i = 0; i < candidates_.size(); ++i) {
                if (costs_[i].first < costs_[best].first) {
                    best = i;
                }
            }
            return candidates_[best];
        }
    }

    void clear() {
        candidates_.clear();
        hash_to_index_.clear();
        full_ = false;
    }

  private:
    using S = std::pair<Cost, int>;
    static constexpr S seg_op(S a, S b) { return (a.first >= b.first) ? a : b; }
    static constexpr S seg_e() {
        return {std::numeric_limits<Cost>::min(), -1};
    }
    using MaxSegtree = atcoder::segtree<S, seg_op, seg_e>;

    size_t beam_width;
    vector<Candidate> candidates_;
    HashMap<Hash, int> hash_to_index_;
    bool full_;
    vector<pair<Cost, int>> costs_;
    MaxSegtree st_;
    vector<Candidate> finished_candidates_;
};

// 深さ優先探索に沿って更新する情報をまとめたクラス
class State {
  public:
    const Input &in;
    int now_turn;
    int used_tube_cnt;
    vector<Well> well_list;
    int well_h;
    int well_w;
    int well_cap = well_h * well_w;
    int well_num = (in.N / well_h) * (in.N / well_w);
    vector<vector<MixStateWithAction>> actions_list;
    explicit State(const Input &input, int now_turn, int used_tube_cnt,
                   int well_h, int well_w)
        : in(input), now_turn(now_turn), used_tube_cnt(used_tube_cnt),
          well_h(well_h), well_w(well_w) {
        well_cap = well_h * well_w;
        well_num = (in.N / well_h) * (in.N / well_w);
        make_init_actions_list();
        make_init_well_list();
    }

    // EvaluatorとHashの初期値を返す
    pair<Evaluator, Hash> make_initial_node() {
        Hash hash = 0;
        Evaluator evaluator(0);
        return {evaluator, hash};
    }

    // 次の状態候補を全てselectorに追加する
    // 引数
    //   evaluator : 今の評価器
    //   hash      : 今のハッシュ値
    //   parent    : 今のノードID（次のノードにとって親となる）
    void expand(const Evaluator &evaluator, Hash hash, int parent,
                Selector &selector) {
        bool checked_clean_well = false;
        Well tmp_well;
        const Color &tgt = in.targets[now_turn];
        Cost init_cost = evaluator.evaluate();
        rep(well_idx, well_num) {
            const Well &well = well_list[well_idx];
            Action new_action;
            new_action.well_idx = well_idx;
            auto tmp = MixState(well.c, well.m, well.y, well.amt);
            new_action.before = tmp;
            Evaluator new_evaluator(1e300);
            Hash after_hash = 0;
            if (well.is_clear) {
                if (checked_clean_well) {
                    continue;
                }
                checked_clean_well = true;
                rep(action_cnt, 5) {
                    if ((double)(well.amt + action_cnt) > well_cap) {
                        break;
                    }
                    rep(action_idx, (int)actions_list[action_cnt].size()) {
                        const MixStateWithAction &a =
                            actions_list[action_cnt][action_idx];
                        Cost cost = init_cost;
                        auto [err, new_c, new_m, new_y] =
                            well.error_if_add(tgt, a);
                        cost += err;
                        if (in.H <= used_tube_cnt) {
                            cost += in.D * action_cnt;
                        } else if (in.H < used_tube_cnt + action_cnt) {
                            cost += in.D * (used_tube_cnt + action_cnt - in.H);
                        }
                        if (cost < new_evaluator.evaluate()) {
                            new_evaluator.cost = cost;
                            new_action.action_idx = action_idx;
                            new_action.action_cnt = action_cnt;
                            auto tmp =
                                MixState(new_c, new_m, new_y,
                                         well.amt + (double)action_cnt - 1.0);
                            new_action.after = tmp;
                            after_hash = tmp.hash();
                        }
                    }
                }
            } else {
                rep(action_cnt, 2) {
                    if ((double)(well.amt + action_cnt) > well_cap) {
                        break;
                    }
                    rep(action_idx, (int)actions_list[action_cnt].size()) {
                        const MixStateWithAction &a =
                            actions_list[action_cnt][action_idx];
                        Cost cost = init_cost;
                        auto [err, new_c, new_m, new_y] =
                            well.error_if_add(tgt, a);
                        cost += err;
                        if (in.H <= used_tube_cnt) {
                            cost += in.D * action_cnt;
                        } else if (in.H < used_tube_cnt + action_cnt) {
                            cost += in.D * (used_tube_cnt + action_cnt - in.H);
                        }
                        if (cost < new_evaluator.evaluate()) {
                            new_evaluator.cost = cost;
                            new_action.action_idx = action_idx;
                            new_action.action_cnt = action_cnt;
                            auto tmp =
                                MixState(new_c, new_m, new_y,
                                         well.amt + (double)action_cnt - 1.0);
                            new_action.after = tmp;
                            after_hash = tmp.hash();
                        }
                    }
                }
            }
            selector.push(
                Candidate(new_action, new_evaluator, after_hash, parent),
                false);
        }
    }

    // actionを実行して次の状態に遷移する
    void move_forward(Action action) {
        now_turn++;
        used_tube_cnt += action.action_cnt;
        well_list[action.well_idx].amt = action.after.amt;
        well_list[action.well_idx].c = action.after.c;
        well_list[action.well_idx].m = action.after.m;
        well_list[action.well_idx].y = action.after.y;
        if (action.after.amt == 0.0) {
            well_list[action.well_idx].is_clear = true;
            well_list[action.well_idx].c = 0.0;
            well_list[action.well_idx].m = 0.0;
            well_list[action.well_idx].y = 0.0;
        } else {
            well_list[action.well_idx].is_clear = false;
        }
    }

    // actionを実行する前の状態に遷移する
    // 今の状態は、親からactionを実行して遷移した状態である
    void move_backward(Action action) {
        now_turn--;
        used_tube_cnt -= action.action_cnt;
        well_list[action.well_idx].amt = action.before.amt;
        well_list[action.well_idx].c = action.before.c;
        well_list[action.well_idx].m = action.before.m;
        well_list[action.well_idx].y = action.before.y;
        if (action.before.amt == 0.0) {
            well_list[action.well_idx].is_clear = true;
            well_list[action.well_idx].c = 0.0;
            well_list[action.well_idx].m = 0.0;
            well_list[action.well_idx].y = 0.0;
        } else {
            well_list[action.well_idx].is_clear = false;
        }
    }

  private:
    void make_init_actions_list() {
        actions_list.resize(5);
        rep(i, 5) { actions_list[i].reserve((int)pow((double)in.K, i)); }
        actions_list[0].push_back(MixStateWithAction());
        for (int i = 0; i < in.K; i++) {
            MixStateWithAction action;
            action.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, 1.0, i);
            actions_list[1].push_back(action);
            for (int j = i; j < in.K; j++) {
                MixStateWithAction action;
                action.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, 1.0, i);
                action.add(in.tubes[j].c, in.tubes[j].m, in.tubes[j].y, 1.0, j);
                actions_list[2].push_back(action);
                for (int k = j; k < in.K; k++) {
                    MixStateWithAction action;
                    action.add(in.tubes[i].c, in.tubes[i].m, in.tubes[i].y, 1.0,
                               i);
                    action.add(in.tubes[j].c, in.tubes[j].m, in.tubes[j].y, 1.0,
                               j);
                    action.add(in.tubes[k].c, in.tubes[k].m, in.tubes[k].y, 1.0,
                               k);
                    actions_list[3].push_back(action);
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
                        actions_list[4].push_back(action);
                    }
                }
            }
        }
    }
    void make_init_well_list() {
        well_list.reserve(well_num);
        for (int i = 0; i < in.N; i += well_h) {
            for (int j = 0; j < in.N; j += well_w) {
                Well well;
                well.i = i;
                well.j = j;
                well.cap = well_cap;
                well_list.push_back(well);
            }
        }
    }
};

// Euler Tourを管理するためのクラス
class Tree {
  public:
    explicit Tree(const State &state, const Config &config) : state_(state) {
        curr_tour_.reserve(config.tour_capacity);
        next_tour_.reserve(config.tour_capacity);
        leaves_.reserve(config.beam_width);
        buckets_.assign(config.beam_width, {});
    }

    // 状態を更新しながら深さ優先探索を行い、次のノードの候補を全てselectorに追加する
    void dfs(Selector &selector) {
        if (curr_tour_.empty()) {
            // 最初のターン
            auto [evaluator, hash] = state_.make_initial_node();
            state_.expand(evaluator, hash, 0, selector);
            return;
        }

        for (auto [leaf_index, action] : curr_tour_) {
            if (leaf_index >= 0) {
                // 葉
                state_.move_forward(action);
                auto &[evaluator, hash] = leaves_[leaf_index];
                state_.expand(evaluator, hash, leaf_index, selector);
                state_.move_backward(action);
            } else if (leaf_index == -1) {
                // 前進辺
                state_.move_forward(action);
            } else {
                // 後退辺
                state_.move_backward(action);
            }
        }
    }

    // 木を更新する
    void update(const vector<Candidate> &candidates) {
        leaves_.clear();

        if (curr_tour_.empty()) {
            // 最初のターン
            for (const Candidate &candidate : candidates) {
                curr_tour_.push_back({(int)leaves_.size(), candidate.action});
                leaves_.push_back({candidate.evaluator, candidate.hash});
            }
            return;
        }

        for (const Candidate &candidate : candidates) {
            buckets_[candidate.parent].push_back(
                {candidate.action, candidate.evaluator, candidate.hash});
        }

        auto it = curr_tour_.begin();

        // 一本道を反復しないようにする
        while (it->first == -1 && it->second == curr_tour_.back().second) {
            Action action = (it++)->second;
            state_.move_forward(action);
            direct_road_.push_back(action);
            curr_tour_.pop_back();
        }

        // 葉の追加や不要な辺の削除をする
        while (it != curr_tour_.end()) {
            auto [leaf_index, action] = *(it++);
            if (leaf_index >= 0) {
                // 葉
                if (buckets_[leaf_index].empty()) {
                    continue;
                }
                next_tour_.push_back({-1, action});
                for (auto [new_action, evaluator, hash] :
                     buckets_[leaf_index]) {
                    int new_leaf_index = leaves_.size();
                    next_tour_.push_back({new_leaf_index, new_action});
                    leaves_.push_back({evaluator, hash});
                }
                buckets_[leaf_index].clear();
                next_tour_.push_back({-2, action});
            } else if (leaf_index == -1) {
                // 前進辺
                next_tour_.push_back({-1, action});
            } else {
                // 後退辺
                auto [old_leaf_index, old_action] = next_tour_.back();
                if (old_leaf_index == -1) {
                    next_tour_.pop_back();
                } else {
                    next_tour_.push_back({-2, action});
                }
            }
        }
        swap(curr_tour_, next_tour_);
        next_tour_.clear();
    }

    // 根からのパスを取得する
    vector<Action> calculate_path(int parent, int turn) const {

        vector<Action> ret = direct_road_;
        ret.reserve(turn);
        for (auto [leaf_index, action] : curr_tour_) {
            if (leaf_index >= 0) {
                if (leaf_index == parent) {
                    ret.push_back(action);
                    return ret;
                }
            } else if (leaf_index == -1) {
                ret.push_back(action);
            } else {
                ret.pop_back();
            }
        }

        // unreachable();
    }

  private:
    State state_;
    vector<pair<int, Action>> curr_tour_;
    vector<pair<int, Action>> next_tour_;
    vector<pair<Evaluator, Hash>> leaves_;
    vector<vector<tuple<Action, Evaluator, Hash>>> buckets_;
    vector<Action> direct_road_;
};

// ビームサーチを行う関数
pair<Cost, vector<Action>> beam_search(const Config &config,
                                       const State &state) {
    Tree tree(state, config);

    // 新しいノード候補の集合
    Selector selector(config);

    for (int turn = 0; turn < config.max_turn; ++turn) {
        // Euler Tourでselectorに候補を追加する
        tree.dfs(selector);

        assert(!selector.select().empty());

        if (turn == config.max_turn - 1) {
            // ターン数固定型の問題で全ターンが終了したとき
            Candidate best_candidate = selector.calculate_best_candidate();
            vector<Action> ret =
                tree.calculate_path(best_candidate.parent, turn + 1);
            ret.push_back(best_candidate.action);
            return {best_candidate.evaluator.evaluate(), ret};
        }

        // 木を更新する
        tree.update(selector.select());

        selector.clear();
    }

    // unreachable();
}

} // namespace beam_search

class BeamSearchSolver {
  public:
    const Input &in;
    int now_turn;
    int used_tube_cnt;
    vector<string> sep_v;
    vector<string> sep_h;
    vector<vector<int>> cmds;
    int well_h = 1;
    int well_w = 4;
    double final_cost;
    int max_turn = 1000;
    size_t beam_width = 1;
    size_t tour_capacity = 15 * beam_width;
    uint32_t hash_map_capacity = 16 * 3 * beam_width;
    BeamSearchSolver(const Input &in, int now_turn, int used_tube_cnt)
        : in(in), now_turn(now_turn), used_tube_cnt(used_tube_cnt) {}
    void solve() {
        make_palette();
        max_turn = in.H - now_turn;
        beam_search::Config config = {max_turn, beam_width, tour_capacity,
                                      hash_map_capacity};
        beam_search::State state(in, now_turn, used_tube_cnt, well_h, well_w);
        auto [cost, actions] = beam_search::beam_search(config, state);
        final_cost = cost;
        for (const auto &a : actions) {
            int i = state.well_list[a.well_idx].i;
            int j = state.well_list[a.well_idx].j;
            for (auto b :
                 state.actions_list[a.action_cnt][a.action_idx].actions) {

                cmds.push_back({1, i, j, b});
            }
            cmds.push_back({2, i, j});
        }
    }
    void make_palette() {
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
    void print_palette() const {
        for (auto s : sep_v) {
            cout << s;
        }
        for (auto s : sep_h) {
            cout << s;
        }
    }
    void print_operate() const {
        for (auto &v : cmds) {
            rep(i, v.size()) {
                cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
            }
        }
    }
};
namespace mixopt {

inline double clamp(double x, double lo, double hi) {
    return std::max(lo, std::min(hi, x));
}

struct Cand {
    std::vector<double> coef; // Σ = 1 (ローカル添字)
    double err2;              // 誤差^2
    double min_pos;           // 正係数の最小値
    int cnt;                  // 使用色数 (正係数の個数)
};
inline double min_positive(const std::vector<double> &v, double eps) {
    double mn = 1.0;
    bool f = false;
    for (double x : v)
        if (x > eps) {
            mn = std::min(mn, x);
            f = true;
        }
    return f ? mn : 0.0;
}

// ―――― 全組合せ列挙 (1〜4 色) ――――――――――――――――――――――――――――――
static void enumerate_all(const Color &tgt, int lim_max,
                          const std::vector<Color> &tubes,
                          std::vector<std::vector<Cand>> &bucket, double eps) {
    int M = tubes.size();
    auto push = [&](const std::vector<double> &coef, double err2) {
        int cnt = 0;
        for (double v : coef)
            if (v > eps)
                ++cnt;
        bucket[cnt].push_back({coef, err2, min_positive(coef, eps), cnt});
    };
    // 1 色
    for (int i = 0; i < M; ++i) {
        std::vector<double> c(M, 0);
        c[i] = 1;
        push(c, norm2(tubes[i] - tgt));
    }
    // 2 色
    if (M >= 2 and lim_max >= 2)
        for (int i = 0; i < M; ++i)
            for (int j = i + 1; j < M; ++j) {
                Color p = tubes[i], q = tubes[j], d = q - p;
                double dd = norm2(d);
                if (dd < 1e-12)
                    continue;
                double u = clamp(dot(tgt - p, d) / dd, 0.0, 1.0);
                Color mix = p * u + q * (1 - u);
                std::vector<double> c(M, 0);
                c[i] = u;
                c[j] = 1 - u;
                push(c, norm2(mix - tgt));
            }
    // 3 色
    if (M >= 3 and lim_max >= 3)
        for (int i = 0; i < M; ++i)
            for (int j = i + 1; j < M; ++j)
                for (int k = j + 1; k < M; ++k) {
                    Color ei = tubes[i] - tubes[k], ej = tubes[j] - tubes[k],
                          v = tgt - tubes[k];
                    double m00 = dot(ei, ei), m01 = dot(ei, ej),
                           m11 = dot(ej, ej);
                    double b0 = dot(ei, v), b1 = dot(ej, v);
                    double det = m00 * m11 - m01 * m01;
                    if (std::abs(det) < 1e-12)
                        continue;
                    double a = (b0 * m11 - b1 * m01) / det,
                           b = (m00 * b1 - m01 * b0) / det, g = 1 - a - b;
                    if (a >= -eps && b >= -eps && g >= -eps) {
                        a = std::max(0.0, a);
                        b = std::max(0.0, b);
                        g = std::max(0.0, g);
                        Color mix = tubes[i] * a + tubes[j] * b + tubes[k] * g;
                        std::vector<double> c(M, 0);
                        c[i] = a;
                        c[j] = b;
                        c[k] = g;
                        push(c, norm2(mix - tgt));
                    }
                }
    // 4 色
    if (M >= 4 and lim_max >= 4)
        for (int i = 0; i < M; ++i)
            for (int j = i + 1; j < M; ++j)
                for (int k = j + 1; k < M; ++k)
                    for (int l = k + 1; l < M; ++l) {
                        Color ei = tubes[i] - tubes[l],
                              ej = tubes[j] - tubes[l],
                              ek = tubes[k] - tubes[l], v = tgt - tubes[l];
                        double m00 = dot(ei, ei), m01 = dot(ei, ej),
                               m02 = dot(ei, ek), m11 = dot(ej, ej),
                               m12 = dot(ej, ek), m22 = dot(ek, ek);
                        double det = m00 * (m11 * m22 - m12 * m12) -
                                     m01 * (m01 * m22 - m12 * m02) +
                                     m02 * (m01 * m12 - m11 * m02);
                        if (std::abs(det) < 1e-12)
                            continue;
                        double b0 = dot(ei, v), b1 = dot(ej, v),
                               b2 = dot(ek, v);
                        double detA = b0 * (m11 * m22 - m12 * m12) -
                                      m01 * (b1 * m22 - m12 * b2) +
                                      m02 * (b1 * m12 - m11 * b2);
                        double detB = m00 * (b1 * m22 - m12 * b2) -
                                      b0 * (m01 * m22 - m12 * m02) +
                                      m02 * (m01 * b2 - b1 * m02);
                        double detC = m00 * (m11 * b2 - b1 * m12) -
                                      m01 * (m01 * b2 - b1 * m02) +
                                      b0 * (m01 * m12 - m11 * m02);
                        double a = detA / det, b = detB / det, c = detC / det,
                               d = 1 - a - b - c;
                        if (a >= -eps && b >= -eps && c >= -eps && d >= -eps) {
                            a = std::max(0.0, a);
                            b = std::max(0.0, b);
                            c = std::max(0.0, c);
                            d = std::max(0.0, d);
                            Color mix = tubes[i] * a + tubes[j] * b +
                                        tubes[k] * c + tubes[l] * d;
                            std::vector<double> cc(M, 0);
                            cc[i] = a;
                            cc[j] = b;
                            cc[k] = c;
                            cc[l] = d;
                            push(cc, norm2(mix - tgt));
                        }
                    }
}

// ―――― 1 つのターゲットにつきまとめて処理 ―――――――――――――――――
struct TargetMixResult {
    std::vector<std::vector<double>> best_coef;              // [lim]
    std::vector<double> best_err;                            // [lim]
    std::vector<std::vector<std::vector<double>>> cand_list; // [lim][idx]
};

static TargetMixResult compute(const Color &tgt,
                               const std::vector<Color> &tubes, int lim_max,
                               int top, double eps_err, double eps_coef) {
    TargetMixResult res;
    res.best_coef.assign(lim_max + 1, {});
    res.best_err.assign(lim_max + 1, 1e300);
    res.cand_list.assign(lim_max + 1, {});

    std::vector<std::vector<Cand>> bucket(lim_max + 1);
    enumerate_all(tgt, lim_max, tubes, bucket, eps_coef);

    for (int lim = 1; lim <= lim_max; ++lim) {
        std::vector<Cand> pool;
        for (int cnt = 1; cnt <= lim; ++cnt)
            pool.insert(pool.end(), bucket[cnt].begin(), bucket[cnt].end());
        if (pool.empty())
            continue;
        double min_err2 = 1e300;
        for (auto &c : pool)
            min_err2 = std::min(min_err2, c.err2);
        std::vector<Cand> f;
        for (auto &c : pool)
            if (c.err2 <= min_err2 + eps_err)
                f.push_back(std::move(c));
        std::sort(f.begin(), f.end(), [&](const Cand &A, const Cand &B) {
            if (std::abs(A.err2 - B.err2) > eps_err)
                return A.err2 < B.err2;
            if (std::abs(A.min_pos - B.min_pos) > eps_coef)
                return A.min_pos > B.min_pos;
            return A.coef < B.coef;
        });
        std::vector<std::vector<double>> uniq;
        for (auto &c : f) {
            bool dup = false;
            for (auto &u : uniq) {
                double diff = 0;
                for (size_t i = 0; i < u.size(); ++i)
                    diff += std::abs(u[i] - c.coef[i]);
                if (diff < 1e-9) {
                    dup = true;
                    break;
                }
            }
            if (!dup) {
                uniq.push_back(c.coef);
                if ((int)uniq.size() >= top)
                    break;
            }
        }
        res.cand_list[lim] = uniq;
        res.best_coef[lim] = uniq.front();
        Color mix{0, 0, 0};
        for (size_t i = 0; i < uniq.front().size(); ++i)
            mix = mix + tubes[i] * uniq.front()[i];
        res.best_err[lim] = std::sqrt(norm2(mix - tgt));
    }
    return res;
}
//----------------------------------------------------------------------
//  mix_with_existing
//      既に a だけ混ざっている色 cur を固定したまま
//      残りの絵の具 (tubes) で tgt を近似する係数を返す
//      · 戻り値サイズ = tubes.size()+1
//          coef[0]   = 既存量 a
//          coef[i+1] = tubes[i] の実量
//      · lim : 追加で同時に使う色数の上限 (1‥4)
//----------------------------------------------------------------------
static vector<std::vector<double>>
mix_with_existing(double a,                        // 既存量 (0 ≤ a ≤ 1)
                  const Color &cur,                // 既存平均色
                  const Color &tgt,                // 目標色
                  const std::vector<Color> &tubes, // 追加チューブ色リスト
                  int lim = 4,                     // 追加色数の上限
                  double eps_err = 1e-8,           // 誤差許容
                  double eps_coef = 1e-12          // “正” とみなす下限
) {
    // 既存量だけで満杯
    if (a >= 1.0 - 1e-12) {
        std::vector<double> coef(tubes.size() + 1, 0.0);
        coef[0] = 1.0;
        return {coef};
    }
    double b = 1.0 - a; // 残量
    Color tprime{(tgt.c - a * cur.c) / b, (tgt.m - a * cur.m) / b,
                 (tgt.y - a * cur.y) / b};

    // 残量 b を 1 とみなし、最適係数を取得
    auto res = compute(tprime, tubes, lim, /*top*/ 1000, eps_err, eps_coef);
    vector<std::vector<double>> &coef_cand =
        res.cand_list[lim]; // Σ=1 (ローカル)
    for (auto &coef : coef_cand) {
        for (auto &a : coef) {
            a *= b;
        }
    }
    return coef_cand; // Σ=1 (実量)
}

} // namespace mixopt

// ──────────────────────────────
//  6. ソルバー本体
// ──────────────────────────────
class Solver {
  public:
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
    vector<vector<vector<vector<double>>>> best_coef_cand;
    // vector<vector<double>> init_coefs;
    int max_palettes;
    int MODE_THRESHOLD = 27000;
    vector<vector<int>> separator_v;
    vector<vector<int>> separator_h;
    vector<Color> tubes;
    vector<vector<int>> target_v;
    vector<vector<int>> target_h;
    vector<vector<int>> best_op;
    vector<vector<int>> change_palette_op;
    int prev_cmds_size;

    int final_cost;

    Solver(const Input &_in, TimeKeeper tk) : in(_in), tk(tk) {
        tubes.reserve(in.Q);
        for (int i : in.need_idxs) {
            tubes.push_back(in.tubes[i]);
        }
        make_best_coefs();
        tk.update();
        // ビーム用の盤面に変更する
        target_v = vector<vector<int>>(in.N, vector<int>(in.N - 1, 0));
        target_h = vector<vector<int>>(in.N - 1, vector<int>(in.N, 1));
        rep(i, in.N) {
            rep(j, in.N - 1) {
                if (j % 4 == 3) {
                    target_v[i][j] = 1;
                }
            }
        }
    }

    //----------------------------------
    void solve() {
        if (in.T >= 15000) { // dpで各ターンの使用色数を暫定計算
            vector<int> can_use_colors = calc_use_colors();
            vector<int> used_tube_cnt(in.K);
            rep(h, in.H) {
                const vector<double> &coef = best_coefs[can_use_colors[h]][h];
                rep(i, in.Q) {
                    if (coef[i] > 0.0) {
                        used_tube_cnt[in.need_idxs[i]]++;
                    }
                }
            }
            // 色の使用頻度に合わせて行数を調整
            for (auto i : in.need_idxs) {
                used_tube_cnt[i]++;
            }
            for (auto &c : used_tube_cnt) {
                c = sqrt(c);
            }
            err_sum = 0;
            tubes_used = 0;
            vector<int> lines_size = calc_lines_size(used_tube_cnt);
            init_palettes(lines_size);

            MixState ms;
            rep(h, in.H) {
                const Color &tgt = in.targets[h];
                int colors = can_use_colors[h];
                max_palettes = (in.T - cmds.size() - 3 * (in.H - h) - 50) /
                               (4 * (in.H - h));

                colors = max(colors, max_palettes);
                colors = min(colors, 4);

                tk.update();
                double disc_tl = (290 - tk.now()) / (in.H - h + 1);
                auto acts =
                    discretise(tgt, best_coef_cand[colors][h], disc_tl, h);

                double sum = 0;
                for (const auto &p : palettes) {
                    if (p.primary.tube_idx >= 0) {
                        sum += p.primary.cap;
                    }
                    if (p.secondary.tube_idx >= 0) {
                        sum += p.secondary.cap;
                    }
                }
                if (sum >= (double)(in.H - h)) {
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
                    if (ok and
                        (int) cmds.size() + (int)tmp_acts.size() * 4 <= in.T) {
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
                        if (tmp_cost < cost) {
                            acts = tmp_acts;
                        }
                    }
                } else if (h == in.H - 1) {
                    tk.update();
                    double disc_tl = (290 - tk.now()) / (in.H - h + 1);
                    vector<double> best_coef;
                    double min_err = 1e100;
                    for (int i : in.need_idxs) {
                        palettes[i].primary.cap += 1.0;
                        auto tmp_coef = optimize_continuous(tgt);
                        auto err = error_only(tgt, tmp_coef);
                        if (err < min_err) {
                            min_err = err;
                            best_coef = tmp_coef;
                        }
                        palettes[i].primary.cap -= 1.0;
                    }

                    int cnt = 0;
                    for (auto c : best_coef) {
                        if (c > 1e-9) {
                            cnt++;
                        }
                    }
                    vector<Action> tmp_acts;
                    bool ok = true;
                    if (cnt <= 6) {
                        tmp_acts = discretise(tgt, best_coef, disc_tl, h);
                    } else {
                        tie(ok, tmp_acts) = discretise_fast(tgt, best_coef, h);
                    }
                    if (ok and
                        (int) cmds.size() + (int)tmp_acts.size() * 4 <= in.T) {
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
                        if (tmp_cost < cost) {
                            acts = tmp_acts;
                        }
                    }
                }
                ms = commit(tgt, acts, ms);
            }
            while (cmds.size() > in.T) {
                cmds.pop_back();
            }
            final_cost = (int)(err_sum + (tubes_used - in.H) * in.D);
            // print();
        } else {
            vector<int> tmp(in.K);
            for (auto i : in.need_idxs) {
                tmp[i]++;
            }
            vector<int> lines_size = calc_lines_size(tmp);
            err_sum = 0;
            tubes_used = 0;
            init_palettes(lines_size);

            int now_turn;
            MixState ms;

            rep(h, in.H) {
                if ((in.T - (int)cmds.size() - 500 - 2 * (in.H - h - 1) - 19) >
                    0) {

                } else {
                    now_turn = h;
                    auto tmp_change_pallete_op = change_palette_sim();
                    BeamSearchSolver beam(in, now_turn, tubes_used);
                    beam.solve();
                    int used_time = cmds.size() + tmp_change_pallete_op.size() +
                                    beam.cmds.size();

                    if (used_time <= in.T) {
                        best_op = beam.cmds;
                        change_palette_op = tmp_change_pallete_op;
                        prev_cmds_size = cmds.size();
                        final_cost = err_sum + beam.final_cost;
                    } else {
                        break;
                    }
                }
                const Color &tgt = in.targets[h];
                int colors = 4;
                auto coef = best_coefs[colors][h];
                tk.update();
                double disc_tl = (250 - tk.now()) / (in.H - h + 1);
                auto acts =
                    discretise(tgt, best_coef_cand[colors][h], disc_tl, h);
                ms = commit(tgt, acts, ms);
            }
            // change_palette();
            while (cmds.size() > prev_cmds_size) {
                cmds.pop_back();
            }
            tk.update();
            // print();
        }
    }
    void print() const {
        for (auto s : sep_v) {
            rep(j, s.size()) {
                cout << s[j] << (j < s.size() - 1 ? " " : "\n");
            }
        }
        for (auto s : sep_h) {
            rep(j, s.size()) {
                cout << s[j] << (j < s.size() - 1 ? " " : "\n");
            }
        }
        for (auto &v : cmds) {
            rep(i, v.size()) {
                cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
            }
        }
        for (auto &v : change_palette_op) {
            rep(i, v.size()) {
                cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
            }
        }
        for (auto &v : best_op) {
            rep(i, v.size()) {
                cout << v[i] << (i + 1 < v.size() ? ' ' : '\n');
            }
        }
    }
    //----------------------------------
    vector<vector<int>> change_palette_sim() {
        int cnt = 0;
        static vector<vector<int>> res;
        res.clear();
        for (const auto &p : palettes) {
            double tmp = p.primary.cap;
            while (tmp > 0) {
                tmp -= 1.0;
                auto tmp = p.primary.cmd_add_tube();
                res.push_back({3, tmp[1], tmp[2]});
            }
            tmp = p.secondary.cap;
            while (tmp > 0) {
                tmp -= 1.0;
                auto tmp = p.secondary.cmd_add_tube();
                res.push_back({3, tmp[1], tmp[2]});
            }
        }

        rep(i, in.N) {
            rep(j, in.N - 1) {
                if (target_v[i][j] != separator_v[i][j]) {
                    res.push_back({4, i, j, i, j + 1});
                }
            }
        }
        rep(i, in.N - 1) {
            rep(j, in.N) {
                if (target_h[i][j] != separator_h[i][j]) {
                    res.push_back({4, i, j, i + 1, j});
                }
            }
        }
        return res;
    }
    void change_palette() {
        for (auto &p : palettes) {
            while (p.primary.cap > 0) {
                p.primary.cap -= 1.0;
                auto tmp = p.primary.cmd_add_tube();
                cmds.push_back({3, tmp[1], tmp[2]});
            }
            while (p.secondary.cap > 0) {
                p.secondary.cap -= 1.0;
                auto tmp = p.secondary.cmd_add_tube();
                cmds.push_back({3, tmp[1], tmp[2]});
            }
        }

        rep(i, in.N) {
            rep(j, in.N - 1) {
                if (target_v[i][j] != separator_v[i][j]) {
                    cmds.push_back({4, i, j, i, j + 1});
                }
            }
        }
        rep(i, in.N - 1) {
            rep(j, in.N) {
                if (target_h[i][j] != separator_h[i][j]) {
                    cmds.push_back({4, i, j, i + 1, j});
                }
            }
        }
    }
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
        if (in.T >= 19000) {
            return vector<int>(in.H, 4);
        }
        // i個目の目標まででjターン使用した場合の(エラーの合計の最小値,
        // iターン目に使用するターン数)
        int can_use_turn = (in.T - 3050) / 4;
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
        int total_lines = 20;

        // まず、used_tube_cnt[i] > 0 なら必ず 1 行を確保
        int count_pos = 0;
        for (int i = 0; i < in.K; ++i) {
            if (used_tube_cnt[i] > 0) {
                count_pos++;
            }
        }

        int remaining = total_lines - count_pos;

        vector<int> lines_size(in.K, 0);
        for (int i = 0; i < in.K; ++i) {
            if (used_tube_cnt[i] > 0) {
                lines_size[i] = 1; // 最低 1 行
            }
        }

        // used_tube_cnt[i] > 0 の合計値を計算
        int sum_pos = 0;
        for (int i = 0; i < in.K; ++i) {
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

        for (int i = 0; i < in.K; ++i) {
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
            rep(j, 18) sep_v[i] += "0";
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
                auto tmp = p.cmd_sep(p.blocks - 1);
                sep_v[min(tmp[1], tmp[3])][min(tmp[2], tmp[4])] = '1';
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
                auto tmp = p.cmd_sep(p.blocks - 1);
                sep_v[min(tmp[1], tmp[3])][min(tmp[2], tmp[4])] = '1';
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
                    sep_h[row] += "0";
                    if (j % 2 == 0) {
                        rep(x, 18) sep_h[row] += "1";
                        sep_h[row] += "0\n";
                        row++;
                    } else {
                        sep_h[row] += "0";
                        rep(x, 18) sep_h[row] += "1";
                        sep_h[row] += "\n";
                        row++;
                    }
                }
                if (row < in.N - 1) {
                    sep_h[row] += "0";
                    rep(x, 19) {
                        sep_h[row] += '1';
                        sep_h[row] += (x == 18 ? "\n" : "");
                    }
                    row++;
                }
            }
            if (palettes[k].secondary.lines > 0) {
                auto &p = palettes[k].secondary;
                if (p.lines == 0 or row == in.N - 1)
                    continue;
                rep(j, p.lines - 1) {
                    sep_h[row] += "0";
                    if (j % 2 == 0) {
                        rep(x, 18) sep_h[row] += "1";
                        sep_h[row] += "0\n";
                        row++;
                    } else {
                        sep_h[row] += "0";
                        rep(x, 18) sep_h[row] += "1";
                        sep_h[row] += "\n";
                        row++;
                    }
                }
                if (row < in.N - 1) {
                    sep_h[row] += "0";
                    rep(x, 19) {
                        sep_h[row] += '1';
                        sep_h[row] += (x == 18 ? "\n" : "");
                    }
                    row++;
                }
            }
        }
        separator_v = vector<vector<int>>(in.N, vector<int>(in.N - 1, 0));
        separator_h = vector<vector<int>>(in.N - 1, vector<int>(in.N, 0));
        rep(i, in.N) {
            rep(j, in.N - 1) {
                if (sep_v[i][j] == '0') {
                } else {
                    separator_v[i][j] ^= 1;
                }
            }
        }
        rep(i, in.N - 1) {
            rep(j, in.N) {
                if (sep_h[i][j] == '0') {
                } else {
                    separator_h[i][j] ^= 1;
                }
            }
        }
        // 全てのパレットに一回ずつ絵具を注ぐ
        for (auto &palette : palettes) {
            if (palette.primary.tube_idx >= 0) {
                palette.primary.cap += 1.0;
                cmds.push_back(palette.primary.cmd_add_tube());
                tubes_used++;
            }
            if (palette.secondary.tube_idx >= 0) {
                palette.secondary.cap += 1.0;
                cmds.push_back(palette.secondary.cmd_add_tube());
                tubes_used++;
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
        rep(i, in.Q) {
            if (coef[i] < 1e-9) {
                continue;
            }
            int j = in.need_idxs[i];
            double amt = coef[i];
            auto [best_l, best_r] = palettes[j].discretise_one(
                amt, now_turn >= 980 and max_palettes >= 8 and
                         in.T >= MODE_THRESHOLD);
            nearest_acts.push_back({best_l, best_r});
            if (in.T >= MODE_THRESHOLD) {
                auto [best_l, best_r] =
                    palettes[j].discretise_two(amt, now_turn >= 980);
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
    vector<Action> discretise(const Color &tgt,
                              const vector<vector<double>> &coef_cand,
                              double tl, int now_turn,
                              MixState ms = MixState()) {
        vector<Action> best_acts;
        double min_cost = 1e100;
        vector<Action> new_acts;
        new_acts.reserve(in.Q);
        // プライマリ or セカンダリ
        vector<pair<Action, Action>> nearest_acts;
        // 併用
        vector<pair<pair<Action, Action>, pair<Action, Action>>>
            nearest_acts_pair;
        vector<double> new_coef(in.Q);
        double best_alph = -1;
        TimeKeeper tk(tl);
        double alp = 1.0;
        rep(i, coef_cand.size()) {
            const vector<double> &coef = coef_cand[i];
            if (i % 10 == 1) {
                tk.update();
                if (tk.over()) {
                    return best_acts;
                }
            }
            nearest_acts.clear();
            nearest_acts_pair.clear();
            rep(i, in.Q) { new_coef[i] = alp * coef[i]; }
            rep(i, in.Q) {
                if (new_coef[i] < 1e-9) {
                    continue;
                }
                int j = in.need_idxs[i];
                double amt = new_coef[i];
                auto [best_l, best_r] = palettes[j].discretise_one(
                    amt, now_turn >= 980 and max_palettes >= 8 and
                             in.T >= MODE_THRESHOLD);
                nearest_acts.push_back({best_l, best_r});
                if (in.T >= MODE_THRESHOLD) {
                    auto [best_l, best_r] =
                        palettes[j].discretise_two(amt, now_turn >= 980);
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
                rep(mask, 1 << (nearest_acts.size() * 2)) {
                    double amt_sum = ms.amt;
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
                    double new_cost = cost(ms, tgt, new_acts);
                    if (new_cost < min_cost) {
                        min_cost = new_cost;
                        best_acts = new_acts;
                        best_alph = alp;
                    }
                }
            }
        }
        int iter = 0;

        while (true) {
            alp = 1.0 + rnd::uniform_real(0.0, 0.1);
            iter++;
            if (iter % 10 == 0) {
                tk.update();
                if (tk.over()) {
                    // cerr << iter << '\n';
                    break;
                }
            }
            const vector<double> &coef =
                coef_cand[rnd::xorshift32() % coef_cand.size()];
            nearest_acts.clear();
            nearest_acts_pair.clear();
            rep(i, in.Q) { new_coef[i] = alp * coef[i]; }
            rep(i, in.Q) {
                if (new_coef[i] < 1e-9) {
                    continue;
                }
                int j = in.need_idxs[i];
                double amt = new_coef[i];
                auto [best_l, best_r] = palettes[j].discretise_one(
                    amt, now_turn >= 980 and max_palettes >= 8 and
                             in.T >= MODE_THRESHOLD);
                nearest_acts.push_back({best_l, best_r});
                if (in.T >= MODE_THRESHOLD) {
                    auto [best_l, best_r] =
                        palettes[j].discretise_two(amt, now_turn >= 980);
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
                rep(mask, 1 << (nearest_acts.size() * 2)) {
                    double amt_sum = ms.amt;
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
                    double new_cost = cost(ms, tgt, new_acts);
                    if (new_cost < min_cost) {
                        min_cost = new_cost;
                        best_acts = new_acts;
                        best_alph = alp;
                    }
                }
            }
        }
        return best_acts;
    }
    vector<Action> discretise(const Color &tgt, const vector<double> &coef,
                              double tl, int now_turn) {
        vector<Action> best_acts;
        double min_cost = 1e100;
        vector<Action> new_acts;
        new_acts.reserve(in.Q);
        // プライマリ or セカンダリ
        vector<pair<Action, Action>> nearest_acts;
        // 併用
        vector<pair<pair<Action, Action>, pair<Action, Action>>>
            nearest_acts_pair;
        vector<double> new_coef(in.Q);
        double best_alph = -1;
        TimeKeeper tk(tl);
        double alp = 1.0;
        int iter = 0;

        while (true) {
            if (iter == 0) {
                alp = 1.0;
            } else {
                alp = 1.0 + rnd::uniform_real(0.0, 0.3);
            }
            iter++;
            if (iter % 3 == 0) {
                tk.update();
                if (tk.over()) {
                    break;
                }
            }
            nearest_acts.clear();
            nearest_acts_pair.clear();
            rep(i, in.Q) { new_coef[i] = alp * coef[i]; }
            rep(i, in.Q) {
                if (new_coef[i] < 1e-9) {
                    continue;
                }
                int j = in.need_idxs[i];
                double amt = new_coef[i];
                auto [best_l, best_r] = palettes[j].discretise_one(
                    amt, now_turn >= 980 and max_palettes >= 8 and
                             in.T >= MODE_THRESHOLD);
                nearest_acts.push_back({best_l, best_r});
                if (in.T >= MODE_THRESHOLD) {
                    auto [best_l, best_r] =
                        palettes[j].discretise_two(amt, now_turn >= 980);
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
                        min_cost = new_cost;
                        best_acts = new_acts;
                        best_alph = alp;
                    }
                }
            }
        }
        return best_acts;
    }

    vector<double> optimize_continuous(const Color &tgt,
                                       int max_iters = 10000) {
        int Q = in.Q;
        vector<double> coef(Q, 0.0), best_coef(Q, 0.0), max_coef(Q, 0.0);
        double sum = 0.0;

        // 上限を設定しつつ初期coefにキャパを足してsumを計算
        rep(i, Q) {
            double cap = 0;
            int j = in.need_idxs[i];
            if (palettes[j].primary.tube_idx >= 0)
                cap += palettes[j].primary.cap;
            if (palettes[j].secondary.tube_idx >= 0)
                cap += palettes[j].secondary.cap;
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

            int idx = rnd::xorshift32() % Q;
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
        rep(i, in.Q) {
            s.add(tubes[i].c, tubes[i].m, tubes[i].y, coef[i]);
            total += coef[i];
        }
        if (total < 1 - 1e-6) {
            return 1e100;
        }
        return s.error(tgt) + max(0.0, (total - 1.0)) * in.D;
    }
    double cost(MixState s, const Color &tgt,
                const vector<Action> &actions) const {
        double total = 0;
        for (const auto &a : actions) {
            int tube_idx = a.tube_idx;
            s.add(in.tubes[tube_idx].c, in.tubes[tube_idx].m,
                  in.tubes[tube_idx].y, a.real_amt);
            total += a.real_amt;
        }
        if (s.amt < 1 - 1e-6) {
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
        rep(i, in.Q) s.add(tubes[i].c, tubes[i].m, tubes[i].y, coef[i]);
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
        const int Q = in.Q, H = in.H, LIM_MAX = 4, TOP = 2000;
        const double EPS = 1e-6;
        best_coefs.assign(5, std::vector<std::vector<double>>(
                                 H, std::vector<double>(Q, 0.0)));
        best_coefs_err.assign(5, std::vector<double>(H, 1e300));
        best_coef_cand.assign(5,
                              std::vector<std::vector<std::vector<double>>>(H));

        // 抜粋チューブ (ローカル添字)
        std::vector<Color> &sub = tubes;
        int sum_cnt = 0;
        for (int h = 0; h < H; ++h) {
            const Color &tgt = in.targets[h];
            auto res = mixopt::compute(tgt, sub, LIM_MAX, TOP, EPS, 1e-12);
            sum_cnt += res.cand_list[4].size();
            for (int lim = 1; lim <= LIM_MAX; ++lim) {
                if (res.best_coef[lim].empty())
                    continue;
                // best
                best_coefs[lim][h] = res.best_coef[lim];
                best_coefs_err[lim][h] = res.best_err[lim];
                // candidates
                best_coef_cand[lim][h] = res.cand_list[lim];
            }
        }
    }

    //----------------------------------
    MixState commit(const Color &tgt, const vector<Action> &acts,
                    const MixState &init_color) {
        vector<vector<int>> sep;
        MixState ms = init_color;
        err_sum += error_only(tgt, acts);
        for (auto a : acts) {
            if (a.use_blocks == 0) {
                continue;
            }
            auto &p = a.primary_or_secondary == 1
                          ? palettes[a.tube_idx].primary
                          : palettes[a.tube_idx].secondary;
            // 分母の変更
            if (p.used_blocks != a.blocks) {
                // 左を閉じる(分母を決める)
                auto s = p.cmd_sep(p.blocks - a.blocks);
                if (!s.empty()) {
                    int i = s[1];
                    int j = s[2];
                    int ii = s[3];
                    int jj = s[4];
                    if (i == ii) {
                        separator_v[i][min(j, jj)] ^= 1;
                    } else {
                        separator_h[min(i, ii)][j] ^= 1;
                    }
                    cmds.push_back(s);
                }
                // 区切りを空ける
                s = p.cmd_sep(p.blocks - p.used_blocks);
                if (!s.empty()) {
                    int i = s[1];
                    int j = s[2];
                    int ii = s[3];
                    int jj = s[4];
                    if (i == ii) {
                        separator_v[i][min(j, jj)] ^= 1;
                    } else {
                        separator_h[min(i, ii)][j] ^= 1;
                    }
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
                int i = s[1];
                int j = s[2];
                int ii = s[3];
                int jj = s[4];
                if (i == ii) {
                    separator_v[i][min(j, jj)] ^= 1;
                } else {
                    separator_h[min(i, ii)][j] ^= 1;
                }
                cmds.push_back(s);
            }
            // 左を開ける
            s = p.cmd_sep(p.blocks - a.blocks);
            if (!s.empty()) {
                int i = s[1];
                int j = s[2];
                int ii = s[3];
                int jj = s[4];
                if (i == ii) {
                    separator_v[i][min(j, jj)] ^= 1;
                } else {
                    separator_h[min(i, ii)][j] ^= 1;
                }
                sep.push_back(s);
            }
            p.used_blocks = a.blocks - a.use_blocks;
            p.cap = p.cap * p.used_blocks / a.blocks;
            ms.add(in.tubes[a.tube_idx].c, in.tubes[a.tube_idx].m,
                   in.tubes[a.tube_idx].y, a.real_amt);
        }
        for (auto &v : sep)
            cmds.push_back(v);
        cmds.push_back({2, 0, 0});
        ms.dump();
        while (ms.amt > 0.0) {
            ms.dump();
            cmds.push_back({3, 0, 0});
        }
        return ms;
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

    in.Q = in.need_idxs.size();
    vector<string> sep_v;
    vector<string> sep_h;
    vector<vector<int>> cmds;
    vector<vector<int>> change_palette_op;
    vector<vector<int>> best_op;

    double best_cost = 1e300;
    rep(i, 10) {
        tk.update();
        if (tk.now() > 2600) {
            break;
        }
        Solver sol(in, tk);
        sol.solve();
        if (sol.final_cost < best_cost) {
            best_cost = sol.final_cost;
            cerr << best_cost << '\n';
            sep_v = sol.sep_v;
            sep_h = sol.sep_h;
            cmds = sol.cmds;
            change_palette_op = sol.change_palette_op;
            best_op = sol.best_op;
        }
    }
    for (auto s : sep_v) {
        rep(j, s.size()) { cout << s[j] << (j < s.size() - 1 ? " " : "\n"); }
    }
    for (auto s : sep_h) {
        rep(j, s.size()) { cout << s[j] << (j < s.size() - 1 ? " " : "\n"); }
    }
    for (auto &v : cmds) {
        rep(i, v.size()) { cout << v[i] << (i + 1 < v.size() ? ' ' : '\n'); }
    }
    for (auto &v : change_palette_op) {
        rep(i, v.size()) { cout << v[i] << (i + 1 < v.size() ? ' ' : '\n'); }
    }
    for (auto &v : best_op) {
        rep(i, v.size()) { cout << v[i] << (i + 1 < v.size() ? ' ' : '\n'); }
    }

    // sol.cerr_report();
    return 0;
}

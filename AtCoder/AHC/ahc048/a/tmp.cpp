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
// struct Action {

//     Action() {}

//     bool operator==(const Action &other) const {}
// };
using Action = int;

using Cost = double;
// 状態のコストを評価するための構造体
// メモリ使用量をできるだけ小さくしてください
struct Evaluator {
    MixState ms;
    Cost cost;
    Evaluator(MixState ms, Cost cost) : ms(ms), cost(cost) {}

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
    explicit State(const Input &in, const Color &tgt, const MixState &init_ms,
                   double well_cap)
        : in(in), tgt(tgt), init_ms(init_ms), well_cap(well_cap) {}

    // EvaluatorとHashの初期値を返す
    pair<Evaluator, Hash> make_initial_node() {
        Evaluator ev(init_ms, 0);
        if (init_ms.amt == 0) {
            ev.cost = 1e100;
        } else {
            ev.cost = init_ms.error(tgt);
        }
        Hash hash = init_ms.hash();
        return {ev, hash};
    }

    // 次の状態候補を全てselectorに追加する
    // 引数
    //   evaluator : 今の評価器
    //   hash      : 今のハッシュ値
    //   parent    : 今のノードID（次のノードにとって親となる）
    void expand(const Evaluator &evaluator, Hash hash, int parent,
                Selector &selector) {
        // dump
        // if (evaluator.ms.amt > 1e-6) {
        //     MixState new_ms = evaluator.ms;
        //     Action new_action = -1;
        //     new_ms.dump();
        //     Hash new_hash = new_ms.hash();
        //     Cost new_cost;
        //     if (new_ms.amt == 0.0) {
        //         new_cost = 1e100;
        //     } else {
        //         new_cost = new_ms.error(tgt) +
        //                    max(0, used_tube_cnt - 1) * in.D +
        //                    (dump_cnt + 1) * 0.2 * in.D;
        //     }
        //     Evaluator new_evaluator = Evaluator(new_ms, new_cost);
        //     selector.push(
        //         Candidate(new_action, new_evaluator, new_hash, parent),
        //         false);
        // }

        // 絵具追加
        for (int new_action = 0; new_action < in.K; new_action++) {
            MixState new_ms = evaluator.ms;
            if (new_ms.amt == well_cap) {
                return;
            }
            double amt = 1.0;
            new_ms.add(in.tubes[new_action], amt, well_cap);
            Hash new_hash = new_ms.hash();
            Cost new_cost;
            if (new_ms.amt == 0.0) {
                new_cost = 1e100;
            } else {
                new_cost = new_ms.error(tgt) + used_tube_cnt * 0 * in.D +
                           dump_cnt * 0.2 * in.D;
            }
            Evaluator new_evaluator = Evaluator(new_ms, new_cost);
            selector.push(
                Candidate(new_action, new_evaluator, new_hash, parent), false);
        }
    }

    // actionを実行して次の状態に遷移する
    void move_forward(Action action) {
        if (action == -1) {
            dump_cnt++;
        } else {
            used_tube_cnt++;
        }
    }

    // actionを実行する前の状態に遷移する
    // 今の状態は、親からactionを実行して遷移した状態である
    void move_backward(Action action) {
        if (action == -1) {
            dump_cnt--;
        } else {
            used_tube_cnt--;
        }
    }

  private:
    const Input &in;
    const Color &tgt;
    const MixState &init_ms;
    double well_cap;
    int used_tube_cnt = 0;
    int dump_cnt = 0;
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
        // cerr << curr_tour_.size() << endl;

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
        return {};
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
    Cost best_cost = 1e300;
    vector<Action> best_actions;
    for (int turn = 0; turn < config.max_turn; ++turn) {
        // Euler Tourでselectorに候補を追加する
        tree.dfs(selector);

        if (selector.select().empty()) {
            break;
        }

        // ターン数固定型の問題で全ターンが終了したとき
        Candidate best_candidate = selector.calculate_best_candidate();
        if (best_candidate.evaluator.evaluate() < best_cost) {
            vector<Action> ret =
                tree.calculate_path(best_candidate.parent, turn + 1);
            ret.push_back(best_candidate.action);
            best_actions = ret;
            best_cost = best_candidate.evaluator.evaluate();
        }

        // 木を更新する
        tree.update(selector.select());

        selector.clear();
    }
    return {best_cost, best_actions};

    // unreachable();
}

} // namespace beam_search

// ──────────────────────────────
//  仕切り変更ではなくチューブ追加を主としたソルバー
// ──────────────────────────────
class AddTubeSolver {
    const Input &in;
    int tubes_used = 0;
    double err_sum = 0;
    double eps = 1e-6;
    int well_h = 4;
    int well_w = 4;
    int well_cap = well_h * well_w;
    int well_num = in.N * in.N / well_cap;
    vector<vector<int>> cmds;
    vector<string> sep_v;
    vector<string> sep_h;
    // vector<Color> standard_colors;
    // double random_tl = 500;
    // double anneal_tl = 500;
    vector<Well2> wells;
    // vector<int> target_well_index;

  public:
    int final_cost;
    AddTubeSolver(const Input &_in) : in(_in) {}
    void solve() {
        init_palettes();
        init_wells();
        cerr << wells.size() << '\n';
        rep(i, well_num) {
            cerr << i << '\n';
            cerr << wells[i].i << '\n';
            cerr << wells[i].j << '\n';
            cerr << wells[i].cap << '\n';
        }
        // make_standard_colors();
        // make_target_well_index();
        rep(h, in.H) {
            int remains_turn = in.T - cmds.size() - (in.H - h);
            int max_turn = remains_turn / (in.H - h);
            auto [idx, actions] = calc_best_action(max_turn, in.targets[h]);
            commit(in.targets[h], idx, actions);
        }
        while (cmds.size() > in.T) {
            cmds.pop_back();
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
        cerr << "Add Tube Solve: \n";
        cerr << "Cost: " << (long long)(err_sum + (tubes_used - in.H) * in.D)
             << '\n';
        cerr << "Err: " << (long long)err_sum << '\n';
        cerr << "Tube: " << (tubes_used - in.H) * in.D << '\n';
        cerr << "Used_Tubes: " << tubes_used << '\n';
        cerr << "Used_Turn: " << cmds.size() << " / " << in.T << '\n';
    }

  private:
    void commit(const Color &tgt, int well_index,
                const vector<beam_search::Action> &actions) {
        Well2 &well = wells[well_index];
        for (auto action : actions) {
            if (action == -1) {
                cmds.push_back({3, well.i, well.j});
                well.ms.dump();
            } else {
                tubes_used++;
                cmds.push_back({1, well.i, well.j, action});
                well.ms.add(in.tubes[action], 1.0, well_cap);
            }
        }
        err_sum += well.ms.error(tgt);
        cmds.push_back({2, well.i, well.j});
        well.ms.dump();
        while (well_cap - well.ms.amt < 3 and in.T > 8000) {
            well.ms.dump();
            cmds.push_back({3, well.i, well.j});
        }
    }
    // void make_target_well_index() {
    //     target_well_index.reserve(in.H);
    //     rep(i, in.H) {
    //         double min_err = 1e100;
    //         int best_idx;
    //         rep(idx, well_num) {
    //             double err = d2(in.targets[i], standard_colors[idx]);
    //             if (err < min_err) {
    //                 min_err = err;
    //                 best_idx = idx;
    //             }
    //         }
    //         cerr << best_idx << " " << min_err << '\n';
    //         target_well_index.push_back(best_idx);
    //     }
    // }
    void init_wells() {
        wells.reserve(well_num);
        for (int i = 0; i < in.N; i += well_h) {
            for (int j = 0; j < in.N; j += well_w) {
                Well2 well;
                well.i = i;
                well.j = j;
                well.cap = well_cap;
                wells.push_back(well);
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
    pair<int, vector<beam_search::Action>> calc_best_action(int mt,
                                                            const Color &tgt) {
        // msの状態のwellに最大max_turnを投じて,colorに近似させる操作列を返す
        static size_t beam_width = 1000;
        static size_t tour_capacity = 15 * beam_width;
        static uint32_t hash_map_capacity = 16 * 3 * beam_width;
        int max_turn;
        beam_search::Config config = {min(3, max_turn), beam_width,
                                      tour_capacity, hash_map_capacity};
        vector<beam_search::Action> best_actions;
        double best_cost = 1e100;
        int best_idx;
        rep(i, well_num) {
            beam_search::State state(in, tgt, wells[i].ms, well_cap);
            auto [cost, actions] = beam_search::beam_search(config, state);
            if (cost < best_cost) {
                best_actions = actions;
                best_cost = cost;
                best_idx = i;
            }
        }
        return {best_idx, best_actions};
    }

    double evaluate(const vector<Color> &standard_colors) {
        static vector<double> min_cost(in.H);
        fill(min_cost.begin(), min_cost.end(), 1e100);
        rep(i, in.H) {
            const auto &color = in.targets[i];
            for (const auto &standard_color : standard_colors) {
                double _d2 = d2(color, standard_color);
                if (_d2 < min_cost[i]) {
                    min_cost[i] = _d2;
                }
            }
        }
        double err_sum = 0;
        for (auto d : min_cost) {
            err_sum += sqrt(d);
        }
        return err_sum * 10000.0;
    }
    // vector<Color> make_colors_by_random() {
    //     double c_min, c_max, m_min, m_max, y_min, y_max;
    //     c_min = 1e100;
    //     m_min = 1e100;
    //     y_min = 1e100;
    //     c_max = 1e-100;
    //     m_max = 1e-100;
    //     y_max = 1e-100;
    //     for (auto &color : in.tubes) {
    //         c_min = min(c_min, color.c);
    //         c_max = max(c_max, color.c);
    //         y_min = min(y_min, color.m);
    //         y_max = max(y_max, color.m);
    //         m_min = min(m_min, color.y);
    //         m_max = max(m_max, color.y);
    //     }
    //     vector<Color> best_colors;
    //     double min_err_sum = 1e100;
    //     vector<Color> tmp_colors(well_num);
    //     TimeKeeper tk(random_tl);
    //     int iter = 0;
    //     while (true) {
    //         iter++;
    //         if (iter % 100 == 0) {
    //             tk.update();
    //             if (tk.over()) {
    //                 break;
    //             }
    //         }
    //         rep(i, well_num) {
    //             tmp_colors[i].c = rnd::uniform_real(c_min, c_max);
    //             tmp_colors[i].m = rnd::uniform_real(m_min, m_max);
    //             tmp_colors[i].y = rnd::uniform_real(y_min, y_max);
    //         }
    //         double err_sum = evaluate(tmp_colors);

    //         if (err_sum < min_err_sum) {
    //             min_err_sum = err_sum;
    //             best_colors = tmp_colors;
    //         }
    //     }
    //     return best_colors;
    // }
    // vector<Color> make_colors_by_anneal(const vector<Color> &colors) {
    //     vector<Color> curr_colors = colors;
    //     double curr_err = evaluate(curr_colors);

    //     vector<Color> best_colors = curr_colors;
    //     double best_err = curr_err;

    //     TimeKeeper tk(anneal_tl);

    //     // --- 2. 温度パラメータ（線形スケジューリング用） ---
    //     const double T0 = 1000;      // 初期温度
    //     const double T_final = 1e-4; // 最終温度
    //     int iter = -1;
    //     double t_ratio;
    //     double T;
    //     // 最後に返す最良解を保持
    //     // --- 3. 焼きなましループ ---
    //     while (true) {
    //         iter++;
    //         if (iter % 50 == 0) {
    //             tk.update();
    //             if (tk.over()) {
    //                 break;
    //             }
    //             // 3-1. 経過時間 t を [0,1) の比率で取得
    //             t_ratio = double(tk.now()) / double(anneal_tl);
    //             if (t_ratio > 1.0)
    //                 t_ratio = 1.0;
    //             T = T0 + (T_final - T0) * t_ratio;
    //         }

    //         int idx = rnd::xorshift32() % well_num;     //
    //         どのウェルをいじるか int cmy = rnd::xorshift32() % 3; // 0->C,
    //         1->M, 2->Y double diff = rnd::uniform_real(-0.2, 0.2); // 変化量

    //         // 候補解を作るために元の値を退避
    //         Color backup = curr_colors[idx];
    //         if (cmy == 0) {
    //             curr_colors[idx].c += diff;
    //             if (curr_colors[idx].c < 0.0)
    //                 curr_colors[idx].c = 0.0;
    //             else if (curr_colors[idx].c > 1.0)
    //                 curr_colors[idx].c = 1.0;
    //         } else if (cmy == 1) {
    //             curr_colors[idx].m += diff;
    //             if (curr_colors[idx].m < 0.0)
    //                 curr_colors[idx].m = 0.0;
    //             else if (curr_colors[idx].m > 1.0)
    //                 curr_colors[idx].m = 1.0;
    //         } else {
    //             curr_colors[idx].y += diff;
    //             if (curr_colors[idx].y < 0.0)
    //                 curr_colors[idx].y = 0.0;
    //             else if (curr_colors[idx].y > 1.0)
    //                 curr_colors[idx].y = 1.0;
    //         }

    //         double new_err = evaluate(curr_colors);

    //         double delta = new_err - curr_err;
    //         bool accept = false;
    //         if (delta < 0) {
    //             accept = true;
    //         } else {
    //             double prob = std::exp(-delta / std::max(T, 1e-12));
    //             if (rnd::uniform01() < prob) {
    //                 accept = true;
    //             }
    //         }

    //         if (accept) {
    //             // 受け入れ：current を更新
    //             curr_err = new_err;
    //             // 最良解の更新
    //             if (curr_err < best_err) {
    //                 best_err = curr_err;
    //                 best_colors = curr_colors;
    //             }
    //         } else {
    //             curr_colors[idx] = backup;
    //         }
    //     }

    //     return best_colors;
    // }
    // void make_standard_colors() {
    //     auto random_colors = make_colors_by_random();
    //     cerr << evaluate(random_colors) << '\n';
    //     auto anneal_colors = make_colors_by_anneal(random_colors);
    //     cerr << evaluate(anneal_colors) << '\n';

    //     standard_colors = anneal_colors;
    // }
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
        int expected_used_turn = 0;
        rep(h, in.H) {
            const Color &tgt = in.targets[h];
            int colors = can_use_colors[h];
            // ターン数に余裕があるなら追加
            if (colors < 4 and expected_used_turn - cmds.size() >= 4) {
                int can_add = (expected_used_turn - cmds.size()) / 4;
                colors += min(can_add, 4 - colors);
            }
            cerr << "Use_Colors: " << h + 1 << " " << colors << '\n';
            auto coef = best_coefs[colors][h];
            auto acts = discretise(tgt, coef);
            cerr << "連続値のエラー: " << error_only(tgt, coef)
                 << " 離散値のエラー: " << error_only(tgt, acts) << '\n';
            commit(tgt, acts);
            expected_used_turn += 3;
            expected_used_turn += can_use_colors[h] * 4;
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
            auto &p = palettes[a.tube_idx];
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
        // Small_T_Solver sol(in);
        // AddTubeSolver sol(in);
        // sol.solve();
        // tk.update();
        // if (tk.now() < 2000.0 and 11000 <= in.T) {
        //     Solver sol2(in, tk);
        //     sol2.solve();
        //     sol.cerr_report();
        //     sol2.cerr_report();
        //     if (sol.final_cost < sol2.final_cost) {
        //         sol.print();
        //     } else {
        //         sol2.print();
        //     }
        // } else {
        //     sol.cerr_report();
        //     sol.print();
        // }
    } else {
        tk.update();
        Solver sol(in, tk);
        sol.solve();
        sol.cerr_report();
        sol.print();
    }
    return 0;
}

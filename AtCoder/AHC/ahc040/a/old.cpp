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
namespace xorshift64 {

inline static uint64_t a = 12345;

uint64_t next() {
    uint64_t x = a;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    return a = x;
}

} // namespace xorshift64
#ifndef ATCODER_INTERNAL_BITOP_HPP
#define ATCODER_INTERNAL_BITOP_HPP 1

#ifdef _MSC_VER
#include <intrin.h>
#endif

#if __cplusplus >= 202002L
#include <bit>
#endif

namespace atcoder {

namespace internal {

#if __cplusplus >= 202002L

using std::bit_ceil;

#else

// @return same with std::bit::bit_ceil
unsigned int bit_ceil(unsigned int n) {
    unsigned int x = 1;
    while (x < (unsigned int)(n))
        x *= 2;
    return x;
}

#endif

// @param n `1 <= n`
// @return same with std::bit::countr_zero
int countr_zero(unsigned int n) {
#ifdef _MSC_VER
    unsigned long index;
    _BitScanForward(&index, n);
    return index;
#else
    return __builtin_ctz(n);
#endif
}

// @param n `1 <= n`
// @return same with std::bit::countr_zero
constexpr int countr_zero_constexpr(unsigned int n) {
    int x = 0;
    while (!(n & (1 << x)))
        x++;
    return x;
}

} // namespace internal

} // namespace atcoder

#endif // ATCODER_INTERNAL_BITOP_HPP

#ifndef ATCODER_SEGTREE_HPP
#define ATCODER_SEGTREE_HPP 1

namespace atcoder {

#if __cplusplus >= 201703L

template <class S, auto op, auto e> struct segtree {

#else

template <class S, S (*op)(S, S), S (*e)()> struct segtree {

#endif

  public:
    segtree() : segtree(0) {}
    explicit segtree(int n) : segtree(std::vector<S>(n, e())) {}
    explicit segtree(const std::vector<S> &v) : _n(int(v.size())) {
        size = (int)internal::bit_ceil((unsigned int)(_n));
        log = internal::countr_zero((unsigned int)size);
        d = std::vector<S>(2 * size, e());
        for (int i = 0; i < _n; i++)
            d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) {
            update(i);
        }
    }

    void set(int p, S x) {
        assert(0 <= p && p < _n);
        p += size;
        d[p] = x;
        for (int i = 1; i <= log; i++)
            update(p >> i);
    }

    S get(int p) const {
        assert(0 <= p && p < _n);
        return d[p + size];
    }

    S prod(int l, int r) const {
        assert(0 <= l && l <= r && r <= _n);
        S sml = e(), smr = e();
        l += size;
        r += size;

        while (l < r) {
            if (l & 1)
                sml = op(sml, d[l++]);
            if (r & 1)
                smr = op(d[--r], smr);
            l >>= 1;
            r >>= 1;
        }
        return op(sml, smr);
    }

    S all_prod() const { return d[1]; }

    template <bool (*f)(S)> int max_right(int l) const {
        return max_right(l, [](S x) { return f(x); });
    }
    template <class F> int max_right(int l, F f) const {
        assert(0 <= l && l <= _n);
        assert(f(e()));
        if (l == _n)
            return _n;
        l += size;
        S sm = e();
        do {
            while (l % 2 == 0)
                l >>= 1;
            if (!f(op(sm, d[l]))) {
                while (l < size) {
                    l = (2 * l);
                    if (f(op(sm, d[l]))) {
                        sm = op(sm, d[l]);
                        l++;
                    }
                }
                return l - size;
            }
            sm = op(sm, d[l]);
            l++;
        } while ((l & -l) != l);
        return _n;
    }

    template <bool (*f)(S)> int min_left(int r) const {
        return min_left(r, [](S x) { return f(x); });
    }
    template <class F> int min_left(int r, F f) const {
        assert(0 <= r && r <= _n);
        assert(f(e()));
        if (r == 0)
            return 0;
        r += size;
        S sm = e();
        do {
            r--;
            while (r > 1 && (r % 2))
                r >>= 1;
            if (!f(op(d[r], sm))) {
                while (r < size) {
                    r = (2 * r + 1);
                    if (f(op(d[r], sm))) {
                        sm = op(d[r], sm);
                        r--;
                    }
                }
                return r + 1 - size;
            }
            sm = op(d[r], sm);
        } while ((r & -r) != r);
        return 0;
    }

  private:
    int _n, size, log;
    std::vector<S> d;

    void update(int k) { d[k] = op(d[2 * k], d[2 * k + 1]); }
};

} // namespace atcoder

#endif // ATCODER_SEGTREE_HPP
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
TimeKeeperDouble time_keeper(9500);
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

// ---------------------------------------------------------
constexpr double TIME_LIMIT = 2900;
int N, T, Sig;
const array<string, 2> UL = {"U", "L"};
struct Input {
    vector<pii> wh;
    void input() {
        cin >> N >> T >> Sig;
        wh.resize(N);
        rep(i, N) {
            int w, h;
            cin >> w >> h;
            wh[i] = {w, h};
        }
    }
};
struct Action {
    int p;
    int r;
    string d;
    int b;
    array<int, 4> udlr;
    Action(int p, int r, string d, int b) : p(p), r(r), d(d), b(b) {};
    bool operator==(const Action &other) const {
        return (p == other.p and r == other.r and d == other.d and
                b == other.b);
    }
};
struct Output {
    pair<int, int> query(const vector<Action> &actions) {
        int size = actions.size();
        cout << size << el;
        rep(i, size) {
            if (i == size - 1) {
                cout << actions[i].p << ' ' << actions[i].r << ' '
                     << actions[i].d << ' ' << actions[i].b << endl;
            } else {
                cout << actions[i].p << ' ' << actions[i].r << ' '
                     << actions[i].d << ' ' << actions[i].b << el;
            }
        }
        int w, h;
        cin >> w >> h;
        return {w, h};
    }
};
array<int, 4> get_pos(int w, int h, Action action,
                      const vector<tuple<int, int, int>> &vertical,
                      const vector<tuple<int, int, int>> &horizon) {
    int n = vertical.size();
    if (action.r == 1) {
        swap(w, h);
    }
    int l, r, u, d;
    if (action.d == "U") {
        if (action.b == -1) {
            l = 0;
            r = l + w;
        } else {
            l = get<1>(horizon[action.b]);
            r = l + w;
        }
        u = 0;
        rep(j, n) {
            auto [x, y, z] = horizon[j];
            if (l <= y and x <= r) {
                chmax(u, z);
            }
        }
        d = u + h;
    } else {
        if (action.b == -1) {
            u = 0;
            d = 0 + h;
        } else {
            u = get<1>(vertical[action.b]);
            d = u + h;
        }
        l = 0;
        rep(j, n) {
            auto [x, y, z] = vertical[j];
            if (u <= y and x <= d) {
                chmax(l, z);
            }
        }
        r = l + w;
    }
    return {u, d, l, r};
}
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

using Hash = uint64_t; // TODO

// // 状態遷移を行うために必要な情報
// // メモリ使用量をできるだけ小さくしてください
// struct Action {
//     // TODO

//     Action() {
//         // TODO
//     }

//     bool operator==(const Action &other) const {
//         // TODO
//     }
// };

using Cost = int;

// 状態のコストを評価するための構造体
// メモリ使用量をできるだけ小さくしてください
struct Evaluator {
    int w;
    int h;

    Evaluator(int w, int h) : w(w), h(h) {}

    // 低いほどよい
    Cost evaluate() const { return w + h; }
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
    static pair<Cost, int> op(pair<Cost, int> a, pair<Cost, int> b) {
        return (a.first >= b.first) ? a : b;
    }

    static pair<Cost, int> e() {
        return make_pair(numeric_limits<Cost>::min(), -1);
    }

    // 削除可能な優先度付きキュー
    using MaxSegtree = atcoder::segtree<pair<Cost, int>, &op, &e>;
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
    explicit State(const vector<pair<int, int>> &whs) : whs(whs) {
        vertical.reserve(N);
        horizon.reserve(N);
    }

    // EvaluatorとHashの初期値を返す
    pair<Evaluator, Hash> make_initial_node() { return {{0, 0}, 0}; }

    // 次の状態候補を全てselectorに追加する
    // 引数
    //   evaluator : 今の評価器
    //   hash      : 今のハッシュ値
    //   parent    : 今のノードID（次のノードにとって親となる）
    void expand(const Evaluator &evaluator, Hash hash, int parent,
                Selector &selector) {
        int p = vertical.size();
        auto [w, h] = whs[p];
        rep(r, 2) {
            rep(d, 2) {
                for (int b = -1; b < (int)vertical.size(); b++) {
                    auto [W, H] = evaluator;
                    Action new_action = {p, r, UL[d], b};
                    auto [u, d, l, r] =
                        get_pos(w, h, new_action, vertical, horizon);
                    new_action.udlr = array<int, 4>{u, d, l, r};
                    chmax(W, r);
                    chmax(H, d);
                    Hash hash = (d << 30) | r;
                    selector.push(
                        Candidate(new_action, Evaluator(W, H), hash, parent),
                        false);
                }
            }
        }
    }

    // actionを実行して次の状態に遷移する
    void move_forward(Action action) {
        auto [u, d, l, r] = action.udlr;
        vertical.emplace_back(u, d, r);
        horizon.emplace_back(l, r, d);
    }

    // actionを実行する前の状態に遷移する
    // 今の状態は、親からactionを実行して遷移した状態である
    void move_backward(Action action) {
        vertical.pop_back();
        horizon.pop_back();
    }

  private:
    vector<tuple<int, int, int>> vertical;
    vector<tuple<int, int, int>> horizon;
    vector<pair<int, int>> whs;
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
vector<Action> beam_search(const Config &config, const State &state) {
    Tree tree(state, config);

    // 新しいノード候補の集合
    Selector selector(config);

    for (int turn = 0; turn < config.max_turn; ++turn) {
        // Euler Tourでselectorに候補を追加する
        tree.dfs(selector);

        if (selector.have_finished()) {
            // ターン数最小化型の問題で実行可能解が見つかったとき
            Candidate candidate = selector.get_finished_candidates()[0];
            vector<Action> ret =
                tree.calculate_path(candidate.parent, turn + 1);
            ret.push_back(candidate.action);
            return ret;
        }

        assert(!selector.select().empty());

        if (turn == config.max_turn - 1) {
            // ターン数固定型の問題で全ターンが終了したとき
            Candidate best_candidate = selector.calculate_best_candidate();
            vector<Action> ret =
                tree.calculate_path(best_candidate.parent, turn + 1);
            ret.push_back(best_candidate.action);
            return ret;
        }

        // 木を更新する
        tree.update(selector.select());

        selector.clear();
    }
    return {};
    // unreachable();
}

} // namespace beam_search
constexpr size_t beam_width = 2000;
constexpr size_t tour_capacity = 16 * beam_width;
constexpr uint32_t hash_map_capacity = 64 * beam_width;

constexpr double kSqrt2 = 1.41421356237309514547;

inline double calc_norm_cdf(double mu, double sigma, double x) {
    return 0.5 * (1.0 + erf((x - mu) / (kSqrt2 * sigma)));
}

inline double calc_pr(double mu, double sigma, int vs) {
    return calc_norm_cdf(mu, sigma, (double)vs + 0.5) -
           calc_norm_cdf(mu, sigma, (double)vs - 0.5);
}

constexpr double kLogLogPrThreshold = -200.0;

inline double calc_fix_log_pr(double pr) {
    double log_pr = (pr <= 0.0) ? DBL_MIN_EXP : log2(pr);
    if (log_pr < kLogLogPrThreshold) {
        return kLogLogPrThreshold;
    } else {
        return log_pr;
    }
}
// 平均0、標準偏差sigmaの正規分布から値をランダム生成する関数
int generate_normal_random(int sigma) {
    if (sigma <= 0) {
        throw std::invalid_argument(
            "Standard deviation (sigma) must be positive.");
    }

    // 静的な乱数エンジン（再利用）
    static std::random_device rd; // ハードウェア乱数生成器
    static std::mt19937 gen(rd()); // メルセンヌツイスタ乱数エンジン

    // 正規分布（平均0、標準偏差sigmaをdoubleにキャスト）
    std::normal_distribution<> dist(0.0, static_cast<double>(sigma));

    // ランダム値を生成して返す
    return round(dist(gen));
}

struct Solver {
    Input input;
    Output output;
    vector<pair<vector<Action>, pair<int, int>>> queryed;
    int id = 0;
    Solver(const Input &input) : input(input) { queryed.reserve(T); }
    void make_neighbor(int max_times, int max_size,
                       vector<pair<double, vector<pair<int, int>>>> &cands,
                       int sig) {
        // 現在の候補を元に、新たな候補を追加する
        int init_size = cands.size();
        rep(i, max_times) {
            auto new_cand = cands[xorshift64::next() % init_size].second;
            rep(j, N) {
                rep(j, N) {
                    new_cand[j].first += generate_normal_random(sig);
                    chmin(new_cand[j].first, 100000);
                    chmax(new_cand[j].first, 10000);
                    new_cand[j].second += generate_normal_random(sig);
                    chmin(new_cand[j].second, 100000);
                    chmax(new_cand[j].second, 10000);
                }
            }
            double ev = 0;
            ev += evaluate_init(new_cand);
            ev += evaluate_all_query(new_cand);
            cands.emplace_back(ev, new_cand);
        }
        sort(all(cands),
             [](const auto &a, const auto &b) { return a.first > b.first; });
        if (cands.size() > max_size) {
            cands.resize(max_size);
        }
    }

    pair<int, int> get_wh(const vector<Action> &actions,
                          const vector<pair<int, int>> &cand) {
        assert(actions.size() == cand.size());
        // 各辺の長さがcandのとき、actionsで指定された置き方で置いた場合のW,Hを返す。
        int n = actions.size();
        static vector<tuple<int, int, int>> vertical;
        static vector<tuple<int, int, int>> horizon;

        vertical.clear();
        horizon.clear();
        int W = 0;
        int H = 0;
        rep(i, n) {
            Action action = actions[i];
            auto [w, h] = cand[i];
            auto [u, d, l, r] = get_pos(w, h, action, vertical, horizon);
            vertical.emplace_back(u, d, r);
            horizon.emplace_back(l, r, d);
            chmax(W, r);
            chmax(H, d);
        }
        return {W, H};
    }
    double evaluate_init(const vector<pair<int, int>> &cand) {
        double res = 0.0;
        rep(i, N) {
            res +=
                calc_fix_log_pr(calc_pr(cand[i].first, Sig, input.wh[i].first));
            res += calc_fix_log_pr(
                calc_pr(cand[i].second, Sig, input.wh[i].second));
        }
        return res;
    }
    double evaluate_all_query(const vector<pair<int, int>> &cand) {
        double res = 0.0;
        rep(i, (int)queryed.size()) {
            auto [w, h] = get_wh(queryed[i].first, cand);
            auto [rw, rh] = queryed[i].second;
            res += calc_fix_log_pr(calc_pr(w, Sig, rw));
            res += calc_fix_log_pr(calc_pr(h, Sig, rh));
        }
        return res;
    }
    double evaluate_query(const vector<pair<int, int>> &cand,
                          const pair<vector<Action>, pair<int, int>> query) {
        double res = 0.0;
        auto [w, h] = get_wh(query.first, cand);
        auto [rw, rh] = query.second;
        res += calc_fix_log_pr(calc_pr(w, Sig, rw));
        res += calc_fix_log_pr(calc_pr(h, Sig, rh));
        return res;
    }
    void solve() {
        beam_search::Config config = {N, beam_width, tour_capacity,
                                      hash_map_capacity};
        beam_search::State state(input.wh);
        vector<Action> actions = beam_search::beam_search(config, state);
        rep(i, T) { auto wh = output.query(actions); }
        dump(get_wh(actions, input.wh));

        // int max_size = 100;
        // int max_times = 100;
        // vector<pair<double, vector<pair<int, int>>>> cands;
        // cands.reserve(max_size);
        // cands.emplace_back(evaluate_init(input.wh), input.wh);
        // make_neighbor(max_times, max_size, cands, Sig);
        // beam_search::Config config = {N, beam_width, tour_capacity,
        //                               hash_map_capacity};
        // rep(t, T) {
        //     beam_search::State state(cands[0].second);
        //     // for (auto c : cands[0].second) {
        //     //     cerr << c.first << " " << c.second << el;
        //     // }
        //     vector<Action> actions = beam_search::beam_search(config,
        //     state); auto wh = output.query(actions);
        //     // dump(wh, get_wh(actions, cands[0].second));
        //     queryed.emplace_back(actions, wh);
        //     rep(i, cands.size()) {
        //         cands[i].first +=
        //             evaluate_query(cands[i].second,
        //             *queryed.rbegin());
        //     }
        //     make_neighbor(max_times, max_size, cands, Sig / 10);
        //     dump(t, cands[0].first);
        //     for (auto [ev, _] : cands) {
        //         dump(t, ev);
        //     }
        // }
    }
};

int main() {
    time_keeper = TimeKeeperDouble(TIME_LIMIT);
    Input input;
    input.input();
    Solver solver(input);
    solver.solve();
    return 0;
}

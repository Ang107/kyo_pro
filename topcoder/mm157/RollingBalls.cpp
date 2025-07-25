/*
考察メモ
ペナルティが重くないので、必ずしも揃える必要ないのかも
解法は、無難に行くなら石の配置を焼きながらビーム打つとかで良さそう。
↑これ普通に無理
ビーム一回が重すぎ
石の置きはよくわからんから、適当に置くのを試してみてスコア見てみたい。
とりあえずは移動する順番決め打ってビームを時間の間繰り返す感じかなー
*/
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
// ---------------------------------------------------------
// ---------------------------------------------------------
constexpr array<pair<int, int>, 4> UDLR = {{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};
constexpr double TIME_LIMIT = 9800;
int N;
int C;
int K;
int BALLS_NUM;
struct Input {
    vector<vector<int>> grid;
    vector<vector<int>> target;
    void input() {
        cin >> N >> C >> K;
        grid.resize(N, vector<int>(N));
        target.resize(N, vector<int>(N));
        for (int r = 0; r < N; r++)
            for (int c = 0; c < N; c++)
                cin >> grid[r][c];
        for (int r = 0; r < N; r++)
            for (int c = 0; c < N; c++)
                cin >> target[r][c];
    }
};
struct Output {
    vector<tuple<int, int, string>> ans;
    vector<pair<int, int>> blocks;
    void output() {
        cout << ans.size() + blocks.size() << el;
        cout.flush();
        for (auto [r, c] : blocks) {
            cout << r << " " << c << " " << "B" << el;
            cout.flush();
        }
        for (auto [r, c, cmd] : ans) {
            cout << r << " " << c << " " << cmd << el;
            cout.flush();
        }
    }
};

pair<int, int> next_pos(int x, int y, int cmd,
                        const vector<vector<int>> &grid) {
    int nx = x;
    int ny = y;
    while (true) {
        int tmp_x = nx + UDLR[cmd].first;
        int tmp_y = ny + UDLR[cmd].second;
        if (tmp_x < 0 || tmp_x >= N || tmp_y < 0 || tmp_y >= N ||
            grid[tmp_x][tmp_y] != 0) {
            break;
        }
        nx = tmp_x;
        ny = tmp_y;
    }
    return {nx, ny};
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

// 状態遷移を行うために必要な情報
// メモリ使用量をできるだけ小さくしてください
struct Action {
    int px;
    int py;
    int nx;
    int ny;
    int cmd;
    uint64_t index;

    Action(int px, int py, int nx, int ny, vector<int> cmd_vec, uint64_t index)
        : px(px), py(py), nx(nx), ny(ny), index(index) {
        cmd = encode(cmd_vec);
    }
    // 0~3からなるvector(要素数は最大4)をintにエンコードする関数
    int encode(const vector<int> &cmd_vec) {
        int res = 0;
        for (auto cmd : cmd_vec) {
            res <<= 3;
            res |= cmd + 1;
        }
        return res;
    }
    // intからvectorにデコードする関数
    vector<int> decode() {
        int cmd_int = cmd;
        vector<int> res;
        while (cmd_int > 0) {
            int c = cmd_int & 7;
            if (c == 0) {
                break;
            }
            res.push_back(c - 1);
            cmd_int >>= 3;
        }
        return res;
    }
    bool operator==(const Action &other) const {
        return px == other.px and py == other.py and nx == other.nx and
               ny == other.ny and cmd == other.cmd;
    }
};

using Cost = int;

// 状態のコストを評価するための構造体
// メモリ使用量をできるだけ小さくしてください
struct Evaluator {
    int turn;
    int ok;
    int diff;

    Evaluator(int turn, int ok, int diff) : turn(turn), ok(ok), diff(diff) {}

    // 低いほどよい
    Cost evaluate() const {
        if (ok >= BALLS_NUM * 5 / 6 or time_keeper.getNowTime() > 8000) {
            return turn - N * diff * (float(ok) / float(BALLS_NUM)) / 2 -
                   N * ok;
        } else {
            return turn - N * ok;
        }
    }
};

namespace zobrist_hash {
vector<vector<vector<Hash>>> zobrist_hashes;
void make_hash(Input &input) {
    int max_c = 0;
    rep(x, N) {
        rep(y, N) { chmax(max_c, input.grid[x][y]); }
    }
    zobrist_hashes.resize(max_c + 1, vector<vector<Hash>>(N, vector<Hash>(N)));
    rep(i, max_c + 1) {
        rep(x, N) {
            rep(y, N) { zobrist_hashes[i][x][y] = xorshift64::next(); }
        }
    }
}
} // namespace zobrist_hash

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
    // finished = true とする
    // ビーム幅分の候補をCandidateを追加したときにsegment treeを構築する
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
    explicit State(const Input &input, const vector<pair<int, int>> &balls)
        : grid(input.grid), target(input.target), balls(balls),
          balls_size(balls.size()) {}

    // EvaluatorとHashの初期値を返す
    pair<Evaluator, Hash> make_initial_node() {
        Evaluator evaluator{0, 0, 0};
        Hash hash = 0;
        rep(x, N) {
            rep(y, N) {
                if (grid[x][y] > 0) {
                    // dump(x, y, grid[x][y], target[x][y]);
                    hash ^= zobrist_hash::zobrist_hashes[grid[x][y]][x][y];
                    if (target[x][y] == grid[x][y]) {
                        evaluator.ok++;
                    } else if (target[x][y] != grid[x][y]) {
                        evaluator.diff++;
                    }
                }
            }
        }
        return {evaluator, hash};
    }

    // 次の状態候補を全てselectorに追加する
    // 引数
    //   evaluator : 今の評価器
    //   hash      : 今のハッシュ値
    //   parent    : 今のノードID（次のノードにとって親となる）
    void expand(const Evaluator &evaluator, Hash hash, int parent,
                Selector &selector, uint64_t index) {
        queue<tuple<int, int, int>> que;
        map<pair<int, int>, tuple<int, int, int>> visited;
        // dump(index);
        index %= balls.size();

        auto [px, py] = balls[index];
        const int color = grid[px][py];
        grid[px][py] = 0;
        visited[{px, py}] = {-1, -1, -1};
        que.push({0, px, py});
        selector.push(Candidate({px, py, px, py, {}, index},
                                {evaluator.turn, evaluator.ok, evaluator.diff},
                                hash, parent),
                      false);
        while (!que.empty()) {
            auto [cnt, x, y] = que.front();
            que.pop();
            rep(cmd, 4) {
                auto [nx, ny] = next_pos(x, y, cmd, grid);
                if (nx == x and ny == y) {
                    continue;
                }
                if (nx == px and ny == py) {
                    continue;
                }
                if (visited.find({nx, ny}) == visited.end()) {
                    visited[{nx, ny}] = {cmd, x, y};
                    if (cnt <= 4) {
                        que.push({cnt + 1, nx, ny});
                    }
                    auto [turn, ok, diff] = evaluator;
                    Hash new_hash = hash;
                    new_hash ^= zobrist_hash::zobrist_hashes[color][px][py];
                    new_hash ^= zobrist_hash::zobrist_hashes[color][nx][ny];
                    turn += cnt + 1;
                    if (target[px][py] == color) {
                        ok--;
                    } else if (target[px][py] != 0) {
                        diff--;
                    }
                    if (target[nx][ny] == color) {
                        ok++;
                    } else if (target[nx][ny] != 0) {
                        diff++;
                    }
                    vector<int> cmd_vec;
                    int tmp_x = nx;
                    int tmp_y = ny;
                    while (true) {
                        auto [cmd, x, y] = visited[{tmp_x, tmp_y}];
                        if (cmd == -1) {
                            break;
                        } else {
                            cmd_vec.push_back(cmd);
                            tmp_x = x;
                            tmp_y = y;
                        }
                    }
                    // dump(turn, mis_match, mis_placed);
                    if (ok < balls_size) {
                        selector.push(
                            Candidate({px, py, nx, ny, cmd_vec, index},
                                      {turn, ok, diff}, new_hash, parent),
                            false);
                    } else {
                        selector.push(
                            Candidate({px, py, nx, ny, cmd_vec, index},
                                      {turn, ok, diff}, new_hash, parent),
                            true);
                    }
                }
            }
        }
        grid[px][py] = color;
    }

    // actionを実行して次の状態に遷移する
    void move_forward(Action action) {
        auto [px, py, nx, ny, cmd, index] = action;
        // index++;
        balls[index] = {nx, ny};
        int c = grid[px][py];
        grid[px][py] = 0;
        grid[nx][ny] = c;
    }

    // actionを実行する前の状態に遷移する
    // 今の状態は、親からactionを実行して遷移した状態である
    void move_backward(Action action) {
        auto [px, py, nx, ny, cmd, index] = action;
        // index--;
        balls[index] = {px, py};
        int c = grid[nx][ny];
        grid[nx][ny] = 0;
        grid[px][py] = c;
    }

    //   private:
    // TODO
    vector<vector<int>> grid;
    vector<vector<int>> target;
    vector<pair<int, int>> balls;
    int balls_size;
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
    void dfs(Selector &selector, const State &state) {
        uint64_t index;
        while (true) {
            index = xorshift64::next();
            auto [x, y] = state.balls[index % state.balls_size];
            if ((0 <= x - 1 and state.grid[x - 1][y] == 0) or
                (0 <= y - 1 and state.grid[x][y - 1] == 0) or
                (x + 1 < N and state.grid[x + 1][y] == 0) or
                (y + 1 < N and state.grid[x][y + 1] == 0)) {
                break;
            }
        }

        if (curr_tour_.empty()) {
            // 最初のターン
            auto [evaluator, hash] = state_.make_initial_node();
            state_.expand(evaluator, hash, 0, selector, index);
            return;
        }

        for (auto [leaf_index, action] : curr_tour_) {
            if (leaf_index >= 0) {
                // 葉
                state_.move_forward(action);
                auto &[evaluator, hash] = leaves_[leaf_index];
                state_.expand(evaluator, hash, leaf_index, selector, index);
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
vector<Action> beam_search(const Config &config, State &state) {

    auto init_grid = state.grid;
    auto init_balls = state.balls;
    vector<Action> best_ans;
    int best_cost = 1 << 30;
    while (true) {
        Tree tree(state, config);
        // 新しいノード候補の集合
        Selector selector(config);
        int turn = 0;
        while (true) {
            turn++;
            if (turn % 10 == 0) {
                time_keeper.setNowTime();
                if (time_keeper.isTimeOver()) {
                    break;
                }
            }
            // Euler Tourでselectorに候補を追加する
            tree.dfs(selector, state);

            if (selector.have_finished()) {
                break;
            }
            assert(!selector.select().empty());

            // 木を更新する
            tree.update(selector.select());
            selector.clear();
        }
        Candidate best_candidate = selector.calculate_best_candidate();
        dump(best_candidate.evaluator.evaluate());
        if (best_candidate.evaluator.evaluate() < best_cost) {
            best_cost = best_candidate.evaluator.evaluate();
            // dump(turn, best_candidate.evaluator.evaluate());
            vector<Action> ret =
                tree.calculate_path(best_candidate.parent, turn + 1);
            ret.push_back(best_candidate.action);
            best_ans = ret;
        }
        if (time_keeper.isTimeOver()) {
            return best_ans;
        } else {
            state.grid = init_grid;
            state.balls = init_balls;
        }
    }

    return {};
}

} // namespace beam_search

constexpr size_t beam_width = 1000;
constexpr size_t tour_capacity = 16 * beam_width;
constexpr uint32_t hash_map_capacity = 64 * beam_width;

struct Solver {
    Input input;
    Output output;
    const array<string, 4> UDLR_string = {"U", "D", "L", "R"};

    Solver(const Input &input) : input(input) {}

    void solve() {
        vector<pair<int, int>> balls;
        balls.reserve(N * N / 2);
        rep(x, N) {
            rep(y, N) {
                if (input.grid[x][y] > 0) {
                    balls.emplace_back(x, y);
                }
            }
        }

        // vector<vector<int>> block(N, vector<int>(N));
        // rep(x, N) {
        //     rep(y, N) {
        //         if (input.target[x][y] > 0) {
        //             if (0 <= x - 1 and x + 1 < N and
        //                 input.target[x - 1][y] == 0 and
        //                 input.target[x + 1][y] == 0 and 0 <= y - 1 and
        //                 y + 1 < N and input.target[x][y - 1] == 0 and
        //                 input.target[x][y + 1] == 0) {
        //                 if (input.grid[x - 1][y] == 0) {
        //                     output.ans.emplace_back(x - 1, y, "B");
        //                     input.grid[x - 1][y] = -1;
        //                 } else if (input.grid[x - 1][y] == 0) {
        //                     output.ans.emplace_back(x + 1, y, "B");
        //                     input.grid[x + 1][y] = -1;
        //                 }
        //             } else {
        //                 if (0 <= x - 1 and x + 1 < N and
        //                     input.target[x - 1][y] == 0 and
        //                     input.target[x + 1][y] == 0) {
        //                     if (input.grid[x - 1][y] == 0) {
        //                         block[x - 1][y] += 1;
        //                     } else if (input.grid[x - 1][y] == 0) {
        //                         output.ans.emplace_back(x + 1, y, "B");
        //                         block[x + 1][y] += 1;
        //                     }
        //                 }
        //                 if (0 <= y - 1 and y + 1 < N and
        //                     input.target[x][y - 1] == 0 and
        //                     input.target[x][y + 1] == 0) {
        //                     if (input.grid[x][y - 1] == 0) {
        //                         block[x][y - 1] += 1;
        //                     } else if (input.grid[x][y + 1] == 0) {
        //                         block[x][y + 1] += 1;
        //                     }
        //                 }
        //             }
        //         }
        //     }
        // }
        // rep(x, N) {
        //     rep(y, N) {
        //         if (block[x][y] >= 2) {
        //             output.ans.emplace_back(x, y, "B");
        //             input.grid[x][y] = -1;
        //         }
        //     }
        // }

        // auto cmp = [](pair<int, int> x, pair<int, int> y) -> bool {
        //     return abs(x.first - N / 2) + abs(x.second - N / 2) >
        //            abs(y.first - N / 2) + abs(y.second - N / 2);
        // };
        // sort(all(balls), cmp);
        BALLS_NUM = balls.size();
        beam_search::Config config = {static_cast<int>(balls.size()),
                                      beam_width, tour_capacity,
                                      hash_map_capacity};
        beam_search::State state(input, balls);
        vector<beam_search::Action> actions =
            beam_search::beam_search(config, state);

        // make output
        // dump(actions.size());
        output.ans.reserve(balls.size() * 4);
        for (auto action : actions) {
            int x = action.px;
            int y = action.py;
            for (auto cmd : action.decode()) {
                auto [nx, ny] = next_pos(x, y, cmd, input.grid);
                output.ans.emplace_back(x, y, UDLR_string[cmd]);
                int c = input.grid[x][y];
                input.grid[x][y] = 0;
                input.grid[nx][ny] = c;
                x = nx;
                y = ny;
            }
        }
    }

    void print() { output.output(); }
};

int main() {
    time_keeper = TimeKeeperDouble(TIME_LIMIT);
    Input input;
    input.input();
    beam_search::zobrist_hash::make_hash(input);
    Solver solver(input);
    solver.solve();
    solver.print();
    return 0;
}

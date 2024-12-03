#include <atcoder/segtree>
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
TimeKeeperDouble time_keeper(2900);
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
constexpr double TIME_LIMIT = 2950;
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
struct Action_ {
    int p;
    int r;
    string d;
    int b;
    Action_(int p, int r, string d, int b) : p(p), r(r), d(d), b(b) {};
    bool operator==(const Action_ &other) const {
        return (p == other.p and r == other.r and d == other.d and
                b == other.b);
    }
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

using Hash = uint64_t; // TODO

// // 状態遷移を行うために必要な情報
// // メモリ使用量をできるだけ小さくしてください
struct Action {
    int p;
    int r;
    string d;
    int b;

    Action() {
        // TODO
    }

    bool operator==(const Action &other) const {
        // TODO
    }
};

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
        // int p = vertical.size();
        // auto [w, h] = whs[p];
        // rep(r, 2) {
        //     rep(d, 2) {
        //         for (int b = -1; b < (int)vertical.size(); b++) {
        //             auto [W, H] = evaluator;
        //             Action new_action = {p, r, UL[d], b};
        //             auto [u, d, l, r] =
        //                 get_pos(w, h, new_action, vertical, horizon);
        //             new_action.udlr = array<int, 4>{u, d, l, r};
        //             chmax(W, r);
        //             chmax(H, d);
        //             Hash hash = (d << 30) | r;
        //             selector.push(
        //                 Candidate(new_action, Evaluator(W, H), hash, parent),
        //                 false);
        //         }
        //     }
        // }
    }

    // actionを実行して次の状態に遷移する
    void move_forward(Action action) {}

    // actionを実行する前の状態に遷移する
    // 今の状態は、親からactionを実行して遷移した状態である
    void move_backward(Action action) {}

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

struct Output {
    pair<int, int> query(const vector<Action_> &actions) {
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
    pair<int, int> query(const vector<beam_search::Action> &actions) {
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

uint32_t xorshift() {
    static uint32_t y = 2463534242;
    y = y ^ (y << 13);
    y = y ^ (y >> 17);
    return y = y ^ (y << 15);
}
string seed;
struct Solver {
    Input input;
    Output output;
    vector<pair<int, int>> wh;
    vector<Action_> actions;
    int best_wh;
    int lim_wh;
    // vector<int> split;
    int sqrt_;
    int id = 0;
    ll sum_s;
    Solver(const Input &input) : input(input) {
        wh = input.wh;
        sum_s = 0;
        for (auto [w, h] : input.wh) {
            sum_s += (ll)w * (ll)h;
        }
        best_wh = sqrt(sum_s / 0.65);
        lim_wh = sqrt(sum_s / 0.7);
    }
    void make_init_sol() {
        sqrt_ = (int)ceil(sqrt(N));
        actions.reserve(N);
        // rep(i, sqrt_) {
        //     if (i * sqrt_ < N) {
        //         split[i * sqrt_] = 1;
        //     }
        // }
        rep(i, N) {
            if (i % sqrt_ == 0) {
                actions.emplace_back(i, 0, "U", -1);
            } else {
                actions.emplace_back(i, 0, "U", i - 1);
            }
        }
    }
    int evaluate(int lim, const vector<pair<int, int>> &wh) {
        static map<pair<int, int>, int> horizon;
        // static map<pair<int, int>, int> vertical;
        int max_ = 1000000000;
        horizon.clear();
        // vertical.clear();
        horizon[{0, max_}] = 0;
        // vertical[{0, max_}] = 0;

        int prev_r = 0;
        int prev_d = 0;
        int W = 0;
        int H = 0;
        rep(i, N) {
            auto [w, h] = wh[i];
            if (actions[i].r == 1) {
                swap(w, h);
            }
            int l, r, u, d;
            if (actions[i].d == "U") {
                u = 0;
                if (actions[i].b == -1) {
                    l = 0;
                    r = l + w;
                } else {
                    l = prev_r;
                    r = l + w;
                }
                pair<pair<int, int>, int> l_l = {{0, 0}, 0};
                pair<pair<int, int>, int> r_r = {{max_, max_}, 0};

                auto l_ = horizon.lower_bound({l, l});
                l_l = *l_;
                auto r_ = horizon.lower_bound({r, r});
                r_r = *prev(r_);

                for (auto it = l_; it != r_; it++) {
                    chmax(u, (*it).second);
                }

                d = u + h;
                horizon.erase(l_, r_);
                if (l_l.first.first < l) {
                    horizon[{l_l.first.first, l}] = l_l.second;
                }
                horizon[{l, r}] = d;
                if (r < r_r.first.second) {
                    horizon[{r, r_r.first.second}] = r_r.second;
                }
                prev_r = r;

                pair<pair<int, int>, int> u_u = {{0, 0}, 0};
                pair<pair<int, int>, int> d_d = {{max_, max_}, 0};
            }
            // auto u_ = vertical.lower_bound({u, u});
            // u_u = *u_;
            // auto d_ = vertical.lower_bound({d, d});
            // d_d = *prev(d_);
            // vertical.erase(u_, d_);
            // if (u_u.first.first < u) {
            //     vertical[{u_u.first.first, u}] = u_u.second;
            // }
            // vertical[{u, d}] = r;
            // if (d < d_d.first.second) {
            //     vertical[{d, d_d.first.second}] = d_d.second;
            // }
            // } else {
            //     l = 0;
            //     if (actions[i].b == -1) {
            //         u = 0;
            //         d = u + h;
            //     } else {
            //         u = prev_d;
            //         d = u + h;
            //     }
            //     pair<pair<int, int>, int> u_u = {{0, 0}, 0};
            //     pair<pair<int, int>, int> d_d = {{max_, max_}, 0};

            //     auto u_ = vertical.lower_bound({u, u});
            //     u_u = *u_;
            //     auto d_ = vertical.lower_bound({d, d});
            //     d_d = *prev(d_);

            //     for (auto it = u_; it != d_; it++) {
            //         chmax(l, (*it).second);
            //     }

            //     r = l + w;
            //     vertical.erase(u_, d_);
            //     if (u_u.first.first < l) {
            //         vertical[{u_u.first.first, l}] = u_u.second;
            //     }
            //     vertical[{u, d}] = r;
            //     if (d < d_d.first.second) {
            //         vertical[{d, d_d.first.second}] = d_d.second;
            //     }
            //     prev_d = d;

            //     pair<pair<int, int>, int> l_l = {{0, 0}, 0};
            //     pair<pair<int, int>, int> r_r = {{max_, max_}, 0};

            //     auto l_ = horizon.lower_bound({l, l});
            //     l_l = *l_;
            //     auto r_ = horizon.lower_bound({r, r});
            //     r_r = *prev(r_);
            //     horizon.erase(l_, r_);
            //     if (l_l.first.first < l) {
            //         horizon[{l_l.first.first, l}] = l_l.second;
            //     }
            //     horizon[{l, r}] = d;
            //     if (r < r_r.first.second) {
            //         horizon[{r, r_r.first.second}] = r_r.second;
            //     }
            // }

            chmax(W, r);
            chmax(H, d);
            if (W + H > lim) {
                return lim + 1;
            }
        }
        return W + H;
    }
    int sa(int time_lim) {
        int cnt = 0;
        double start_temp = 300;
        double end_temp = 0.0;
        double now_temp = -1.0;
        int now_score = inf;
        int diff_lim = 0;
        while (true) {
            if ((cnt & 63) == 0) {
                time_keeper.setNowTime();
                // now_temp = start_temp + (end_temp - start_temp) *
                //                             time_keeper.getNowTime() /
                //                             TIME_LIMIT;
                // diff_lim = ceil(now_temp * log(xorshift() / double(1ll <<
                // 32)));
                if (time_keeper.getNowTime() > time_lim) {
                    break;
                }
            }
            int mode = xorshift() % 10;
            if (mode <= 1) {
                int index = xorshift() % (N - 1) + 1;
                if (actions[index].b == -1 and mode == 0) {
                    int pm = xorshift() & 1;
                    if (pm == 0) {
                        pm = -1;
                    }
                    if (index + pm < 0 or index + pm >= N) {
                        continue;
                    }
                    if (index + pm >= 0 and
                        actions[index].d != actions[index + pm].d) {
                        continue;
                    }
                    if (index + pm < N and
                        actions[index].d != actions[index + pm].d) {
                        continue;
                    }
                    actions[index].b = index - 1;
                    int memo = actions[index + pm].b;
                    actions[index + pm].b = -1;
                    int lim = now_score + diff_lim;
                    int new_score = evaluate(lim, wh);
                    if (new_score <= lim) {
                        // if (new_score < now_score) {
                        //     cerr << time_keeper.getNowTime() << " " <<
                        //     new_score
                        //          << el;
                        // }
                        now_score = new_score;
                    } else {
                        actions[index].b = -1;
                        actions[index + pm].b = memo;
                    }

                } else {
                    if (actions[index].b == -1 and
                        actions[index - 1].d != actions[index].d) {
                        continue;
                    }
                    int memo;
                    memo = actions[index].b;
                    if (actions[index].b == -1) {
                        actions[index].b = index - 1;
                    } else {
                        actions[index].b = -1;
                    }
                    int lim = now_score + diff_lim;
                    int new_score = evaluate(lim, wh);
                    if (new_score <= lim) {
                        // if (new_score < now_score) {
                        //     cerr << time_keeper.getNowTime() << " " <<
                        //     new_score
                        //          << el;
                        // }
                        now_score = new_score;
                    } else {
                        actions[index].b = memo;
                    }
                }
            } else {
                int index = xorshift() % N;
                actions[index].r ^= 1;
                int lim = now_score + diff_lim;
                int new_score = evaluate(lim, wh);
                if (new_score <= lim) {
                    // if (new_score < now_score) {
                    //     cerr << time_keeper.getNowTime() << " " << new_score
                    //          << el;
                    // }
                    now_score = new_score;
                } else {
                    actions[index].r ^= 1;
                }
            }
            cnt++;
        }
        // dump(cnt);
        return now_score;
    }
    void solve() {
        // vector<pair<int, int>> actual_wh(N);
        // ifstream file("actual/" + seed + ".txt");
        // if (!file) { // ファイルが開けない場合のエラーチェック
        //     cerr << "Error: Could not open the file!" << el;
        //     return;
        // }
        // int x, y;
        // rep(i, N) {
        //     file >> x >> y;
        //     actual_wh[i] = {x, y};
        // }

        int size = 200;
        make_init_sol();
        int time = 2900 / size;
        vector<vector<Action_>> cands;
        vector<pair<int, int>> scores;
        cands.reserve(size);
        vector<int> tmp(N / sqrt_, sqrt_);
        rep(i, N % sqrt_) { tmp[i] += 1; }
        vector<int> sp1;
        sp1.emplace_back(0);
        for (auto i : tmp) {
            sp1.emplace_back(*(sp1.rbegin()) + i);
        }
        vector<double> p = {0.65, 0.8, 0.95};
        rep(i, size) {
            rep(i, N) {
                actions[i].r = xorshift() & 1;
                actions[i].b = i - 1;
            }
            if (xorshift() & 1 == 0) {
                for (auto i : sp1) {
                    if (i < N) {
                        actions[i].b = -1;
                    }
                }
            } else {
                int r = 0;
                best_wh = sqrt(sum_s / p[xorshift() % 3]);
                rep(i, N) {
                    if (actions[i].r == 0) {
                        if (r + wh[i].first <= best_wh) {
                            r += wh[i].first;
                        } else {
                            actions[i].b = -1;
                            r = wh[i].first;
                        }
                    } else {
                        if (r + wh[i].second <= best_wh) {
                            r += wh[i].second;
                        } else {
                            actions[i].b = -1;
                            r = wh[i].second;
                        }
                    }
                }
            }

            // int c = xorshift() % 2;
            // rep(i, c) { actions[xorshift() % N].b = -1; }

            int predicted_score = sa(time * (i + 1));
            cands.emplace_back(actions);
            scores.emplace_back(predicted_score, (int)scores.size());
            // pair<int, int> tmp = output.query(actions);
            // int query_score = tmp.first + tmp.second;
            // int actual_score = evaluate(1000000000, actual_wh);
            // cerr << predicted_score << " " << actual_score << " " <<
            // query_score
            //      << el;
        }
        sort(all(scores));
        int cnt = 0;
        int i = -1;
        while (cnt < T) {
            i++;
            if (i % (int)scores.size() > 0 and
                scores[i % (int)scores.size()].first ==
                    scores[i % (int)scores.size() - 1].first) {
                continue;
            }
            cnt++;
            pair<int, int> tmp =
                output.query(cands[scores[i % (int)scores.size()].second]);
            // int query_score = tmp.first + tmp.second;
            // actions = cands[scores[i % (int)scores.size()].second];
            // int actual_score = evaluate(1000000000, actual_wh);
            // int predicted_score = scores[i % (int)scores.size()].first;
            // cerr << predicted_score << " " << actual_score << " " <<
            // query_score
            //      << el;
            // cerr << (predicted_score < query_score) << el;
        }
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
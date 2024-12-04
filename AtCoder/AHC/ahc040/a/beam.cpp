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
int best_len;
const array<string, 2> UL = {"U", "L"};
struct Input {
    vector<pii> wh;
    void input() {
        cin >> N >> T >> Sig;
        wh.resize(N);
        rep(i, N) {
            int w, h;
            cin >> w >> h;
            chmin(w, 100000);
            chmax(w, 10000);
            chmin(h, 100000);
            chmax(h, 10000);
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

using Hash = uint32_t; // TODO

// 状態遷移を行うために必要な情報
// メモリ使用量をできるだけ小さくしてください
struct Action {
    int p;
    int r;
    string d;
    int b;
    vector<pair<pair<int, int>, pair<int, int>>> dell_h;
    vector<pair<pair<int, int>, pair<int, int>>> add_h;
    vector<pair<pair<int, int>, pair<int, int>>> dell_v;
    vector<pair<pair<int, int>, pair<int, int>>> add_v;

    Action(int p, int r, string d, int b,
           vector<pair<pair<int, int>, pair<int, int>>> dell_h,
           vector<pair<pair<int, int>, pair<int, int>>> add_h,
           vector<pair<pair<int, int>, pair<int, int>>> dell_v,
           vector<pair<pair<int, int>, pair<int, int>>> add_v)
        : p(p), r(r), d(d), b(b), dell_h(dell_h), add_h(add_h), dell_v(dell_v),
          add_v(add_v) {}

    bool operator==(const Action &other) const {
        return p == other.p and b == other.b and r == other.r and d == other.d;
    }
};
using Cost = int;

// 状態のコストを評価するための構造体
// メモリ使用量をできるだけ小さくしてください
// struct Evaluator {
//     int w;
//     int h;
//     int cant_use;

//     Evaluator(int w, int h, int cant_use) : w(w), h(h), cant_use(cant_use) {}

//     // 低いほどよい
//     Cost evaluate() const {
//         return max(0, h - best_len) + max(0, w - best_len) +
//                (int)sqrt(cant_use);
//     }
// };
struct Evaluator {
    int w;
    int h;

    Evaluator(int w, int h) : w(w), h(h) {}

    // 低いほどよい
    Cost evaluate() const { return w + h + (int)(sqrt((ll)w * (ll)h)); }
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
        // hash使わないけど、消し方分かんないから、乱数割り当てるか...
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
    explicit State(const vector<pair<int, int>> &wh) : wh(wh) {
        max_ = 1000000000;
        vertical[{0, max_}] = {0, -1};
        horizon[{0, max_}] = {0, -1};
        turn = 0;
    }

    // EvaluatorとHashの初期値を返す
    pair<Evaluator, Hash> make_initial_node() { return {{0, 0}, 0}; }

    void add(vector<pair<pair<int, int>, pair<int, int>>> &vh,
             const pair<pair<int, int>, pair<int, int>> &x) {
        auto rb = vh.rbegin();
        if (not vh.empty() and rb->first.second == x.first.first and
            rb->second == x.second) {
            rb->first.second = x.first.second;
        } else {
            vh.emplace_back(x);
        }
    }
    void
    make_add_dell(const map<pair<int, int>, pair<int, int>> &vh,
                  const map<pair<int, int>, pair<int, int>> &other_vh,
                  vector<pair<pair<int, int>, pair<int, int>>> &add_vh,
                  vector<pair<pair<int, int>, pair<int, int>>> &dell_vh,
                  vector<pair<pair<int, int>, pair<int, int>>> &other_add_vh,
                  vector<pair<pair<int, int>, pair<int, int>>> &other_dell_vh,
                  int lower, int upper, int &other_lower, int &other_upper,
                  int len) {
        {
            auto start_it = vh.lower_bound({lower, lower});
            auto end_it = vh.lower_bound({upper, upper});

            for (auto it = start_it; it != end_it; it++) {
                dell_vh.emplace_back(*it);
                chmax(other_lower, (*it).second.first);
            }
            other_upper = other_lower + len;
            add_vh.emplace_back(make_pair(lower, upper),
                                make_pair(other_upper, turn));
            if (start_it->first.first < lower) {
                add_vh.emplace_back(make_pair(start_it->first.first, lower),
                                    start_it->second);
            }
            auto prev_end = *prev(end_it);
            if (upper < prev_end.first.second) {
                add_vh.emplace_back(make_pair(upper, prev_end.first.second),
                                    prev_end.second);
            }
        }
        {
            auto start_it = other_vh.lower_bound({other_lower, other_lower});
            auto end_it = other_vh.lower_bound({other_upper, other_upper});
            for (auto it = start_it; it != end_it; it++) {
                if ((*it).second.first <= upper) {
                    other_dell_vh.emplace_back(*it);

                    if (other_lower <= it->first.first and
                        it->first.second <= other_upper) {
                        add(other_add_vh, {it->first, {upper, turn}});

                    } else if (it->first.first < other_lower and
                               other_upper < it->first.second) {
                        add(other_add_vh,
                            {{it->first.first, other_lower}, it->second});
                        add(other_add_vh,
                            {{other_lower, other_upper}, {upper, turn}});
                        add(other_add_vh,
                            {{other_upper, it->first.second}, it->second});

                    } else if (other_lower <= it->first.first) {
                        add(other_add_vh,
                            {{it->first.first, other_upper}, {upper, turn}});
                        add(other_add_vh,
                            {{other_upper, it->first.second}, it->second});

                    } else if (it->first.second <= other_upper) {
                        add(other_add_vh,
                            {{it->first.first, other_lower}, it->second});
                        add(other_add_vh,
                            {{other_lower, it->first.second}, {upper, turn}});
                    } else {
                        runtime_error("bug");
                    }
                }
            }
        }
    }
    // 次の状態候補を全てselectorに追加する
    // 引数
    //   evaluator : 今の評価器
    //   hash      : 今のハッシュ値
    //   parent    : 今のノードID（次のノードにとって親となる）
    void expand(const Evaluator &evaluator, Hash hash, int parent,
                Selector &selector) {
        auto [w, h] = wh[turn];
        static vector<pair<pair<int, int>, pair<int, int>>> dell_h;
        static vector<pair<pair<int, int>, pair<int, int>>> add_h;
        static vector<pair<pair<int, int>, pair<int, int>>> dell_v;
        static vector<pair<pair<int, int>, pair<int, int>>> add_v;
        rep(i, 2) {
            for (auto [key, value] : horizon) {
                auto [W, H] = evaluator;
                if (value.second == -1) {
                    continue;
                }

                int l, r, u, d;
                auto [l_, r_] = key;
                auto [d_, b] = value;
                l = r_;
                r = l + w;
                u = 0;
                dell_h.clear();
                dell_v.clear();
                add_h.clear();
                add_v.clear();
                make_add_dell(horizon, vertical, add_h, dell_h, add_v, dell_v,
                              l, r, u, d, h);
                chmax(W, r);
                chmax(H, d);
                Action new_action =
                    Action(turn, i, "U", b, dell_h, add_h, dell_v, add_v);
                selector.push(
                    Candidate(new_action, Evaluator(W, H), xorshift(), parent),
                    false);
            }
            {
                auto [W, H] = evaluator;
                int l, r, u, d;
                l = 0;
                r = l + w;
                u = 0;
                dell_h.clear();
                dell_v.clear();
                add_h.clear();
                add_v.clear();
                make_add_dell(horizon, vertical, add_h, dell_h, add_v, dell_v,
                              l, r, u, d, h);
                chmax(W, r);
                chmax(H, d);
                Action new_action =
                    Action(turn, i, "U", -1, dell_h, add_h, dell_v, add_v);
                selector.push(
                    Candidate(new_action, Evaluator(W, H), xorshift(), parent),
                    false);
            } // 下からの挿入

            for (auto [key, value] : vertical) {
                if (value.second == -1) {
                    continue;
                }
                auto [W, H] = evaluator;
                int l, r, u, d;
                auto [u_, d_] = key;
                auto [r_, b] = value;
                u = d_;
                d = u + h;
                l = 0;
                dell_h.clear();
                dell_v.clear();
                add_h.clear();
                add_v.clear();
                make_add_dell(vertical, horizon, add_v, dell_v, add_h, dell_h,
                              u, d, l, r, w);
                chmax(W, r);
                chmax(H, d);
                Action new_action =
                    Action(turn, i, "L", b, dell_h, add_h, dell_v, add_v);
                selector.push(
                    Candidate(new_action, Evaluator(W, H), xorshift(), parent),
                    false);
            }
            {
                auto [W, H] = evaluator;
                int l, r, u, d;
                u = 0;
                d = u + h;
                l = 0;
                dell_h.clear();
                dell_v.clear();
                add_h.clear();
                add_v.clear();
                make_add_dell(vertical, horizon, add_v, dell_v, add_h, dell_h,
                              u, d, l, r, w);
                chmax(W, r);
                chmax(H, d);
                Action new_action =
                    Action(turn, i, "L", -1, dell_h, add_h, dell_v, add_v);
                selector.push(
                    Candidate(new_action, Evaluator(W, H), xorshift(), parent),
                    false);
            } // 右からの挿入
            swap(w, h);
        }
    }

    // actionを実行して次の状態に遷移する
    void move_forward(const Action &action) {
        turn++;
        // dump(action.add_v);
        // dump(action.dell_v);
        // dump(action.add_h);
        // dump(action.dell_h);
        // dump(vertical);
        // dump(horizon);

        for (auto [key, value] : action.dell_v) {
            vertical.erase(key);
        }
        for (auto [key, value] : action.add_v) {
            vertical[key] = value;
        }

        for (auto [key, value] : action.dell_h) {
            horizon.erase(key);
        }
        for (auto [key, value] : action.add_h) {
            horizon[key] = value;
        }

        // dump(vertical);
        // dump(horizon);
        for (auto it = vertical.begin(); it != vertical.end(); it++) {
            assert(it == vertical.begin() or
                   prev(it)->first.second == it->first.first);
        }
        for (auto it = horizon.begin(); it != horizon.end(); it++) {
            assert(it == horizon.begin() or
                   prev(it)->first.second == it->first.first);
        }
    }

    // actionを実行する前の状態に遷移する
    // 今の状態は、親からactionを実行して遷移した状態である
    void move_backward(const Action &action) {
        turn--;
        // dump(action.add_v);
        // dump(action.dell_v);
        // dump(action.add_h);
        // dump(action.dell_h);
        // dump(vertical);
        // dump(horizon);
        for (auto [key, value] : action.add_v) {
            vertical.erase(key);
        }
        for (auto [key, value] : action.dell_v) {
            vertical[key] = value;
        }
        for (auto [key, value] : action.add_h) {
            horizon.erase(key);
        }
        for (auto [key, value] : action.dell_h) {
            horizon[key] = value;
        }
        // dump(vertical);
        // dump(horizon);
        for (auto it = vertical.begin(); it != vertical.end(); it++) {
            assert(it == vertical.begin() or
                   prev(it)->first.second == it->first.first);
        }
        for (auto it = horizon.begin(); it != horizon.end(); it++) {
            assert(it == horizon.begin() or
                   prev(it)->first.second == it->first.first);
        }
    }

  private:
    map<pair<int, int>, pair<int, int>> vertical;
    map<pair<int, int>, pair<int, int>> horizon;
    vector<pair<int, int>> wh;
    int turn;
    int max_;
    int lim;
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
            cout << "#" << best_candidate.evaluator.w << " "
                 << best_candidate.evaluator.h << el;
            cerr << "#" << best_candidate.evaluator.w << " "
                 << best_candidate.evaluator.h << el;
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
constexpr size_t beam_width = 5000;
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
constexpr double kSqrt2 = 1.41421356237309514547;

inline double calc_norm_cdf(double mu, double sigma, double x) {
    return 0.5 * (1.0 + erf((x - mu) / (kSqrt2 * sigma)));
}

inline double calc_pr(double mu, double sigma, double vs) {
    return calc_norm_cdf(mu, sigma, vs + 0.5) -
           calc_norm_cdf(mu, sigma, vs - 0.5);
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
        best_len = sqrt(sum_s / 0.9);
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
        static vector<int> r_vec;
        // static map<pair<int, int>, int> vertical;
        int max_ = 1000000000;
        horizon.clear();
        r_vec.clear();
        // vertical.clear();
        horizon[{0, max_}] = 0;
        // vertical[{0, max_}] = 0;

        // int prev_d = 0;
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
                    l = r_vec[actions[i].b];
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
                r_vec.emplace_back(r);
            }

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
        int now_score = inf;
        int diff_lim = 0;
        // static vector<pair<int, int>> cand;
        // cand.reserve(N);
        while (true) {
            if ((cnt & 63) == 0) {
                time_keeper.setNowTime();
                if (time_keeper.getNowTime() > time_lim) {
                    break;
                }
            }
            int mode = xorshift() % 15;
            if (mode == 0) {
                int index = xorshift() % (N - 1) + 1;
                if (actions[index].b == -1) {
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
                        if (new_score < now_score) {
                            cerr << "1 " << time_keeper.getNowTime() << " "
                                 << new_score << el;
                        }
                        now_score = new_score;
                    } else {
                        actions[index].b = -1;
                        actions[index + pm].b = memo;
                    }
                } else {
                    if (Sig > 2000) {
                        continue;
                    }
                    int cnt = 0;
                    int i = index;
                    int memo1 = actions[index].b;
                    actions[index].b = actions[index - 1].b;
                    int memo2 = -1;
                    if (index + 1 < N) {
                        memo2 = actions[index + 1].b;
                    }
                    if (memo2 == index) {
                        actions[index + 1].b = index - xorshift() % 2;
                    }

                    int lim = now_score + diff_lim;
                    int new_score = evaluate(lim, wh);
                    if (new_score <= lim) {
                        if (new_score < now_score) {
                            cerr << "2 " << time_keeper.getNowTime() << " "
                                 << new_score << el;
                        }
                        now_score = new_score;
                    } else {
                        actions[index].b = memo1;
                        if (index + 1 < N) {
                            actions[index + 1].b = memo2;
                        }
                    }
                }
            } else if (false and mode == 1) {
                continue;
                int index = xorshift() % (N - 1) + 1;
                int memo = actions[index].b;
                if (actions[index].b == -1) {
                    actions[index].b = index - 1;
                } else {
                    actions[index].b = -1;
                }

                int lim = now_score + diff_lim;
                int new_score = evaluate(lim, wh);
                if (new_score <= lim) {
                    if (new_score < now_score) {
                        cerr << "4 " << time_keeper.getNowTime() << " "
                             << new_score << el;
                    }
                    now_score = new_score;
                } else {
                    actions[index].b = memo;
                }
            } else {
                int index = xorshift() % N;
                actions[index].r ^= 1;
                int lim = now_score + diff_lim;
                int new_score = evaluate(lim, wh);
                if (new_score <= lim) {
                    if (new_score < now_score) {
                        cerr << "3 " << time_keeper.getNowTime() << " "
                             << new_score << el;
                    }
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

    bool trans(vector<Action_> &actions) {
        // 右端のものを左スライドに変更してスコアが改善する可能性があるかを判定
        vector<int> tmp(1, N);
        rep(i, N) {
            if (actions[i].b != -1) {
                tmp[actions[i].b] = 0;
            }
        }

        for (auto i : tmp) {
            actions[i].d = "L";
        }
    }
    void solve() {
        vector<vector<Action_>> queryes;
        queryes.reserve(T);
        vector<tuple<int, int, int>> results;
        results.reserve(T);

        vector<vector<pair<int, int>>> tmp_wh_vec(N);
        rep(i, N) { tmp_wh_vec[i].emplace_back(wh[i]); }
        rep(i, T - 1) {
            auto tmp = output.query({Action_(i % N, 0, "U", -1)});
            chmin(tmp.first, 100000);
            chmax(tmp.first, 10000);
            chmin(tmp.second, 100000);
            chmax(tmp.second, 10000);
            tmp_wh_vec[i % N].emplace_back(tmp);
            queryes.push_back({Action_(i % N, 0, "U", -1)});
            results.emplace_back(1000000000, 1000000000, results.size());
        }
        vector<pair<int, int>> tmp_wh(N);
        rep(i, N) {
            for (auto [w, h] : tmp_wh_vec[i]) {
                tmp_wh[i].first += w;
                tmp_wh[i].second += h;
            }
            tmp_wh[i].first /= tmp_wh_vec[i].size();
            tmp_wh[i].second /= tmp_wh_vec[i].size();
        }
        wh = tmp_wh;

        beam_search::State state = beam_search::State(input.wh);
        beam_search::Config config = {N, beam_width, tour_capacity,
                                      hash_map_capacity};

        vector<beam_search::Action> a = beam_search::beam_search(config, state);
        output.query(a);
        return;

        //     // vector<pair<int, int>> actual_wh(N);
        //     // ifstream file("actual/" + seed + ".txt");
        //     // if (!file) { // ファイルが開けない場合のエラーチェック
        //     //     cerr << "Error: Could not open the file!" << el;
        //     //     return;
        //     // }
        //     // int x, y;
        //     // rep(i, N) {
        //     //     file >> x >> y;
        //     //     actual_wh[i] = {x, y};
        //     // }

        //     vector<vector<Action_>> queryes;
        //     queryes.reserve(T);
        //     vector<tuple<int, int, int>> results;
        //     results.reserve(T);

        //     vector<vector<pair<int, int>>> tmp_wh_vec(N);
        //     rep(i, N) { tmp_wh_vec[i].emplace_back(wh[i]); }
        //     rep(i, T - 100) {
        //         auto tmp = output.query({Action_(i % N, 0, "U", -1)});
        //         chmin(tmp.first, 100000);
        //         chmax(tmp.first, 10000);
        //         chmin(tmp.second, 100000);
        //         chmax(tmp.second, 10000);
        //         tmp_wh_vec[i % N].emplace_back(tmp);
        //         queryes.push_back({Action_(i % N, 0, "U", -1)});
        //         results.emplace_back(1000000000, 1000000000, results.size());
        //     }
        //     vector<pair<int, int>> tmp_wh(N);
        //     rep(i, N) {
        //         for (auto [w, h] : tmp_wh_vec[i]) {
        //             tmp_wh[i].first += w;
        //             tmp_wh[i].second += h;
        //         }
        //         tmp_wh[i].first /= tmp_wh_vec[i].size();
        //         tmp_wh[i].second /= tmp_wh_vec[i].size();
        //     }
        //     wh = tmp_wh;

        //     int size = 200;
        //     make_init_sol();
        //     int time = 2900 / size;
        //     vector<vector<Action_>> cands;
        //     vector<pair<int, int>> scores;
        //     cands.reserve(size);
        //     vector<int> tmp(N / sqrt_, sqrt_);
        //     rep(i, N % sqrt_) { tmp[i] += 1; }
        //     vector<int> sp1;
        //     sp1.emplace_back(0);
        //     for (auto i : tmp) {
        //         sp1.emplace_back(*(sp1.rbegin()) + i);
        //     }
        //     vector<double> p = {0.65, 0.8, 0.95};
        //     rep(i, size) {
        //         rep(i, N) {
        //             actions[i].r = xorshift() & 1;
        //             actions[i].b = i - 1;
        //         }
        //         if ((xorshift() & 1) == 0) {
        //             for (auto i : sp1) {
        //                 if (i < N) {
        //                     actions[i].b = -1;
        //                 }
        //             }
        //         } else {
        //             int r = 0;
        //             best_wh = sqrt(sum_s / p[xorshift() % 3]);
        //             rep(i, N) {
        //                 if (actions[i].r == 0) {
        //                     if (r + wh[i].first <= best_wh) {
        //                         r += wh[i].first;
        //                     } else {
        //                         actions[i].b = -1;
        //                         r = wh[i].first;
        //                     }
        //                 } else {
        //                     if (r + wh[i].second <= best_wh) {
        //                         r += wh[i].second;
        //                     } else {
        //                         actions[i].b = -1;
        //                         r = wh[i].second;
        //                     }
        //                 }
        //             }
        //         }

        //         // int c = xorshift() % 2;
        //         // rep(i, c) { actions[xorshift() % N].b = -1; }

        //         int predicted_score = sa(time * (i + 1));
        //         cands.emplace_back(actions);
        //         scores.emplace_back(predicted_score, (int)scores.size());
        //         // pair<int, int> tmp = output.query(actions);
        //         // int query_score = tmp.first + tmp.second;
        //         // int actual_score = evaluate(1000000000, actual_wh);
        //         // cerr << predicted_score << " " << actual_score << " " <<
        //         // query_score
        //         //      << el;
        //     }
        //     sort(all(scores));

        //     int best_score = inf;
        //     rep(i, size) {
        //         if (i % (int)scores.size() > 0 and
        //             scores[i % (int)scores.size()].first ==
        //                 scores[i % (int)scores.size() - 1].first) {
        //             continue;
        //         }
        //         if (scores[i].first < best_score + (double)Sig) {
        //             pair<int, int> tmp =
        //             output.query(cands[scores[i].second]); chmin(best_score,
        //             tmp.first + tmp.second);
        //             queryes.emplace_back(cands[scores[i].second]);
        //             results.emplace_back(tmp.first, tmp.second,
        //             results.size());
        //         }
        //         if (queryes.size() >= T) {
        //             break;
        //         }

        //         // int query_score = tmp.first + tmp.second;
        //         // actions = cands[scores[i % (int)scores.size()].second];
        //         // int actual_score = evaluate(1000000000, actual_wh);
        //         // int predicted_score = scores[i %
        //         (int)scores.size()].first;
        //         // cout << "#" << predicted_score << el;
        //         // cerr << predicted_score << " " << actual_score << " " <<
        //         // query_score
        //         //      << el;
        //         // cerr << (predicted_score < query_score) << el;
        //     }
        //     cerr << "query_times: " << queryes.size() << el;
        //     sort(all(results), [](tuple<int, int, int> a, tuple<int, int,
        //     int> b) {
        //         return (get<0>(a) + get<1>(a) < get<0>(b) + get<1>(b));
        //     });
        //     auto best_ans = queryes[get<2>(results[0])];
        //     int W = get<0>(results[0]);
        //     int H = get<1>(results[0]);
        //     int cnt = queryes.size();
        //     while (cnt < T) {
        //         int index = xorshift() % N;
        //         int w = wh[index].first;
        //         int h = wh[index].second;
        //         if (actions[index].r == 1) {
        //             swap(w, h);
        //         }
        //         if (W < H and ((double)h * 2 < (double)w)) {
        //             continue;
        //         }
        //         if (H < W and ((double)w * 2 < (double)h)) {
        //             continue;
        //         }
        //         best_ans[index].r ^= 1;
        //         auto [new_w, new_h] = output.query(best_ans);
        //         cnt++;
        //         if (new_w + new_h < W + H) {
        //             W = new_w;
        //             H = new_h;
        //         } else {
        //             best_ans[index].r ^= 1;
        //         }
        //     };
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
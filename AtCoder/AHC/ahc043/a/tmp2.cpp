#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
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
// --- 定数とグローバル変数 ---
const int STATION_COST = 5000;
const int LINE_COST = 100;
const int TIME_LIMIT = 2950;
int N, M, K, T;
int MAX_SCORE = 0;
// dxy: マンハッタン距離2以内の全オフセット
vector<pair<int, int>> dxy;
// dxy4: 上下左右
vector<pair<int, int>> dxy4 = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
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
    int idx1;
    int idx2;
    int g;
    Action() : idx1(0), idx2(0), g(0) {} // ← デフォルトコンストラクタを追加
    Action(int idx1, int idx2, int g) : idx1(idx1), idx2(idx2), g(g) {
        // TODO
    }

    bool operator==(const Action &other) const {
        return idx1 == other.idx1 and idx2 == other.idx2 and g == other.g;
    }
};
// using Action = int;
using Cost = double;

// 状態のコストを評価するための構造体
// メモリ使用量をできるだけ小さくしてください
struct Evaluator {
    int score_a_day;
    int now_turn;
    int now_K;
    Evaluator() : score_a_day(0), now_turn(0), now_K(0) {}
    Evaluator(int score_a_day, int now_turn, int now_K)
        : score_a_day(score_a_day), now_turn(now_turn), now_K(now_K) {}
    // TODO

    // 低いほどよい
    Cost evaluate() const {
        // TODO
        return -(double)score_a_day / now_turn;
    }
};

// 展開するノードの候補を表す構造体
struct Candidate {
    Action action;
    Evaluator evaluator;
    Hash hash;
    int parent;
    Candidate() = default; // 追加
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
            if (finished_candidates_map_.find(candidate.evaluator.evaluate()) ==
                finished_candidates_map_.end()) {
                finished_candidates_map_[candidate.evaluator.evaluate()] =
                    candidate;
            }
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
    bool have_finished() const { return !finished_candidates_map_.empty(); }

    // 実行可能解に到達するCandidateを返す
    vector<Candidate> get_finished_candidates() const {
        vector<Candidate> finished_candidates_;
        finished_candidates_.reserve(finished_candidates_map_.size());
        for (auto &[key, value] : finished_candidates_map_) {
            finished_candidates_.push_back(value);
        }
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
        finished_candidates_map_.clear();

        full_ = false;
    }

  private:
    static pair<Cost, int> op(pair<Cost, int> a, pair<Cost, int> b) {
        return (a.first >= b.first) ? a : b;
    }

    static pair<Cost, int> e() {
        return make_pair(-numeric_limits<Cost>::max(), -1);
    }

    using MaxSegtree = atcoder::segtree<pair<Cost, int>, &op, &e>;
    size_t beam_width;
    vector<Candidate> candidates_;
    HashMap<Hash, int> hash_to_index_;
    bool full_;
    vector<pair<Cost, int>> costs_;
    MaxSegtree st_;
    unordered_map<Cost, Candidate> finished_candidates_map_;
};

// 深さ優先探索に沿って更新する情報をまとめたクラス
class State {
  public:
    explicit State(const vector<pair<int, int>> &need_ijs,
                   const vector<vector<vector<pair<int, int>>>> &people)
        : need_ijs(need_ijs), people(people) {
        zobrist_hash = vector<vector<Hash>>(N, vector<Hash>(N));
        included = vector<vector<int>>(N, vector<int>(N, 0));
        visited = vector<vector<int>>(N, vector<int>(N, 0));
        rep(i, N) {
            rep(j, N) { zobrist_hash[i][j] = xorshift64(); }
        }
        gain.push_back(K);
    }

    // EvaluatorとHashの初期値を返す
    pair<Evaluator, Hash> make_initial_node() {
        // TODO
        return {Evaluator(0, 0, K), 0};
    }
    int get_dis(int ni, int nj) {
        // 必要な路線の長さ
        int res = 1e9;
        for (auto [i, j] : stations) {
            chmin(res, abs(i - ni) + abs(j - nj) - 1);
        }
        return res;
    }
    pair<int, int> calc_add_score_and_update_hash(int ni, int nj, Hash &hash) {
        // (ni,nj)に駅を設置することによる利得
        int res1 = 0;
        int res2 = 0;
        for (auto [dx, dy] : dxy) {
            int nx = ni + dx;
            int ny = nj + dy;
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                if (included[nx][ny] == 0 and !people[nx][ny].empty()) {
                    hash ^= zobrist_hash[nx][ny];
                    for (auto &pr : people[nx][ny]) {
                        int p = pr.first, q = pr.second;
                        if (included[p][q] > 0) {
                            res1 += abs(nx - p) + abs(ny - q);
                        } else {
                            res2 += abs(nx - p) + abs(ny - q);
                        }
                    }
                }
            }
        }
        return {res1, res2};
    }
    int calc_need_turn(const Evaluator &evaluator, int dis) {
        if (evaluator.score_a_day == 0) {
            return dis + 1;
        }

        int res = max(dis + 1,
                      (int)ceil((double)max(0, STATION_COST + LINE_COST * dis -
                                                   evaluator.now_K) /
                                (double)evaluator.score_a_day));
        return res;
    }
    // 次の状態候補を全てselectorに追加する
    // 引数
    //   evaluator : 今の評価器
    //   hash      : 今のハッシュ値
    //   parent    : 今のノードID（次のノードにとって親となる）
    void expand(const Evaluator &evaluator, Hash hash, int parent,
                Selector &selector) {
        if (stations.empty()) {
            rep(idx1, (int)need_ijs.size()) {
                for (int idx2 = idx1 + 1; idx2 < need_ijs.size(); idx2++) {
                    auto [i, j] = need_ijs[idx1];
                    auto [ii, jj] = need_ijs[idx2];
                    int dis = abs(i - ii) + abs(j - jj) - 1;
                    int need_turn = dis + 2;
                    if (dis * LINE_COST + STATION_COST * 2 > K) {
                        continue;
                    }
                    Hash n_hash = hash;
                    int tmp = 0;
                    vector<pair<int, int>> cands;
                    for (auto &[dx, dy] : dxy) {
                        int nx = i + dx;
                        int ny = j + dy;
                        if (0 <= nx and nx < N and 0 <= ny and ny < N and
                            !people[nx][ny].empty()) {
                            cands.push_back({nx, ny});
                        }
                    }
                    for (auto &[dx, dy] : dxy) {
                        int nx = ii + dx;
                        int ny = jj + dy;
                        if (0 <= nx and nx < N and 0 <= ny and ny < N and
                            !people[nx][ny].empty()) {
                            for (auto [p, q] : people[nx][ny]) {
                                if (find(cands.begin(), cands.end(),
                                         make_pair(p, q)) != cands.end()) {
                                    tmp += abs(nx - p) + abs(ny - q);
                                }
                            }
                        }
                    }

                    int add_score = tmp;
                    if (add_score == 0) {
                        continue;
                    }

                    // assert(tmp == add_score);

                    set<pair<int, int>> cand;
                    for (auto &[dx, dy] : dxy) {
                        {
                            int nx = i + dx;
                            int ny = j + dy;
                            if (0 <= nx and nx < N and 0 <= ny and ny < N and
                                !people[nx][ny].empty()) {
                                cand.insert({nx, ny});
                            }
                        }
                        {
                            int nx = ii + dx;
                            int ny = jj + dy;
                            if (0 <= nx and nx < N and 0 <= ny and ny < N and
                                !people[nx][ny].empty()) {
                                cand.insert({nx, ny});
                            }
                        }
                    }
                    for (auto &[x, y] : cand) {
                        n_hash ^= zobrist_hash[x][y];
                    }
                    Evaluator n_evaluator = Evaluator(
                        evaluator.score_a_day + add_score,
                        evaluator.now_turn + need_turn,
                        evaluator.now_K - 2 * STATION_COST - LINE_COST * dis);
                    Action n_action =
                        Action(idx1, idx2,
                               (T - n_evaluator.now_turn) * add_score -
                                   STATION_COST * 2 - LINE_COST * dis);
                    selector.push(
                        Candidate(n_action, n_evaluator, n_hash, parent),
                        false);
                }
            }
        } else {
            rep(idx, (int)need_ijs.size()) {
                auto [i, j] = need_ijs[idx];
                if (visited[i][j]) {
                    continue;
                }
                Hash n_hash = hash;
                auto [add_score, sub_score] =
                    calc_add_score_and_update_hash(i, j, n_hash);
                if (add_score + sub_score == 0) {
                    continue;
                }
                int dis = get_dis(i, j);

                if (evaluator.score_a_day == 0 and
                    evaluator.now_K - STATION_COST < LINE_COST * dis) {
                    continue;
                }
                int need_turn = calc_need_turn(evaluator, dis);

                Evaluator n_evaluator =
                    Evaluator(evaluator.score_a_day + add_score,
                              evaluator.now_turn + need_turn,
                              evaluator.now_K - STATION_COST - LINE_COST * dis +
                                  evaluator.score_a_day * need_turn);
                Action n_action =
                    Action(idx, -1,
                           (T - n_evaluator.now_turn) * add_score -
                               STATION_COST - LINE_COST * dis);
                assert(dis <= need_turn);
                assert(n_evaluator.score_a_day <= MAX_SCORE);
                assert(n_evaluator.now_K >= 0);
                if (n_evaluator.now_turn >= 800 or
                    n_evaluator.score_a_day == MAX_SCORE) {
                    if (gain.size() <= 5) {
                        continue;
                    }
                    dump(dis, need_turn);
                    dump(n_hash, n_evaluator.score_a_day, n_evaluator.now_turn,
                         n_evaluator.now_K, n_evaluator.evaluate());
                    n_evaluator.now_turn = 1;
                    n_evaluator.score_a_day = 0;
                    int tmp = 0;
                    n_hash = hash;

                    for (auto g : gain) {
                        tmp += g;
                        chmax(n_evaluator.score_a_day, tmp);
                    }

                    dump(stations);
                    dump(gain);
                    dump(n_hash, n_evaluator.score_a_day, n_evaluator.now_turn,
                         n_evaluator.evaluate());
                    // for (int index = best_index + 1; index < stations.size();
                    //      index++) {
                    //     n_hash ^= zobrist_hash[stations[index].first]
                    //                           [stations[index].second];
                    // }
                    selector.push(
                        Candidate(n_action, n_evaluator, n_hash, parent), true);
                    break;
                } else {
                    selector.push(
                        Candidate(n_action, n_evaluator, n_hash, parent),
                        false);
                }
            }
        }
    }

    // actionを実行して次の状態に遷移する
    void move_forward(Action action) {
        auto [idx1, idx2, g] = action;
        auto [i, j] = need_ijs[idx1];
        stations.emplace_back(i, j);
        visited[i][j] = 1;
        for (auto [dx, dy] : dxy) {
            int nx = i + dx;
            int ny = j + dy;
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                included[nx][ny] += 1;
            }
        }
        if (idx2 != -1) {
            auto [i, j] = need_ijs[idx2];
            stations.emplace_back(i, j);
            visited[i][j] = 1;
            for (auto [dx, dy] : dxy) {
                int nx = i + dx;
                int ny = j + dy;
                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    included[nx][ny] += 1;
                }
            }
        }
        gain.push_back(g);
    }

    // actionを実行する前の状態に遷移する
    // 今の状態は、親からactionを実行して遷移した状態である
    void move_backward(Action action) {
        auto [idx1, idx2, g] = action;
        auto [i, j] = need_ijs[idx1];
        stations.pop_back();
        visited[i][j] = 0;
        for (auto [dx, dy] : dxy) {
            int nx = i + dx;
            int ny = j + dy;
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                included[nx][ny] -= 1;
            }
        }
        if (idx2 != -1) {
            auto [i, j] = need_ijs[idx2];
            stations.pop_back();
            visited[i][j] = 0;
            for (auto [dx, dy] : dxy) {
                int nx = i + dx;
                int ny = j + dy;
                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    included[nx][ny] -= 1;
                }
            }
        }
        gain.pop_back();
    }

  private:
    // TODO
    vector<vector<int>> included;
    vector<vector<int>> visited;
    vector<int> gain;
    vector<pair<int, int>> need_ijs;
    vector<vector<vector<pair<int, int>>>> people;
    vector<vector<Hash>> zobrist_hash;
    vector<pair<int, int>> stations;
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
                curr_tour_.emplace_back((int)leaves_.size(), candidate.action);
                leaves_.emplace_back(candidate.evaluator, candidate.hash);
            }
            return;
        }

        for (const Candidate &candidate : candidates) {
            buckets_[candidate.parent].emplace_back(
                candidate.action, candidate.evaluator, candidate.hash);
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
                next_tour_.emplace_back(-1, action);
                for (auto [new_action, evaluator, hash] :
                     buckets_[leaf_index]) {
                    int new_leaf_index = leaves_.size();
                    next_tour_.emplace_back(new_leaf_index, new_action);
                    leaves_.emplace_back(evaluator, hash);
                }
                buckets_[leaf_index].clear();
                next_tour_.emplace_back(-2, action);
            } else if (leaf_index == -1) {
                // 前進辺
                next_tour_.emplace_back(-1, action);
            } else {
                // 後退辺
                auto [old_leaf_index, old_action] = next_tour_.back();
                if (old_leaf_index == -1) {
                    next_tour_.pop_back();
                } else {
                    next_tour_.emplace_back(-2, action);
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
// ビームサーチを行う関数（終了したノードの中から上位 N 個の解を取得）
unordered_map<Cost, vector<Action>> beam_search(const Config &config,
                                                const State &state, int topN) {
    Tree tree(state, config);
    Selector selector(config);
    int turn = 0;
    unordered_map<Cost, vector<Action>> solutions;
    // 探索可能な候補がなくなるか、最大ターンに達するまで探索を続ける
    while (true) {
        tree.dfs(selector);

        // 非終了候補を取得
        vector<Candidate> non_finished = selector.select();

        if (selector.have_finished()) {
            vector<Candidate> finishedCandidates =
                selector.get_finished_candidates();

            for (int i = 0; i < (int)finishedCandidates.size(); ++i) {
                Candidate candidate = finishedCandidates[i];

                if (solutions.find(candidate.evaluator.evaluate()) ==
                    solutions.end()) {
                    cerr << "pred_score: " << i << " "
                         << candidate.evaluator.evaluate() << el;
                    solutions[candidate.evaluator.evaluate()] =
                        tree.calculate_path(candidate.parent, turn + 1);
                }
            }
        }
        if (non_finished.empty())
            break; // これ以上展開できる候補がなければ終了
        // 現在の候補から木を更新（子ノードの展開準備）
        tree.update(non_finished);
        selector.clear(); // 候補リストはクリアするが、finished_candidates_
                          // はそのまま保持
        ++turn;
        if (turn >= config.max_turn)
            break;
    }
    cerr << "size1: " << solutions.size() << el;
    return solutions;
}
} // namespace beam_search

// --- 各種関数 ---

// calc_score: 駅を (ni, nj) に増設したときの利得を計算
pair<int, int> calc_score(int ni, int nj,
                          const vector<vector<vector<pair<int, int>>>> &people,
                          const vector<vector<int>> &visited) {
    int score = 0, sub_score = 0;
    for (auto &off : dxy) {
        int nx = ni + off.first, ny = nj + off.second;
        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if (visited[nx][ny] == 0) {
                for (auto &pr : people[nx][ny]) {
                    int p = pr.first, q = pr.second;
                    if (visited[p][q] > 0)
                        score += abs(nx - p) + abs(ny - q);
                    else
                        sub_score += abs(nx - p) + abs(ny - q);
                }
            }
        }
    }
    return {score, sub_score};
}

// add_station: 駅 (ni,nj) 増設時に visited を更新し，利得を返す
int add_station(int ni, int nj,
                const vector<vector<vector<pair<int, int>>>> &people,
                vector<vector<int>> &visited) {
    int add_score = 0;
    for (auto &off : dxy) {
        int nx = ni + off.first, ny = nj + off.second;
        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            visited[nx][ny]++;
            if (visited[nx][ny] == 1) {
                for (auto &pr : people[nx][ny]) {
                    int p = pr.first, q = pr.second;
                    if (visited[p][q] > 0)
                        add_score += abs(nx - p) + abs(ny - q);
                }
            }
        }
    }
    return add_score;
}

// get_line_num: ３点 (a,b,c) から路線操作番号と中間座標を決定
vector<int> get_line_num(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
    int dx1 = b.first - a.first, dx2 = c.first - b.first;
    int dy1 = b.second - a.second, dy2 = c.second - b.second;
    if (dx1 == 0 && dx2 == 0)
        return {1, b.first, b.second};
    else if (dy1 == 0 && dy2 == 0)
        return {2, b.first, b.second};
    else if ((dx1 == 0 && dx2 == 1 && dy1 == 1 && dy2 == 0) ||
             (dx1 == -1 && dx2 == 0 && dy1 == 0 && dy2 == -1))
        return {3, b.first, b.second};
    else if ((dx1 == 0 && dx2 == -1 && dy1 == 1 && dy2 == 0) ||
             (dx1 == 1 && dx2 == 0 && dy1 == 0 && dy2 == -1))
        return {4, b.first, b.second};
    else if ((dx1 == 1 && dx2 == 0 && dy1 == 0 && dy2 == 1) ||
             (dx1 == 0 && dx2 == -1 && dy1 == -1 && dy2 == 0))
        return {5, b.first, b.second};
    else if ((dx1 == -1 && dx2 == 0 && dy1 == 0 && dy2 == 1) ||
             (dx1 == 0 && dx2 == 1 && dy1 == -1 && dy2 == 0))
        return {6, b.first, b.second};
    return {0, b.first, b.second};
}

// bfs: 指定セルからマップ(mp)上で経路探索を行い，経路（逆順）を返す
vector<pair<int, int>> bfs(int si, int sj, vector<vector<int>> &mp,
                           vector<vector<double>> &wt) {
    int n = mp.size();
    static int id = 0;
    id++;
    static vector<vector<pair<int, int>>> dis(
        n, vector<pair<int, int>>(n, {id, -1}));
    static vector<vector<pair<int, int>>> frm(
        n, vector<pair<int, int>>(n, {-1, -1}));
    static vector<vector<pair<int, double>>> sum_wt(
        n, vector<pair<int, double>>(n, {id, -1}));
    wt[si][sj] = 0;
    if (mp[si][sj] == 0) {
        mp[si][sj] = 1;
        return {{si, sj}};
    }

    int gx = -1, gy = -1, min_dis = INT_MAX;
    static deque<pair<int, int>> dq;
    dq.clear();
    dis[si][sj] = {id, 0};
    frm[si][sj] = {-1, -1};
    sum_wt[si][sj] = {id, 0};
    dq.emplace_back(si, sj);

    double best_weight = -1;
    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();
        // ループ内での共通計算：現在の距離と次の距離
        int curDist = dis[x][y].second;
        int nd = curDist + 1;
        if (nd > min_dis) {
            break;
        }
        for (const auto &d : dxy4) {
            int nx = x + d.first, ny = y + d.second;
            if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                continue;
            if (mp[nx][ny] == 0)
                continue;
            // 最短距離候補の場合
            if (min_dis >= nd && mp[nx][ny] == 1 && (nx != si || ny != sj)) {
                min_dis = min(min_dis, nd);
                dis[nx][ny] = {id, nd};
                double new_weight = sum_wt[x][y].second + wt[nx][ny];
                if (new_weight > best_weight) {
                    best_weight = new_weight;
                    frm[nx][ny] = {x, y};
                    gx = nx;
                    gy = ny;
                }
            }
            // 既知の最短距離より短い場合のみ探索を続行
            else if (nd < min_dis) {
                if (dis[nx][ny].first != id) {
                    dis[nx][ny] = {id, nd};
                    dq.emplace_back(nx, ny);
                }
                if (dis[nx][ny].second == nd &&
                    (sum_wt[nx][ny].first != id ||
                     sum_wt[x][y].second + wt[nx][ny] >
                         sum_wt[nx][ny].second)) {
                    frm[nx][ny] = {x, y};
                    sum_wt[nx][ny] = {id, sum_wt[x][y].second + wt[nx][ny]};
                }
            }
        }
    }
    if (gx == -1)
        return {};
    mp[si][sj] = 1;
    static vector<pair<int, int>> route;
    route.clear();
    int curx = gx, cury = gy;
    route.emplace_back(curx, cury);
    int steps = dis[gx][gy].second;
    for (int i = 0; i < steps; i++) {
        auto p = frm[curx][cury];
        curx = p.first;
        cury = p.second;
        route.emplace_back(curx, cury);
    }

    return route;
}

// evaluate: (シミュレーション) 駅順序における総利得を評価
ll evaluate(const vector<pair<int, int>> &stations,
            const vector<vector<vector<pair<int, int>>>> &people) {
    ll now_K = K;
    int now_turn = 0;
    vector<vector<int>> visited(N, vector<int>(N, 0));
    ll score_a_day = 0;
    score_a_day +=
        add_station(stations[0].first, stations[0].second, people, visited);
    score_a_day +=
        add_station(stations[1].first, stations[1].second, people, visited);
    now_K -= 12000;
    now_turn += 2;
    vector<ll> gain;
    gain.push_back(now_K);
    gain.push_back((T - now_turn) * score_a_day - 5500);
    for (size_t i = 2; i < stations.size(); i++) {
        int delay = max((ll)max(0, 6000 - (int)now_K) / score_a_day, 10LL);
        if (now_turn + delay > T)
            break;
        int add_score_val =
            add_station(stations[i].first, stations[i].second, people, visited);
        now_turn += delay;
        score_a_day += add_score_val;
        gain.push_back((T - now_turn) * add_score_val - 6000);
    }
    ll best_val = 0, cur = 0;
    for (auto g : gain) {
        cur += g;
        best_val = max(best_val, cur);
    }
    return best_val;
}

// make_ans: 駅の順序から操作手順(ans)と総利得を生成
pair<vector<vector<int>>, ll>
make_ans(const vector<pair<int, int>> &stations,
         const vector<vector<vector<pair<int, int>>>> &people) {
    static vector<vector<int>> ans;
    bool free_flag = true, fin = false;
    int index1 = 1, index2 = 1;
    ll now_K = K;
    int now_turn = 0;
    ll score_a_day = 0;
    int n = N;
    static vector<vector<int>> mp(n, vector<int>(n, -1)); // マップ (mp)
    static vector<vector<double>> wt(n, vector<double>(n, 0));
    static vector<vector<int>> visited(n, vector<int>(n, 0));
    rep(i, N) {
        rep(j, N) {
            mp[i][j] = -1;
            wt[i][j] = 0;
            visited[i][j] = 0;
        }
    }
    ans.clear();

    for (size_t idx = 0; idx < stations.size(); idx++) {
        int i = stations[idx].first, j = stations[idx].second;
        wt[i][j] = pow((double)(stations.size() - idx), 0.5);
    }

    // 初手：最初の駅を設置
    ans.push_back({0, stations[0].first, stations[0].second});
    mp[stations[0].first][stations[0].second] = 1;
    wt[stations[0].first][stations[0].second] = 0;
    int add_score_val =
        add_station(stations[0].first, stations[0].second, people, visited);
    now_K -= STATION_COST;
    now_turn++;
    score_a_day += add_score_val;
    vector<ll> gain;
    gain.push_back(now_K);
    vector<ll> score_a_day_change;
    vector<pair<int, int>> route;

    for (int t = 1; t < T; t++) {
        if (fin || index1 >= (int)stations.size())
            break;
        if (free_flag && index1 < (int)stations.size()) {
            while (index1 < (int)stations.size()) {
                route = bfs(stations[index1].first, stations[index1].second, mp,
                            wt);
                if (route.empty()) {
                    index1++;
                } else {
                    break;
                }
            }
            if (!route.empty()) {
                add_score_val =
                    add_station(stations[index1].first, stations[index1].second,
                                people, visited);
                if (route.size() >= 2) {
                    for (size_t k = 1; k < route.size() - 1; k++) {
                        int ii = route[k].first, jj = route[k].second;
                        mp[ii][jj] = 0;
                    }
                }
                index2 = (route.size() > 1 ? 1 : 0);
            } else {
                fin = true;
            }
            free_flag = false;
        }
        if (fin || index1 >= (int)stations.size())
            break;
        if (index2 < (int)route.size() - 1) {
            if (now_K >= LINE_COST) {
                now_K -= LINE_COST;
                if (index2 - 1 >= 0 && index2 + 1 < (int)route.size()) {
                    vector<int> mv = get_line_num(
                        route[index2 - 1], route[index2], route[index2 + 1]);
                    ans.push_back(mv);
                } else {
                    ans.push_back({-1});
                }
                index2++;
            } else {
                ans.push_back({-1});
            }
        } else if (index2 == (int)route.size() - 1) {
            if (now_K >= STATION_COST) {
                now_K -= STATION_COST;
                ans.push_back(
                    {0, stations[index1].first, stations[index1].second});
                free_flag = true;
                index1++;
                score_a_day += add_score_val;
                int penalty = max(0, (int)route.size() - 2);
                gain.push_back((T - t) * add_score_val - penalty * LINE_COST -
                               STATION_COST);
            } else {
                ans.push_back({-1});
            }
        }
        now_K += score_a_day;
        score_a_day_change.push_back(score_a_day);
    }
    ll best_sum = 0, cur_sum = 0;
    int best_index = 0;
    for (size_t i = 0; i < gain.size(); i++) {
        cur_sum += gain[i];
        if (cur_sum > best_sum) {
            best_sum = cur_sum;
            best_index = i;
        }
    }
    while (!ans.empty() && ans.back()[0] != 0)
        ans.pop_back();
    while ((int)gain.size() > best_index + 1) {
        if (!ans.empty())
            ans.pop_back();
        gain.pop_back();
        while (!ans.empty() && ans.back()[0] != 0)
            ans.pop_back();
    }
    // ll total_gain = 0;
    // for (auto v : gain)
    //     total_gain += v;
    return {ans, best_sum};
}
vector<tuple<int, int, int, int>> input() {
    cin >> N >> M >> K >> T;
    // 入力 (M行の4整数)
    vector<tuple<int, int, int, int>> trips(M);
    for (int i = 0; i < M; i++) {
        int si, sj, ti, tj;
        cin >> si >> sj >> ti >> tj;
        trips[i] = make_tuple(si, sj, ti, tj);
    }
    return trips;
}
void setup() { // dxyの生成（マンハッタン距離2以内）
    for (int i = -2; i <= 2; i++) {
        for (int j = -2; j <= 2; j++) {
            if (abs(i) + abs(j) <= 2)
                dxy.push_back({i, j});
        }
    }
}
vector<vector<vector<pair<int, int>>>>
make_people(const vector<tuple<int, int, int, int>> &trips) {
    vector<vector<vector<pair<int, int>>>> people(
        N, vector<vector<pair<int, int>>>(N));
    for (int i = 0; i < M; i++) {
        int si, sj, ti, tj;
        tie(si, sj, ti, tj) = trips[i];
        MAX_SCORE += abs(si - ti) + abs(sj - tj);
        people[si][sj].push_back({ti, tj});
        people[ti][tj].push_back({si, sj});
    }
    return people;
}
vector<pair<int, int>>
make_need_ijs(const vector<vector<vector<pair<int, int>>>> &people) {
    // dxy:
    // マンハッタン距離2以内のオフセット（グローバル変数として定義済みとする）
    // 例: vector<pair<int,int>> dxy = { {-2,0}, {-1,-1}, {-1,0}, {-1,1},
    //                                    {0,-2}, {0,-1}, {0,0}, {0,1}, {0,2},
    //                                    {1,-1}, {1,0}, {1,1}, {2,0} };

    // 各セル周辺で人がいるセルの集合を構築
    vector<vector<set<pair<int, int>>>> include(N,
                                                vector<set<pair<int, int>>>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (auto &off : dxy) {
                int ni = i + off.first, nj = j + off.second;
                if (ni >= 0 && ni < N && nj >= 0 && nj < N &&
                    !people[ni][nj].empty()) {
                    include[i][j].insert({ni, nj});
                }
            }
        }
    }

    // is_need の初期化（各セルを「必要」と仮定）
    vector<vector<int>> is_need(N, vector<int>(N, true));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (include[i][j].empty()) {
                is_need[i][j] = false;
                continue;
            }
            // (i,j) に対して，右下方向のセル (i+p, j+q) についてチェック
            for (int p = 0; p < 4; p++) {
                for (int q = 0; q < 4; q++) {
                    // Python の "if p == q == 0 or p + q > 4 or i+p not in
                    // range(N) or j+q not in range(N): continue"
                    if ((p == 0 && q == 0) || (p + q > 4) || (i + p >= N) ||
                        (j + q >= N))
                        continue;
                    // もし両セルの集合が全く同じなら，
                    // Python: if include[i][j] == include[i+p][j+q]:
                    // is_need[i+p][j+q] = False
                    if (include[i][j] == include[i + p][j + q]) {
                        is_need[i + p][j + q] = false;
                    } else {
                        // Python の "elif include[i][j] < include[i+p][j+q]:"
                        // は include[i][j] が厳密な部分集合であれば真
                        if (include[i][j].size() <
                            include[i + p][j + q].size()) {
                            bool isSubset = true;
                            for (auto &elem : include[i][j]) {
                                if (include[i + p][j + q].find(elem) ==
                                    include[i + p][j + q].end()) {
                                    isSubset = false;
                                    break;
                                }
                            }
                            if (isSubset)
                                is_need[i][j] = false;
                        }
                        // Python の "elif include[i][j] > include[i+p][j+q]:"
                        // は include[i][j] が厳密な上位集合であれば真
                        if (include[i][j].size() >
                            include[i + p][j + q].size()) {
                            bool isSuperset = true;
                            for (auto &elem : include[i + p][j + q]) {
                                if (include[i][j].find(elem) ==
                                    include[i][j].end()) {
                                    isSuperset = false;
                                    break;
                                }
                            }
                            if (isSuperset)
                                is_need[i + p][j + q] = false;
                        }
                    }
                }
            }
        }
    }

    // is_need が true のセルを need_ijs に追加
    vector<pair<int, int>> need_ijs;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (is_need[i][j])
                need_ijs.push_back({i, j});
        }
    }
    return need_ijs;
}

vector<vector<vector<vector<int>>>>
make_point(const vector<vector<vector<pair<int, int>>>> &people,
           const vector<pair<int, int>> &need_ijs) { // 4次元配列 point の生成
    vector<vector<vector<vector<int>>>> point(
        N, vector<vector<vector<int>>>(
               N, vector<vector<int>>(N, vector<int>(N, 0))));
    // for (int i = 0; i < M; i++) {
    //     int si, sj, ti, tj;
    //     tie(si, sj, ti, tj) = trips[i];
    //     for (auto &off1 : dxy) {
    //         int sni = si + off1.first, snj = sj + off1.second;
    //         if (sni < 0 || sni >= N || snj < 0 || snj >= N)
    //             continue;
    //         for (auto &off2 : dxy) {
    //             int tni = ti + off2.first, tnj = tj + off2.second;
    //             if (tni < 0 || tni >= N || tnj < 0 || tnj >= N)
    //                 continue;
    //             point[sni][snj][tni][tnj] += abs(si - ti) + abs(sj - tj);
    //         }
    //     }
    // }
    rep(idx1, (int)need_ijs.size()) {
        for (int idx2 = idx1 + 1; idx2 < need_ijs.size(); idx2++) {
            auto [i, j] = need_ijs[idx1];
            auto [ii, jj] = need_ijs[idx2];
            int tmp = 0;
            vector<pair<int, int>> cands;
            for (auto &[dx, dy] : dxy) {
                int nx = i + dx;
                int ny = j + dy;
                if (0 <= nx and nx < N and 0 <= ny and ny < N and
                    !people[nx][ny].empty()) {
                    cands.push_back({nx, ny});
                }
            }
            for (auto &[dx, dy] : dxy) {
                int nx = ii + dx;
                int ny = jj + dy;
                if (0 <= nx and nx < N and 0 <= ny and ny < N and
                    !people[nx][ny].empty()) {
                    for (auto [p, q] : people[nx][ny]) {
                        if (find(cands.begin(), cands.end(), make_pair(p, q)) !=
                            cands.end()) {
                            tmp += abs(nx - p) + abs(ny - q);
                        }
                    }
                }
            }
            point[i][j][ii][jj] = tmp;
            point[ii][jj][i][j] = tmp;
        }
    }
    return point;
}
int add_stations(vector<int> &s, vector<pair<int, int>> &stations,
                 vector<int> &used, vector<vector<int>> &included,
                 const vector<pair<int, int>> &need_ijs,
                 const vector<vector<vector<pair<int, int>>>> &people) {
    int res = 0;
    for (auto idx : s) {
        auto ij = need_ijs[idx];
        stations.push_back(ij);
        auto [i, j] = ij;
        for (auto &[dx, dy] : dxy) {
            int nx = i + dx;
            int ny = j + dy;
            if (0 <= nx and nx < N and 0 <= ny and ny < N) {
                included[nx][ny] += 1;
                if (included[nx][ny] == 1) {
                    for (auto &[p, q] : people[nx][ny]) {
                        if (included[p][q] > 0) {
                            res += abs(nx - p) + abs(ny - q);
                        }
                    }
                }
            }
        }
    }
    return res;
}
vector<int>
calc_best_order(vector<int> &s, vector<pair<int, int>> &stations,
                vector<int> &used, vector<vector<int>> &included,
                const vector<pair<int, int>> &need_ijs,
                const vector<vector<vector<pair<int, int>>>> &people) {}
int calc_score_diff(int ai, int aj, int bi, int bj,
                    vector<vector<int>> &included) {}
void restore(int ai, int aj, int bi, int bj, vector<vector<int>> &included) {}
vector<pair<int, int>>
make_stations(const vector<pair<int, int>> &need_ijs,
              const vector<vector<vector<vector<int>>>> &point,
              const vector<vector<vector<pair<int, int>>>> &people) {
    vector<pair<int, int>> res;
    vector<int> can_use(need_ijs.size(), -1);
    vector<int> used(need_ijs.size(), 0);
    vector<vector<int>> included(N, vector<int>(N, 0));
    rep(i, (int)need_ijs.size()) { can_use[i] = i; }
    int score_a_day = 0;

    vector<int> best_pair = {-1, -1};
    int max_p = 0;
    rep(idx1, need_ijs.size()) {
        auto p = need_ijs[idx1];
        int i = p.first, j = p.second;
        for (int idx2 = idx1 + 1; idx2 < need_ijs.size(); idx2++) {
            auto q = need_ijs[idx2];
            int ii = q.first, jj = q.second;
            if (point[i][j][ii][jj] != 0 &&
                ((abs(i - ii) + abs(j - jj) - 1) * LINE_COST <=
                 K - STATION_COST * 2)) {
                int p = point[i][j][ii][jj];
                if (p > max_p) {
                    max_p = p;
                    best_pair = {idx1, idx2};
                }
            }
        }
    }
    int add_score =
        add_stations(best_pair, res, used, included, need_ijs, people);
    score_a_day += add_score;
    const int num = 5;
    const int cand_num = 100;
    while (true) {
        vector<vector<int>> cand;
        cand.reserve(cand_num);
        rep(i, cand_num) {
            vector<int> tmp;
            tmp.reserve(num);
            rep(j, num) {
                // if (j == 0) {
                //     tmp.push_back()
                // }
            }
        }
    }
}
vector<pair<int, int>>
make_greedy_ans(const vector<pair<int, int>> &need_ijs,
                const vector<vector<vector<vector<int>>>> &point,
                const vector<vector<vector<pair<int, int>>>> &people) {
    double min_t_val = 1e9;
    // visited初期化
    vector<vector<int>> visited(N, vector<int>(N, 0));
    pair<pair<int, int>, pair<int, int>> best_pair = {{-1, -1}, {-1, -1}};
    int max_p = 0;
    double best_a = 0;
    for (auto &p : need_ijs) {
        int i = p.first, j = p.second;
        for (auto &q : need_ijs) {
            int ii = q.first, jj = q.second;
            if (point[i][j][ii][jj] != 0 &&
                (abs(i - ii) + abs(j - jj) - 1 <= (K - 10000) / 100)) {
                double cur_t = abs(i - ii) + abs(j - jj) +
                               max(0.0, 7500.0 / (double)point[i][j][ii][jj]);
                int p = point[i][j][ii][jj];
                double a = pow(point[i][j][ii][jj], 1) /
                           (double)(abs(i - ii) + abs(j - jj) - 1);
                if (cur_t < min_t_val) {
                    // if (p > max_p) {
                    // if (a > best_a) {
                    min_t_val = cur_t;
                    best_a = a;
                    max_p = p;
                    best_pair = {{i, j}, {ii, jj}};
                }
            }
        }
    }
    // 初期の駅リスト作成
    vector<pair<int, int>> stations;
    stations.push_back(best_pair.first);
    int add_score_station = add_station(
        best_pair.first.first, best_pair.first.second, people, visited);
    ll score_a_day = add_score_station;
    stations.push_back(best_pair.second);
    add_score_station = add_station(best_pair.second.first,
                                    best_pair.second.second, people, visited);
    score_a_day += add_score_station;

    while (true) {
        pair<int, int> best_ij = {-1, -1};
        int best_score_val = 0;
        for (auto &cell : need_ijs) {
            int i = cell.first, j = cell.second;
            // int d = INT_MAX;
            // for (auto &st : stations)
            //     d = min(d, abs(i - st.first) + abs(j - st.second));
            auto sc = calc_score(i, j, people, visited);
            int cur_val = sc.first * 8 + sc.second;
            if (sc.first == 0 && sc.second == 0)
                continue;
            if (best_score_val < cur_val) {
                best_score_val = cur_val;
                best_ij = {i, j};
            }
        }
        if (best_score_val == 0)
            break;
        assert(best_ij.first != -1);
        stations.push_back(best_ij);
        int add_val =
            add_station(best_ij.first, best_ij.second, people, visited);
        score_a_day += add_val;
    }
    return stations;
}

// 複数の温度関数を返す関数
double get_temperature(int type, double T_init, double T_final, double progress,
                       double total_time, double current_time) {
    // type==0: 指数減衰
    if (type == 0) {
        return T_init * pow(T_final / T_init, progress);
    }
    // type==1: 線形減衰
    else if (type == 1) {
        return T_init + (T_final - T_init) * progress;
    }
    // type==2: 逆比例型（reciprocal decay）
    else if (type == 2) {
        double alpha = (T_init - T_final) / (T_final * total_time);
        return T_init / (1.0 + alpha * current_time);
    }
    // デフォルトは指数減衰
    return T_init * pow(T_final / T_init, progress);
}
bool is_ok(vector<pair<int, int>> stations) {
    return K - STATION_COST * 2 >=
           (abs(stations[0].first - stations[1].first) +
            abs(stations[0].second - stations[1].second) - 1) *
               LINE_COST;
}
vector<vector<int>> clim(vector<pair<int, int>> &stations,
                         const vector<vector<vector<pair<int, int>>>> &people,
                         TimeKeeperDouble &timer) { // 操作手順の生成と局所探索
    auto res = make_ans(stations, people);
    vector<vector<int>> best_ans = res.first;
    ll best_total_score = res.second;
    ll tmp = best_total_score;

    timer.setNowTime();
    int sz = stations.size();
    int cnt = 0;
    int mode = xorshift() % 4;
    // 反転する長さの最大値
    int l_max = 2;
    while (!timer.isTimeOver()) {
        if (cnt % 10 == 0) {
            cerr << best_total_score << el;
        }
        if (mode == 0) {
            int i = (xorshift() % sz);
            int j = (xorshift() % sz);
            if (i == j) {
                continue;
            }
            swap(stations[i], stations[j]);
            if (min(i, j) <= 1 and !is_ok(stations)) {
                swap(stations[i], stations[j]);
                continue;
            }
            cnt++;
            auto cur_res = make_ans(stations, people);
            ll cur_score = cur_res.second;
            if (cur_score >= best_total_score) {
                best_total_score = cur_score;
                best_ans = cur_res.first;
            } else {
                swap(stations[i], stations[j]); // 元に戻す
            }
        } else if (false and mode == 1) {
            int i = (xorshift() % (sz - 1));
            int l = (xorshift() % l_max) + 1;
            reverse(stations.begin() + i,
                    stations.begin() + min(sz - 1, i + l));
            if (i <= 1 and !is_ok(stations)) {
                reverse(stations.begin() + i,
                        stations.begin() + min(sz - 1, i + l));
                continue;
            }
            cnt++;
            auto cur_res = make_ans(stations, people);
            ll cur_score = cur_res.second;
            if (cur_score >= best_total_score) {
                best_total_score = cur_score;
                best_ans = cur_res.first;
            } else {
                reverse(stations.begin() + i,
                        stations.begin() + min(sz - 1, i + l));
            }
        } else {
            int i = (xorshift() % sz);
            int j = (xorshift() % sz);
            if (i == j) {
                continue;
            }
            pair<int, int> temp = stations[i];    // i番目の要素を保存
            stations.erase(stations.begin() + i); // i番目の要素を削除
            stations.insert(stations.begin() + j, temp);
            if (min(i, j) <= 1 and !is_ok(stations)) {
                pair<int, int> temp = stations[j];    // i番目の要素を保存
                stations.erase(stations.begin() + j); // i番目の要素を削除
                stations.insert(stations.begin() + i, temp);
                continue;
            }
            cnt++;

            auto cur_res = make_ans(stations, people);
            ll cur_score = cur_res.second;
            if (cur_score >= best_total_score) {
                best_total_score = cur_score;
                best_ans = cur_res.first;
            } else {
                temp = stations[j];
                stations.erase(stations.begin() + j);
                stations.insert(stations.begin() + i, temp);
            }
        }

        timer.setNowTime();
    }
    cerr << "cnt: " << cnt << el;
    cerr << "before: " << tmp << " after: " << best_total_score << el;
    return best_ans;
}
// 焼きなまし法による局所探索（SA）
// tempType: 0→指数，1→線形，2→逆比例型の温度関数を利用
vector<vector<int>> sa(vector<pair<int, int>> &stations,
                       const vector<vector<vector<pair<int, int>>>> &people,
                       TimeKeeperDouble &timer, int tempType = 0) {
    auto res = make_ans(stations, people);
    vector<vector<int>> best_ans = res.first;
    ll best_total_score = res.second;
    ll current_score = res.second;
    ll tmp = best_total_score;

    int sz = stations.size();
    int cnt = 0;

    // 温度スケジュールのパラメータ（調整可能）
    const double T_init = best_total_score / 50.0, T_final = 0;
    const double total_time = TIME_LIMIT; // 総探索時間(ms)

    timer.setNowTime();
    while (!timer.isTimeOver()) {

        // 局所操作：swap または 挿入操作をランダムに選択
        int mode = xorshift() % 4;
        int i, j;
        if (mode == 0) {
            i = (xorshift() % sz);
            j = (xorshift() % sz);
            if (i == j) {
                continue;
            }
            swap(stations[i], stations[j]);
            if (min(i, j) <= 1 and !is_ok(stations)) {
                swap(stations[i], stations[j]);
                continue;
            }
        } else if (false and mode <= 1) {
            i = (xorshift() % (sz - 1));
            j = i + 1;
            if (i == j) {
                continue;
            }
            swap(stations[i], stations[j]);
            if (min(i, j) <= 1 and !is_ok(stations)) {
                swap(stations[i], stations[j]);
                continue;
            }
        } else {
            i = (xorshift() % sz);
            j = (xorshift() % sz);
            if (i == j) {
                continue;
            }
            pair<int, int> temp = stations[i];
            stations.erase(stations.begin() + i);
            stations.insert(stations.begin() + j, temp);
            if (min(i, j) <= 1 and !is_ok(stations)) {
                pair<int, int> temp = stations[j];
                stations.erase(stations.begin() + j);
                stations.insert(stations.begin() + i, temp);
                continue;
            }
        }
        cnt++;
        // 新状態の評価
        auto cur_res = make_ans(stations, people);
        ll new_score = cur_res.second;
        ll delta = new_score - current_score;

        // 経過時間に応じた進捗率 [0,1] を計算
        double current_time = timer.getNowTime();
        double progress = min(current_time / total_time, 1.0);

        // 複数の温度関数のうち、指定したものを利用
        double current_temperature = get_temperature(
            tempType, T_init, T_final, progress, total_time, current_time);

        // デバッグ出力：各温度関数の温度を出力（必要に応じてコメントアウト）
        // cerr << "cnt: " << cnt << " current_time: " << current_time
        //      << " progress: " << progress
        //      << " temperature: " << current_temperature << endl;

        // 焼きなましの受容判定
        bool accept = false;
        if (delta >= 0) {
            accept = true;
        } else {
            double prob = exp((double)delta / current_temperature);
            double r = (xorshift() % 10000) / 10000.0;
            cerr << delta << " " << prob << " " << current_temperature << " "
                 << progress << el;
            if (r < prob)
                accept = true;
        }

        if (accept) {
            current_score = new_score;
            if (new_score > best_total_score) {
                best_total_score = new_score;
                best_ans = cur_res.first;
            }
        } else {
            // 状態を元に戻す
            if (mode == 0) {
                swap(stations[i], stations[j]);
            } else {
                pair<int, int> temp = stations[j];
                stations.erase(stations.begin() + j);
                stations.insert(stations.begin() + i, temp);
            }
        }

        timer.setNowTime();
        if (cnt % 10 == 0) {
            cerr << timer.getNowTime() << " " << current_score << el;
        }
    }
    cerr << "cnt: " << cnt << "\n";
    cerr << "before: " << tmp << " after: " << best_total_score << el;
    return best_ans;
}
size_t beam_width = 1000;
size_t tour_capacity = 16 * beam_width;
uint32_t hash_map_capacity = 64 * beam_width;
// --- main ---
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    TimeKeeperDouble timer(TIME_LIMIT);
    vector<tuple<int, int, int, int>> trips = input();
    setup();

    // people: 各グリッドに接点情報を登録
    vector<vector<vector<pair<int, int>>>> people = make_people(trips);
    vector<pair<int, int>> need_ijs = make_need_ijs(people);
    vector<vector<vector<vector<int>>>> point = make_point(people, need_ijs);
    vector<pair<int, pair<int, int>>> ij_score;
    for (auto [i, j] : need_ijs) {
        int s = 0;
        for (auto [dx, dy] : dxy) {
            int nx = i + dx;
            int ny = j + dy;
            if (0 <= nx and nx < N and 0 <= ny and ny < N) {
                for (auto [p, q] : people[nx][ny]) {
                    s += abs(p - nx) + abs(q - ny);
                }
            }
        }
        ij_score.push_back({s, {i, j}});
    }
    sort(all(ij_score),
         [](const pair<int, pair<int, int>> &a,
            const pair<int, pair<int, int>> &b) { return a.first < b.first; });
    cerr << "need_ijs.size: " << need_ijs.size() << el;
    cout << "#need_ijs.size: " << need_ijs.size() << el;
    timer.setNowTime();
    cerr << "time1: " << timer.getNowTime() << el;
    vector<vector<int>> best_ans;
    vector<pair<int, int>> stations;
    if (need_ijs.size() > 500) {
        auto tmp = make_greedy_ans(need_ijs, point, people);
        timer.setNowTime();
        cerr << "fin greedy: " << timer.getNowTime() << el;
        dump(need_ijs.size());
        cerr << "tmp_size: " << tmp.size()
             << " need_ijs_size: " << need_ijs.size() << el;
        vector<vector<int>> used(N, vector<int>(N, 0));
        for (auto [i, j] : tmp) {
            used[i][j] = 1;
        }

        // while (!ij_score.empty() and tmp.size() < 500) {
        //     auto [p, q] = ij_score.back().second;
        //     ij_score.pop_back();
        //     if (used[p][q] == 1) {
        //     } else {
        //         tmp.push_back({p, q});
        //     }
        // }
        // vector<vector<int>> best_ans = sa(stations, people, timer,
        // 0);
    }
    beam_width = (double)20000000 / M / need_ijs.size();
    cerr << "beam_width: " << beam_width << el;
    beam_search::Config config = {1000, beam_width, tour_capacity,
                                  hash_map_capacity};
    beam_search::State state = beam_search::State(need_ijs, people);
    unordered_map<beam_search::Cost, vector<beam_search::Action>> solutions =
        beam_search::beam_search(config, state, 10000);
    cerr << "size2: " << solutions.size() << el;

    ll best_score = 0;
    int index = 0;
    for (const auto &[cost, actions] : solutions) {
        vector<pair<int, int>> tmp;
        tmp.reserve(actions.size() + 1);
        rep(i, actions.size()) {
            if (actions[i].idx2 != -1) {
                tmp.push_back(need_ijs[actions[i].idx1]);
                tmp.push_back(need_ijs[actions[i].idx2]);
            } else {
                tmp.push_back(need_ijs[actions[i].idx1]);
            }
        }
        auto cur_res = make_ans(tmp, people);
        ll cur_score = cur_res.second;
        cerr << "score: " << index << " " << cur_score << el;
        if (cur_score > best_score) {
            best_score = cur_score;
            best_ans = cur_res.first;
            stations = tmp;
        }
        index++;
    }
    timer.setNowTime();
    cerr << "fin beam: " << timer.getNowTime() << el;

    best_ans = clim(stations, people, timer);
    // best_ans = sa(stations, people, timer, 0);
    while ((int)best_ans.size() < 800)
        best_ans.push_back({-1});
    for (auto &mv : best_ans) {
        for (size_t i = 0; i < mv.size(); i++) {
            cout << mv[i] << (i + 1 == mv.size() ? "\n" : " ");
        }
    }

    return 0;
}
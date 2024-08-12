#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

#define NDEBUG

#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;

constexpr int n = 30;
constexpr int m = n * (n + 1) / 2;

struct Input {
    vector<vector<int>> b;

    void input() {
        b.resize(n);
        for (int x = 0; x < n; ++x) {
            b[x] = vector<int>(x + 1);
            for (int y = 0; y <= x; ++y) {
                cin >> b[x][y];
            }
        }
    }
};

inline int get_pyramid_index(int x, int y) {
    return x * (x - 1) / 2 + y;
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
template <class Key, class T>
struct HashMap {
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
        pair<bool,int> get_index(Key key) const {
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

        void clear() {
            fill(valid_.begin(), valid_.end(), false);
        }

    private:
        uint32_t n_;
        vector<bool> valid_;
        vector<pair<Key,T>> data_;
};

using Hash = uint32_t;

constexpr Hash hash_mask = ((1U << 23) - 1U) << 9;

inline Hash update_target_position(Hash hash, int x, int y) {
    return (hash & hash_mask) | get_pyramid_index(x, y);
}

inline Hash update_sorted_position(Hash hash, int x, int y) {
    Hash zobrist_hash = get_pyramid_index(x, y);
    zobrist_hash |= 512U; // 10-bit
    zobrist_hash *= zobrist_hash * zobrist_hash; // 30-bit
    return hash ^ (zobrist_hash & hash_mask);
}

// 状態遷移を行うために必要な情報
// メモリ使用量をできるだけ小さくしてください
struct Action {
    int xyxy;

    Action(int x1, int y1, int x2, int y2) {
        xyxy = x1 | (y1 << 8) | (x2 << 16) | (y2 << 24);
    }

    tuple<int,int,int,int> decode() const {
        return {xyxy & 255, (xyxy >> 8) & 255, (xyxy >> 16) & 255, xyxy >> 24};
    }

    bool operator==(const Action& other) const {
        return xyxy == other.xyxy;
    }
};

using Cost = int;

constexpr int target_coefficient = 600;

// 状態のコストを評価するための構造体
// メモリ使用量をできるだけ小さくしてください
struct Evaluator {
    int target_ball;
    int potential;

    Evaluator(int target_ball, int potential) :
        target_ball(target_ball),
        potential(potential) {}

    // 低いほどよい
    Cost evaluate() const {
        return potential - target_coefficient * target_ball;
    }
};

// 展開するノードの候補を表す構造体
struct Candidate {
    Action action;
    Evaluator evaluator;
    Hash hash;
    int parent;

    Candidate(Action action, Evaluator evaluator, Hash hash, int parent) :
        action(action),
        evaluator(evaluator),
        hash(hash),
        parent(parent) {}
};

// ノードの候補から実際に追加するものを選ぶクラス
// ビーム幅の個数だけ、評価がよいものを選ぶ
// ハッシュ値が一致したものについては、評価がよいほうのみを残す
class Selector {
    public:
        explicit Selector(const Config& config) :
            hash_to_index_(config.hash_map_capacity)
        {
            beam_width = config.beam_width;
            candidates_.reserve(beam_width);
            full_ = false;

            costs_.resize(beam_width);
            for (size_t i = 0; i < beam_width; ++i) {
                costs_[i] = {0, i};
            }
        }

        // 候補を追加する
        // ターン数最小化型の問題で、candidateによって実行可能解が得られる場合にのみ finished = true とする
        // ビーム幅分の候補をCandidateを追加したときにsegment treeを構築する
        void push(const Candidate& candidate, bool finished) {
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
                    // 保持している候補がビーム幅分になったときにsegment treeを構築する
                    full_ = true;
                    st_ = MaxSegtree(costs_);
                }
            }
        }

        // 選んだ候補を返す
        const vector<Candidate>& select() const {
            return candidates_;
        }

        // 実行可能解が見つかったか
        bool have_finished() const {
            return !finished_candidates_.empty();
        }

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
        // 削除可能な優先度付きキュー
        using MaxSegtree = atcoder::segtree<
            pair<Cost,int>,
            [](pair<Cost,int> a, pair<Cost,int> b){
                if (a.first >= b.first) {
                    return a;
                } else {
                    return b;
                }
            },
            []() { return make_pair(numeric_limits<Cost>::min(), -1); }
        >;

        size_t beam_width;
        vector<Candidate> candidates_;
        HashMap<Hash,int> hash_to_index_;
        bool full_;
        vector<pair<Cost,int>> costs_;
        MaxSegtree st_;
        vector<Candidate> finished_candidates_;
};

// 深さ優先探索に沿って更新する情報をまとめたクラス
class State {
    public:
        explicit State(const Input& input) {
            b_ = input.b;

            for (int x = 0; x < n; ++x) {
                for (int y = 0; y <= x; ++y) {
                    positions_[b_[x][y]] = {x, y};
                }
            }
        }

        // EvaluatorとHashの初期値を返す
        pair<Evaluator,Hash> make_initial_node() {
            return {Evaluator(update_target_ball(0, 0).first, 0), 0};
        }

        // 次の状態候補を全てselectorに追加する
        // 引数
        //   evaluator : 今の評価器
        //   hash      : 今のハッシュ値
        //   parent    : 今のノードID（次のノードにとって親となる）
        void expand(const Evaluator& evaluator, Hash hash, int parent, Selector& selector) {
            auto push_candidate = [&](int x1, int y1, int x2, int y2) {
                assert(x1 > x2);
                assert(b_[x1][y1] < b_[x2][y2]);

                Action new_action(x1, y1, x2, y2);

                int new_potential = evaluator.potential + b_[x1][y1] - b_[x2][y2];

                swap_balls(x1, y1, x2, y2);
                auto [new_target_ball, new_hash] = update_target_ball(evaluator.target_ball, hash);
                swap_balls(x1, y1, x2, y2);

                bool finished = (new_target_ball == m);

                Evaluator new_evaluator(new_target_ball, new_potential);

                selector.push(Candidate(new_action, new_evaluator, new_hash, parent), finished);
            };

            auto [x, y] = positions_[evaluator.target_ball];

            if (can_move_left(x, y)) {
                push_candidate(x, y, x - 1, y - 1);
                if (can_move_left(x - 1, y - 1)) {
                    push_candidate(x - 1, y - 1, x - 2, y - 2);
                }
                if (can_move_right(x - 1, y - 1)) {
                    push_candidate(x - 1, y - 1, x - 2, y - 1);
                }
            }
            if (can_move_right(x, y)) {
                push_candidate(x, y, x - 1, y);
                if (can_move_left(x - 1, y)) {
                    push_candidate(x - 1, y, x - 2, y - 1);
                }
                if (can_move_right(x - 1, y)) {
                    push_candidate(x - 1, y, x - 2, y);
                }
            }
        }

        // actionを実行して次の状態に遷移する
        void move_forward(Action action) {
            auto [x1, y1, x2, y2] = action.decode();
            swap_balls(x1, y1, x2, y2);
        }

        // actionを実行する前の状態に遷移する
        // 今の状態は、親からactionを実行して遷移した状態である
        void move_backward(Action action) {
            auto [x1, y1, x2, y2] = action.decode();
            swap_balls(x1, y1, x2, y2);
        }

    private:
        vector<vector<int>> b_;
        array<pair<int,int>,m> positions_;

        void swap_balls(int x1, int y1, int x2, int y2) {
            int b1 = b_[x1][y1];
            int b2 = b_[x2][y2];
            b_[x1][y1] = b2;
            b_[x2][y2] = b1;
            positions_[b2] = {x1, y1};
            positions_[b1] = {x2, y2};
        }

        bool can_move_left(int x, int y) const {
            return y && b_[x - 1][y - 1] > b_[x][y];
        }

        bool can_move_right(int x, int y) const {
            return y < x && b_[x - 1][y] > b_[x][y];
        }

        pair<int,Hash> update_target_ball(int target_ball, Hash hash) const {
            while (target_ball < m) {
                auto [x, y] = positions_[target_ball];
                if (can_move_left(x, y) || can_move_right(x, y)) {
                    hash = update_target_position(hash, x, y);
                    break;
                } else {
                    hash = update_sorted_position(hash, x, y);
                    ++target_ball;
                }
            }
            return {target_ball, hash};
        }
};

// Euler Tourを管理するためのクラス
class Tree {
    public:
        explicit Tree(const State& state, const Config& config) :
            state_(state)
        {
            curr_tour_.reserve(config.tour_capacity);
            next_tour_.reserve(config.tour_capacity);
            leaves_.reserve(config.beam_width);
            buckets_.assign(config.beam_width, {});
        }

        // 状態を更新しながら深さ優先探索を行い、次のノードの候補を全てselectorに追加する
        void dfs(Selector& selector) {
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
                    auto& [evaluator, hash] = leaves_[leaf_index];
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
        void update(const vector<Candidate>& candidates) {
            leaves_.clear();

            if (curr_tour_.empty()) {
                // 最初のターン
                for (const Candidate& candidate : candidates) {
                    curr_tour_.push_back({(int)leaves_.size(), candidate.action});
                    leaves_.push_back({candidate.evaluator, candidate.hash});
                }
                return;
            }

            for (const Candidate& candidate : candidates) {
                buckets_[candidate.parent].push_back({candidate.action, candidate.evaluator, candidate.hash});
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
                    for (auto [new_action, evaluator, hash] : buckets_[leaf_index]) {
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

            unreachable();
        }

    private:
        State state_;
        vector<pair<int,Action>> curr_tour_;
        vector<pair<int,Action>> next_tour_;
        vector<pair<Evaluator,Hash>> leaves_;
        vector<vector<tuple<Action,Evaluator,Hash>>> buckets_;
        vector<Action> direct_road_;
};

// ビームサーチを行う関数
vector<Action> beam_search(const Config& config, const State& state) {
    Tree tree(state, config);

    // 新しいノード候補の集合
    Selector selector(config);

    for (int turn = 0; turn < config.max_turn; ++turn) {
        // Euler Tourでselectorに候補を追加する
        tree.dfs(selector);

        if (selector.have_finished()) {
            // ターン数最小化型の問題で実行可能解が見つかったとき
            Candidate candidate = selector.get_finished_candidates()[0];
            vector<Action> ret = tree.calculate_path(candidate.parent, turn + 1);
            ret.push_back(candidate.action);
            return ret;
        }

        assert(!selector.select().empty());

        if (turn == config.max_turn - 1) {
            // ターン数固定型の問題で全ターンが終了したとき
            Candidate best_candidate = selector.calculate_best_candidate();
            vector<Action> ret = tree.calculate_path(best_candidate.parent, turn + 1);
            ret.push_back(best_candidate.action);
            return ret;
        }

        // 木を更新する
        tree.update(selector.select());

        selector.clear();
    }

    unreachable();
}

} // namespace beam_search


constexpr int max_turn = 10000;
constexpr size_t beam_width = 4500;
constexpr size_t tour_capacity = 15 * beam_width;
constexpr uint32_t hash_map_capacity = 16 * 3 * beam_width;

struct Solver {
    const Input input;
    vector<beam_search::Action> output;

    Solver(const Input& input) :
        input(input) {}

    void solve() {
        beam_search::Config config = {
            max_turn,
            beam_width,
            tour_capacity,
            hash_map_capacity
        };
        beam_search::State state(input);
        output = beam_search::beam_search(config, state);
    }

    void print() const {
        cout << output.size() << "\n";
        for (beam_search::Action action : output) {
            auto [x1, y1, x2, y2] = action.decode();
            cout << x1 << " " << y1 << " " << x2 << " " << y2 << "\n";
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    Input input;
    input.input();

    Solver solver(input);
    solver.solve();
    solver.print();

    return 0;
}

#include <atcoder/segtree>
#include <bits/stdc++.h>
using namespace std;

// グローバル問題設定
int N, M;
int initial_i, initial_j;
vector<pair<int, int>> targets;

// 方向ベクトル：U, D, L, R
const int di[4] = {-1, +1, 0, 0};
const int dj[4] = {0, 0, -1, +1};

namespace beam_search {

using Hash = uint64_t;
using Cost = int;

//------------------------------------------------------------
// ビームサーチ全体の設定
//------------------------------------------------------------
struct Config {
    int max_turn;
    size_t beam_width;
    size_t tour_capacity;
    uint32_t hash_map_capacity;
};

//------------------------------------------------------------
// シンプルなオープンアドレス連想配列
//------------------------------------------------------------
template <class Key, class T> struct HashMap {
    explicit HashMap(uint32_t n) {
        if (n % 2 == 0)
            ++n;
        n_ = n;
        valid_.assign(n_, false);
        data_.resize(n_);
    }
    pair<bool, int> get_index(Key key) const {
        uint32_t i = key % n_;
        while (valid_[i]) {
            if (data_[i].first == key)
                return {true, (int)i};
            if (++i == n_)
                i = 0;
        }
        return {false, (int)i};
    }
    void set(int i, Key key, T val) {
        valid_[i] = true;
        data_[i] = {key, val};
    }
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

//------------------------------------------------------------
// 行動(Action)：移動／滑走／切替 の種類＋undo情報
//------------------------------------------------------------
struct Action {
    uint8_t type;           // 0=移動,1=滑走,2=切替
    uint8_t dir;            // 0=U,1=D,2=L,3=R
    uint8_t dist;           // 実行後の移動量
    uint8_t prev_target;    // 実行前の次ターゲット番号
    int16_t prev_i, prev_j; // 切替セル座標（undo用）

    Action()
        : type(0), dir(0), dist(0), prev_target(0), prev_i(-1), prev_j(-1) {}
    Action(uint8_t t, uint8_t d)
        : type(t), dir(d), dist(0), prev_target(0), prev_i(-1), prev_j(-1) {}

    bool operator==(const Action &o) const {
        return type == o.type && dir == o.dir && dist == o.dist &&
               prev_target == o.prev_target && prev_i == o.prev_i &&
               prev_j == o.prev_j;
    }
};

//------------------------------------------------------------
// 評価関数(Evaluator)：訪問済み数最大化＋次ターゲット距離最小化
//------------------------------------------------------------
struct Evaluator {
    uint8_t i, j, tidx;
    Evaluator() : i(0), j(0), tidx(0) {}
    Evaluator(int _i, int _j, int _t) : i(_i), j(_j), tidx(_t) {}
    Cost evaluate() const {
        int visited = tidx;
        int md = abs(i - targets[tidx].first) + abs(j - targets[tidx].second);
        // 訪問1件分を距離2000分の価値に置き換え
        return md - visited * 2000;
    }
};

//------------------------------------------------------------
// 候補(Candidate)：1ビーム分のエントリ
//------------------------------------------------------------
struct Candidate {
    Action action;
    Evaluator evaluator;
    Hash hash;
    int parent;
    Candidate(Action a, Evaluator e, Hash h, int p)
        : action(a), evaluator(e), hash(h), parent(p) {}
};

//------------------------------------------------------------
// segtree 用関数
//------------------------------------------------------------
pair<Cost, int> seg_op(pair<Cost, int> a, pair<Cost, int> b) {
    return a.first >= b.first ? a : b;
}
pair<Cost, int> seg_e() { return make_pair(numeric_limits<Cost>::min(), -1); }

//------------------------------------------------------------
// ビーム選択器(Selector)：重複排除＋上位 k 件キープ
//------------------------------------------------------------
class Selector {
  public:
    explicit Selector(const Config &config)
        : beam_width(config.beam_width),
          hash_to_index_(config.hash_map_capacity), full_(false),
          costs_(config.beam_width),
          st_(config.beam_width) // e() を beam_width 回
    {
        candidates_.reserve(beam_width);
        for (size_t i = 0; i < beam_width; ++i) {
            costs_[i] = {numeric_limits<Cost>::max(), (int)i};
        }
    }

    void push(const Candidate &c, bool finished) {
        if (finished) {
            finished_candidates_.push_back(c);
            return;
        }
        Cost cost = c.evaluator.evaluate();
        if (full_ && cost >= st_.all_prod().first)
            return;

        auto [hit, idx] = hash_to_index_.get_index(c.hash);
        if (hit) {
            int j = hash_to_index_.get(idx);
            if (c.hash == candidates_[j].hash) {
                // 既存 state はコストが小さい方を採用
                if (full_) {
                    if (cost < st_.get(j).first) {
                        candidates_[j] = c;
                        st_.set(j, {cost, j});
                    }
                } else {
                    if (cost < costs_[j].first) {
                        candidates_[j] = c;
                        costs_[j].first = cost;
                    }
                }
                return;
            }
        }
        if (full_) {
            auto [worstCost, worstIdx] = st_.all_prod();
            hash_to_index_.set(idx, c.hash, worstIdx);
            candidates_[worstIdx] = c;
            st_.set(worstIdx, {cost, worstIdx});
        } else {
            int j = (int)candidates_.size();
            hash_to_index_.set(idx, c.hash, j);
            candidates_.push_back(c);
            costs_[j].first = cost;
            if (candidates_.size() == beam_width) {
                full_ = true;
                st_ = MaxSegtree(costs_);
            }
        }
    }

    const vector<Candidate> &select() const { return candidates_; }
    bool have_finished() const { return !finished_candidates_.empty(); }
    vector<Candidate> get_finished_candidates() const {
        return finished_candidates_;
    }

    Candidate calculate_best_candidate() const {
        int best = 0;
        if (full_) {
            for (int i = 1; i < (int)beam_width; ++i)
                if (st_.get(i).first < st_.get(best).first)
                    best = i;
        } else {
            for (int i = 1; i < (int)candidates_.size(); ++i)
                if (costs_[i].first < costs_[best].first)
                    best = i;
        }
        return candidates_[best];
    }

    void clear() {
        candidates_.clear();
        hash_to_index_.clear();
        full_ = false;
        finished_candidates_.clear();
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
    HashMap<Hash, int> hash_to_index_;
    bool full_;
    vector<pair<Cost, int>> costs_;
    vector<Candidate> candidates_;
    MaxSegtree st_;
    vector<Candidate> finished_candidates_;
};

//------------------------------------------------------------
// 現在状態(State)：位置,次ターゲット,壁配置＋Zobrist
//------------------------------------------------------------
class State {
  public:
    State() {
        init_zobrist();
        walls.reset();
    }

    // 初期ノードの Evaluator と Hash を返す
    pair<Evaluator, Hash> make_initial_node() {
        cur_i = initial_i;
        cur_j = initial_j;
        cur_t = 0;
        walls.reset();
        Hash h = 0;
        h ^= zob_pos[cur_i * N + cur_j];
        h ^= zob_t[cur_t];
        return {Evaluator(cur_i, cur_j, cur_t), h};
    }

    // 全 12 通りのアクションを試し、Selector に追加
    void expand(const Evaluator &, Hash h0, int parent, Selector &sel) {
        for (uint8_t ty = 0; ty < 3; ++ty) {
            for (uint8_t d = 0; d < 4; ++d) {
                Action a(ty, d);
                move_forward(a);
                Hash h = h0;
                h ^= zob_pos[cur_i * N + cur_j];
                h ^= zob_t[cur_t];
                if (a.type == 2 && a.prev_i >= 0) {
                    h ^= zob_wall[a.prev_i * N + a.prev_j];
                }
                bool finished = (cur_t >= M);
                sel.push(
                    Candidate(a, Evaluator(cur_i, cur_j, cur_t), h, parent),
                    finished);
                move_backward(a);
            }
        }
    }

    //   private:
    int cur_i, cur_j, cur_t;
    bitset<400> walls;

    // Zobrist テーブル
    static inline bool zob_init = false;
    static inline array<Hash, 400> zob_pos, zob_wall;
    static inline array<Hash, 41> zob_t;

    static void init_zobrist() {
        if (zob_init)
            return;
        mt19937_64 rng(123456);
        for (auto &x : zob_pos)
            x = rng();
        for (auto &x : zob_wall)
            x = rng();
        for (auto &x : zob_t)
            x = rng();
        zob_init = true;
    }

    // アクション適用
    void move_forward(Action &a) {
        a.dist = 0;
        a.prev_target = cur_t;
        if (a.type == 0) {
            // 一マス移動
            int ni = cur_i + di[a.dir], nj = cur_j + dj[a.dir];
            if (ni >= 0 && ni < N && nj >= 0 && nj < N && !walls[ni * N + nj]) {
                cur_i = ni;
                cur_j = nj;
                a.dist = 1;
            }
        } else if (a.type == 1) {
            // 滑走
            int ni = cur_i, nj = cur_j, cnt = 0;
            while (true) {
                int ti = ni + di[a.dir], tj = nj + dj[a.dir];
                if (ti < 0 || ti >= N || tj < 0 || tj >= N ||
                    walls[ti * N + tj])
                    break;
                ni = ti;
                nj = tj;
                cnt++;
            }
            cur_i = ni;
            cur_j = nj;
            a.dist = cnt;
        } else {
            // ブロック切替
            int ti = cur_i + di[a.dir], tj = cur_j + dj[a.dir];
            a.prev_i = ti;
            a.prev_j = tj;
            if (ti >= 0 && ti < N && tj >= 0 && tj < N) {
                walls.flip(ti * N + tj);
            }
        }
        // ターゲット到達チェック
        if (cur_t < M && cur_i == targets[cur_t].first &&
            cur_j == targets[cur_t].second) {
            ++cur_t;
        }
    }

    // Undo
    void move_backward(const Action &a) {
        cur_t = a.prev_target;
        if (a.type == 0 && a.dist) {
            cur_i -= di[a.dir];
            cur_j -= dj[a.dir];
        } else if (a.type == 1) {
            cur_i -= a.dist * di[a.dir];
            cur_j -= a.dist * dj[a.dir];
        } else if (a.type == 2 && a.prev_i >= 0) {
            walls.flip(a.prev_i * N + a.prev_j);
        }
    }
};

//------------------------------------------------------------
// Euler Tour 管理＋ビームサーチ本体
//------------------------------------------------------------
class Tree {
  public:
    explicit Tree(const State &state, const Config &cfg) : state_(state) {
        curr_tour_.reserve(cfg.tour_capacity);
        next_tour_.reserve(cfg.tour_capacity);
        leaves_.reserve(cfg.beam_width);
        buckets_.assign(cfg.beam_width, {});
    }

    // DFS しながら Selector に候補を追加
    void dfs(Selector &sel) {
        if (curr_tour_.empty()) {
            auto [ev, h] = state_.make_initial_node();
            state_.expand(ev, h, 0, sel);
            return;
        }
        for (auto [leaf, act] : curr_tour_) {
            if (leaf >= 0) {
                state_.move_forward(act);
                auto &[ev, h] = leaves_[leaf];
                state_.expand(ev, h, leaf, sel);
                state_.move_backward(act);
            } else if (leaf == -1) {
                state_.move_forward(act);
            } else {
                state_.move_backward(act);
            }
        }
    }

    // 木構造をビーム結果で更新
    void update(const vector<Candidate> &cands) {
        leaves_.clear();
        if (curr_tour_.empty()) {
            for (auto &c : cands) {
                curr_tour_.push_back({(int)leaves_.size(), c.action});
                leaves_.push_back({c.evaluator, c.hash});
            }
            return;
        }
        for (auto &c : cands) {
            buckets_[c.parent].push_back({c.action, c.evaluator, c.hash});
        }
        auto it = curr_tour_.begin();
        // 直進エッジをはずす
        while (it->first == -1 && it->second == curr_tour_.back().second) {
            state_.move_forward(it->second);
            direct_road_.push_back(it->second);
            curr_tour_.pop_back();
        }
        // 再構築
        while (it != curr_tour_.end()) {
            auto [leaf, act] = *it++;
            if (leaf >= 0) {
                if (buckets_[leaf].empty())
                    continue;
                next_tour_.push_back({-1, act});
                for (auto &tpl : buckets_[leaf]) {
                    auto [na, ne, nh] = tpl;
                    int ni = leaves_.size();
                    next_tour_.push_back({ni, na});
                    leaves_.push_back({ne, nh});
                }
                buckets_[leaf].clear();
                next_tour_.push_back({-2, act});
            } else if (leaf == -1) {
                next_tour_.push_back({-1, act});
            } else {
                auto [ol, oa] = next_tour_.back();
                if (ol == -1)
                    next_tour_.pop_back();
                else
                    next_tour_.push_back({-2, act});
            }
        }
        swap(curr_tour_, next_tour_);
        next_tour_.clear();
    }

    // 最終パスを復元
    vector<Action> calculate_path(int parent, int turn) const {
        vector<Action> ret = direct_road_;
        ret.reserve(turn);
        for (auto &pr : curr_tour_) {
            auto [leaf, act] = pr;
            if (leaf >= 0) {
                if (leaf == parent) {
                    ret.push_back(act);
                    return ret;
                }
            } else if (leaf == -1) {
                ret.push_back(act);
            } else {
                ret.pop_back();
            }
        }
    }

  private:
    State state_;
    vector<pair<int, Action>> curr_tour_, next_tour_;
    vector<pair<Evaluator, Hash>> leaves_;
    vector<vector<tuple<Action, Evaluator, Hash>>> buckets_;
    vector<Action> direct_road_;
};

//------------------------------------------------------------
// ビームサーチ実行関数
//------------------------------------------------------------
vector<Action> beam_search(const Config &cfg, const State &init_state) {
    Tree tree(init_state, cfg);
    Selector sel(cfg);

    for (int turn = 0; turn < cfg.max_turn; ++turn) {
        tree.dfs(sel);

        if (sel.have_finished()) {
            auto c = sel.get_finished_candidates()[0];
            auto path = tree.calculate_path(c.parent, turn + 1);
            path.push_back(c.action);
            return path;
        }
        if (turn == cfg.max_turn - 1) {
            auto best = sel.calculate_best_candidate();
            auto path = tree.calculate_path(best.parent, turn + 1);
            path.push_back(best.action);
            return path;
        }
        auto chosen = sel.select();
        tree.update(chosen);
        sel.clear();
    }
}

} // namespace beam_search

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 入力
    cin >> N >> M;
    cin >> initial_i >> initial_j;
    targets.resize(M);
    for (int i = 0; i < M; ++i) {
        cin >> targets[i].first >> targets[i].second;
    }

    // 設定
    beam_search::Config cfg;
    cfg.max_turn = 2 * N * M;
    cfg.beam_width = 1000;
    cfg.tour_capacity = 1200;
    cfg.hash_map_capacity = 1u << 15;

    // 初期状態を作成
    beam_search::State init_state;
    auto plan = beam_search::beam_search(cfg, init_state);

    // 出力
    const char *Atyp = "MSA";
    const char *Ddir = "UDLR";
    for (auto &a : plan) {
        cout << Atyp[a.type] << Ddir[a.dir] << "\n";
    }
    return 0;
}

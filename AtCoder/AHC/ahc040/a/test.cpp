#include <bits/stdc++.h>
using namespace std;

struct Nodo_horizon {
    int l;
    int r;
    int d;
    Nodo_horizon(int l, int r, int d) : l(l), r(r), d(d) {}
    bool operator<(const Nodo_horizon &other) const {
        if (l != other.l) {
            return l < other.l;
        } else {
            return r < other.r;
        }
    }
};

struct Action {
    int b;    // base index
    int r;    // rotation flag (0 or 1)
    string d; // direction, e.g. "U"
};

static vector<Action> actions;
static int N;

inline void chmax(int &a, int b) {
    if (a < b)
        a = b;
}

int evaluate(int lim, const vector<pair<int, int>> &wh,
             const vector<deque<int>> &state_l,
             const vector<deque<int>> &state_m,
             const vector<deque<int>> &state_r) {
    int s = (int)state_l.size();
    for (int i = 0; i < s; i++) {
        int prev = -1;
        for (auto j : state_l[i]) {
            actions[j].b = prev;
            prev = j;
        }
        for (auto j : state_m[i]) {
            actions[j].b = prev;
            prev = j;
        }
        for (auto j : state_r[i]) {
            actions[j].b = prev;
            prev = j;
        }
    }
    static vector<Nodo_horizon> horizon;
    static vector<int> r_vec;
    int max_ = 1000000000;
    horizon.clear();
    r_vec.clear();
    horizon.emplace_back(0, max_, 0);

    int W = 0;
    int H = 0;
    for (int i = 0; i < N; i++) {
        auto [w, h] = wh[i];
        if (actions[i].r == 1) {
            std::swap(w, h);
        }

        if (actions[i].d == "U") {
            int u = 0;
            int l, r, d;
            if (actions[i].b == -1) {
                l = 0;
                r = l + w;
            } else {
                // bが指すものが先に処理されている前提
                // このテストでは単純化してb=-1のみを使う。
                l = r_vec[actions[i].b];
                r = l + w;
            }

            // ここでl,rを内包する区間を特定する
            // 元コード:
            // auto l_ = lower_bound(horizon.begin(), horizon.end(),
            // Nodo_horizon(l, l, 0)); バグを再現したいのであえてこのまま使う。
            auto l_ = lower_bound(horizon.begin(), horizon.end(),
                                  Nodo_horizon(l, l, 0));
            if (l_ == horizon.end()) {
                cerr << "l_ == end() error" << endl;
                return lim + 1;
            }

            auto r_ = lower_bound(horizon.begin(), horizon.end(),
                                  Nodo_horizon(r, r, 0));
            if (r_ == horizon.end()) {
                // rが非常に大きくない限りここには来ないはずだが、
                // テストであえてr < max_で内部区間の場合を検証
            }

            // prev(r_)がbegin()を指す場合の対処なし → バグ発生の可能性あり
            auto r_r = *prev(r_);

            // l_からr_までで最大のdを求める
            for (auto it = l_; it != r_; it++) {
                chmax(u, it->d);
            }

            d = u + h;
            horizon.erase(l_, r_);

            // 左側の部分区間再挿入
            // l_l, r_rが正しい区間を指しているか不明
            // 下記ではl_取得前に*l_したりしていたがここでは簡略化
            // 本来はl_やr_取得前に*l_や*prev(r_)を格納しておくべき
            // (元コードと同じ構造にするとテストが複雑になるため簡略化)

            // 左端が食い込む場合
            // ※テストではhorizonが (0, max_,0) のみなので、
            //   l_l.l < l となるか検証。
            // 本来なら l_l = *(l_) する前にl_を一つ戻す等が必要。
            // 今回はバグを起こすために何もしないでこのまま。
            // horizon.emplace_back(l_l.l, l, l_l.d) のような処理本来必要

            // 中央に新しい区間
            {
                Nodo_horizon node(l, r, d);
                auto it = lower_bound(horizon.begin(), horizon.end(), node);
                horizon.insert(it, node);
            }

            // 右端余り区間
            // horizon.emplace_back(r, r_r.r, r_r.d)
            // のような処理が本来必要だが省略

            r_vec.emplace_back(r);

            chmax(W, r);
            chmax(H, d);
            if (W + H > lim) {
                return lim + 1;
            }
        }
    }

    return W + H;
}

int main() {
    // テスト:
    // horizon = [(0, max_, 0)] から始める
    // actions: 縦にスライド (d="U"), b=-1(基準なし), r=0(回転なし)
    // wh: (w,h)
    // 下記のようなテストでバグ発生を狙う
    //
    // 1回目: l=0に幅5の長方形を置く
    // 2回目: l=5に幅5の長方形を置く ->
    // ここで最初の区間(0,1000000000)を分割する必要があり、
    //  lower_bound((5,5,0)) が期待通りに区間を見つけられない可能性あり。

    N = 2;
    actions.resize(N);
    // 全て U 方向、b=-1, r=0
    actions[0] = {-1, 0, "U"};
    actions[1] = {-1, 0, "U"};

    vector<pair<int, int>> wh = {
        {5, 10}, // w=5,h=10
        {5, 10}  // w=5,h=10
    };

    // state_l, state_m, state_r:
    // シンプルに、最初のものを最初の行に、その次を同じ行にという感じでテスト
    vector<deque<int>> state_l = {{0}, {1}};
    vector<deque<int>> state_m = {{}, {}};
    vector<deque<int>> state_r = {{}, {}};

    int limit = 1000000000;
    int res = evaluate(limit, wh, state_l, state_m, state_r);
    cout << "Result: " << res << endl;
    return 0;
}

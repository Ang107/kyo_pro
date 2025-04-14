#include <atcoder/dsu>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;

//------------------------------------------------------------------------------
// 1. 乱数生成: xorshift + シャッフル
//------------------------------------------------------------------------------
static uint64_t s_xorshift64_state = 88172645463325252ULL;
uint64_t xorshift64() {
    uint64_t &y = s_xorshift64_state;
    y ^= (y << 13);
    y ^= (y >> 7);
    y ^= (y << 17);
    return y;
}

static uint32_t s_xorshift32_state = 2463534242;
uint32_t xorshift32() {
    uint32_t &y = s_xorshift32_state;
    y ^= (y << 13);
    y ^= (y >> 17);
    y ^= (y << 5);
    return y;
}

// 配列を乱数でシャッフル (Knuth-Fisher-Yates)
template <typename T> void random_shuffle_xor(vector<T> &arr) {
    for (int i = (int)arr.size() - 1; i >= 1; i--) {
        int r = (int)(xorshift32() % (i + 1));
        if (r != i) {
            std::swap(arr[i], arr[r]);
        }
    }
}

// [0, n) の一様乱数を返す (n <= 0 なら 0)
int randrange(int n) {
    if (n <= 0)
        return 0;
    return (int)(xorshift32() % n);
}

//------------------------------------------------------------------------------
// 2. MST 構築 (Kruskall など) : Pythonでの edges[::-1] の流れを再現
//    - 距離順にソートして Union-Find でマージ
//------------------------------------------------------------------------------
struct Edge {
    long double dist;
    int u, v;
};

// edges は「距離大きい順」にソート済みとして、後ろから見る = 距離小さい順
// MST (adjacency) を構築
//  - adjacency[u] = u と直接つながっている頂点一覧
void buildMST(const vector<Edge> &edges, int N,
              vector<vector<int>> &adjacency) {
    dsu uf(N);
    // もともと adjacency は全頂点 empty でOK
    // edgesを後ろから(=距離小さい順)
    for (int idx = (int)edges.size() - 1; idx >= 0; idx--) {
        int u = edges[idx].u;
        int v = edges[idx].v;
        if (!uf.same(u, v)) {
            uf.merge(u, v);
            adjacency[u].push_back(v);
            adjacency[v].push_back(u);
        }
    }
}

//------------------------------------------------------------------------------
// 3. cand 生成 (BFS or DFS mix):
// Pythonで「候補頂点を取得」→「辺を除去」する流れ
//    - adjacency からランダムに辿り L 個まで収集
//    - 使った辺は一旦 adjacency から削除
//------------------------------------------------------------------------------
vector<int>
getCandidateByMixedSearch(vector<vector<int>> &adjacency, // 参照(削除操作あり)
                          int startNode,                  // 開始ノード
                          int L) {
    int N = (int)adjacency.size();
    vector<int> candidateSet;
    candidateSet.push_back(startNode);

    deque<int> dq;
    dq.push_back(startNode);
    vector<bool> visited(N, false);
    visited[startNode] = true;

    vector<pair<int, int>> usedEdges; // 後で adjacency から削除

    while ((int)candidateSet.size() < L && !dq.empty()) {
        // BFS or DFS を混合
        int current;
        if (randrange(2) == 0) {
            current = dq.front();
            dq.pop_front();
        } else {
            current = dq.back();
            dq.pop_back();
        }
        // ランダムに巡回
        vector<int> neighbors = adjacency[current];
        random_shuffle_xor(neighbors);
        for (int nxt : neighbors) {
            if (!visited[nxt] && (int)candidateSet.size() < L) {
                visited[nxt] = true;
                dq.push_back(nxt);
                candidateSet.push_back(nxt);
                usedEdges.push_back({current, nxt});
            }
        }
    }

    // adjacency から usedEdges を削除
    //  おおざっぱに O(deg) かかりますが、デモ用なので単純実装
    for (auto &ed : usedEdges) {
        int a = ed.first;
        int b = ed.second;
        // a 側
        auto &va = adjacency[a];
        va.erase(remove(va.begin(), va.end(), b), va.end());
        // b 側
        auto &vb = adjacency[b];
        vb.erase(remove(vb.begin(), vb.end(), a), vb.end());
    }

    return candidateSet;
}

//------------------------------------------------------------------------------
// 4. 入出力 (インタラクティブ想定)
//    - "? size cand[0] cand[1] ..." を出力
//    - (size -1) 本の辺を入力で受け取り adjacency に再追加
//------------------------------------------------------------------------------
void queryAndRestoreEdges(const vector<int> &cand,
                          vector<vector<int>> &adjacency) {
    // 出力: "? len(cand) cand..."
    cout << "? " << (int)cand.size();
    for (int x : cand)
        cout << " " << x;
    cout << "\n";
    cout.flush();

    // 入力 (len(cand)-1) 行
    //  -> (u, v) を adjacency に再追加
    for (int i = 0; i < (int)cand.size() - 1; i++) {
        int u, v;
        cin >> u >> v;
        adjacency[u].push_back(v);
        adjacency[v].push_back(u);
    }
}

//------------------------------------------------------------------------------
// 5. メイン処理
//------------------------------------------------------------------------------
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 入力1: N,M,Q,L,W
    int N, M, Q, L, W;
    cin >> N >> M >> Q >> L >> W;

    // 入力2: G (サイズ M)
    vector<int> groupSizes(M);
    for (int i = 0; i < M; i++) {
        cin >> groupSizes[i];
    }

    // 入力3: sq, pos
    //  sq は (lx,rx,ly,ry)、pos はその中心
    vector<array<long long, 4>> sq(N);
    vector<pair<long double, long double>> pos(N);
    for (int i = 0; i < N; i++) {
        long long lx, rx, ly, ry;
        cin >> lx >> rx >> ly >> ry;
        sq[i] = {lx, rx, ly, ry};
        long double cx = ((long double)lx + (long double)rx) / 2.0L;
        long double cy = ((long double)ly + (long double)ry) / 2.0L;
        pos[i] = {cx, cy};
    }

    // dis[][] 計算
    vector<vector<long double>> dist(N, vector<long double>(N, 0.0L));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            long double dx = pos[i].first - pos[j].first;
            long double dy = pos[i].second - pos[j].second;
            dist[i][j] = sqrtl(dx * dx + dy * dy);
        }
    }

    // edges 作成
    vector<Edge> edgeList;
    edgeList.reserve(N * (N - 1) / 2);
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            edgeList.push_back({dist[i][j], i, j});
        }
    }
    // Python で reverse=True (大きい順)
    sort(edgeList.begin(), edgeList.end(), [](auto &a, auto &b) {
        return a.dist > b.dist; // 距離大きい順
    });

    // MST 構築
    vector<vector<int>> adjacency(N);
    buildMST(edgeList, N, adjacency);

    // first_times, second_times, query_times 計算
    int first_times = 100;
    int second_times = Q - first_times;
    vector<int> queryCount(M, 0);

    {
        long long sumQ = 0;
        for (int i = 0; i < M; i++) {
            // int(second_times * (G[i]/N)) 相当
            long double factor = (long double)groupSizes[i] / (long double)N;
            long double val = (long double)second_times * factor;
            int c = (int)floor(val);
            queryCount[i] = c;
            sumQ += c;
        }
        first_times = Q - sumQ;
        if (first_times < 0)
            first_times = 0;
    }

    //--------------------------------------------------------------------------
    // (A) 全体の最適化 ( first_times 回 )
    //--------------------------------------------------------------------------
    for (int loop = 0; loop < first_times; loop++) {
        // 1つランダム頂点を start に
        int startNode = randrange(N);
        // BFS/DFS混在で L 個収集
        vector<int> cand = getCandidateByMixedSearch(adjacency, startNode, L);
        // インタラクティブ問合せ + (len(cand)-1) 辺追加
        queryAndRestoreEdges(cand, adjacency);
    }

    //--------------------------------------------------------------------------
    // (B) 分割 (Python で used や vv, ee を管理していた)
    //--------------------------------------------------------------------------
    vector<bool> used(N, false);
    vector<vector<int>> partitionSets;          // vv
    vector<vector<vector<int>>> partitionEdges; // ee (各グループの adjacency)

    // edgeList は後で「小さい順」に使いたいので逆から見る
    //  ただし MST 構築時にも使ったので、このまま再利用可
    //  ここでは Python のコード同様 edges[::-1] 的に参照する

    for (int group_i = 0; group_i < M; group_i++) {
        int groupSize = groupSizes[group_i];

        // 開始ノード s (usedでなく、隣接のunusedが1つあるところ)を探す
        int s = -1;
        for (int nidx = 0; nidx < N; nidx++) {
            if (!used[nidx]) {
                s = nidx; // fallback
                int cnt = 0;
                for (int nx : adjacency[nidx]) {
                    if (!used[nx])
                        cnt++;
                }
                if (cnt == 1) {
                    s = nidx;
                    break;
                }
            }
        }
        if (s < 0) {
            // 全usedかもしれない → 適当に0番とか
            s = 0;
        }

        // BFS で groupSize 個取る
        vector<int> vs;
        vs.push_back(s);
        used[s] = true;

        deque<int> dq;
        dq.push_back(s);
        vector<vector<int>> es(N); // 各頂点につながる辺(同グループ内)

        while (!dq.empty()) {
            int v = dq.front();
            dq.pop_front();
            for (int nx : adjacency[v]) {
                if (!used[nx] && (int)vs.size() < groupSize) {
                    used[nx] = true;
                    vs.push_back(nx);
                    dq.push_back(nx);
                    es[v].push_back(nx);
                    es[nx].push_back(v);
                }
            }
        }

        // 未使用ノード同士をさらに接続するために dsu
        {
            dsu uf2(N);
            // used==false で MST上繋がってるところ
            for (int j = 0; j < N; j++) {
                for (int nx : adjacency[j]) {
                    if (!used[j] && !used[nx]) {
                        uf2.merge(j, nx);
                    }
                }
            }
            // edgeList: 距離小さい順に (後ろから) チェックして繋げる
            for (int idx = (int)edgeList.size() - 1; idx >= 0; idx--) {
                int a = edgeList[idx].u;
                int b = edgeList[idx].v;
                if (!used[a] && !used[b]) {
                    if (!uf2.same(a, b)) {
                        uf2.merge(a, b);
                        // adjacency に追加
                        adjacency[a].push_back(b);
                        adjacency[b].push_back(a);
                    }
                }
            }
        }

        partitionSets.push_back(vs);
        partitionEdges.push_back(es);
    }

    //--------------------------------------------------------------------------
    // (C) 分割ごとの最適化 ( queryCount[i] 回 )
    //--------------------------------------------------------------------------
    for (int i = 0; i < M; i++) {
        int t = queryCount[i];
        for (int loop = 0; loop < t; loop++) {
            auto &currentSet = partitionSets[i];
            if (currentSet.empty())
                continue;

            // ランダムに1つ選んで BFS/DFS mix
            int startNode = currentSet[randrange((int)currentSet.size())];
            // adjacency は partitionEdges[i]
            vector<int> &adj = partitionEdges[i][startNode];
            // getCandidateByMixedSearch の簡易版を作る
            //  → ここでは関数化せず、インライン書き
            vector<int> cand;
            cand.push_back(startNode);

            deque<int> dq;
            dq.push_back(startNode);
            vector<bool> visited(N, false);
            visited[startNode] = true;

            vector<pair<int, int>> usedEdges;
            while ((int)cand.size() < L && !dq.empty()) {
                int v;
                if (randrange(2) == 0) {
                    v = dq.front();
                    dq.pop_front();
                } else {
                    v = dq.back();
                    dq.pop_back();
                }
                // partitionEdges[i][v] をシャッフル
                vector<int> neighbors = partitionEdges[i][v];
                random_shuffle_xor(neighbors);
                for (int nx : neighbors) {
                    if (!visited[nx] && (int)cand.size() < L) {
                        visited[nx] = true;
                        dq.push_back(nx);
                        cand.push_back(nx);
                        usedEdges.push_back({v, nx});
                    }
                }
            }
            // usedEdges を partitionEdges[i] から削除
            for (auto &ed : usedEdges) {
                int a = ed.first;
                int b = ed.second;
                auto &va = partitionEdges[i][a];
                auto &vb = partitionEdges[i][b];
                va.erase(remove(va.begin(), va.end(), b), va.end());
                vb.erase(remove(vb.begin(), vb.end(), a), vb.end());
            }

            // インタラクティブ問い合わせ
            cout << "? " << (int)cand.size();
            for (auto &c : cand)
                cout << " " << c;
            cout << "\n";
            cout.flush();

            // (len(cand)-1) 辺を入力
            for (int k = 0; k < (int)cand.size() - 1; k++) {
                int u, v;
                cin >> u >> v;
                partitionEdges[i][u].push_back(v);
                partitionEdges[i][v].push_back(u);
            }
        }
    }

    //--------------------------------------------------------------------------
    // (D) 結果出力
    //--------------------------------------------------------------------------
    cout << "!\n";
    // 各グループごとに:
    //   1) partitionSets[i] のノード一覧
    //   2) partitionEdges[i] で j<k の辺を出力
    for (int i = 0; i < M; i++) {
        // グループ i の頂点一覧
        for (int node : partitionSets[i]) {
            cout << node << " ";
        }
        cout << "\n";

        // partitionEdges[i] の辺リスト出力
        for (int j = 0; j < N; j++) {
            for (int nxt : partitionEdges[i][j]) {
                if (j < nxt) {
                    cout << j << " " << nxt << "\n";
                }
            }
        }
        cout.flush();
    }

    return 0;
}

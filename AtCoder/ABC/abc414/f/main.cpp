#include <bits/stdc++.h>
using namespace std;

constexpr int INF32 = std::numeric_limits<int>::max();

/* oriented-edge を 64 bit 符号無し整数にパック */
static inline uint64_t pack(int v, int frm) {
    return (static_cast<uint64_t>(v) << 32) | static_cast<uint32_t>(frm);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;

        /* 木の隣接リスト（0-indexed） */
        std::vector<std::vector<int>> g(n);
        for (int i = 0; i < n - 1; ++i) {
            int u, v;
            cin >> u >> v;
            --u;
            --v;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        /* visited[edge][mod] = 最短距離（辺数） */
        unordered_map<uint64_t, std::vector<int>> visited;
        auto ensure_vec = [&](uint64_t key) -> std::vector<int> & {
            auto &vec = visited[key];
            if (vec.empty())
                vec.assign(k, INF32);
            return vec;
        };

        /* BFS: (v, mod, frm) */
        deque<tuple<int, int, int>> deq;
        {
            uint64_t rootEdge = pack(0, 0);
            ensure_vec(rootEdge)[0] = 0;
            deq.emplace_back(0, 0, 0);
        }

        while (!deq.empty()) {
            auto [v, mod, frm] = deq.front();
            deq.pop_front();
            uint64_t curKey = pack(v, frm);
            int curDist = visited[curKey][mod];

            for (int nxt : g[v]) {
                if (nxt == frm)
                    continue; // Python と同等の枝刈り
                int nmod = (mod + 1) % k;
                uint64_t nxtKey = pack(nxt, v);
                auto &vecNxt = ensure_vec(nxtKey);
                if (vecNxt[nmod] != INF32)
                    continue; // 既訪問

                vecNxt[nmod] = curDist + 1;

                if (nmod == 0) {
                    /* frm = nxt で “リセット” する特殊分岐 */
                    uint64_t resetKey = pack(nxt, nxt);
                    ensure_vec(resetKey)[0] = curDist + 1;
                    deq.emplace_back(nxt, 0, nxt);
                } else {
                    deq.emplace_back(nxt, nmod, v);
                }
            }
        }

        /* 答え生成 */
        std::vector<int> ans(n - 1, -1);
        for (int i = 1; i < n; ++i) {
            int best = INF32;
            for (int j : g[i]) {
                uint64_t key = pack(i, j);
                auto it = visited.find(key);
                if (it != visited.end() && it->second[0] != INF32) {
                    best = std::min(best, it->second[0] / k);
                }
            }
            if (best != INF32)
                ans[i - 1] = best;
        }

        /* 出力 */
        for (int i = 0; i < n - 1; ++i) {
            if (i)
                cout << ' ';
            cout << ans[i];
        }
        cout << '\n';
    }
    return 0;
}
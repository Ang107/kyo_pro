#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define repr(i, a, b) for (int i = a; i < b; i++)
#define rep(i, n) for (int i = 0; i < n; i++)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> P;
#define mod 998244353
random_device rnd;
mt19937 mt(rnd());

ll dx[5] = {1, 0, -1, 0, 0};
ll dy[5] = {0, -1, 0, 1, 0};

ll pc(ll x) { return __builtin_popcount(x); }

// ll chmin(ll& a,ll b){return a=min(a,b);}

int chmin(int &a, int b) { return a = min(a, b); }
int chmax(int &a, int b) { return a = max(a, b); }

struct Edge {
    int score, nagasa, z;
    double bai;
    Edge(int score, int nagasa, int z, double bai)
        : score(score), nagasa(nagasa), z(z), bai(bai) {}

    bool operator<(const Edge &other) const { return score < other.score; }
};

struct status {
    int l, ma, id, kazu;
    status(int l = 0, int ma = 0, int id = -1, int kazu = 0)
        : l(l), ma(ma), id(id), kazu(kazu) {}
};

// 変数
int ti;
int N;
int T;
int t;
int sigma;
int new_sigma;
vector<int> W;
vector<int> H;
vector<int> real_w;
vector<int> real_h;
vector<int> dw;
vector<int> dh;
int total_w = 0;
int total_h = 0;
ll total_s = 0;
int kijun;
const int INF = 1001001001;
vector<Edge> ans;
vector<int> max_length;
int ave_length = 0;
double kasan = 0.005;
int min_length = INF;

bool test = false; // テスト用
int d_cnt = 0;

void output(int p, int r, char d, int b) {
    cout << p << ' ' << r << ' ' << d << ' ' << b << endl;
}

void input() {
    cin >> N >> T >> sigma;
    // if(N<=50) kasan=0.005;
    // else kasan=0.010;

    int nokori = T - 15;
    new_sigma = sigma * N / (nokori + N);

    for (int i = 0; i < N; i++) {
        int w, h;
        cin >> w >> h;
        W.emplace_back(w);
        H.emplace_back(h);
    }

    if (test) {
        for (int i = 0; i < N; i++) {
            int w, h;
            cin >> w >> h;
            real_w.emplace_back(w);
            real_h.emplace_back(h);
        }
        for (int i = 0; i < T; i++) {
            int w, h;
            cin >> w >> h;
            dw.emplace_back(w);
            dh.emplace_back(h);
        }
    }

    /*
    if(flag){
      for(int i=0;i<N;i++){
        cout << 1 << endl;
        cout << i << ' ' << 0 << ' ' << 'U' << ' ' << -1 << endl;
        int cinw,cinh;
        cin >> cinw >> cinh;
        W[i]=(W[i]+cinw)/2;
        H[i]=(H[i]+cinh)/2;
        T--;
      }
    }

    t=T;
    */

    if (nokori > 0) {
        for (int i = 0; i < N; i++) {
            int kazu = (nokori + N - i - 1) / (N - i);
            for (int j = 0; j < kazu; j++) {
                cout << 1 << endl;
                int cinw, cinh;
                output(i, 0, 'U', -1);
                if (test) {
                    cinw = real_w[i] + dw[d_cnt];
                    cinh = real_h[i] + dh[d_cnt];
                    d_cnt++;
                } else {
                    cin >> cinw >> cinh;
                }
                W[i] += cinw;
                H[i] += cinh;
            }
            W[i] /= (kazu + 1);
            H[i] /= (kazu + 1);
            nokori -= kazu;
        }
    }

    t = min(15, T);

    // 平均の長さを計算
    for (int i = 0; i < N; i++) {
        ave_length += W[i];
        ave_length += H[i];
    }
    ave_length /= 2 * N;

    // 最短の辺を計算
    for (int i = 0; i < N; i++) {
        min_length = min(min_length, W[i]);
        min_length = min(min_length, H[i]);
    }

    for (int i = 0; i < N; i++) {
        total_w += W[i];
        total_h += H[i];
        total_s += 1ll * W[i] * 1ll * H[i];
    }
    // kijun=round(sqrt(N));
    kijun = round(sqrt(total_s * 1.2));
}

void pre() {
    // 残りの最大の長さを計算
    max_length.resize(N, 0);
    max_length[N - 1] = max(H[N - 1], W[N - 1]);
    for (int i = N - 2; i >= 0; i--) {
        max_length[i] += max_length[i + 1] + max(H[i], W[i]);
    }
}

// 区間のmaxを返す
int prod_max(set<pair<int, int>> &s, int l, int r) {
    int res = -1;
    auto its = s.lower_bound(make_pair(l, 0));
    auto itf = s.lower_bound(make_pair(r, 0));
    res = (*itf).second;
    while (its != itf) {
        chmax(res, (*its).second);
        its++;
    }
    return res;
}

// 区間を更新
void apply(set<pair<int, int>> &s, int l, int r, int f) {
    auto its = s.lower_bound(make_pair(l, 0));
    auto itf = s.lower_bound(make_pair(r, 0));
    auto itss = its;
    itss--;
    if ((*itss).first != l - 1)
        s.emplace(l - 1, (*its).second);
    while (its != itf) {
        auto it = its;
        its++;
        s.erase(it);
    }
    if ((*itf).first == r)
        s.erase(itf);
    s.emplace(r, f);
    return;
}

// 先読み計算用
int pre_cal(int z, double bai, set<pair<int, int>> S, int nagasa, int now_j,
            vector<status> g, int R, int max_kai) {

    // 実際に配置する
    auto arrange = [&](int now_kai, int yoko, int tate, int id) {
        apply(S, g[now_kai].l, g[now_kai].l + yoko - 1, tate);
        chmax(g[now_kai].ma, tate);
        g[now_kai].l += yoko;
        g[now_kai].id = id;
        g[now_kai].kazu++;
        chmax(max_kai, now_kai);
    };

    {
        int kai = R / 2;
        int r = R % 2;
        if (r == 0) {
            int new_ma =
                prod_max(S, g[kai].l, g[kai].l + W[now_j] - 1) + H[now_j];
            arrange(kai, W[now_j], new_ma, now_j);
        } else {
            int new_ma =
                prod_max(S, g[kai].l, g[kai].l + H[now_j] - 1) + W[now_j];
            arrange(kai, H[now_j], new_ma, now_j);
        }
    }

    now_j++;

    for (int j = now_j; j < N; j++) {

        for (int kai = 0; kai <= max_kai + 1; kai++) {
            if (kai == max_kai + 1) {
                if (z >> (kai - 1) & 1) {
                    int new_ma =
                        prod_max(S, g[kai].l, g[kai].l + W[j] - 1) + H[j];
                    arrange(kai, W[j], new_ma, j);
                    break;
                } else {
                    int new_ma =
                        prod_max(S, g[kai].l, g[kai].l + H[j] - 1) + W[j];
                    arrange(kai, H[j], new_ma, j);
                    break;
                }
            }
            if (g[kai].l < g[kai + 1].l + new_sigma)
                continue;
            int noko = nagasa - g[kai].l;
            if ((H[j] <= noko) && (W[j] <= noko)) {
                int new_h = H[j] + prod_max(S, g[kai].l, g[kai].l + W[j] - 1);
                int new_w = W[j] + prod_max(S, g[kai].l, g[kai].l + H[j] - 1);
                int a, b;
                if (new_w >= g[kai].ma)
                    a = round((new_w - g[kai].ma) *
                              (bai + 0.50 * g[kai].l / nagasa));
                else
                    a = g[kai].ma - new_w;
                if (new_h >= g[kai].ma)
                    b = round((new_h - g[kai].ma) *
                              (bai + 0.50 * g[kai].l / nagasa));
                else
                    b = g[kai].ma - new_h;
                if (a < b) {
                    arrange(kai, H[j], new_w, j);
                    break;
                } else {
                    arrange(kai, W[j], new_h, j);
                    break;
                }
            } else if (H[j] <= noko) {
                int new_w = W[j] + prod_max(S, g[kai].l, g[kai].l + H[j] - 1);
                if (new_w <= g[kai].ma) {
                    arrange(kai, H[j], new_w, j);
                    break;
                }
            } else if (W[j] <= noko) {
                int new_h = H[j] + prod_max(S, g[kai].l, g[kai].l + W[j] - 1);
                if (new_h <= g[kai].ma) {
                    arrange(kai, W[j], new_h, j);
                    break;
                }
            }
        }
    }
    int max_r = 0;
    for (int i = 0; i <= max_kai; i++)
        chmax(max_r, g[i].l);
    return max_r + prod_max(S, 0, INF);
}

// 左から右へ埋めていく
void cal1(int nagasa, int z, double bai) {
    // 疑似遅延セグ木生成
    set<pair<int, int>> S;
    S.emplace(-1, 0);
    S.emplace(INF, 0);

    t--;
    int nokori = nagasa;
    cout << N << endl;
    vector<status> g(50);
    int min_kai = 0;
    int max_kai = -1;

    // 実際に配置する
    auto arrange = [&](int now_kai, int yoko, int tate, int id) {
        apply(S, g[now_kai].l, g[now_kai].l + yoko - 1, tate);
        chmax(g[now_kai].ma, tate);
        g[now_kai].l += yoko;
        g[now_kai].id = id;
        g[now_kai].kazu++;
        chmax(max_kai, now_kai);
    };

    for (int j = 0; j < N; j++) {

        vector<P> score;
        for (int kai = min_kai; kai <= max_kai + 1; kai++) {
            if (g[kai].l > 200000 && g[kai].l < g[kai + 1].l + new_sigma) {
                min_kai = kai + 1;
                continue;
            }
            int noko = nagasa - g[kai].l;
            if (kai == max_kai + 1) {
                if (W[j] <= noko) {
                    int a =
                        pre_cal(z, bai, S, nagasa, j, g, kai * 2, max_kai + 1);
                    score.emplace_back(a, kai * 2);
                }
                if (H[j] <= noko) {
                    int a = pre_cal(z, bai, S, nagasa, j, g, kai * 2 + 1,
                                    max_kai + 1);
                    score.emplace_back(a, kai * 2 + 1);
                }
            } else {
                if (W[j] <= noko && H[j] <= noko) {
                    int new_h =
                        H[j] + prod_max(S, g[kai].l, g[kai].l + W[j] - 1);
                    int new_w =
                        W[j] + prod_max(S, g[kai].l, g[kai].l + H[j] - 1);
                    int a, b;
                    if (new_w >= g[kai].ma)
                        a = round((new_w - g[kai].ma) *
                                  (bai + 0.50 * g[kai].l / nagasa));
                    else
                        a = g[kai].ma - new_w;
                    if (new_h >= g[kai].ma)
                        b = round((new_h - g[kai].ma) *
                                  (bai + 0.50 * g[kai].l / nagasa));
                    else
                        b = g[kai].ma - new_h;
                    if (a >= b) {
                        int a =
                            pre_cal(z, bai, S, nagasa, j, g, kai * 2, max_kai);
                        score.emplace_back(a, kai * 2);
                    } else {
                        int a = pre_cal(z, bai, S, nagasa, j, g, kai * 2 + 1,
                                        max_kai);
                        score.emplace_back(a, kai * 2 + 1);
                    }
                } else if (W[j] <= noko) {
                    int a = pre_cal(z, bai, S, nagasa, j, g, kai * 2, max_kai);
                    score.emplace_back(a, kai * 2);
                } else if (H[j] <= noko) {
                    int a =
                        pre_cal(z, bai, S, nagasa, j, g, kai * 2 + 1, max_kai);
                    score.emplace_back(a, kai * 2 + 1);
                }
            }
        }

        sort(score.begin(), score.end());
        int kai = score[0].second / 2;
        int r = score[0].second % 2;

        cout << j << ' ' << r << ' ' << 'U' << ' ' << g[kai].id << endl;
        if (r == 0) {
            int new_ma = prod_max(S, g[kai].l, g[kai].l + W[j] - 1) + H[j];
            arrange(kai, W[j], new_ma, j);
        } else {
            int new_ma = prod_max(S, g[kai].l, g[kai].l + H[j] - 1) + W[j];
            arrange(kai, H[j], new_ma, j);
        }
    }

    int cinw, cinh;
    if (test) {
        cinw = 0;
        cinh = 0;
    } else {
        cin >> cinw >> cinh;
    }
}

void solve(int z, double bai) {
    for (double i = 0.85; i <= 1.05; i += kasan) {
        // 疑似遅延セグ木生成
        set<pair<int, int>> S;
        S.emplace(-1, 0);
        S.emplace(INF, 0);

        int nagasa = round(i * kijun);
        ans.emplace_back(0, nagasa, z, bai);
        int nokori = nagasa;

        int max_r = 0;
        vector<status> g(50);
        int min_kai = 0;
        int max_kai = -1;

        // 実際に配置する
        auto arrange = [&](int now_kai, int yoko, int tate, int id) {
            apply(S, g[now_kai].l, g[now_kai].l + yoko - 1, tate);
            chmax(g[now_kai].ma, tate);
            g[now_kai].l += yoko;
            g[now_kai].id = id;
            g[now_kai].kazu++;
            chmax(max_kai, now_kai);
        };

        for (int j = 0; j < N; j++) {

            vector<P> score;
            for (int kai = min_kai; kai <= max_kai + 1; kai++) {
                if (g[kai].l > 200000 && g[kai].l < g[kai + 1].l + new_sigma) {
                    min_kai = kai + 1;
                    continue;
                }
                int noko = nagasa - g[kai].l;
                if (kai == max_kai + 1) {
                    if (W[j] <= noko) {
                        int a = pre_cal(z, bai, S, nagasa, j, g, kai * 2,
                                        max_kai + 1);
                        score.emplace_back(a, kai * 2);
                    }
                    if (H[j] <= noko) {
                        int a = pre_cal(z, bai, S, nagasa, j, g, kai * 2 + 1,
                                        max_kai + 1);
                        score.emplace_back(a, kai * 2 + 1);
                    }
                } else {
                    if (W[j] <= noko && H[j] <= noko) {
                        int new_h =
                            H[j] + prod_max(S, g[kai].l, g[kai].l + W[j] - 1);
                        int new_w =
                            W[j] + prod_max(S, g[kai].l, g[kai].l + H[j] - 1);
                        int a, b;
                        if (new_w >= g[kai].ma)
                            a = round((new_w - g[kai].ma) *
                                      (bai + 0.50 * g[kai].l / nagasa));
                        else
                            a = g[kai].ma - new_w;
                        if (new_h >= g[kai].ma)
                            b = round((new_h - g[kai].ma) *
                                      (bai + 0.50 * g[kai].l / nagasa));
                        else
                            b = g[kai].ma - new_h;
                        if (a >= b) {
                            int a = pre_cal(z, bai, S, nagasa, j, g, kai * 2,
                                            max_kai);
                            score.emplace_back(a, kai * 2);
                        } else {
                            int a = pre_cal(z, bai, S, nagasa, j, g,
                                            kai * 2 + 1, max_kai);
                            score.emplace_back(a, kai * 2 + 1);
                        }
                    } else if (W[j] <= noko) {
                        int a =
                            pre_cal(z, bai, S, nagasa, j, g, kai * 2, max_kai);
                        score.emplace_back(a, kai * 2);
                    } else if (H[j] <= noko) {
                        int a = pre_cal(z, bai, S, nagasa, j, g, kai * 2 + 1,
                                        max_kai);
                        score.emplace_back(a, kai * 2 + 1);
                    }
                }
            }

            sort(score.begin(), score.end());
            int kai = score[0].second / 2;
            int r = score[0].second % 2;

            if (r == 0) {
                int new_ma = prod_max(S, g[kai].l, g[kai].l + W[j] - 1) + H[j];
                arrange(kai, W[j], new_ma, j);
            } else {
                int new_ma = prod_max(S, g[kai].l, g[kai].l + H[j] - 1) + W[j];
                arrange(kai, H[j], new_ma, j);
            }
        }
        for (int i = 0; i <= max_kai; i++)
            chmax(max_r, g[i].l);
        ans.back().score = max_r + prod_max(S, 0, INF);
    }
}

void result() {
    sort(ans.begin(), ans.end());
    map<int, int> flag;
    int now_id = 0;
    for (auto [score, nagasa, z, bai] : ans) {
        if (1.0 * (clock() - ti) / CLOCKS_PER_SEC >= 2.9)
            break;
        if (now_id == t)
            break;
        if (flag[score])
            continue;
        flag[score] = 1;
        cal1(nagasa, z, bai);
    }

    for (int i = now_id; i < t; i++) {
        cout << 1 << endl;
        cout << 0 << ' ' << 0 << ' ' << 'U' << ' ' << -1 << endl;
        int cinw, cinh;
        cin >> cinw >> cinh;
    }
}

int main() {
    ti = clock();
    input();
    pre();
    // if(N>50) return 0;
    vector<double> bai = {0.9, 1.1, 1.7, 1.3, 1.5};
    /*
    if(N<=50){
      for(int i=0;i<(1<<4);i++){
        for(double x:bai){
          solve(i,x);
        }
      }
    }else if(N<=70){
      for(int i=0;i<(1<<3);i++){
        for(double x:bai){
          solve(i,x);
        }
      }
    }else{
      for(int i=0;i<(1<<2);i++){
        for(double x:bai){
          solve(i,x);
        }
      }
    }
    */

    int now_id = 0;
    if (N >= 70) {
        while (1.0 * (clock() - ti) / CLOCKS_PER_SEC <= 2.6) {
            solve(now_id, bai[1]);
            if (1.0 * (clock() - ti) / CLOCKS_PER_SEC > 2.6)
                break;
            solve(now_id, bai[3]);
            now_id++;
        }
    } else if (N >= 40) {
        while (1.0 * (clock() - ti) / CLOCKS_PER_SEC <= 2.6) {
            solve(now_id, bai[1]);
            if (1.0 * (clock() - ti) / CLOCKS_PER_SEC > 2.6)
                break;
            solve(now_id, bai[3]);
            if (1.0 * (clock() - ti) / CLOCKS_PER_SEC > 2.6)
                break;
            solve(now_id, bai[4]);
            now_id++;
        }
    } else {
        while (1.0 * (clock() - ti) / CLOCKS_PER_SEC <= 2.6) {
            solve(now_id, bai[0]);
            if (1.0 * (clock() - ti) / CLOCKS_PER_SEC > 2.6)
                break;
            solve(now_id, bai[2]);
            if (1.0 * (clock() - ti) / CLOCKS_PER_SEC > 2.6)
                break;
            solve(now_id, bai[1]);
            if (1.0 * (clock() - ti) / CLOCKS_PER_SEC > 2.6)
                break;
            solve(now_id, bai[3]);
            if (1.0 * (clock() - ti) / CLOCKS_PER_SEC > 2.6)
                break;
            solve(now_id, bai[4]);
            now_id++;
        }
    }

    /*
    for(int i=0;i<(1<<1);i++){
      for(double x:bai){
        solve(i,x);
      }
    }
    */

    result();

    return 0;
}

#include <iostream>
#include <vector>
#include <numeric>
#include <tuple>
#include <cmath>
#include <map>
#include <limits>
#include <random>
#include <chrono>
#include <set>
#include <algorithm>
#include <atcoder/segtree>
using namespace std;

void fastIO()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
}
std::tuple<int, int, int, std::vector<std::vector<int>>, double, int> Input()
{
    // 関数の実装...
    {
        fastIO();
        int W, D, N;
        cin >> W >> D >> N;

        vector<vector<int>> A(D, vector<int>(N));
        int temp, sum, max_amari = 0;
        double total_amari = 0;

        for (int i = 0; i < D; ++i)
        {
            sum = 0;
            for (int j = 0; j < N; ++j)
            {
                cin >> A[i][j];
                sum += A[i][j];
            }
            int amari = 1000000 - sum;
            total_amari += amari;
            max_amari = max(max_amari, amari);
        }

        double avr_amari = total_amari / D / 10000.0;

        return make_tuple(W, D, N, A, avr_amari, max_amari);
    }
}

tuple<vector<vector<int>>, int, bool> put(const vector<int> &a, const vector<int> &h, const vector<int> &height)
{
    bool isover = false;
    vector<int> w(h.size(), 0);
    vector<vector<int>> result;
    int cost = 0;

    for (auto it = a.rbegin(); it != a.rend(); ++it)
    {
        bool placed = false;
        double Hi = 1e18;
        tuple<int, int, vector<int>> bestPlacement;
        for (size_t j = 0; j < h.size(); ++j)
        {
            int width = ceil(static_cast<double>(*it) / h[j]);
            if (w[j] + width <= 1000)
            {
                placed = true;
                double hi = max(width, h[j]) / static_cast<double>(min(width, h[j]));
                if (Hi > hi)
                {
                    Hi = hi;
                    bestPlacement = make_tuple(j, width, vector<int>{height[j], w[j], height[j + 1], w[j] + width});
                }
            }
        }
        if (placed)
        {
            auto [j, width, tmp] = bestPlacement;
            w[j] += width;
            cost += h[j];
            result.push_back(tmp);
        }
        else
        {
            isover = true;
            bool spaceFound = false;
            tuple<int, int, vector<int>> bestOption;
            int maxArea = 0;
            for (size_t j = 0; j < h.size(); ++j)
            {
                int width = min(1000 - w[j], static_cast<int>(ceil(static_cast<double>(*it) / h[j])));
                int area = width * h[j];
                if (area > maxArea)
                {
                    maxArea = area;
                    spaceFound = true;
                    bestOption = make_tuple(j, width, vector<int>{height[j], w[j], height[j + 1], min(1000, w[j] + width)});
                }
            }
            if (!spaceFound)
            {
                // スペースが0の場合
                size_t tmp = 1;
                while (result[result.size() - tmp][3] - result[result.size() - tmp][1] < 2)
                {
                    tmp++;
                }

                result[result.size() - tmp][3] = result[result.size() - tmp][1] + 1;
                int deltaWidth = 1000 - result[result.size() - tmp][3];
                int deltaHeight = result[result.size() - tmp][2] - result[result.size() - tmp][0];
                cost += 1000 * (*it - deltaWidth * deltaHeight);
                cost += 1000 * deltaWidth * deltaHeight;
                cost += deltaHeight;

                vector<int> rs = result[result.size() - tmp];
                rs[1] = rs[3];
                rs[3] = 1000;
                result.push_back(rs);
            }
            else
            {
                // スペースが存在する場合
                auto [idx, width, rs] = bestOption;
                cost += 1000 * (*it - width * h[idx]);
                cost += h[idx];
                w[idx] = 1000;
                result.push_back(rs);
            }
        }
    }

    // Adjusting the cost based on adjacent 0-width partitions
    cost -= 1000;
    for (size_t i = 0; i < w.size() - 1; ++i)
    {
        if (w[i] == 0 && w[i + 1] == 0)
        {
            cost += 1000;
        }
    }

    return make_tuple(result, cost, isover);
}

tuple<vector<vector<vector<int>>>, int, vector<int>> get_ans(const vector<vector<int>> &A, const vector<int> &h, const vector<int> &height)
{
    vector<vector<vector<int>>> ans;
    int cost = 0;
    vector<int> over;

    for (size_t idx = 0; idx < A.size(); ++idx)
    {
        auto [rslt, c, is_over] = put(A[idx], h, height);
        ans.push_back(rslt);
        cost += c;
        if (is_over)
        {
            over.push_back(idx);
        }
    }

    return make_tuple(ans, cost, over);
}

void Output(const std::vector<std::vector<std::vector<int>>> &ans)
{
    for (const auto &i : ans)
    {
        for (const auto &j : i)
        {
            for (const auto &k : j)
            {
                std::cout << k << " ";
            }
            std::cout << "\n"; // 各内部ベクトルの後に改行を挿入
        }
    }
}

void most_right_line_change(std::vector<std::vector<std::vector<int>>> &ans)
{
    std::map<std::pair<int, int>, int> d;                     // (行, 高さ) -> 最も右の位置
    std::map<std::pair<int, int>, std::pair<int, int>> d_idx; // (行, 高さ) -> (i, j) のインデックス

    for (int i = 0; i < ans.size(); ++i)
    {
        for (int j = 0; j < ans[i].size(); ++j)
        {
            std::pair<int, int> key = {i, ans[i][j][0]};
            if (d[key] < ans[i][j][3])
            {
                d[key] = ans[i][j][3];
                d_idx[key] = {i, j};
            }
        }
    }

    // d_idxの内容を更新
    for (const auto &kv : d_idx)
    {
        auto [i, j] = kv.second;
        ans[i][j][3] = 1000; // 最も右の線の位置を1000に設定
    }
}

std::mt19937 rng(std::chrono::steady_clock::now().time_since_epoch().count()); // 乱数生成器

std::tuple<std::vector<std::vector<std::vector<int>>>, int, std::vector<int>, std::vector<int>, std::vector<int>> yamanobori(const std::vector<std::vector<int>> &A, std::vector<int> h, double time_limit)
{
    int cnt = 0;
    int lh = h.size();
    std::vector<int> height(lh + 1, 0);
    for (int i = 0; i < lh; ++i)
    {
        height[i + 1] = height[i] + h[i];
    }

    auto [ans, cost, over] = get_ans(A, h, height); // 仮のget_ans関数の呼び出し
    if (lh == 1)
    {
        return {ans, cost, over, h, height};
    }

    cost = std::numeric_limits<long long>::max();
    double bunsan = std::numeric_limits<double>::max();
    double avr = 1000.0 / lh;
    auto start_time = std::chrono::steady_clock::now();

    std::uniform_int_distribution<int> dist(0, lh - 1); // 高さのリストのインデックス用
    bool not_over_got = false;

    while (true)
    {
        int give_idx = dist(rng), take_idx = dist(rng);
        if (give_idx == take_idx)
        {
            continue;
        }

        std::vector<int> h_n = h;
        std::uniform_int_distribution<int> num_dist(0, h[give_idx] / 4);
        int num = num_dist(rng);
        h_n[give_idx] -= num;
        h_n[take_idx] += num;

        std::vector<int> height_n(lh + 1, 0);
        for (int i = 0; i < lh; ++i)
        {
            height_n[i + 1] = height_n[i] + h_n[i];
        }

        auto [ans_n, cost_n, over_n] = get_ans(A, h_n, height_n); // 新しい高さでget_ansを呼び出し

        if (over_n.empty())
        {
            not_over_got = true;
        }

        if (cost_n < cost)
        {
            double bunsan_n = std::accumulate(h_n.begin(), h_n.end(), 0.0, [avr](double acc, int x)
                                              { return acc + std::pow(x - avr, 2); });
            if (not_over_got && bunsan_n < bunsan)
            {
                bunsan = bunsan_n;
                h = h_n;
                height = height_n;
                cost = cost_n;
                ans = ans_n;
                over = over_n;
            }
            else if (!not_over_got)
            {
                h = h_n;
                height = height_n;
                cost = cost_n;
                ans = ans_n;
                over = over_n;
            }
        }

        cnt++;
        if (cnt % 100 == 0)
        {
            auto current_time = std::chrono::steady_clock::now();
            std::chrono::duration<double> elapsed = current_time - start_time;
            if (elapsed.count() > time_limit)
            {
                return {ans, cost, over, h, height};
            }
        }
    }
}
std::tuple<std::vector<std::vector<std::vector<int>>>, std::vector<std::vector<std::vector<int>>>, std::vector<int>, std::vector<int>, std::vector<int>, std::vector<int>> solve(int W, int D, int N, const std::vector<std::vector<int>> &A, int max_amari)
{
    int h_num = static_cast<int>(std::pow(N, 0.5) * 1.75);
    long long cost = std::numeric_limits<long long>::max();

    // 初期解生成
    std::vector<int> h = {1000}; // 縦のみの保険用
    auto [ans_hoken, cost_hoken, over_hoken, h_hoken, hight_hoken] = yamanobori(A, h, 0.0);

    int l = static_cast<int>(std::pow(N, 0.5)) - 1;
    int r = (max_amari < 20) ? N : (N / 2 + 1);

    std::vector<std::vector<std::vector<int>>> ans;
    std::vector<int> over;
    std::vector<int> rs_h, rs_hight;

    while (r - l > 1)
    {
        int m = (l + r) / 2;
        int h_num_n = m;
        double w_num = std::ceil(static_cast<double>(N) / h_num_n);

        std::vector<int> avr(h_num_n, 0);
        for (const auto &tmp : A)
        {
            for (int j = 0; j < N; ++j)
            {
                avr[j / static_cast<int>(w_num)] += tmp[j];
            }
        }

        std::vector<int> h;
        for (int i = 0; i < avr.size(); ++i)
        {
            avr[i] = static_cast<int>(std::pow(avr[i], 0.25));
        }
        int avr_sum = std::accumulate(avr.begin(), avr.end(), 0);
        for (int i = 0; i < avr.size() - 1; ++i)
        {
            h.push_back(1000 * avr[i] / avr_sum);
        }
        h.push_back(1000 - std::accumulate(h.begin(), h.end(), 0));

        auto [ans_n, cost_n, over_n, h_n, hight_n] = yamanobori(A, h, 0.4);
        if (!over_n.empty())
        {
            r = m;
        }
        else
        {
            l = m;
            if (cost > cost_n)
            {
                ans = ans_n;
                cost = cost_n;
                over = over_n;
                rs_h = h_n;
                rs_hight = hight_n;
            }
        }
    }

    // 解の最終調整
    std::set<int> over_hoken_set(over_hoken.begin(), over_hoken.end()), over_set(over.begin(), over.end());
    for (int idx : over_set)
    {
        if (over_hoken_set.find(idx) == over_hoken_set.end())
        {
            ans[idx] = ans_hoken[idx];
        }
    }

    return {ans, ans_hoken, rs_h, rs_hight, std::vector<int>(over_set.begin(), over_set.end()), over_hoken};
}

std::pair<bool, std::vector<std::vector<int>>> is_OK_v2(const std::vector<int> &same, const std::vector<int> &a, const std::vector<int> &h, const std::vector<int> &height)
{
    bool OK = true;
    std::vector<int> w(h.size(), 0);
    std::vector<std::vector<int>> rslt(a.size(), std::vector<int>(4, 0));
    std::vector<int> a_rev(a.rbegin(), a.rend()); // Reverse a

    for (size_t idx = 0; idx < a.size(); ++idx)
    {
        int i = (idx < same.size()) ? same[idx] : a_rev[idx];
        double Hi = 1e18;
        bool puted = false;
        std::tuple<int, int, std::vector<int>> rs;

        for (size_t j = 0; j < h.size(); ++j)
        {
            int width = (i + h[j] - 1) / h[j]; // Ceiling division
            if (w[j] + width <= 1000)
            {
                puted = true;
                double hi = static_cast<double>(std::max(width, h[j])) / std::min(width, h[j]);
                if (Hi > hi)
                {
                    Hi = hi;
                    rs = {j, width, {height[j], w[j], height[j + 1], w[j] + width}};
                }
            }
        }
        // 配置可能な場合
        if (puted)
        {
            auto [j, width, tmp] = rs;
            w[j] += width;
            rslt[idx] = tmp;
        }
        else
        {
            return {false, std::vector<std::vector<int>>{}};
        }
    }

    std::reverse(rslt.begin(), rslt.end()); // Reverse the result to match Python's behavior
    return {OK, rslt};
}

// 最大値を取得するための二項演算
int op(int a, int b)
{
    return std::max(a, b);
}

// 単位元
int e()
{
    return -1;
}

std::vector<int> change_ans_v2(const std::vector<std::vector<int>> &A, const std::vector<int> &h, const std::vector<int> &height, std::vector<std::vector<std::vector<int>>> &ans, const std::vector<int> &over, const std::vector<int> &Mode, bool test, const std::vector<std::vector<int>> &A_tenti)
{
    if (!over.empty())
    {
        return {-100, -100};
    }

    // セグメントツリーの初期化
    std::vector<atcoder::segtree<int, op, e>> ST;
    for (const auto &tenti : A_tenti)
    {
        ST.emplace_back(tenti.begin(), tenti.end());
    }

    std::vector<int> more_good(2, 0);
    for (int mode : Mode)
    {
        int Idx_l, Idx_r;
        if (mode == 1)
        {
            Idx_l = 0;
            Idx_r = 2;
        }
        else
        {
            Idx_l = A.size() - 2;
            Idx_r = A.size();
        }

        std::vector<int> prv_same;
        int prv_len_same = 0;

        while (true)
        {
            std::vector<int> same;
            int idx = A[0].size() - 1;

            while (idx >= 0)
            {
                int val = ST[idx].prod(Idx_l, Idx_r);
                same.push_back(val);

                bool is_ok = true;
                for (int i = Idx_l; i < Idx_r; ++i)
                {
                    auto [ok, rslt] = is_OK_v2(same, A[i], h, height);
                    if (!ok)
                    {
                        is_ok = false;
                        break;
                    }
                }
                if (is_ok)
                {
                    idx--;
                }
                else
                {
                    same.pop_back();
                    break;
                }
            }

            if (same.size() > A[0].size() / 2)
            {
                prv_len_same = same.size();
                prv_same = same;

                if (mode == 1)
                {
                    Idx_r++;
                }
                else
                {
                    Idx_l--;
                }

                if (Idx_r > ans.size() || Idx_l < 0)
                {
                    if (mode == 1)
                    {
                        more_good[0] += (Idx_r - Idx_l - 2) * prv_len_same;
                    }
                    else
                    {
                        more_good[1] += (Idx_r - Idx_l - 2) * prv_len_same;
                    }
                    break;
                }
            }
            else
            {
                if (mode == 1)
                {
                    more_good[0] += (Idx_r - Idx_l - 2) * prv_len_same;
                }
                else
                {
                    more_good[1] += (Idx_r - Idx_l - 2) * prv_len_same;
                }
                break;

                if (!test)
                {
                    if (mode == 1)
                    {
                        for (int i = Idx_l; i < Idx_r - 1; ++i)
                        {
                            auto [OK, rslt] = is_OK_v2(prv_same, A[i], h, height);
                            ans[i] = rslt;
                        }
                    }
                    else
                    {
                        for (int i = Idx_l + 1; i < Idx_r; ++i)
                        {
                            auto [OK, rslt] = is_OK_v2(prv_same, A[i], h, height);
                            ans[i] = rslt;
                        }
                    }
                }
                prv_same.clear();
                prv_len_same = 0;
                if (mode == 1)
                {
                    Idx_l = Idx_r - 1;
                    Idx_r = Idx_l + 2;
                }
                else
                {
                    Idx_r = Idx_l;
                    Idx_l = Idx_r - 2;
                }
                if (Idx_r > ans.size() || Idx_l < 0)
                {
                    break;
                }
            }
        }
    }

    return more_good;
}
pair<bool, vector<vector<int>>> is_OK(const vector<pair<int, int>> &same,
                                      const vector<int> &other,
                                      const vector<int> &Idx,
                                      const vector<int> &h,
                                      const vector<int> &height)
{
    bool isover = false;
    vector<int> w(h.size(), 0);
    vector<vector<int>> rslt(same.size() + other.size(), vector<int>(4, -1)); // Initialized with -1 for simplicity

    for (const auto &[i, idx] : same)
    {
        double Hi = numeric_limits<double>::max();
        bool puted = false;
        tuple<int, int, vector<int>> rs;

        for (int j = 0; j < h.size(); ++j)
        {
            int width = (i + h[j] - 1) / h[j]; // Ceiling division
            if (w[j] + width <= 1000)
            {
                puted = true;
                double hi = static_cast<double>(max(width, h[j])) / min(width, h[j]);
                if (Hi > hi)
                {
                    Hi = hi;
                    rs = make_tuple(j, width, vector<int>{height[j], w[j], height[j + 1], w[j] + width});
                }
            }
        }
        if (puted)
        {
            auto [j, width, tmp] = rs;
            w[j] += width;
            rslt[idx] = tmp;
        }
        else
        {
            isover = true;
            return make_pair(!isover, rslt);
        }
    }

    auto it = Idx.rbegin();
    for (auto i : other)
    {
        if (it == Idx.rend())
            break; // Safety check
        int idx = *it;
        double Hi = numeric_limits<double>::max();
        bool puted = false;
        tuple<int, int, vector<int>> rs;

        for (int j = 0; j < h.size(); ++j)
        {
            int width = (i + h[j] - 1) / h[j];
            if (w[j] + width <= 1000)
            {
                puted = true;
                double hi = static_cast<double>(max(width, h[j])) / min(width, h[j]);
                if (Hi > hi)
                {
                    Hi = hi;
                    rs = make_tuple(j, width, vector<int>{height[j], w[j], height[j + 1], w[j] + width});
                }
            }
        }
        if (puted)
        {
            auto [j, width, tmp] = rs;
            w[j] += width;
            rslt[idx] = tmp;
        }
        else
        {
            isover = true;
            return make_pair(!isover, rslt);
        }
        ++it;
    }

    reverse(rslt.begin(), rslt.end()); // Reverse the result to match Python's behavior
    return make_pair(!isover, rslt);
}

int main()
{
    auto [W, D, N, A, avr_amari, max_amari] = Input();
    auto [ans, ans_hoken, h, height, over, over_hoken] = solve(W, D, N, A, max_amari);
    Output(ans);

    // 以降で処理を行う

    return 0;
}
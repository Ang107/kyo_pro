#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <climits>

using namespace std;

#define INF INT_MAX
#define MOD 998244353

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(n), c(m);
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        cin >> b[i];
    for (int i = 0; i < m; ++i)
        cin >> c[i];

    vector<tuple<int, int, int>> ab(n);
    for (int i = 0; i < n; ++i)
    {
        ab[i] = make_tuple(a[i], b[i], a[i] - b[i]);
    }

    sort(ab.begin(), ab.end());

    vector<tuple<int, int, int>> ab_new;
    int tmp = INF;
    for (auto &[i, j, k] : ab)
    {
        if (tmp > k)
        {
            tmp = k;
            ab_new.emplace_back(i, j, k);
        }
    }

    ab = ab_new;

    vector<pair<int, int>> score;
    for (int idx = 0; idx < ab.size(); ++idx)
    {
        score.emplace_back(get<2>(ab[idx]), idx);
    }

    vector<int> a_sorted;
    for (auto &[i, j, k] : ab)
    {
        a_sorted.push_back(i);
    }

    vector<pair<int, int>> min_;
    for (auto &s : score)
    {
        if (min_.empty())
        {
            min_.push_back(s);
        }
        else
        {
            min_.push_back(min(min_.back(), s));
        }
    }

    long long ans = 0;
    for (int i : c)
    {
        int amari = i;
        while (amari > 0)
        {
            auto it = upper_bound(a_sorted.begin(), a_sorted.end(), amari);
            if (it == a_sorted.begin())
            {
                break;
            }
            int idx = distance(a_sorted.begin(), it) - 1;
            auto [min_value, min_idx] = min_[idx];
            int tmp = (amari - a_sorted[min_idx]) / min_value + 1;
            ans += tmp * 2;
            amari -= tmp * min_value;
        }
    }

    cout << ans << endl;

    return 0;
}

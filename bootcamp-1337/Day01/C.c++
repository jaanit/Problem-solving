#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdlib>

# define ll long long

using namespace std;

void solve()
{
	ll n, x; cin >> n >> x;

	map<ll, ll> mp;

	vector<ll> a(n+1, 0);
	for (ll i = 1; i <= n; i++)
	{
		cin >> a[i];
		a[i] += a[i - 1];
	}

	ll res = 0;
	for (ll i = 0; i <= n; i++)
	{
		ll re = a[i] - x;
		if (mp.find(re) != mp.end())
		{
			res += mp[re];
		}
		mp[a[i]] += 1;
	}
	cout << res << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	solve();
}


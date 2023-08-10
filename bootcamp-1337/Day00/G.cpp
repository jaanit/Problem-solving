#include <iostream>
#include <vector>
#include <map>

using namespace std;
#define ll long long

pair<ll, ll> solver(vector<ll>& a, ll x)
{
    map<ll, ll> mp;
    for (ll i = 0; i < a.size(); i++)
    {
        ll num = a[i];
        ll sum = x - num;
        if (mp.find(sum) != mp.end())
            return make_pair(mp[sum] + 1, i + 1);
        mp[num] = i;
    }
    return make_pair(-1, -1);
}

int main()
{
    ll n,x; cin >> n >> x;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++)
        cin >> a[i];

    pair<ll, ll> p = solver(a, x);
    if (p.first != -1 && p.second != -1)
        cout << p.first << " " << p.second << endl;
    else
        cout << "IMPOSSIBLE" << endl;
    return 0;    
}

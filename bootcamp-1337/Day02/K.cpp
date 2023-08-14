#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

long long gcd(long long a, long long b)
{
    return b == 0 ? a : gcd(b, a % b);   
}

int main()
{
    int n;
    long long g,v;
    cin >> n;
    vector <long long> arr(n);
    vector <long long> gcd1(n);
    vector <long long> gcd2(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    gcd1[0] = arr[0];
    gcd2[n - 1] = arr[n - 1];
    for (int i = 1; i < n; i++)
    {
        gcd1[i] = gcd(gcd1[i - 1], arr[i]);
        gcd2[n - i - 1] = gcd(gcd2[n - i], arr[n - i - 1]);
        
    }
    
    long long res = 1;
    for (size_t i = 0; i < n; i++)
    {
        if(!i)
            res = max(res, gcd2[1]);
        else if (i == n - 1)
            res = max(res, gcd1[n - 2]);
        else
            res = max(res, gcd(gcd1[i - 1], gcd2[i + 1]));
    }
    cout << res;
        
}
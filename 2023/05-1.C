#include <iostream>
#include <cstdint>
#include <string>
#include <istream>
#include <vector>
#include <map>
#include <algorithm>
#define int long long
using namespace std;

vector<pair<int,int>> seeds;
vector<map<int, int>> rmaps;
int findSrc(int src)
{
    for (map<int,int> m: rmaps)
    {
        int dst;
        auto iter = m.upper_bound(src);
        if (iter == m.begin())
            dst = src;
        else {
            dst =  (--iter)->second + src ;
        }
        src=dst;
    }
    return src;
}

int32_t main()
{
    int n;
    cin >> n;
    int maxi = 0;
    for (int i = 0; i < n/2; i++)
    {
        int seed, rangeSize;
        cin >> seed >> rangeSize;
        seeds.push_back({seed, rangeSize});
        maxi = max(maxi, seed+rangeSize);
    }

    //7 maps
    for(int i = 0; i < 7; i++)
    {
        map<int, int> rmapping;
        int m;
        cin >> m;
        for (int j = 0; j < m; j++)
        {
            int d,s,l;
            cin >> d >> s >> l;
            rmapping[d]  = s - d;
            if (rmapping.find(d+l) == rmapping.end())
            {
                rmapping[d+l] = 0;
            }
        }
        rmaps.push_back(rmapping);
    }

    reverse(rmaps.begin(), rmaps.end());

    for (int i = 0; i <maxi; i++)
    {
        int res = findSrc(i) ;
        int found = 0;
        if (i% 100000 == 0) cout  << "-----" << i << endl;
        for (auto seed: seeds)
        {
            if (res >= seed.first && res < (seed.first + seed.second))
            {
                cout << i << endl;
                found = 1;
                break;
            }
        }
        if (found) break;
        
    }
}
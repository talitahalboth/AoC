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
vector<map<int, int>> maps;
vector<map<int, int>> rmaps;

int findDst (int src)
{
    for (map<int,int> m: maps)
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
    for (int i = 0; i < n/2; i++)
    {
        int seed, rangeSize;
        cin >> seed >> rangeSize;
        seeds.push_back({seed, rangeSize});
    }

    //7 maps
    for(int i = 0; i < 7; i++)
    {
        map<int, int> mapping;
        int m;
        cin >> m;
        for (int j = 0; j < m; j++)
        {
            int d,s,l;
            cin >> d >> s >> l;
            mapping[s] = d - s;
            mapping[s+l - 1] = d-s ;
            if (mapping.find(s-1) == mapping.end())
            {
                mapping[s-1] = 0;
            }
            if (mapping.find(s+l) == mapping.end())
            {
                mapping[s+l] = 0;
            }
        }
        maps.push_back(mapping);
    }
    for (auto mapp: maps)
    {
        map<int, int> mapping;
        for (auto [k, v]: mapp)
        {
            mapping[v] = k;
        }
        rmaps.push_back(mapping);
    }
   
    int min = -1;
    for (int i = 0; i < seeds.size(); i++)
    {
        pair<int, int> src = seeds[i];
        for(int j = src.first; j < src.first+ src.second; j++)
        {
            int res = (findDst(j));
            if (j%100000 == 0)
            {
                cout << j << " " << res << " " << min << endl;

            }

            if (min == -1 || res < min)
                min = res;
        }
    }
    cout << min << endl;



}
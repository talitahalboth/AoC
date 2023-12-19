#include <iostream>
#include <cstdint>
#include <string>
#include <istream>
#include <vector>
#include <map>
#include <algorithm>
#define int long long
using namespace std;

vector<int> seeds;
vector<map<int, int>> maps;

int32_t main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int seed;
        cin >> seed;
        seeds.push_back(seed);
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
            if (mapping.find(s+l) == mapping.end())
            {
                mapping[s+l] = 0;
            }
        }
        maps.push_back(mapping);
    }
   
    // for(auto v: maps)
    // {
    //     for (auto[k,v]: v)
    //     {
    //         cout << '[' <<k << "]: " << v ;
    //         cout << endl;
    //     }
    //     cout << endl;
    // }
    int min = -1;
    for (int i = 0; i < seeds.size(); i++)
    {
        int src = seeds[i];
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
        if (min == -1 || src < min)
            min = src;
    }
    cout << min << endl;



}
#include <iostream>
#include <vector>
#include <cstdint>
#include <map>
#include <algorithm>
#include <set>

#define int long long
using namespace std;

vector<string> v;
set<int> dists[1321][1321] ;
vector<pair<int,int>> neighbours = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int32_t main()
{
    string s;
    pair<int,int>start;
    while(cin >> s)
    {
        v.push_back(s);
        int startLocation = s.find('S');
        if ( startLocation != string::npos)
        {
            start = {v.size() - 1, startLocation};
            dists[start.first][start.second].insert(0);
        }
    }
    for (int i = 0; i < 64; i++)
    {
        for (int row = 0; row < v.size(); row++)
        {
            for (int col = 0; col < v[row].size(); col++)
            {
                for(pair<int,int> p: neighbours)
                {
                    int x = row + p.first;
                    int y = col + p.second;
                    if (x >= 0 && x < v.size() && y >= 0 && y < v[x].size())
                    {
                        if (v[x][y] != '#')
                        {
                            for(auto a: dists[row][col])
                            {
                                dists[x][y].insert(a+1);
                            }
                        }
                    }
                }
            }
        }
    }
    int count = 0;
    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            if (dists[i][j].find(64) != dists[i][j].end())
            {
                count +=1;
                cout << 'O';
            }
            else {
                cout << v[i][j];
            }
        }
        cout << endl;
    }
    cout << endl;
    cout << count << endl;
    
}
#include <iostream>
#include <vector>
#include <cstdint>
#include <queue>
#include <algorithm>
#include <string>

#define int long long
using namespace std;

vector<string> v;
int dists[1321][1321] ;
vector<pair<int,int>> neighbours = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

void bfs(pair<int, int> root)
{
    int count =0 ;
    queue<pair<pair<int,int>,int>> q;
    q.push({root, 0});
    while(!q.empty())
    {
        count+=1;
        pair<pair<int,int>,int> front = q.front();
        pair<int,int> coord = front.first;
        int d = front.second;
        q.pop();
        if (dists[coord.first][coord.second] == -1)
        {
            dists[coord.first][coord.second] = d;
            for(pair<int,int> p: neighbours)
            {
                int x = coord.first + p.first;
                int y = coord.second+ p.second;
                if (x >= 0 && x < v.size() && y >= 0 && y < v[x].size())
                {
                    if (v[x][y] != '#' && dists[x][y] == -1 && (d+1 <= 64)) q.push({{x,y}, d+1});   
                }
            }
        }
    }
    cout << count << endl;
}

int32_t main()
{
    int mul = 3;
    string s;
    pair<int,int>start;
    while(cin >> s)
    {
        int startLocation = s.find('S');
        string s2 = s;
        if (startLocation != string::npos)
        {
            s2[startLocation] = '.';
        }
        for (int j = 0; j < mul; j++)
        {
            string str = "";
            for (int i = 0; i < mul; i++)
            {
                str = str + ((i == mul/2 && j == mul/2) ? s : s2);
            }
            startLocation = str.find('S');
            if (startLocation != string::npos)
            {
                start = {v.size() - 1, startLocation};
            }
            v.push_back(str);
        }
    }
    bfs(start);
    int count = 0;
    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            if (dists[i][j] >= 0 && dists[i][j]%2 == 0 )
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
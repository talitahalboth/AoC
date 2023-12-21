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
                    if (v[x][y] != '#' && dists[x][y] == -1 && (d+1 <= 11*3 )) q.push({{x,y}, d+1});   
                }
            }
        }
    }
}

int32_t main()
{
    string s;
    pair<int,int>start;
    int mul = 15;
    while(cin >> s)
    {
        int startLocation = s.find('S');
        if (startLocation != string::npos)
        {
            s[startLocation] = '.';
        }
        string str = "";
        for (int i = 0; i < mul; i++)
        {
            str = str + s;
        }
        v.push_back(str); 
    }
    int size = v.size();
    for (int k = 0; k < mul-1; k++)
    {
        for (int i =0; i < size; i++)
        {
            
            v.push_back(v[i]);

        }
    }
    for(int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
            dists[i][j] = -1;
    }
    start = {v.size()/2, v.size()/2};
    bfs(start);
    int count = 0;
    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            if (dists[i][j] >= 0 && dists[i][j]%2 == 1 )
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
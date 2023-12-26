#include <iostream>
#include <cstdint>
#include <map>
#include <vector>
#include <queue>
#include <stdio.h>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define para(X,Y) for (ll (X) = 0;(X) < (Y);++(X))
#define paraIni(X,S,Y) for (ll (X) = S;(X) < (Y);++(X))
#define rpara(X,Y) for (ll (X) = (Y)-1;(X) >=0;--(X))
#define all(X) (X).begin(),(X).end()
#define rall(X) (X).rbegin(),(X).rend()
#define unicos(X) (X).erase(unique(all(X)),(X).end())
#define NL <<"\n"
#define EPS 1e-6
#define MOD 1000000007
#define iinf 0x3f3f3f3f
#define llinf 0x3f3f3f3f3f3f3f3f
#define ll long long
#define pii pair<int, int>
#define pll pair<long, long>
using namespace std;

#define N 0
#define E 1
#define S 2
#define W 3

int v[1321][1321];
int dists[1321][1321][4][11];
int n;
int m;
vector<pii> neighbours = { {-1, 0} , {0, 1}, {1, 0}, {0, -1}};
int directions[4] = {'n', 'e', 's', 'w'};

void dijkstra ()
{
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>> > fila;
	fila.push({0,0,0,1,0}); //i, j, dist, dir, count
	fila.push({0,0,0,2,0}); //i, j, dist, dir, count
    int c = 0;
	while (!fila.empty())
	{
		vector<int> cur = fila.top();
		fila.pop();
        int x = cur[0];
        int y = cur[1];
        int dist = cur[2];
        int dir = cur[3];
        int count = cur[4];
        for (int i = -1; i <=1; i++)
        {
            if (i != 0 && count < 4)
                continue;
            if (i == 0 && count == 10)
                continue;
            int newDir = (dir + i+4) % 4;
            pii nei = neighbours[newDir];
            
            int newX = x + nei.first;
            int newY = y + nei.second;
            if (newX < 0 || newX >= n || newY < 0 || newY >= m)
            {
                continue;
            }
            int weight = dist + v[newX][newY];
            int newCount = newDir == dir ? count+1 : 1;
            if (weight < dists[newX][newY][newDir][ newCount])
            {
                dists[newX][newY][newDir][ newCount] = weight;
                fila.push({newX,newY,weight, newDir, newCount});     
            }
        }
	}
    int mini  = iinf;
    for (int x = 0; x < 4; x++)
        for (int l = 4; l < 11; l++)
            mini = min(mini, dists[n-1][m-1][x][l]);
    printf("%d", mini);
}

int32_t main() 
{
    string str;
    int i =0;
    while(cin >> str)
    {
        int j = 0;
        for (auto c: str)
        {
            v[i][j] = c - '0';
            for (int k = 0; k < 4; k++)
            {
                for (int l = 0; l < 11; l++)
                    dists[i][j][k][l] = iinf;
            }
            j++;
        }
        m = j;
        i++;
    }
    n = i;
    dijkstra ();
    return 0;    
}
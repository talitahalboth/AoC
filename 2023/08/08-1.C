#include <iostream>
#include <cstdint>
#include <map>
#include <vector>
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
#define int long long
using namespace std;

map<pii, int>lcmM;

using namespace std;

int start[1321] = {-1};
string adjMatri[1321][2] = {""};
map<string, int>m;
map<int, bool> isEnd;
vector<int> pathLen;

int getOrAddToMap(string str, int &id)
{
    int res;
    if (m.find(str) == m.end())
    {
        m[str] = id++;
    }
    res = m[str];
    return res;
}

ll gcd(ll a, ll b)
{
   ll gcd = a;
    ll tmp = b;
    while (gcd != tmp)
    {
        if (gcd > tmp)
            gcd -= tmp;
        else
            tmp-=gcd;
    }
    return gcd; 
}


ll lcm(ll a, ll b)
{
    ll men = min(a,b);
    ll mai = max(a,b);
    if (lcmM.count(mp(men,mai)))
        return lcmM[mp(a,b)];
    
    lcmM[mp(a,b)] = (a*b) / gcd(a,b);
    return lcmM[mp(a,b)];
}

void cycle(int start, string path)
{
    int pathIdx = pathLen.size();
    bool atEnd = false;
    bool atStart = false;
    int cur = start;
    int pos = 0;
    int res = 0;
    while (!atEnd)
    {
        int next = ( path[pos] == 'L' ? m[adjMatri[cur][0]] : m[adjMatri[cur][1]]);
        if (isEnd[next]) atEnd = true;
        cur = next;
        pos++;
        if (pos >= path.size()) pos=0;
        res++;
    }
    pathLen.push_back(res);
}

int32_t main() 
{
    int startVecIdx = 0;
    string route;
    cin >> route;
    string o, l, r;
    int id = 0;
    while (cin >> o >> l >> r ) {
        int oMap = getOrAddToMap(o, id);
        if ( o[2] == 'A') start[startVecIdx++] = oMap;
        isEnd[oMap] = o[2] == 'Z';
        adjMatri[oMap][0] = l;
        adjMatri[oMap][1] = r;
    }
    cout << startVecIdx <<endl;
    int res = 1;
    for (int i = 0; i < startVecIdx; i++)
    {
        cycle(start[i], route);
        res = lcm(res,pathLen.back());
    }
    cout << res << endl;
    
}
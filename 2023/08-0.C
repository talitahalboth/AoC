#include <iostream>
#include <cstdint>
#include <map>
#include <stdio.h>

#define int long long
using namespace std;
map<string, pair<string,string>> m;
int32_t main() 
{
    string route;
    cin >> route;
    string o, l, r;
    while (cin >> o >> l >> r ) {
        m[o] = {l, r};
    }
    bool isEnd = 0;
    int pos = 0;
    string cur = "AAA";
    int res = 0;
    while (!isEnd)
    {
        string next = ( route[pos] == 'L' ? m[cur].first :m[cur].second);
        if (next == "ZZZ") isEnd = true;
        else {
            cur = next;
        }

        pos++;
        if (pos >= route.size()) pos=0;
        res++;
    }
        
    cout << res;

    return 0;
}
#include <iostream>
#include <vector>
#include <cstdint>
#include <map>
#include <algorithm>
#include <set>

#define int long long
using namespace std;

bool isNumber (char c)
{
    return (c >= '0' && c <= '9');

}

int32_t main()
{
    vector<vector<int>> vec(210, vector<int>(210, 0));
    vector<pair<int,int>> gears;
    set<int> nums;
    int count = 1;
    int row =0 ;
    map<int, int> m;

    string line;
    while (cin >> line)
    {
        int col = 0;
        while (col < line.size())
        {
            char c = line[col];
            if ( c == '*')
            {
                gears.push_back({row,col});
            }
            int flag = 0;
            while (col < line.size() && isNumber(c))
            {
                flag = flag*10 + (c - '0');
                vec[row][col] = count;
                col++;
                c = line[col];
            }
            if (!flag)
            {
                col++;
            }
            else 
            {
                m[count] = flag;
                count++;
            }
        }
        row++;
    }
    int sum = 0;
    for (int i = 0; i < gears.size(); i++)
    {
        pair<int,int> p = gears[i];
        set<int> adj {};
        for (int r = max(p.first-1, 0ll); r <= min(p.first+1, row-1); r++)
        {
            for (int c = max(p.second-1, 0ll); c <= min(p.second+1, row-1); c++)
            {
                if (vec[r][c])
                {
                    adj.insert(vec[r][c]);
                }
            }
        }
        if (adj.size() == 2)
        {
            int ratio = 1;
            for(auto a: adj)
            {               
                ratio *= m[a];
            }
            sum+=ratio;
        }
            cout <<sum<< endl;
    }

    cout << sum << endl;
    

    return 0;
}


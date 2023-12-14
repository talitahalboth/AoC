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
    vector<pair<int,int>> positions;
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
            if (!isNumber(c) && c != '.')
            {
                positions.push_back({row,col});
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
    for (int i = 0; i < positions.size(); i++)
    {
        pair<int,int> p = positions[i];
        for (int r = max(p.first-1, 0ll); r <= min(p.first+1, row-1); r++)
        {
            for (int c = max(p.second-1, 0ll); c <= min(p.second+1, row-1); c++)
            {
                if (vec[r][c])
                {
                    nums.insert(vec[r][c]);
                }
            }

        }
    }
    int sum = 0;
    for (auto num: nums)
    {
        sum+=m[num];
    }

    cout << sum << endl;
    // for (int i = 0; i < row; i++)
    // {
    //     for (int j = 0; j < row; j++)
    //     {
    //         cout << vec[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    

    return 0;
}


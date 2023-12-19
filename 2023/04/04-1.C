#include <iostream>
#include <cstdint>
#include <string>
#include <istream>
#include <vector>
#include <map>
#include <algorithm>
#define int long long
using namespace std;

int32_t main()
{
    string line;
    vector<vector<int>> winningVec;
    vector<int> copies;
    vector<vector<int>> myVec;
    while(getline(cin, line))
    {
        copies.push_back(1);
        winningVec.push_back({});
        myVec.push_back({});
        string winning = line.substr(line.find(':')+1, line.find('|') - line.find(':') - 1);
        string mine = line.substr(line.find('|')+1, line.size()-  line.find('|'));
        map<int, int>winningNums{};
        while(winning.find(' ') != string::npos)
        {
            string s =  winning.substr(0, winning.find(' '));
            if (s.size() > 0) winningVec.back().push_back(stoi(s));
            winning = winning.substr(winning.find(' ')+1, winning.size());
        }
        if (winning.size() > 0) winningVec.back().push_back(stoi(winning));

        while(mine.find(' ') != string::npos)
        {
            string s =  mine.substr(0, mine.find(' '));
            if (s.size() > 0)  myVec.back().push_back(stoi(s));
            mine = mine.substr(mine.find(' ')+1, mine.size());
        }
        if (mine.size() > 0) myVec.back().push_back(stoi(mine));
    }

    for (int i = 0; i < myVec.size(); i++)
    {
        map<int,int> m {};
        for (int j = 0; j < winningVec[i].size(); j++)
        {
            m[winningVec[i][j]] = 1;
        }
        int points = 0;
        for (int j = 0; j < myVec[i].size(); j++)
        {
            if (m.find(myVec[i][j]) != m.end())
            {
                points++;
            }
        }
        for (int j = i+1; j < min((int)myVec.size(), i + points+1); j++)
        {
            copies[j]+=copies[i];
        }

    }

    int sum = 0;
    for (int i = 0; i < copies.size(); i++)
    {
        sum +=copies[i] ;
    }
    cout << sum<< endl;
    return 0;
}
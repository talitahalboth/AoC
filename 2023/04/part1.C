#include <iostream>
#include <cstdint>
#include <string>
#include <istream>
#include <vector>
#include <map>

#define int long long
using namespace std;

int32_t main()
{
    string line;
    int sum =0 ;
    while(getline(cin, line))
    {
        string winning = line.substr(line.find(':')+1, line.find('|') - line.find(':') - 1);
        string mine = line.substr(line.find('|')+1, line.size()-  line.find('|'));
        // vector<int> winningNums {};
        map<int, int>winningNums{};
        while(winning.find(' ') != string::npos)
        {
            string s =  winning.substr(0, winning.find(' '));
            if (s.size() > 0)
            {
                winningNums[stoi(s)] = 1;

            }
            winning = winning.substr(winning.find(' ')+1, winning.size());
        }
        if (winning.size() > 0)
        {
            if (winning.size() > 0)
            {
                winningNums[stoi(winning)] = 1;
            }

        }
        int countMatch = 0;
        while(mine.find(' ') != string::npos)
        {
            string s =  mine.substr(0, mine.find(' '));
            if (s.size() > 0)
            {
                int num = stoi(s);
                if (winningNums.find(num) != winningNums.end())
                {
                    countMatch++;
                }
            }
            mine = mine.substr(mine.find(' ')+1, mine.size());
        }
        if (mine.size() > 0)
        {
            int num = stoi(mine);
            if (winningNums.find(num) != winningNums.end())
            {
                countMatch++;
            }
        }
        if (countMatch > 0)
        {
            int res=  (1<<(countMatch-1));
            cout <<res <<endl;
            sum += 1<<(countMatch-1);
        }
    }
    cout << sum << endl;
    return 0;
}
#include <iostream>
#include <cstdint>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

#define int long long
using namespace std;
map<char, int> order;
vector<pair<string, int>> list; 

int calculateHandGrade(string hand)
{
    map<char, int> m;
    for (auto c: hand)
    {
        if (m.find(c) == m.end())
            m[c] = 1;
        else
            m[c] = m[c] + 1;
    }
    int grade = 0;
    for(auto [k, v]: m)
    {
        // 5 of a kind
        if (v == 5) grade = 7;
        // 4 of a kind
        else if (v == 4) grade = 6;
        // full house
        else if (v == 3 && grade == 2) grade = 5;
        // three of a kind
        else if (v == 3 && grade < 4) grade = 4;
        // full house
        else if (v == 2 && grade == 4) grade = 5;
        // 2 pairs
        else if (v == 2 && grade == 2) grade = 3;
        // pair
        else if (v == 2 && grade < 2) grade = 2;
        // high card
        else if (grade == 0) grade = 1;
    }
    return grade;

}

struct handComparator
{
    bool operator ()(const pair<string, int> & hand1, const pair<string, int> & hand2)
    {
        int grade1 = calculateHandGrade(hand1.first);
        int grade2 = calculateHandGrade(hand2.first);
        if (grade1 != grade2)
            return grade1 > grade2;
        for(int i = 0; i < hand1.first.size(); i++)
        {
            if (order.at(hand1.first[i]) != order.at(hand2.first[i]))
                return order.at(hand1.first[i]) > order.at(hand2.first[i]);
        }
        return 0 == 0;
    }
};

int32_t main()
{
    string hand;
    int bid;
    int o = 20;
    order['A'] = o--;
    order['K'] = o--;
    order['Q'] = o--;
    order['J'] = o--;
    order['T'] = o--;
    for (int i = '9'; i >= '2'; i--)
    {
        order[i] = o--;
    }
    
    while (cin >> hand >> bid)
    {
        list.push_back({hand, bid});
    }

    sort(list.begin(), list.end(), handComparator());
    reverse(list.begin(), list.end());
    int rank =1 ;
    int res= 0;
    for (auto e: list)
    {
        res += e.second * rank++; 
    }
    cout << res << endl;
    return 0;
}
#include <iostream>
#include <cstdint>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

#define int long long
using namespace std;
map<char, int> order;
vector<pair<pair<string, char>, int>> list; 


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
    bool operator ()(const pair<pair<string, char>, int> & hand1, const pair<pair<string, char>, int> & hand2)
    {
        string hand1Str = hand1.first.first;
        string hand2Str = hand2.first.first;
        string replacedHand1 = hand1Str;
        replace(replacedHand1.begin(), replacedHand1.end(), 'J', hand1.first.second);
        string replacedHand2 = hand2Str;
        replace(replacedHand2.begin(), replacedHand2.end(), 'J', hand2.first.second);

        int grade1 = calculateHandGrade(replacedHand1);
        int grade2 = calculateHandGrade(replacedHand2);
        if (grade1 != grade2)
            return grade1 > grade2;
        for(int i = 0; i < hand1Str.size(); i++)
        {
            if (order.at(hand1Str[i]) != order.at(hand2Str[i]))
                return order.at(hand1Str[i]) > order.at(hand2Str[i]);
        }
        return 0 == 0;
    }
};

int32_t main()
{
    string hand;
    int bid;
    int o = 20;
    vector<char> cards{'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'};
    for(char c:cards)
    {
        order[c] = o--;
    }
    
    handComparator cmp;
    while (cin >> hand >> bid)
    {
        string tmpHand = hand;
        char sub = 'J';
        for (char c: cards)
        {
            pair<pair<string, char>, int> p1 = {{tmpHand, 0}, bid};
            string hand2 = hand;
            replace(hand2.begin(), hand2.end(), 'J', c);
            pair<pair<string, char>, int> p2 = {{hand2, 0}, bid};
            if (!cmp(p1,p2))
            {  
                sub = c;
                tmpHand = hand2;
            }
        }
        // cout << hand << " " << tmpHand << endl;
        
        list.push_back({{hand,sub }, bid});
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
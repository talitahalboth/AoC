#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() 
{
    
    vector<string> v= {"one", "two", "three", "four", "five", "six", "seven", "eight",  "nine"};

    string str;
    int sum =0 ;
    while (cin >> str)
    {
        int first = -1;
        int last = -1;
        for (int i = 0; i < str.size(); i++)
        {
            char c = str[i];

            for (int j = 0; j < v.size(); j++)
            {
                string num = v[j];
                if (str.substr(i, num.size()) == num)
                {
                    last = j+1;
                    if (first == -1)
                    {
                        first = last;
                    }
                }
            }

            if (c >= '0' && c <= '9')
            {
                last = c - '0';
                if (first == -1)
                {
                    first = last;
                }
            }
        }
        cout <<  first*10 + last << endl << endl;
        sum += first*10 + last;
    }
    cout << sum << endl;
    return 0;
}
#include <iostream>
#include <string>
using namespace std;
int main() 
{
    string str;
    int sum =0 ;
    while (cin >> str)
    {
        int first = -1;
        int last = -1;
        for (char c: str)
        {
            if (c >= '0' && c <= '9')
            {
                last = c - '0';
                if (first == -1)
                {
                    first = last;
                }
            }
        }
        sum += first*10 + last;
    }
    cout << sum << endl;
    return 0;
}
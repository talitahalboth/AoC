#include <iostream>
#include <string>
#include <cstdint>
#include <algorithm>
#include <regex>

#define int long long
using namespace std;

int countMatches(string game, regex exp)
{
    int maxi = -1;
    smatch res;
    string::const_iterator searchStart( game.cbegin() );
    while ( regex_search( searchStart, game.cend(), res, exp ) )
    {
        string str = res[0];
        string numStr = str.substr(0, str.find(' '));
        int  num = stoi(numStr);
        maxi = max(maxi,num);

        searchStart = res.suffix().first;
    }
    return maxi;
}

int32_t main()
{   
    /*
    Determine which games would have been possible 
    if the bag had been loaded with only 
    12 red cubes, 13 green cubes, and 14 blue cubes. 
    What is the sum of the IDs of those games?
    */

   string in;
   int sum =0;
   while (getline(cin, in))
   {
        int colonPos = in.find(':');
        string gameName = in.substr(0, colonPos);
        string idStr = gameName.substr(gameName.find(' '), 10);
        int id = stoi(idStr);
        string game = in.substr(colonPos, in.size() - colonPos);
        regex redExp("[0-9]* red");
        regex greenExp("[0-9]* green");
        regex blueExp("[0-9]* blue");
        int blue = countMatches(game, blueExp);
        int green = countMatches(game, greenExp);
        int red = countMatches(game, redExp);
        sum+=blue*green*red;
        cout << sum << endl;
   }
   cout << sum<<endl;
    return 0;
}
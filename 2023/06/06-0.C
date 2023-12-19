#include <iostream>
#include <cstdint>
#include <vector>
#include <cmath>

#define int long long
using namespace std;

vector<int> times;
vector<int> recs;

int f(int pressed, int time)
{
    int remainingTime = time-pressed;
    int dist = remainingTime*pressed;
    return dist;
}

int binarySearch (int x, int n)
{
	int sup = floor(n/2);
	int inf = 0;
	while (inf < sup)
	{
		int mid = (sup+inf)/2;
		if (f(mid, n) < x)
			inf = mid + 1;
		else if (f(mid, n) > x)
			sup = mid ;
        else 
            sup = mid;
	}
    return sup;

}


int32_t main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        times.push_back(x); 
    }
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        recs.push_back(x); 
    }
    int res =1;

    for (int i = 0; i < n; i++)
    { 
        int val = binarySearch( recs[i]+1, times[i]);
        res *= times[i] - 2*val + 1;
    }
    cout << res << endl;
    return 0;
}
#include <iostream>
using namespace std;
int main ()
{
	int SX = 0;
	int MX = 0;
	int GC = 0;
	int H = 0;
	cout << "等差数列求和，\n请输入：\n首项：" << endl;
	cin >> SX;
	cout << "末项：" << endl;
	cin >> MX; 
	cout << "公差：" << endl;
	cin >> GC ;
	H = ((MX + SX) * ((MX - SX)/GC + 1))/2;
	cout << H << endl;
}


#include <iostream>
using namespace std;
int main ()
{
	int SX = 0;
	int MX = 0;
	int GC = 0;
	int H = 0;
	cout << "�Ȳ�������ͣ�\n�����룺\n���" << endl;
	cin >> SX;
	cout << "ĩ�" << endl;
	cin >> MX; 
	cout << "���" << endl;
	cin >> GC ;
	H = ((MX + SX) * ((MX - SX)/GC + 1))/2;
	cout << H << endl;
}


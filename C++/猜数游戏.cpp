#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int number()
{
	int num = 0;
	srand ((unsigned)time(NULL));
	num = rand();
	return num%100;
} 
 
int main()
{   
	while(1)
	{
		int tries = 0; 
	 	int num = 0;
	 	int inputnum = 0; 
	 	char start = 0;
	 	num = number();
	 	cout <<"猜数游戏开始!你有5次机会。\n请输入：";
		while (tries < 5)
		{
			tries ++;
			cin >> inputnum;
			if (inputnum == num)
			{
				cout <<"你猜对了";
				break;
			}
			else if (inputnum < num)
			{
				cout <<"比" << inputnum <<"要大" << endl; 
			}
			else 
			{
				cout <<"比" << inputnum <<"要小" << endl; 
			
			}
		}
		if (tries >=5)
		{
		 	cout <<"答题机会已用完，答案是" << num << endl; 
		}
	
		cout <<"是否要再来一次，是请按y，否则就退出。" << endl;
		cin >> start;
		if (start != 'y')
		{
			break;				
		}
	}
}


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
	 	cout <<"������Ϸ��ʼ!����5�λ��ᡣ\n�����룺";
		while (tries < 5)
		{
			tries ++;
			cin >> inputnum;
			if (inputnum == num)
			{
				cout <<"��¶���";
				break;
			}
			else if (inputnum < num)
			{
				cout <<"��" << inputnum <<"Ҫ��" << endl; 
			}
			else 
			{
				cout <<"��" << inputnum <<"ҪС" << endl; 
			
			}
		}
		if (tries >=5)
		{
		 	cout <<"������������꣬����" << num << endl; 
		}
	
		cout <<"�Ƿ�Ҫ����һ�Σ����밴y��������˳���" << endl;
		cin >> start;
		if (start != 'y')
		{
			break;				
		}
	}
}


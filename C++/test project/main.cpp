#include <iostream>
#include <cstring>
#include "func.h"
#include <cstdlib>
#include <iomanip> 

using namespace std;

struct people
{
	char name[32];
	int age;
};

struct value
{
   int weight;
   int price;
};

int compare()
{
	int x = 9;
	int y = 10;
	char *str;
	char a = 20;
	int b = (int) a;
	str = (char *)(x>y?"good":"bad");
	cout << str <<endl;	
}
int test()
{
	int a = 0;
	if (++a || ++a || ++a)
	{
		cout <<a << endl;
	}
	
}

int calc(int *sum, int b, int c)
{
	int aaa;
    *sum = b + c;
    cout << "The sum is " << *sum << endl;
    cout << "The pointer sum 1 is"<< sum << endl;
    return 1;
}

int get_second_number()
{
	int x = 0,y = 0,z = 0;
	cin >> x >> y >> z;
	cout << y << endl;	
}

int number8()
{
	int a = 0,b = 0,c = 0,n = 0;
	cin >> a >> b >> c;
	cout << setw(8) << right << a;
	cout << setw(8) << right << b;
	cout << setw(8) << right << c;
}

void print_n_char(char c, int n)
{
	int i = 0;
	for (i=0; i<n; i++)
	{
		cout << c;
	}
} 

int triangle()
{	
	char a = 0;
	int n = 0;
	int i = 0;
	cout << "请输入想要打印的字符和行数:" ;
	cin >> a >> n; 

	for ( i = 0; i < n; i++ )
	{
		print_n_char(' ', n-i-1);
		print_n_char(a, 2*i+1);
		cout << endl;
	}
} 

int niu_chi_cao()
{	
	int x,a,y,b = 0;
	float z = 0;
	cout << "请输入x,a,y,b:" << endl;
	cin >> x >> a >> y >> b;
	if (x>=10000 || a>=10000 || y>=10000 || b>=10000 || x<=y || a>=b || a*x>=b*y )
	{
		cout << "出错，要求：x>y，a<b，ax<by" << endl; 
	}
	else
	{
		z = (b*y-a*x)/(b-a);
		cout << setiosflags(ios::fixed) << setprecision(2) << z;
	}
	
}
	
	
int main()
{
//	triangle();
	//print_n_char('*', 16);
	niu_chi_cao();
}

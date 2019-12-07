#include <stdio.h>
 
//use while
int bingbao(unsigned long  a )
{
    int ret=0;
    while(a!=1)
    {
        if (a%2)
        {
            a=a*3+1;            
        }
        else 
        {
            a=a/2;
        }
        printf("%ld\n",a );
        ret++;
    }
    return ret;
}
//µÝ¹é·¨¡£
void bingbao2(unsigned long n)
{
 
    printf("%ld\n",n);
 
    if(n!=1)
    {
        unsigned long newValue;
        if(n%2)
        {
            newValue=n*3+1;
        }
        else
        {
             
            newValue=n/2;
        }
        bingbao2(newValue);
         
    }
}
 
int main(int argc, char const *argv[])
{
    unsigned long  a;
    int b;
 
    printf("please input a number.\n");
    scanf("%ld",&a);
     
    b=bingbao(a);
    printf("times=%d\n",b );
 
    bingbao2(a);
     
 
    return 0;
}

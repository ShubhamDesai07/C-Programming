// comma operator problem 2

#include<stdio.h>

int main ()

{
    int a,b,c,d;
    d = (a=1,b=2,c=3,a+b+c); // as operator 
    //d = (a+b+c,a=1,b=2,c=3);// prints d = 3 
    printf("%d\n",d);
    return 0 ;
}
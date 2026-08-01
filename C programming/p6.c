// example of increment and decrement


#include<stdio.h>

int main ()

{
    int m = 10; // m = 10
    printf("%d\n",m);
    int n , n1 ;
    n = ++m; // m = 11 n = 11
    printf("%d\n",m);
    printf("%d\n",n);
    n1 = m++; // n1 = 11 m = 12
    printf("%d\n",n1);
    printf("%d\n",m);
    n--; // n 11 then n = 10
    printf("%d\n",n);
    --n1; // n1 = 10
    printf("%d\n",n1);
    n-=n1; // n = n-n1 = 10 - 10 = n = 0
    printf("%d\n",n);
    return 0 ;


}
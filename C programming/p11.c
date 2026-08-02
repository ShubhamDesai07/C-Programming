#include<stdio.h>

int main()
{
    int x;
    printf("%d\n",sizeof(x)); //4 byte
    printf("%d\n",sizeof(int));//4 
    printf("%d\n",sizeof(5));//4
    printf("%d\n",sizeof(char));//1
    printf("%d\n",sizeof(short int));//2
    printf("%d\n",sizeof(float));//4
    printf("%d\n",sizeof(double));//8
    printf("%d\n",sizeof(long double));//16
    return 0;
}
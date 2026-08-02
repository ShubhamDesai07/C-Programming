#include<stdio.h>

int main ()
{
    int x = 2,y = 4 ,z;
    z = (x==3?(y==4?6:8):0);
    printf("%d",z);
    return 0 ;
}
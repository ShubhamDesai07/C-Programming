#include<stdio.h>

int main (){

    int n,i = 1,mul = 0;
    scanf("%d",&n);

    while (i<=10)
    {
        mul = (i*n);
        printf("%d ",mul);
        i++;
    }
   

    return 0 ;

}
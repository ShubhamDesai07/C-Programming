#include<stdio.h>

int main ()

{
    int x,y,max;
    printf("Enter the values of x and y ");
    scanf("%d,%d",&x,&y);
    max = x>y?x:y;
    printf("Largest of %d and %d is %d",x,y,max);
    return 0;
}
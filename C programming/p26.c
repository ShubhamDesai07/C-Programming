#include<stdio.h>

void main (){
    int n1,n2,n3;

    printf("Enter a number :");
    scanf("%d",&n1);

    printf("Enter a number :");
    scanf("%d",&n2);

    printf("Enter a number :");
    scanf("%d",&n3);

    if (n1>n2 && n1>n3)
        printf("%d is greater",n1);
    else if (n2>n1 && n2>n3)
        printf("%d is greater",n2);         
    else
        printf("%d is greater",n3);



}
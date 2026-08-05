#include<stdio.h>

void main ()

{
    int n1=20,n2=20,n3=20;
    if (n1>=n2 && n1>=n3)
        printf(" %d is greater",n1);
    if (n2>=n3 && n2>=n1) 
        printf(" %d is greater",n2);
    if (n3>=n2 && n3>=n1)       
        printf(" %d is greater",n2);   
}
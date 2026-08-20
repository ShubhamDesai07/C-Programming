#include <stdio.h>

int add(int n)
{
    static int sum = 0;

    sum = sum + n;

    return sum;
}

int main(void)
{
    printf("%d\n", add(5));
    printf("%d\n", add(10));
    printf("%d\n", add(20));

    return 0;
}
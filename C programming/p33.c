#include <stdio.h>

int main() {
    int a, b, c, second;

    scanf("%d %d %d", &a, &b, &c);

    if ((a > b && a < c) || (a > c && a < b))
        second = a;
    else if ((b > a && b < c) || (b > c && b < a))
        second = b;
    else
        second = c;

    printf("Second largest is = %d", second);

    return 0;
}
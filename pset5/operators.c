#include <stdio.h>

int main (void)
{
    int a = 10;
    int b = 20;

    int Addition,Substraction,multiplication,Division,modulus;

    Addition = a + b;
    Substraction = b - a;
    multiplication = a * b;
    Division = b / a;
    modulus = a % b;

    printf("addition of a+b is %d\n",Addition);
    printf("subtraction of a-b is %d\n",Substraction);
    printf("multiplication of a*b is %d\n",multiplication);
    printf("division of b/a is %d\n",Division);
    printf("Remainder of a and b is %d\n",modulus);

    return 0;

}
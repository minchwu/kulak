#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int hello();
double resin(double theta);

int main(){
    printf("hello c");
    hello();
    /* system("pause"); */
    return 0;
}

int hello(){
    int *p[10];
    int *q[10];
    int a = 1, b = 2;
    double c = resin(2.0);
    printf("%d\t%d\t%d\t%d\t%.2f\n", a, b, p, q, c);
    /* system("pause"); */
    return 0;
}

double resin(double theta){
    return sin(theta);
}

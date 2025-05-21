#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define N 100

int sum_square_difference(int n){
    int sum_of_squares = 0;
    int sum = 0;

    for (int i =1; i<=n; i++){
        sum_of_squares += pow(i,2);
        sum += i;
    }
 return (pow(sum,2) - sum_of_squares);
}


int main(void){
    printf("%d", sum_square_difference(N));
  return 0;
}

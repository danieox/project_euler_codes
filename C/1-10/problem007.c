#include <stdlib.h>
#include <stdio.h>
#define N 10001



int nth_prime(int n){
    int count = 0;
    int number = 1;
    while (count!= n ){
        number ++;
        for(int i =2; i*i <= number; i++){
            if(number%i == 0) goto label;}
        count ++;   
        label:
   }
 return number; }

int main(void){
    printf("%d", nth_prime(N));
}


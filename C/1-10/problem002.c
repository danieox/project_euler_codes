#include <stdio.h>
#include <stdlib.h>
#define LIMIT 4000000

int nth_fibonacci(int n){
if (n == 1|| n==2)
return n;
else
return nth_fibonacci(n-1) + nth_fibonacci(n-2);

}


int sum_even_valued_terms(int limit){
 int sum = 0;
 int i = 1;
 while(nth_fibonacci(i) <= limit){
    if (nth_fibonacci(i)%2 == 0){
       sum+= nth_fibonacci(i);
    }
  i++;
 }
 return sum;

}

int main(void){

    printf("%d", sum_even_valued_terms(LIMIT));
    return 0;
}

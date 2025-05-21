#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define NUMBER_OF_DIGITS 3


int is_palindrome(int number){
    int reversed = 0, original = number;
    while(number > 0){
        reversed = reversed * 10 +number%10;
        number/= 10;
    }
    return original == reversed;
}
int largest_palindrome(int number_of_digits){
    int limit = pow(10, number_of_digits-1);
    int start = pow(10, number_of_digits)-1 ;
   int largest_palindrome = 0;
  for(int a = start; a>=limit; a--){
    for(int b=a; b>=limit; b--){
        if(( a*b > largest_palindrome) && is_palindrome(a*b)){
            largest_palindrome = a*b;
        
        }
    }
  }
  return largest_palindrome;
}



int main(void){
printf("%d", largest_palindrome(NUMBER_OF_DIGITS));
return 0;

}
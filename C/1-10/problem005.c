#include <stdlib.h>
#include <stdio.h>


int smallest_multiple(void){
  int  number = 2520;
  int all_factors = 1;
  while(all_factors){
    number ++;
    for (int a = 1; a <= 21; a++){
        if (number%a != 0) goto label;
    }
    all_factors = 0;
    label: 
  }
  return number;
}


int main(void){
    printf("%d\n", smallest_multiple());
}
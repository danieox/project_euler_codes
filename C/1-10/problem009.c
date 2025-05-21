#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define SUM 1000

int pythagorean_triplet_product(int sum ){
int a,b,c,product;

 for ( a=1; a< sum; a++){
    for ( b = a+1; b < sum; b++){
        c = sum - a- b;
        if( c > b && (a*a + b*b == c*c)) {
        product = a*b*c;
        return product;
        }
    }
 }
 return -1;
}


int main(void){
    printf("%d\n",pythagorean_triplet_product(SUM));
    return 0;
}

#include <stdlib.h>
#include <stdio.h>
#define X 600851475143LL

long long int largest_prime_factor_of_X(long long int x){
    long long int factor = 2;
    long long int lastfactor = 1;

    while (x>1){
        if(x%factor == 0){
            lastfactor = factor;
            x/=factor;
            while (x % factor == 0){
                x/= factor;
            }
        }
        factor ++;
        if (factor * factor > x && x >1){
            lastfactor =  x;
            break;
        }
    }
     return lastfactor;
}

int main(void){
printf("%lld\n", largest_prime_factor_of_X(X));
return 0;
}



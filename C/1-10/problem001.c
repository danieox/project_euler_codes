#include <stdio.h>
#include <stdlib.h>

int sum_multiples_of_3x5(int limit){
    int sum = 0;
    for ( int i = 1; i< limit; i++){
        if (i%5 == 0 || i%3 == 0){
            sum+=i;
        }
    }

    return sum;
}

int main(void){

    printf("%d", sum_multiples_of_3x5(1000));

return 0;

}
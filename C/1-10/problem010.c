#include <stdio.h>
#include <stdbool.h>
#define LIMIT 2000000

int main() {
    bool is_prime[LIMIT] = { [0] = false, [1] = false };
    for (int i = 2; i < LIMIT; i++) is_prime[i] = true;

    for (int i = 2; i * i < LIMIT; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j < LIMIT; j += i)
                is_prime[j] = false;
        }
    }

    long long sum = 0;
    for (int i = 2; i < LIMIT; i++) {
        if (is_prime[i]) sum += i;
    }

    printf("%lld\n", sum);
    return 0;
}

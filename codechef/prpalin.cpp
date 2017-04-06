// https://www.codechef.com/problems/PRPALIN
// Find the first prime palindromic number after the given number
#include <stdio.h>
#include <math.h>

bool is_palindrome(long int &n) {
    long int a = n;
    long int b = 0;

    // We don't know the n_digits of n, hence we can't check the r/l half alone
    while (a > 0) {
        b *= 10;
        b += a % 10;
        a /= 10;
    }

    return b == n;
}

bool is_prime(long int &n) {
    long int max_factor = sqrt(n);

    if (!(n % 3) or !(n % 5) or !(n % 7))
        return false;

    for (long int f = 11; f < max_factor; f += 2)
        if (!(n % f))
            return false;

    return true;
}

int main() {
    // Global array to store all the prime numbers
    long int n;

    scanf("%li", &n);

    // If even, advance by one so we can skip all even numbers
    if(n % 2 == 0)
        n += 1;

    for(;; n+=2)
        if (is_palindrome(n) and is_prime(n)) {
            printf("%li\n", n);
            break;
        }
}

// https://www.codechef.com/problems/PRIME1
// Find all primes within the range of two very large numbers

// Uses Atkin seiving. NOTE that for all practical purposes, properly
// implemented eratosthenes' seiving is by itself as fast as Atkin's
// (if not faster). Atkin's has been implemented here for pedagogical purpose.

#include<iostream>
#include<math.h>

#define MAX_SIZE 1000000001
#define MAX_RANGE 100001
#define SQRT_MAX_SIZE 32000

using namespace std;

void build_sieve(bool *is_prime,
                 unsigned long int upper_limit) {

    // Base primes
    is_prime[2] = true;
    is_prime[3] = true;
    is_prime[5] = true;

    /* According to atkin's theorem,
     *
     * A number, n, is prime if 1) the number of solutions to the quadratic is
     * odd, 2) it meets the criterion for that quadratic and 3) if n does not
     * have a perfect square factor.
     * 
     * As for the quadratic, we have 3 as defined in Atkin's paper,
     *
     * Q1, Quadratic 1 --> 4 * x^2 + y^2; criterion n % 4 == 1
     * Q2, Quadratic 2 --> 3 * x^2 + y^2; criterion n % 6 == 1
     * Q3, Quadratic 3 --> 3 * x^2 - y^2 | x > y; criterion n % 12 == 11
     *
     * These three quadratics are sufficient to cover all the prime numbers.
     *
     */ 

    // We try all possible solution pairs (x, y),
    // now if the quadratic evaluates to n, we have one solution to n = Q1/Q2/Q3
    // so we flip the is_prime entry for that number (n)
    // At the end, the number of flips correspond to the number of solution
    // pairs that satisfy n = Q1/Q2/Q3

    // So for any number n, if the number of solutions (to n = Q1/Q2/Q3) is
    // odd --> number of flips is odd --> is_prime entry changes from initial
    // state (composite) to prime.
    
    unsigned long n;
    unsigned long n_mod_60;
    unsigned long n_mod_12;

    // We need to check for primes in the range (0, upper_limit]
    // So the range of x for all 3 quadratics is [0, sqrt(upper_limit)]
    
    unsigned long sqrt_upper_limit = sqrt(upper_limit);

    unsigned long x_y_lower_limit = 1;
    unsigned long x_y_upper_limit = sqrt_upper_limit + 1;

    bool x_is_odd;
    bool y_is_odd;

    unsigned long x_squared, y_squared, thrice_x_squared;

    for (unsigned long int x=x_y_lower_limit; x <= x_y_upper_limit; x++) {
        for (unsigned long int y=x_y_lower_limit; y <= x_y_upper_limit; y++) {

            x_squared = x * x;
            y_squared = y * y;

            x_is_odd = (x%2 != 0);
            y_is_odd = (y%2 != 0);

            // Quadratic 1 : 4 * x^2 + y^2;
            // All x's odd y's
            if (y_is_odd) {
                n = 4 * x_squared + y_squared;
                n_mod_60 = n % 60;  // Wheel factored for base wheel of size 60

                // Eleminating composites based on the criterion (n % 4 == 1)

                // Flip the main_sieve entry if n is a prime candidate
                if ((n <= upper_limit) &&
                        (n_mod_60 == 1 || n_mod_60 == 13 || n_mod_60 == 17 ||
                         n_mod_60 == 29 || n_mod_60 == 37 || n_mod_60 == 41 ||
                         n_mod_60 == 49 || n_mod_60 == 53))
                    is_prime[n] = !is_prime[n];
            }

            // All even/odd combinations
            if (x_is_odd ^ y_is_odd) {

                thrice_x_squared = 3 * x_squared;

                // Quadratic 2 : 3 * x^2 + y^2;
                n = thrice_x_squared + y_squared;
                n_mod_60 = n % 60;

                // Eleminating composites based on the criterion (n % 3 == 1)

                // Flip the is_prime entry if n is a prime candidate
                if ((n <= upper_limit) &&
                        (n_mod_60 == 7 || n_mod_60 == 19 || n_mod_60 == 31 ||
                         n_mod_60 == 43))
                    is_prime[n] = !is_prime[n];

                if (x > y) {

                    // Quadratic 3 : 3 * x^2 - y^2;
                    n = thrice_x_squared - y_squared;
                    n_mod_60 = n % 60;

                    // Eleminating composites based on the criterion (n % 12 == 11)

                    // Flip the is_prime entry if n is a prime candidate
                    if ((n <= upper_limit) &&
                            (n_mod_60 == 11 || n_mod_60 == 23 || n_mod_60 == 47 ||
                             n_mod_60 == 59))
                        is_prime[n] = !is_prime[n];
                }
            }
        }
    }

    // Now eliminate composites with squared primes as factors.
    // (Those incorrectly marked prime by us in the previous steps)
    
    unsigned long int twice_of_factor_squared;
    for (unsigned long int factor = 5; factor <=sqrt_upper_limit; factor += 2) {
        // Skip if the factor is not prime.
        if (is_prime[factor])    {
            // Strike off the multiples of the factor_squared
            twice_of_factor_squared = 2 * factor * factor;

            for (unsigned long int multiple=0.5*twice_of_factor_squared;
                     multiple <= upper_limit;
                     // Skip even multiples
                     multiple += twice_of_factor_squared)
                if (is_prime[multiple])
                    is_prime[multiple] = false;
        }
    }
}

int main() {
    // Lets use a common factor_sieve (for numbers upto SQRT_MAX_SIZE) and
    // cache it for all the n_testcases

    // Force it to store on heap
    bool *main_sieve = new bool[MAX_RANGE];
    bool *factor_sieve = new bool[SQRT_MAX_SIZE];

    unsigned long int lower_limit, upper_limit;

    unsigned int n_testcases;
    cin>>n_testcases;

    // NOTE we are using atkins to build the factor sieve alone
    
    // Build it using Atkin's sieving
    build_sieve(factor_sieve, SQRT_MAX_SIZE - 1);

    /*
    for (int i = 0; i < 100; i++)
        if(factor_sieve[i])
            cout<<i<<" ";
    */

    while(n_testcases--) {
        cin>>lower_limit>>upper_limit;

        // Build the main_sieve for the new limits
        
        // Clear the previous main_sieve
        std::fill(main_sieve, main_sieve + MAX_RANGE + 1, true);

        // Mark all the even numbers as composite
        for (unsigned long int even_no = ((lower_limit <= 2) ? 4 : lower_limit + (lower_limit % 2));
                even_no <= upper_limit; even_no += 2)
            main_sieve[even_no-lower_limit] = false;

        // Mark 0 as not prime
        if (lower_limit == 0)
           main_sieve[0] = false; 

        // Mark 1 as not prime
        if (lower_limit <= 1)
           main_sieve[1-lower_limit] = false; 

        // Mark all the odd multiples of prime factors (from factor_sieve), as
        // composite numbers in the main sieve
        
        unsigned long int next_odd_multiple_increment;
        unsigned long int least_odd_multiple;

        for (unsigned long int prime_factor=3;
                prime_factor <= sqrt(upper_limit); prime_factor += 2) {

            if (!factor_sieve[prime_factor])
                continue;

            next_odd_multiple_increment = 2 * prime_factor;

            // If lower_limit is 0, choose {9, 15, ...} (as 6 is even and 3 is prime)
            // else lower_limit is the least multiple of prime included in the range
            // if lower_limit = 52, choose {57, 63...} (as 54 is even)
            
            // Choose the least multiple of the prime_factor included in the range
            // If the lower limit is an odd multiple of prime_factor choose it
            // as the least_odd_multiple, else choose the next odd multiple of
            // the current prime_factor
            least_odd_multiple = ((lower_limit % prime_factor == 0) ?
                                  lower_limit :
                                  lower_limit + prime_factor - (lower_limit % prime_factor));
            
            // If the lower limit itself is a prime_factor, it should not be marked composite
            // Don't add prime_factor as it will make it even, (we've eleminated evens)
            least_odd_multiple += (least_odd_multiple == prime_factor) ? next_odd_multiple_increment : 0;

            // If we've chosen an even multiple, choose the next one which will be odd
            // (as we have marked all even numbers as composite)
            least_odd_multiple += (least_odd_multiple % 2 == 0) ? prime_factor : 0;

            for (unsigned long int odd_multiple = least_odd_multiple;
                    odd_multiple <= upper_limit;
                    odd_multiple += next_odd_multiple_increment)
                if (main_sieve[odd_multiple-lower_limit])
                    main_sieve[odd_multiple-lower_limit] = false;
        }

        // Print the primes in the range
        for (unsigned long int no=lower_limit; no <= upper_limit; no++) {
            if (main_sieve[no-lower_limit])
                cout<<no<<"\n";
        }

        cout<<"\n";
    }
    return 0;
}

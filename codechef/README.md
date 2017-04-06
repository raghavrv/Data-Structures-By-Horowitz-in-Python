

```python
import os
import time

from IPython.display import Markdown, HTML, display_markdown
from glob import glob

cpp_markdown_template = """```cpp\n%s\n```\n<hr>"""

all_cpp_files = glob("/media/rvraghav93/code/projects/competitive_programming/codechef/*.cpp")
all_cpp_files_sorted_by_date = sorted(all_cpp_files,
                                      key=lambda fpath: os.path.getctime(fpath), reverse=True)

for i, fpath in enumerate(all_cpp_files_sorted_by_date, 1):  
    with open(fpath) as f:
        code = f.read().splitlines()
        url = code[0]
        code_md = cpp_markdown_template % "\n".join(code[1:])

    prob = url.split('/')[-1]
    url = url.strip('/ ')
    display_markdown(Markdown("### %d. %s</br>\n[%s](%s)\n\n(%s)"
                              % (i, prob, url, url,
                                 time.strftime("%d-%b-%Y",
                                               time.localtime(os.stat(fpath).st_mtime)))))
    os.utime
    display_markdown(Markdown(code_md))
```


### 1. PRIME1</br>
[https://www.codechef.com/problems/PRIME1](https://www.codechef.com/problems/PRIME1)

(16-May-2016)



```cpp
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
```
<hr>



### 2. SUBMIN</br>
[https://www.codechef.com/problems/SUBMIN](https://www.codechef.com/problems/SUBMIN)

(16-May-2016)



```cpp
// Print the number of subarrays having the given minimum.

#include<iostream>
#include<stdio.h>
using namespace std;

int getinum()
{
	
	char c;
	int res = 0;
	c = getchar_unlocked();
	while((c!='\n')&&(c!=32))
		{
			res = res*10 + c - 48;
			c = getchar_unlocked();
		}
//	printf("%d",res);
	return res;

}

long getlnum()
{
	char c;
	long res = 0;
	c = getchar_unlocked();
	while((c!='\n')&&(c!=32))
		{
			res = res*10 +c -48;
			c = getchar_unlocked();
		}
//	printf("%li   ",res);
	return res;
}

int main()
{
 
	int size = getinum();
	long val;
	long a[50];
	int i = 0;
	int count = 0;
	while(i<size)
	{	a[i++] = getlnum();
	}
	int nq = getinum();
	while(nq--)
	{
		long q = getlnum();
		i = 0;
		count = 0;
		while(i<size)
		{	
			if (a[i++]<q)
				count = 0;
			else if (a[i++]>q)
				count++;
			else
				{
					while(a[i++]>=q)
						count++;
					break;
				}
		}
		cout<<"o"<<++count<<endl;
	}


}
```
<hr>



### 3. LECANDY</br>
[https://www.codechef.com/problems/LECANDY](https://www.codechef.com/problems/LECANDY)

(31-Jan-2016)



```cpp
// See if we can make all elephants happy

#include<iostream>

using namespace std;

int main() {
    int tries, n, temp;
    long int total_candies;

    scanf("%d", &tries);

    while (tries--) {
        cin>>n;
        cin>>total_candies;

        while (n--) {
            cin>>temp;
            total_candies -= temp;
        }

        if (total_candies >= 0)
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }
return 0;
}
```
<hr>



### 4. PRPALIN</br>
[https://www.codechef.com/problems/PRPALIN](https://www.codechef.com/problems/PRPALIN)

(30-Jan-2016)



```cpp
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
```
<hr>



### 5. HOLES</br>
[https://www.codechef.com/problems/HOLES](https://www.codechef.com/problems/HOLES)

(30-Jan-2016)



```cpp
// Compute the number of holes (fully bounded regions) of all the
// characters in the string

#include<iostream>
#include<stdio.h>
#define g getchar_unlocked

using namespace std;
int main()
{
	char s[] = {'A','D','O','P','Q','R'};
	char c;
	int sum,n;
	
	cin>>n;
	while(n--)
		{	c=g();
			sum = 0;
			while(c!='\n')
				{  	if (c == 'b')
						sum += 2;
					else
						for (int i = 0;i<=5;i++)
							if (c==s[i])
								sum += 1;
					c=g();
				}
			cout<<sum<<endl;
		}
}
```
<hr>



### 6. INTEST</br>
[https://www.codechef.com/problems/INTEST](https://www.codechef.com/problems/INTEST)

(30-Jan-2016)



```cpp
// Input/Output enormous input values

#include<stdio.h>

int main() {	
	unsigned long long n,k,a;
	unsigned long long b=0;
	scanf("%llu %llu",&n,&k);
	while(n--)
	{	scanf("%llu",&a);
		if(!(a%k))
			b++;
	}
	printf("%llu",b);
	return 0;
}
```
<hr>



### 7. MAXCOUNT </br>
[https://www.codechef.com/problems/MAXCOUNT](https://www.codechef.com/problems/MAXCOUNT)

(30-Jan-2016)



```cpp
// Find the element that occurs the maximum no of times
// Choose smallest to break ties

#include<iostream>
#define MAXSIZE 100

using namespace std;


int main() {
    int array[MAXSIZE];
    
    // (Can use hashmap but the MAXSIZE is just 100, it doesn't really matter)
    int count[MAXSIZE] = {1}; // Initialize to 1
    int n_tries, n, elt;
    int max_element, max_count;
    scanf("%d", &n_tries);
    
    while(n_tries--) {
        scanf("%d", &n);
        
        for(int i = 0; i < n; i++) {
            scanf("%d", &elt);
            array[i] = elt;
            count[i] = 1;
            // N^2 complexity? but meh MAXSIZE is 100
            for(int j = 0; j < i; j++) {
                if(elt == array[j]) {
                    // Note that the current element has occured before
                    count[i] = -1;
                    // Increment the previous' count
                    count[j]++;
                    break;
                }
            }
        }
        
        // Reset the max
        max_element = array[0];
        max_count = count[0];
        
        for(int i = 0; i < n; i++) {
            if ((count[i] > max_count) || ((count[i] == max_count) && (array[i] < max_element))) {
                max_count = count[i];
                max_element = array[i];
            }
        }
            
        printf("%d %d\n", max_element, max_count);
    }
    return 0;
}



```
<hr>



### 8. CIELAB</br>
[https://www.codechef.com/problems/CIELAB](https://www.codechef.com/problems/CIELAB)

(30-Jan-2016)



```cpp
// Print a positive difference value with no leading zeros, but exactly one
// incorrect digit

#include<iostream>

using namespace std;

int main() {
    int b, diff;

    scanf("%d %d", &diff, &b);
    diff -= b;

    if(diff%10 == 9)
        // 999 + 1 --> 1000 => take 999 - 1
        // 989 + 1 --> 990 (2 dig changed) => take 999 - 1
        printf("%d", diff-1);
    else
        // 100 - 1 --> 99 => take 100 + 1
        printf("%d", diff+1);
    return 0;
}
```
<hr>



### 9. COOLING</br>
[https://www.codechef.com/problems/COOLING](https://www.codechef.com/problems/COOLING)

(30-Jan-2016)



```cpp
// Find the number of pies that can be cooled

#include<iostream>
#include<new>

using namespace std;

void swap(int *ele1, int *ele2) {
    int temp = *ele2;
    *ele2 = *ele1;
    *ele1 = temp;
}

void quick_sort(int *array, int start, int end) {
    int pivot_i = end;
    int pivot = array[pivot_i];
    int cur=start;

    if (start >= end)
        return;

    if (pivot_i >= 0)
        while (cur < pivot_i) {
            if (array[cur] > array[pivot_i]) {
                array[pivot_i] = array[cur];
                array[cur] = array[pivot_i-- -1];
                array[pivot_i] = pivot;
            }
            else
                cur++;
        }

    quick_sort(array, start, pivot_i - 1);
    quick_sort(array, pivot_i + 1, end);  
}

int main() {
    int n_tries;
    int n_pies;
    int *rack_capacity, *pie_weight;
    int pie_i, rack_i;
    int max_n_pies = 0;
    bool mem_allocated = false;

    scanf("%d", &n_tries);

    while(n_tries--) {
        scanf("%d", &n_pies);
        // Allocate mem for a new int arr if the new size is lesser
        // than the previous size
        if(n_pies > max_n_pies)
            if(mem_allocated)
                // First deallocate previous block of memory
                delete[] rack_capacity;
                delete[] pie_weight;

            max_n_pies = n_pies;

            rack_capacity = new int[max_n_pies];
            pie_weight = new int[max_n_pies];
            mem_allocated = true;

        // If not overwrite the previous array
        
        for(pie_i=0; pie_i<n_pies; pie_i++)
            scanf("%d", &pie_weight[pie_i]);

        for(rack_i=0; rack_i<n_pies; rack_i++)
            scanf("%d", &rack_capacity[rack_i]);

        // Reset the indices to 0
        rack_i = 0;
        pie_i = 0;

        // Sort the racks & pies
        quick_sort(rack_capacity, 0, n_pies-1);
        quick_sort(pie_weight, 0, n_pies-1);

        // Pop one rack by one and match with pie weight
        while(rack_i < n_pies)
            if(rack_capacity[rack_i++] >= pie_weight[pie_i])
                pie_i++;

        // pie_i is the no of pies for which we've found a rack
        printf("%d\n", pie_i);

    }
    // Deallocate the memory
    delete[] rack_capacity;
    delete[] pie_weight;
}
```
<hr>



### 10. NUMGAME</br>
[https://www.codechef.com/problems/NUMGAME](https://www.codechef.com/problems/NUMGAME)

(30-Jan-2016)



```cpp
// Predict the winner in a number game.

#include<iostream>

int main() {
    int tries, n;

    scanf("%d", &tries);

    while(tries--) {
        scanf("%d", &n);
        if(n % 2)
            printf("BOB\n");
        else
            // If the number is even, the 1st player wins the game
            printf("ALICE\n");
    }
}
```
<hr>



### 11. DOUBLE</br>
[https://www.codechef.com/problems/DOUBLE](https://www.codechef.com/problems/DOUBLE)

(30-Jan-2016)



```cpp
// Max size of double string formed from a palindrome of size n

#include<iostream>

using namespace std;

int main() {
    int tries, n;

    scanf("%d", &tries);

    while (tries--) {
        scanf("%d", &n);
        printf("%d\n", n - n%2);
    }
return 0;
}
```
<hr>



### 12. LCPESY</br>
[https://www.codechef.com/problems/LCPESY](https://www.codechef.com/problems/LCPESY)

(30-Jan-2016)



```cpp
// Get the longest common pattern from the two strings

#include<iostream>
#include<stdio.h>

using namespace std;

int main() {
	int t=0;
	long rep;
	char ch;
	ch = getchar_unlocked();
	while(ch != '\n') {
		t *= 10;
		t += ch-48;
		ch = getchar_unlocked();
	}

	int asciiarray[256];
	while(t--) {
        ch = getchar_unlocked();
		rep = 0;
		for (int i = 48; i<123; i++) {
			asciiarray[i] = 0;
		}
		while(ch != '\n') {		
			asciiarray[ch]++;
			ch = getchar_unlocked();
		}
		ch = getchar_unlocked();
		while(ch !='\n') {
            if(asciiarray[ch] > 0) {
				asciiarray[ch]--;
				rep++;
			}
				
			ch = getchar_unlocked();
		}
		printf("%li\n",rep);
	}
	return 0;
}
```
<hr>



```python

```

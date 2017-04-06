// https://www.codechef.com/problems/DOUBLE
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

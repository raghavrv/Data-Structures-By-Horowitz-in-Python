// https://www.codechef.com/problems/CIELAB
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

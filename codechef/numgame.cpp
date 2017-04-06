// https://www.codechef.com/problems/NUMGAME
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

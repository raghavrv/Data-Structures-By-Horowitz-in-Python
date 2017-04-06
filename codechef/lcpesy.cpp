// https://www.codechef.com/problems/LCPESY
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

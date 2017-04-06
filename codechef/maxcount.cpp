// https://www.codechef.com/problems/MAXCOUNT 
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




// https://www.codechef.com/problems/LECANDY
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

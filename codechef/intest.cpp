// https://www.codechef.com/problems/INTEST
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

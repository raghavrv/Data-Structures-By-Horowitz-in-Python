// https://www.codechef.com/problems/HOLES
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

// https://www.codechef.com/problems/SUBMIN
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

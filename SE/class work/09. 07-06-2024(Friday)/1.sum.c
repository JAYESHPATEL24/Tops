// c program for sum of n number.

#include<stdio.h>
main()
{
	int i,n,sum=0;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=n;i>=1;i--)
		sum += i;
		
	printf("sum of all numbers is : %d",sum);
}

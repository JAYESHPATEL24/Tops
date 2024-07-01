//c program for factorial using while.

#include<stdio.h>
main()
{
	int i=1,n,fac=1;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	
	while(i<=n)
	{
		fac *= i ;
		i++;
	}
		
	printf("factorial is : %d",fac);
}

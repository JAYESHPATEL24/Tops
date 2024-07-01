// c program for factorial number

#include<stdio.h>
main()
{
	int i,n,fac=1;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
		fac *= i;
		
	printf("Factorial is : %d",fac);
}

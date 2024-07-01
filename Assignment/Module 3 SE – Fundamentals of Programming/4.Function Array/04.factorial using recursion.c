//C program to find factorial using recursion.

#include<stdio.h>

int fact(int a)	//function definition
{
	if(a>=1)
		return a*fact(a-1);	//recursion
	else
		return 1;	
}

main()
{
	int n;
	
	printf("Enter any number : ");
	scanf("%d",&n);		//user input
	
	printf("factorial of number %d = %d",n,fact(n));
										// call fact function
}


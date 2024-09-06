//C program for print factorial of given number 

#include<stdio.h>
main()
{
	int i,n,fact=1; // n:number fact:factorial
	
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=n;i>0;i--) //formula for factorial
		fact *= i;
	
	printf("Factorial of number %d = %d ",n,fact);
} 

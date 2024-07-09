//C program for print Fibonacci series up to given numbers 

#include<stdio.h>
main()
{
	int i,n,fab1=0,fab2=1,fab; 
	
	printf("Enter a number : ");
	scanf("%d",&n); // n indicates how many numbers you wanna print.
	
	printf("\nfibonacci series : \n0  1  ");
	
	for(i=1;i<n-1;i++)	// logic for fabonacci series
	{
		fab = fab1 + fab2 ; 
		printf("%d  ",fab);  
		fab1 = fab2 ;
		fab2 = fab ;
	}
}

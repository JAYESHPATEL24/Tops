// C program for check whether a number is negative, positive or zero.

#include<stdio.h>

main()
{
	int n;   //n:number 
	
	printf("Enter a number : ");
	scanf("%d",&n);
	
	if(n==0)		//zero
		printf("Number is zero.");
	else if(n<0)	//negative number 
		printf("Number is negative.");
	else			//positive number
		printf("Number is positive.");
}

//C program to Calculate the Sum of N Natural Numbers Using the While Loop 

#include<stdio.h>
main()
{	
	int a=1,n,sum=0; // n:number sum:summation
	
	printf(" Enter a Number : ");
	scanf("%d",&n);

	while(a<=n)		 // calculate sum of all numbers.
	{
		sum = sum + a;
		a++;
	}	
	
	printf("\n Sum of %d Natural Numbers = %d \n",n,sum); //Print final sum.
}


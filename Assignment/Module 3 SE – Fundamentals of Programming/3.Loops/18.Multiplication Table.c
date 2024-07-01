/* C Program to Print the Multiplication Table of N 
  E.g. 5 * 1 = 5
       5 * 2 = 10  
	      . .
	      . . 
	   5 * 10 = 50 */ 

#include<stdio.h>
main()
{
	int i,n; // n:number
	
	printf("Enter a Number : ");
	scanf("%d",&n);
	
	printf("\nTable for no. %d : \n",n);
	
	for(i=1;i<=10;i++) // multiplication table creation
	{
		printf("\n %d * %d = %d\n",n,i,n*i);
	}
}


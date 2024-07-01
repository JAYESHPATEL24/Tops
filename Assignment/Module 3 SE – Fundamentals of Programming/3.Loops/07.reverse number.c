/*c program to print number in reverse order 
 e.g.: number = 64728 ---> reverse = 82746  */

#include<stdio.h>

main()
{
	int n,m,rvs; //n:number rvs:reverse number 
	
	printf(" Enter a number : ");
	scanf("%d",&n);
	
	while(n>0)	// calculate reverse number.
	{
		m = n % 10;
		rvs = rvs*10 + m;  
		n = n/10;
	}
	
	printf(" \n Reverse Number : %d \n",rvs);
}


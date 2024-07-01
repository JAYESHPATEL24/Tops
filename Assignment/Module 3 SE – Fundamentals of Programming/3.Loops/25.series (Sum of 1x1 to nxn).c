//Series Program : (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n).

#include<stdio.h>
main()
{
	int i,n,sum=0; // n:number sum:summation
	
	printf(" Enter a Number : ");
	scanf("%d",&n);
	
	printf("\n\n Series : \n\n");
	
	for(i=1;i<=n;i++)
	{
		sum = sum + i*i; // calculate sum of all numbers.
		
		if(i==n) 		// print Series
			printf(" (%d*%d)",i,i);
		else
			printf(" (%d*%d) +",i,i);
	}	
	
	printf(" = %d \n",sum); //Print final sum.
}


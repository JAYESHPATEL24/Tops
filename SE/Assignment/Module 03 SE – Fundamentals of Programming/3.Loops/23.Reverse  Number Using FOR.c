//C Program to Reverse a Number Using FOR Loop 

#include<stdio.h>
main()
{
	int i,n,x,rv=0; //n:number rv:reverse number 
	
	printf(" Enter a number : ");
	scanf("%d",&n);
	
	for(i=n;i>0;i/=10)	// calculate reverse Number
	{
		x = i % 10;
		rv = rv*10 + x;  
	}
	
	printf(" \n Reverse Number : %d \n",rv);
}


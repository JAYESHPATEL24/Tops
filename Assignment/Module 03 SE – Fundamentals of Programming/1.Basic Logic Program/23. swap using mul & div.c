// c program for swap 2 numbers with using of multiplication and division.

#include<stdio.h>
main()
{
	int a,b; //a,b:numbers
	
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);
	
		//multiply any number by 0 becomes 0. so..
	if(a==0) 
	{
		a=b;
		b=0;
	}
	else if(b==0)
	{
		b=a;
		a=0;
	}
	else
	{
		a=a*b;
		b=a/b;		// swpping using multiplication & division
		a=a/b;
	}
	printf("\nAfter swpping : \n A : %d B : %d",a,b);
}

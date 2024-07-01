//C program for accept two integers and check whether they are equal or not.

#include<stdio.h>
main()
{
	int a,b;    //a,b:numbers
	
	printf("Enter a number A : ");
	scanf("%d",&a);	
	printf("Enter a number B : ");
	scanf("%d",&b);
	
	if(a==b) // check equallity.
		printf("Numbers are equal.");
	else
		printf("Numbers are not equal.");
	
} 

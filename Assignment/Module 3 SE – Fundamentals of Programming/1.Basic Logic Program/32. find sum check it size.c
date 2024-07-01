//C program to Accept 2 numbers and find out its sum check it size 

#include<stdio.h>
main()
{
	int a,b; // a,b:numbers
	printf(" Enter a number A : ");
	scanf("%d",&a);
	
	printf(" Enter a number B : ");
	scanf("%d",&b);
	
	printf("\n A + B = %d",a+b); //Sum of two numbers
	
	printf("\n\n Size of sum = %d \n",sizeof(a+b)); // size of sum. 
}


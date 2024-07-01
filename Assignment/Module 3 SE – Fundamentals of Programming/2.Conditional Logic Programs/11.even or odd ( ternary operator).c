//C program for find number is even or odd using ternary operator 

#include<stdio.h>
main()
{
	int a;	//a:number
	
	printf("Enter a Number : ");
	scanf("%d",&a);
		//ternary operator
	a%2==0 ? (printf("Even Number.")) : (printf("Odd Number")); 
}


//C peogram for chech Number Is Positive or Negative.

#include<stdio.h>
main()
{
	int a;  //a:number 
	
	printf("Enter a number : ");
	scanf("%d",&a);
	
	if(a==0)		// number is zero
		printf("Number is zero.");
	else if(a<0)		//negative number
		printf("Number is negative.");
	else		//Positive Number
		printf("Number is positive.");
}

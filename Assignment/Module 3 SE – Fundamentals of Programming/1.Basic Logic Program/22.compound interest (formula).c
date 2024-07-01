/*C program for Calculate compound interest 
 Compound Interest formula:
 a. Formula to calculate compound interest annually is given by:
  Amount= P(1 + R/100)t 
 b. Compound Interest = Amount - P */

#include<stdio.h>
#include<math.h>
main()
{
	float p,r,t,i,a; //p:Principal amount r:rate t:time i:interest a:amount
	
	printf(" Please Enter Following data :");
	
	printf("\n\n Principal Amount      : Rs. ");
	scanf("%f",&p);
	printf("\n Interest Rate (in %%)  : ");
	scanf("%f",&r);
	printf("\n Time (in years)       : ");
	scanf("%f",&t);
	
	a = p * pow((1+r/100),t); // calculation for amount
	
	i = a - p;  		// calculate interest.
	
	printf("\n\n Compound Interest = Rs.%.2f ",i);
}


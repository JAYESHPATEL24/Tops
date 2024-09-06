//C program for Calculate compound interest 

#include<stdio.h>
#include<math.h>
main()
{
	float p,r,t,i,a,n; //p:Principal amount r:rate t:time i:interest a:amount n:number of times interest is compounded per year
	
	printf(" Please Enter Following data :");
	
	printf("\n\n Principal Amount       \t: Rs. ");
	scanf("%f",&p);
	printf("\n Interest Rate (in %%)  \t\t: ");
	scanf("%f",&r);
	printf("\n Time (in years/months)  \t: ");
	scanf("%f",&t);
	printf("\n Number of times interest is pounded per year : ");
	scanf("%f",&n);
	
	a = p * pow((1+r/(n*100)),(n*t)); // calculation for amount
	
	i = a - p;  		// calculate interest.
	
	printf("\n\n Compound Interest \t\t= Rs.%.2f ",i);
}


/* C program you have to make a summation of first and last Digit.
 (E.g., 1234 Ans: 5) */
 
#include<stdio.h>
main()
{
	int n,f,l; // n:number f:first digit l:last digit
	
	printf("Enter a number : ");
	scanf("%d",&n);

	l=n%10; // formula for last digit 
	
	while(n>0)
	{
		f=n%10; //formula for first digit
		n=n/10;
	}
	
	printf("Summation of First and Last digits of given number is %d. ",f+l);
												//print sum of digits	
}

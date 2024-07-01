// C program make a summation of given number (E.g., 1523 Ans: 11) 

#include<stdio.h>
main()
{
	int n,m,sum=0; //n:number sum:summation of digits
	
	printf("Enter a number : ");
	scanf("%d",&n);
	
	while(n>0) // calculate sum of all digits.
	{
		m=n%10;
		sum += m;  
		n=n/10;
	}
	
	printf("Summation of all the digits of given number is %d. ",sum);
}

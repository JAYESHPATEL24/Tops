 /* Write a program to find out the max from given number.
(E.g., No: 1562 Max number is 6) */

#include<stdio.h>
main()
{
	int n,m,max=0; //n:number m:last digit max:max digit
	
	printf("Enter a number : ");
	scanf("%d",&n);
	
	while(n>0)		//	find max digit
	{
		m=n%10; 
		
		if(m>max)				
			max = m;
		
		n=n/10;
	}
	
	printf("Max digit from number is %d. ",max);
}

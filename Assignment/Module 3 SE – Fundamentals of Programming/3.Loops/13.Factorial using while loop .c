/*C program for calculate the Factorial of a Given Number
 using while loop*/
  
#include<stdio.h>
main()
{
	int i=1,n,fac=1;  //n:number fac:factorial
	printf("Enter a number : ");
	scanf("%d",&n);
	
	while(i<=n)		//calculation of factorial of a number.
	{
		fac *= i ;
		i++;
	}
		
	printf("factorial is : %d",fac);
}


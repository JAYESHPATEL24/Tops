#include<stdio.h>

fact()	// function without parameter with return type
{
	int n,i,fact=1;
	
	printf("Enter the number : ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		fact*=i;
		
	}
	return fact;
}




main()
{
	printf("Factorial is : %d",fact());	//function call
}

#include<stdio.h>

fact(int b)    //function with parameter with return type
{
	int i,fact=1;
	

	for(i=1;i<=b;i++)
	{
		fact*=i;
		
	}
	return fact;
}


main()
{
	int n;
	printf("Enter the number : ");
	scanf("%d",&n);
	
	printf("factorial is : %d",fact(n));	//function call with arguments
	
}

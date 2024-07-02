//prime Number and fabonacci  

#include<stdio.h>

prime()
{
	int i,n,j=0;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		if(n%i==0)
			j++;
	}
	
	if(j==2)
		printf("%d is prime number.\n\n",n);
	else
		printf("%d is not prime number.\n\n",n);
}

fab()
{
	int n,fab1=0,fab2=1,fab,i;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	printf("Fibonacci Series : \n 0  1  ");
	
	for(i=0;i<n-2;i++)
	{
		fab = fab1 + fab2;
		fab1 = fab2;
		fab2 = fab;
		printf("%d  ",fab);
	}
}
main()
{
	prime();
	fab();
}


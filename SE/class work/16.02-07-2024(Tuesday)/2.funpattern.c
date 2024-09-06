#include<stdio.h>

trio_pattern(int a)	//function with parameter without return type
{
	int i,j,k;
	for(i=1;i<=a;i++)
	{
		for(k=a;k>i;k--)
			printf(" ");

		for(j=1;j<=i;j++)	
			printf(" *");
		printf("\n");
	}
}

main()
{
	int n;
	
	printf("Enter number for row = ");
	scanf("%d",&n);		//user input for raw
	
	trio_pattern(n);	//argument (function trio pattern call)
}


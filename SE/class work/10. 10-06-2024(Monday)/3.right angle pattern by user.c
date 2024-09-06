
#include<stdio.h>

main()
{
	int n,i,j; //data members
	
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++) //raw
	{
		for(j=1;j<=i;j++) //colum
		{
			printf("*");
		}	
		printf("\n");
	}
	
}


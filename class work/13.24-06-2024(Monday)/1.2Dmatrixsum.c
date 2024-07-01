#include<stdio.h>

main()
{
	int i,j,a[2][2],b[2][2],c[2][2];
	
	printf("Enter your 1st Matrix : \n");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("Enter number : ");
			scanf("%d",&a[i][j]);
		}
	}
	
	
	
	printf("\nEnter your 2nd Matrix : \n");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("Enter number : ");
			scanf("%d",&b[i][j]);
		}
	}
	
	printf("\nsum of Matrix : \n");
	
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("\t%d",a[i][j]);		
		}
		printf("\n");
	}
	
	printf("\n\n\t   +\n\n\n");
	
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("\t%d",b[i][j]);		
		}
		printf("\n");
	}
	
	printf("\n\n\t   =\n\n");
	
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("\t%d",a[i][j]+b[i][j]);		
		}
		printf("\n");
	}
}


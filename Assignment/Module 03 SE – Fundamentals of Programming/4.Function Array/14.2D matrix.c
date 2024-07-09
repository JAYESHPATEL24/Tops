//Perform 2D matrix array 

#include<stdio.h>
main()
{
	int i,j,a[2][2];
	
	printf("Enter Elements of 2x2 Array : \n");
	
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("Enter number : ");
			scanf("%d",&a[i][j]);
		}
	}
	
	printf("\nEntered 2x2 matrix is : \n");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("\t%d",a[i][j]);
		}
		printf("\n");
	}
}


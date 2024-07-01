/*C program to maze addition, Subtraction and multiplication of 
two matrix using 2-D Array.*/

#include<stdio.h>
main()
{
	int i,j,k,a[2][2],b[2][2],c[2][2],z=0;
	
	printf("Enter 1st 2x2 Matrix : \n");
	
	for(i=0;i<2;i++)		
	{
		for(j=0;j<2;j++)
		{
			printf("Enter Number : ");
			scanf("%d",&a[i][j]); 	//user input for 1st matrix
		}
	}
	
	printf("\nEnter 2nd 2x2 Matrix : \n");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("Enter Number : ");
			scanf("%d",&b[i][j]);	//user input for 2nd matrix
		}
	}
		
		//print 2 matrices
	printf("\n\nEntered 2x2 Matrices are : \nMatrix 1 : \n");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("%3d  ",a[i][j]);
		}
		printf("\n");
	}
	
	printf("\n\nMatrix 2 : \n");
	for(i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			printf("%3d  ",b[i][j]);
		}
		printf("\n");
	}
	
	printf("\n\nAddition : \n");
	for(i=0;i<2;i++)	// print addition of matrices.
	{
		for(j=0;j<2;j++)
		{
			printf("%3d  ",a[i][j]);
		}
		
		if(z==0)
			printf("  +  ");
		else
			printf("     ");
		
		for(j=0;j<2;j++)
		{
			printf("%3d  ",b[i][j]);
		}
		
		if(z==0)
			printf("  =  ");
		else
			printf("     ");
		for(j=0;j<2;j++)
		{
			printf("%3d  ",a[i][j]+b[i][j]);//calculate addition of marices
		}
		printf("\n");
		z++;
	}
	
	printf("\n\nSubtraction : \n");
	for(i=0;i<2;i++)	//print subtraction of matrices
	{
		for(j=0;j<2;j++)
		{
			printf("%3d  ",a[i][j]);
		}
		
		if(z==2)
			printf("  -  ");
		else
			printf("     ");
		
		for(j=0;j<2;j++)
		{
			printf("%3d  ",b[i][j]);
		}
		
		if(z==2)
			printf("  =  ");
		else
			printf("     ");
		for(j=0;j<2;j++)
		{
			printf("%3d  ",a[i][j]-b[i][j]);//calculate subtraction of matrices
		}
		printf("\n");
		z++;
	}
	
	for(i=0;i<2;i++) //calculate maltiplication of matrices
	{
		for(j=0;j<2;j++)
		{
			c[i][j]=0;
			for(k=0;k<2;k++)
			{
				c[i][j] += a[i][k] * b[k][j];
			}
		}
	}
	
	printf("\n\nMultiplication : \n");
	for(i=0;i<2;i++) //print multiplication of matrices
	{
		for(j=0;j<2;j++)
		{
			printf("%3d  ",a[i][j]);
		}
		
		if(z==4)
			printf("  x  ");
		else
			printf("     ");
		
		for(j=0;j<2;j++)
		{
			printf("%3d  ",b[i][j]);
		}
		
		if(z==4)
			printf("  =  ");
		else
			printf("     ");
		for(j=0;j<2;j++)
		{
			printf("%3d  ",c[i][j]);
		}
		printf("\n");
		z++;
	}
}


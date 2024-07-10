#include<stdio.h>

union array
{
	int a[4];
	int b[4];
	int i;
}s1,s2,s3;


main()
{
	for(s1.i=0;s1.i<4;s1.i++)
	{
		printf("\nEnter elements for A : ");
		scanf("%d",&s2.a[s1.i]);
	}
	
	printf("------------------------------------");
	
	for(s1.i=0;s1.i<4;s1.i++)
	{
		printf("\nEnter Elements for B : ");
		scanf("%d",&s3.b[s1.i]);
	}
	
	printf("------------------------------------\nAddition : \n");
	
	for(s1.i=0;s1.i<4;s1.i++)
	{
		printf("\n %d",s2.a[s1.i]+s3.b[s1.i]);
	}
}

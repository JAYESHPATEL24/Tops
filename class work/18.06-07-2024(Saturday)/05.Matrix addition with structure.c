#include<stdio.h>

struct arraysum
{
	int a[4];
    int	b[4];
	int i;
}s1;

main()
{
	for(s1.i=0;s1.i<4;s1.i++)
	{
		printf("Enter the element A : ");
		scanf("%d",&s1.a[s1.i]);
	}
	
	for(s1.i=0;s1.i<4;s1.i++)
	{
	printf("Enter the element B : ");
	scanf("%d",&s1.b[s1.i]);
	}
	
	printf("Sum of array : ");
	for(s1.i=0;s1.i<4;s1.i++)
	{
		printf("\n%d",s1.a[s1.i]+s1.b[s1.i]);
	}
}

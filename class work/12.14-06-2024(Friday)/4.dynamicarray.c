#include<stdio.h>

main()
{
	int i,a[5];
	
	printf("Enter Elements : ");
	
	for(i=0;i<5;i++)
	{
		printf("\n %d = ",i+1);
		scanf("%d",&a[i]);
	}
	
		printf("Elements are : ");
	for(i=0;i<5;i++)
		printf("%d  ",a[i]);
}


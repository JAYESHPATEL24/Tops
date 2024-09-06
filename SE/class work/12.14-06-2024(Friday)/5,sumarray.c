#include<stdio.h>
main()
{
	int i,a[5],sum=0;
	
	printf("Enter Elements : ");
	
	for(i=0;i<5;i++)
	{
		printf("\n %d = ",i+1);
		scanf("%d",&a[i]);
		sum += a[i]; //sum = sum + a[i];
	}
	
		printf("\n\nElements are : ");
	for(i=0;i<5;i++)
		printf("%d  ",a[i]);
		
		printf("\n\nSum of elements : %d",sum);
}


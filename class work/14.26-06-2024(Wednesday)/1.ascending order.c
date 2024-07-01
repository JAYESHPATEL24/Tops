#include<stdio.h>
main()
{
	int a[4],i,j,temp;
	
	printf("Enter 4 Numbers : ");
	
	for(i=0;i<4;i++)
	{
		scanf("%d",&a[i]);
	}
	
	printf("ASCENDING ORDER : ");
	for(i=0;i<4;i++)
	{
		for(j=i+1;j<4;j++)
			if(a[i]>a[j])
			{
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		
		printf("\n%d",a[i]);
	}
}


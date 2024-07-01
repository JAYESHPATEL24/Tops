//C program to Store 5 numbers in array and sort it in ascending order 

#include<stdio.h>
main()
{
	int i,j,a[5],temp; 
	
	printf("Enter 5 Numbers : \n");
	
	for(i=0;i<5;i++)
	{
		printf("%d. ",i+1);
		scanf("%d",&a[i]);	//accept 5 numbers from user
	}
	
	
	printf("\nNumbers in Ascending order : \n");
			//arrange and print numbers in ascending order.
	for(i=0;i<5;i++) 
	{
		for(j=i+1;j<5;j++)
			if(a[i]>a[j])
			{
				temp = a[i];
				a[i] = a[j];
				a[j] = temp; 
			}
		printf(" %d ",a[i]); 
	}
}


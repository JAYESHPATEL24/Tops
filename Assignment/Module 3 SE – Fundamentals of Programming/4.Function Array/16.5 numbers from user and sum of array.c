//C program to Accept 5 numbers from user and perform sum of array. 

#include<stdio.h>
main()
{
	int i,a[5],sum=0;
	
	printf("Enter 5 numbers : \n");
	for(i=0;i<5;i++)
	{
		printf("%d.",i+1);
		scanf("%d",&a[i]);	//accept number
		sum = sum + a[i];	//perform Summation
	}
	
	printf("\nSum of array elemets = %d",sum);
}


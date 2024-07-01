//C program to find out the max number from given array using function 

#include<stdio.h>

int max(int x[5])	//fuction with parameter and with return type.
{
	int max=0,k;
	for(k=0;k<5;k++)
	{
		if(x[k]>max)
		max=x[k];
	}
	return max;		//return value of max.
}


main()
{
	int a[5],i;
	
	printf("Enter 5 numbers : \n");
	
	for(i=0;i<5;i++)	
	{
		printf("%d. ",i+1);
		scanf("%d",&a[i]);	//user input
	}
		
	printf("\nMaximum number from given array : %d",max(a));
										//call max fuction
}


/*C program for Accept 5 numbers from user and 
find those numbers factorials.*/

#include<stdio.h>
main()
{
	int i,j,a[5],fact;
	
	printf(" Enter any 5 number : \n");
	
	for(i=0;i<5;i++)	//Accept 5 numbers from users.
	{
		printf(" No %d = ",i+1);
		scanf("%d",&a[i]);
	}	
	
	for(i=0;i<5;i++)	//calculate factorial for every number.
	{	
		fact=1;
		for(j=a[i];j>0;j--)
		{
			fact *= j;
		}
		printf("\n Factorial of no %d = %d",a[i],fact);
	}
}


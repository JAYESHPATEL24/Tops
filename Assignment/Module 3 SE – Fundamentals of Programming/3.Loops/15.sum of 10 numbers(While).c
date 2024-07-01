//c program Calculate sum of 10 numbers using of while loop .

#include<stdio.h>
main()
{
	int i,a[10],sum=0; //declare array
	
	printf("Enter any 10 numbers : \n");
	
	for(i=0;i<10;i++)	// Accept 10 numbers from users.
	{
		printf(" No. %-2d = ",i+1);
		scanf("%d",&a[i]);
		sum += a[i];		// summation of all numbers.
	}	
	
	printf("\nSum of all 10 Numbers = %d ",sum); 
}


/*C program to Calculate 5 numbers from user and calculate number of 
even and odd using of while loop */

#include<stdio.h>
main()
{
	int i=0,a[5],count=0;
	
	printf("Enter any 5 Number : \n");
	
	while(i<5)		//Accept Number from users.
	{
		printf("No. %-2d = ",i+1);
		scanf("%d",&a[i]);
		i++;
	}
	
	i=0;
	printf("\nEven Numbers : ");
	while(i<5)		
	{
		if(a[i]%2==0)	//Find & print Even numbers.
		{
			printf(" %d",a[i]);
			count++;		//count Even numbers.
		}
		i++;
	}
	printf("\nThere are %d Even Numbers.",count);
	
	i=0;
	count=0;
	
	printf("\n\n\nOdd Numbers : ");
	while(i<5)
	{
		if(a[i]%2==1) //find and print Odd numbers.
		{
			printf(" %d",a[i]);
			count++;	//Count Odd Numbers.
		}
		i++;
	}
	printf("\nThere are %d Odd Numbers.",count);
}


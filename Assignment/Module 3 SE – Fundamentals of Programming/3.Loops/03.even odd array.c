/*C program to take 10 no. Input from user find out below values 
  a. How many Even numbers are there 
  b. How many odd numbers are there 
  c. Sum of even numbers 
  d. Sum of odd numbers */ 

#include<stdio.h>
main()
{
	int i,a[10],sum=0,count=0; 
	
	printf("Enter any 10 numbers : \n");
	
	for(i=0;i<10;i++) //user inputs
	{
		printf(" No. %-2d = ",i+1);
		scanf("%d",&a[i]);
	}
		
			//Even numbers	
			
	printf("\nEven Numbers :");
	for(i=0;i<10;i++)
	{
		if(a[i]%2==0)			//find even numbrs.
		{
			printf(" %d",a[i]);	//print all Even numbers.
			sum += a[i];			//summation of all even numbers.
			count++;			//count even numbers.
		}	
	}
	
	printf("\nThere are %d Even numbers.",count);
	printf("\nSum of Even Numbers = %d ",sum);
	
	
			//Odd numbers
	
	printf("\n\n\nOdd Numbers :");
	sum=0;
	count=0;
	for(i=0;i<10;i++)
	{
		if(a[i]%2==1)		//find odd numbrs.
		{
			printf(" %d",a[i]);	//print all odd numbers.
			sum += a[i];		//summation of all odd numbers.
			count++;			//count Odd numbers.
		}	
	}
	
	printf("\nThere are %d Odd numbers.",count);
	printf("\nSum of Odd Numbers = %d ",sum);
}


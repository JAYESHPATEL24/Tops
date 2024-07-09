//Series Program : 1/2 - 2/3 + 3/4 - 4/5 + 5/6 ........... n 

#include<stdio.h>
main()
{
	float sum; // n:number sum:summation
	int i,n;
	
	printf(" Enter a Number : ");
	scanf("%d",&n);
	
	printf("\n\n Series : \n\n");
	
	for(i=1;i<n;i++) // calculate sum of series
	{		
		if(i%2==0)
			sum = sum - (float)i/(i+1);
		else
			sum = sum + (float)i/(i+1);
	}
	
	for(i=1;i<n;i++) //print Series
	{
		if(i==n-1)
			printf(" %d/%d = ",i,i+1);
			
		else if(i%2==1)
			printf(" %d/%d -",i,i+1);
			
		else
			printf(" %d/%d +",i,i+1);
	}
	
	printf("%.4f",sum); //print final sum
}


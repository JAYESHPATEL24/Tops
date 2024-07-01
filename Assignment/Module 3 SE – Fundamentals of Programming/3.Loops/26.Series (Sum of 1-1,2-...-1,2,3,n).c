//Series Program : (1)+ (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n).

#include<stdio.h>
main()
{
	int i,j,n,sum=0,sum1=0; // n:number sum,sum1:summation
	
	printf(" Enter a Number : ");
	scanf("%d",&n);
	
	printf("\n\n Series : \n\n");
	
	for(i=1;i<=n;i++) // calculate sum of series
	{
		sum = sum + i;
		sum1 = sum1 + sum ;
	}	
	
	for(i=1;i<=n;i++) 			// Print series.
	{
		printf("(");
		for(j=1;j<=i;j++)
		{	
			if(j==i)
				printf("%d",j);
			else
				printf("%d+",j);
		}
		if(i==n)
			printf(")");
		else
			printf(") + ");
	}
	
	printf(" = %d \n",sum1);  		//Print final sum.
}


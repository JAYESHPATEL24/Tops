//Series Program : 1 2 3 6 9 18 27 54... 

#include<stdio.h>
main()
{
	int i,n,x=1,y=2; // n:number x,y:1st two number of series.
	
	printf(" Enter a Number : ");
	scanf("%d",&n);
	
	printf("\n\n Series : \n\n");
	
	printf(" %d %d",x,y); //print first two numbers.
	
	for(i=3;i<=n;i++)  		//print Series
	{
		if(i%2==1)
			{
				x=x*3;
				printf(" %d",x);
			}
			
		else
			{
				y=y*3;
				printf(" %d",y);
			}
	}	
}


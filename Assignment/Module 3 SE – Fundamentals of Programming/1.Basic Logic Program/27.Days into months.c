// c program for Convert days into months.

#include<stdio.h>
main()
{
	int d,m; // d:days m:months
	
	printf("Enter days : ");
	scanf("%d",&d);
	
	m=d/30;//convert days into months (1 month = 30 days).
	
	printf("\nMonths : %d ",m);
}

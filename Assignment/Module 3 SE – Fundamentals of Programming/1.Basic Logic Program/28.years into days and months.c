//c program for Convert years into days and months.

#include<stdio.h>
main()
{
	int y; // y:years d:days m:months
	
	printf("Enter years : ");
	scanf("%d",&y);
	
	printf("\nDays   : %d ",y*365); // 1 year = 365 Days
	
	printf("\nMonths : %d",y*12); // 1 year = 12 months
}

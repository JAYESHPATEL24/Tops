//c program for convert years into days and days into years 

#include<stdio.h>
main()
{
	int y,d; // y:years d:days
	
	printf("Enter years : ");
	scanf("%d",&y);
	
	printf("\nDays of %d years = %d",y,y*365);//1 year = 365 days
	
	printf("\n\n\nEnter days : ");
	scanf("%d",&d);
	
	printf("\nYears of %d days = %d",d,d/365);//365 days = 1 year
}

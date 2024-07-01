//C program Accept the input month number and print number of days in that month. */

#include<stdio.h>
main()
{
	int m; // m:month
	
	printf("Enter a Month no : ");
	scanf("%d",&m);
	
	if(m==1||m==3||m==5||m==7||m==8||m==10||m==12)//Theses months have 31 days.
		printf("Number of Days in month %d = 31.",m);
	else if(m==2) 							// only 2nd months has 28 or 29 days.
		printf("Number of in 2nd Days = 28/29");
	else 									// other months have 30 days.
		printf("Number of Days in month %d = 30.",m);
}

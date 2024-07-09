/* C program to read any Month Number in integer and display the 
number of days for this month. */

#include<stdio.h>
main()
{
	int m; // m:month
	
	printf("Enter a Month no : ");
	scanf("%d",&m);
	
	if(m==1||m==3||m==5||m==7||m==8||m==10||m==12)//This months have 31 days.
		printf("Number of Days in month %d = 31.",m);
	else if(m==2) 							// only 2nd months has 28 or 29 days.
		printf("Number of Days in month  2 = 28/29");
	else 									// other months have 30 days.
		printf("Number of Days in month %d = 30.",m);
}

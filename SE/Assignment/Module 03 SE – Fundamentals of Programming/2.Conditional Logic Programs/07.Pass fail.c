//C program for Accept marks from user and check pass or fail.

#include<stdio.h>
main()
{
	int m; // m:marks
	
	printf("Enter marks from 1 to 100 : ");
	scanf("%d",&m);
	
	if(m>=33) // consider passing marks is 33.
		printf("\nStudent is pass.");
	else 
		printf("\nStudent is fail.");
}

// c program for Convert minutes into seconds and hours 

#include<stdio.h>
main()
{
	int m; // m:minutes
	
	printf("Enter a minutes : ");
	scanf("%d",&m);
	
	printf("\nSeconds : %d",m*60); // 1 minutes = 60 seconds
	
	printf("\nHours   : %d",m/60); // 60 minutes = 1 hour
}

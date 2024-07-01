//C program for input the week number and print week day. 
 
#include<stdio.h>
main()
{
 	int w; //w:week number
 	
 	printf("Enter no of weeks : ");
 	scanf("%d",&w);
 	
 		// day name according to week day no.
 	if(w==1)
 		printf("Monday");
 	else if(w==2)
 		printf("Tuesday");
 	else if(w==3)
 		printf("Wednesday");
 	else if(w==4)
 		printf("Thursday");
 	else if(w==5)
 		printf("Friday");
 	else if(w==6)
 		printf("Saturday");
 	else if(w==7)
 		printf("Sunday");
 	else
 		printf("INCORRECT WEEK NO.");
}

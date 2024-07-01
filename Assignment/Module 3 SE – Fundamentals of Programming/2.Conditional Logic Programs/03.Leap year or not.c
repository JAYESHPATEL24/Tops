//WAP to check if the given year is a leap year or not. 

#include<stdio.h>
main()
{
	int y; // y:year
	
	printf("Enter any Year : ");
	scanf("%d",&y);
	
	if(y%400==0) //leap with last digits 00 always divided by 400. 
		printf("%d is leap year.",y);
	
	else if(y%100==0)//divided by 100 but not by 400 is not leap year.
		printf("%d is not leap year.",y);
		
	else if(y%4==0) //Leap year without last digit 00 is divided by 4.
		printf("%d is leap year.",y);
	
	else
		printf("%d is not leap year.",y);
}

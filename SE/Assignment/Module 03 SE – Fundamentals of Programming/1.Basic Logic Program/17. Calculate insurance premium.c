//C program to Calculate person's insurance premium based on salary 

#include<stdio.h>
main()
{
	float s,y; //s:sum assured y:year
	
	printf(" Enter sum assured : Rs. ");
	scanf("%f",&s);
	
	printf(" Enter insurance policy terms(in years.) : ");
	scanf("%f",&y);
	
				// calculate premiums
	printf("\n\n Monthly Premium   : Rs.%.2f",s/(y*12));
	printf("\n Quarterly Premium   : Rs.%.2f",s/(y*4));
	printf("\n Half yearly Premium : Rs.%.2f",s/(y*2));
	printf("\n yearly Premium      : Rs.%.2f",s/(y));
}


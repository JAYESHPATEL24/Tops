//C program for Accept 5 expense from user and find average of expense 

#include<stdio.h>
main()
{
	float av,ex1,ex2,ex3,ex4,ex5; // av:average ex1-ex5:expenses 
	
	printf("Enter 1st Expense : Rs.");
	scanf("%f",&ex1); 
	
	printf("Enter 2nd Expense : Rs.");
	scanf("%f",&ex2);
	
	printf("Enter 3rd Expense : Rs.");
	scanf("%f",&ex3);
	
	printf("Enter 4th Expense : Rs.");
	scanf("%f",&ex4);
	
	printf("Enter 5th Expense : Rs.");
	scanf("%f",&ex5); 
	
	av = (ex1+ex2+ex3+ex4+ex5)/5.0; //formula for find average.
	
	printf("\nAverage of expenses = Rs.%.2f\n",av);
}


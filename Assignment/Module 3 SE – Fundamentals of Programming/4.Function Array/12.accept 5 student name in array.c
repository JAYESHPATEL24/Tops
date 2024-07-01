//C program to accept 5 students name and store it in array

#include<stdio.h>
main()
{
	char stu[5][30];
	int i;
	
	printf("Enter 5 Student's names : \n");
	
	for(i=0;i<5;i++)	//Accept names from the user.
	{
		printf(" %d. ",i+1);
		gets(stu[i]);
	}
	
	printf("\nEntered Student's names : \n");
	for(i=0;i<5;i++)	//display stored names.
	{
		printf(" %d. ",i+1);
		puts(stu[i]);
	}
}


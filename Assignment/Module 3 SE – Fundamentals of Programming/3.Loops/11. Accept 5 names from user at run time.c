//C program for Accept 5 names from user at run time. 

#include<stdio.h>
#include<string.h>
main()
{
	char a[5][15];	//declare character array.
	int i;
	
	printf("Enter 5 names : \n");
	
	for(i=0;i<5;i++)	//Accept 5 name from user.
	{
		printf(" Name %d. ",i+1);
		gets(a[i]);
	}
	
	printf("\n\n\nList of name : \n");
	
	for(i=0;i<5;i++) 	//print all names : 
	{
		printf(" %d. ",i+1);
		puts(a[i]);
	}
}


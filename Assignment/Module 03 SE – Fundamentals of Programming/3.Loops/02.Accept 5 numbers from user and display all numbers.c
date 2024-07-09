// C program to accept 5 numbers from user and display all numbers 

#include<stdio.h>

main()
{
	int i,a[5]; // array declaration
	
	printf("Enter Any 5 Numbers : \n");
	
	for(i=0;i<5;i++)  
	{
		printf("%d. ",i+1);
		scanf("%d",&a[i]); // Accept elements form user.
	}
	
	printf("\n\n\n Display all Number : \n");
	
	for(i=0;i<5;i++)		// print all number stored in array.
		printf("\n%d. %d",i+1,a[i]);
}


/*C program to accept 5 numbers from user and 
display in reverse order using for loop and array */

#include<stdio.h>
main()
{
	int i,j,a[5];
	
	printf("Enter 5 numbers : \n");

	for(i=0;i<5;i++)
	{
		printf("%d.",i+1);
		scanf("%d",&a[i]);		//user inputs
	}
	
	//print array in order
	printf("\nArray Elements in order : \n");
	for(i=0;i<5;i++)
		printf("%d\n",a[i]);
		
	//print array in reverse order
	printf("\nArray Elements in Reverse Order : \n"); 
	for(i=4;i>=0;i--)
			printf("%d\n",a[i]);
}


/*c program for Accept number of students from user. 
I need to give 5 apples to each student. How many apples are required?*/

#include<stdio.h>
main()
{
	int n; // n:number of students  
	
	printf("Enter a Number of Students : ");
	scanf("%d",&n);
	
	printf("\nThere are '%d' apples are required.",n*5); 
				// (1 student = 5 apples) so (n students = 5n apples) 
}

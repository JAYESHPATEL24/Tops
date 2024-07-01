//c program for circumference of square

#include<stdio.h>
main()
{
	int c,l; // c:Circumference l:length 
	
	printf("Enter a Length of square : ");
	scanf("%d",&l);
	
	c=4*l; // formula for circumference of square
	
	printf("\nCircumference of square : %d",c);
}

//c program for circumference of Triangle

#include<stdio.h>
main()
{
	int c,x,y,z; // c:Circumference x,y,z:sides of Triangle
	
	printf("Enter Length of three sides of Triangle :-   ");
	printf("\n\n X : ");
	scanf("%d",&x);
	printf("\n Y : ");
	scanf("%d",&y);
	printf("\n Z : ");
	scanf("%d",&z);
	
	c=x+y+z; // formula for circumference of Triangle
	
	printf("\nCircumference of Triangle : %d",c);
}

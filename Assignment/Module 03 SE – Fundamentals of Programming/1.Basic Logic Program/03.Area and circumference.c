// c program to Find Area And Circumference of Circle.

#include<stdio.h>
#define pi 3.14
main()
{
	float r,a,c; // r:radius a:area c:circumference
	
	printf("Enter a radius of circle : ");
	scanf("%f",&r);
	
	a=pi*r*r; // formula for Area of Circle.
	
	printf("\nArea of circle          : %.2f ",a);
	
	c=2*pi*r; // formula for Circumference of circle.
	
	printf("\nCircumference of circle : %.2f ",c);
}

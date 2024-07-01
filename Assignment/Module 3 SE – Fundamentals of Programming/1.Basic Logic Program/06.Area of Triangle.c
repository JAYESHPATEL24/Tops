// c program for Area of Triangle

#include<stdio.h>
main()
{
	float b,h,a; // b:base h:perpendicular height a:area
	
	printf("Enter a Base of Triangle : ");
	scanf("%f",&b);
	
	printf("Enter a Perpendicular Height of Triangle : ");
	scanf("%f",&h);
	
	a=(b*h)/2; // formula for Area of Triangle
	
	printf("\nArea of Triangle : %.2f",a);
}

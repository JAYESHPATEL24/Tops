// c program for Area of Rectangle

#include<stdio.h>
main()
{
	int l,w,a; // l:length w:width a:area
	
	printf("Enter a Length of Rectangle : ");
	scanf("%d",&l);
	printf("Enter a width of Rectangle : ");
	scanf("%d",&w);
	
	a=l*w; // formula for Area of Rectangle
	
	printf("\nArea of Rectangle : %d",a);
}

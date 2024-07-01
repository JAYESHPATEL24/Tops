//c program for circumference of Rectangle

#include<stdio.h>
main()
{
	int c,l,w; // c:Circumference l:length w:width
	
	printf("Enter a Length of Rectangle : ");
	scanf("%d",&l);
	printf("Enter a width of Rectangle : ");
	scanf("%d",&w);
	
	c=2*(l+w); // formula for circumference of Rectangle
	
	printf("\nCircumference of Rectangle : %d",c);
}

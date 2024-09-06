//c program for Area of a Rectangular Prism

#include<stdio.h>
main()
{
	int a,l,w,h; // a:area l:length w:width h:height
	
	printf("Enter a Length of Rectangular Prism : ");
	scanf("%d",&l);
	printf("Enter a width  of Rectangular Prism : ");
	scanf("%d",&w);
	printf("Enter a Height of Rectangular Prism : ");
	scanf("%d",&h);
	
	a=2*(l*w+w*h+h*l); // formula for Area of a Rectangular Prism
	
	printf("\nArea of Rectangular Prism : %d",a);
}

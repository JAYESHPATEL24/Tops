/*C program to check whether a triangle can be formed with 
the given values for the angles.*/

#include<stdio.h>
main()
{
	int a,b,c,t; // a,b,c:value of angles t:total
	
	printf("Enter values of three angles of Triangle :-   ");
	printf("\n\n A : ");
	scanf("%d",&a);
	printf("\n B : ");
	scanf("%d",&b);
	printf("\n C : ");
	scanf("%d",&c);
	
	t=a+b+c; // total of all angles
	
	if(t==180) //sum of all the angles of triangle is 180.
		printf("\ntriangle can formed with these angles.");
	else
		printf("\ntriangle can not formed with these angles.");
}


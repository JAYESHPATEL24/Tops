//C program for find minimum number among 3 numbers using ternary operator 

#include<stdio.h>
main()
{
	int a,b,c; //a,b,c:numbers
	
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);
	printf("Enter a number C : ");
	scanf("%d",&c);
	
	a<b ? (a<c?printf("A : %d is Minimum",a):printf("C : %d is Minimum",c)) :  (b<c?printf("B : %d is Minimum",b):printf("C : %d is Minimum",c));
				// ternery operators inside ternery operator with logic to find minimum number.
}


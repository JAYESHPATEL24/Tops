//C program to find maximum number among 3 numbers using ternary operator 

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
	
	a>b ? (a>c?printf("A : %d is maximum",a):printf("C : %d is maximum",c)) :  (b>c?printf("B : %d is maximum",b):printf("C : %d is maximum",c));
				// ternery operators for find maximum number
}


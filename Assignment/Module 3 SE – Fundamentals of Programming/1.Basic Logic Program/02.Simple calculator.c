/*c program for to make Simple calculator
(addition, subtraction, multiplication, division and modulo).*/

#include<stdio.h>
main()
{
	int a,b;  // data members a,b:numbers
	
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);
	
	printf("\nAddition      : %d",a+b);
	printf("\nSubtraction   : %d",a-b);
	printf("\nMultiplication: %d",a*b);
	printf("\nDivision      : %.3f",(float)a/b); // Type Conversion
	printf("\nModulo        : %d",a%b); 
}

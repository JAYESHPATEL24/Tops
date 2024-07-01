/*C program for make simple calculator 
(operation include Addition, Subtraction, Multiplication,
 Division, modulo) using conditional statement */
 
#include<stdio.h>
main()
{
	char c; 		//c:choice
	int a,b;		//a,b:numbers
	
	printf("Enter your choice from (+, -, *, /, %%) : ");
	scanf("%c",&c);	
	
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);
	
	switch(c)
	{
		case '+':
			printf("\nA + B = %d",a+b);		//Addition
			break;
		case '-':
			printf("\nA - B = %d",a-b);		//Subtraction
			break;
		case '*':
			printf("\nA * B = %d",a*b);		//Multiplication
			break;
		case '/':
			printf("\nA / B = %f",(float)a/b);	//Division
			break;
		case '%':
			printf("\nA %% B = %d",a%b);		//Modulo
			break;
		default :
			printf("\nINVALID CHOICE.");
	}
}

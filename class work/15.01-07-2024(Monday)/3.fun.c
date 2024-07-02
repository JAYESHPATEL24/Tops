//functions

#include<stdio.h>
		//functions without parameters and without return type
add()		//fuction defition 
{
	int a,b;
	printf("Enter a Number : ");
	scanf("%d",&a);
	printf("Enter a Number : ");
	scanf("%d",&b);
	
	printf("Addition = %d\n\n",a+b);
}
sub()	
{
	int a,b;
	printf("Enter a Number : ");
	scanf("%d",&a);
	printf("Enter a Number : ");
	scanf("%d",&b);
	
	printf("Subtraction = %d\n\n",a-b);
}
mul()
{
	int a,b;
	printf("Enter a Number : ");
	scanf("%d",&a);
	printf("Enter a Number : ");
	scanf("%d",&b);
	
	printf("Multiplication = %d\n\n",a*b);
}
main()
{	
		//function calling
	add();
	add();
	sub();
	mul();
}

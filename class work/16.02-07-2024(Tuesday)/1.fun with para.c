//Function with parameter and without return type

#include<stdio.h>

add(int x,int y)	//parameters
{
	printf("%d",x);
	printf("\n%d",y);
	
	printf("\nAddition = %d",x+y);
}

main()
{
	int a,b;
	
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);
	
	add(a,b);	//arguments
}


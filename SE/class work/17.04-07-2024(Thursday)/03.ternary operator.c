#include<stdio.h>

main()
{
	int n;
	
	printf("Enter the number : ");
	scanf("%d",&n);
	
	(n%2==0)?printf("number is even."):printf("number is odd."); //ternary operator
}

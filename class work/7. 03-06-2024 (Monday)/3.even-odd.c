#include<stdio.h>

main()
{
	int n;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	if(n==0)
		printf("Zero");
	else if(n%2==0)
		printf("Even Number.");
	else
		printf("Odd Number.");
}


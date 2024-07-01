#include<stdio.h>

main()
{
	int n;
	
	printf("Enter Age : ");
	scanf("%d",&n);
	
	if(n>100)
		printf("invalid age.");
	else if(n>=18)
		printf("Valid for vote.");
	else
		printf("Not Eligible.");
}


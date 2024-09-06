#include<stdio.h>

main()
{
	int a;
	printf("Enter a Number : ");
	scanf("%d",&a);
	
	if(a>0)
		printf("Positive Number.");
	else if(a==0)
		printf("Zero.");
	else
		printf("Nagetive Number.");
}


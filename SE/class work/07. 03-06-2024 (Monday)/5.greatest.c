#include<stdio.h>

main()
{
	int a,b,c;
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);
	printf("Enter a number C : ");
	scanf("%d",&c);
	
	if(a>b)
	{
		if(a>c)
			printf("%d is greatest.",a);
		else
			printf("%d is greatest.",c);
	}
	else
	{
		if(b>c)
			printf("%d is greatest.",b);
		else
			printf("%d is greatest.",c);
	}
}


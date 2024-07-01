#include<stdio.h>

main()
{
	int a,b,c;
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);

	c=a;
	a=b;
	b=c;
	
	printf("After Swapping \n A : %d and B : %d",a,b);
}


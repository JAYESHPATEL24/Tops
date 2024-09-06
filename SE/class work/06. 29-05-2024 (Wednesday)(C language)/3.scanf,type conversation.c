#include<stdio.h>

main()
{
	int a,b; 
	
	printf("Enter A : ");
	scanf("%d",&a);
	printf("Enter B : ");
	scanf("%d",&b);
	
	printf("\nAddition : %d",a+b);
	printf("\nSubtracion : %d ",a-b);
	printf("\nMulplication : %d ",a*b);
	printf("\nDivison : %.2f",(float)a/b);	
}


#include<stdio.h>
struct info			//structure
{
	int a;
	int b;
	
}s1;	//declaration of Structure variable.
main()
{
	printf("Enter the A : ");
	scanf("%d",&s1.a);
	printf("Enter the B : ");
	scanf("%d",&s1.b);
	printf("\n%d",s1.a);
    printf("\t%d",s1.b);
}



#include<stdio.h>

main()
{
	char a[4],b[4];
	
	printf("Enter a string : ");
	gets(a);
	
	strcpy(b,a);
	
	printf("\n A : %s",a);
	printf("\n B : %s",b);
}


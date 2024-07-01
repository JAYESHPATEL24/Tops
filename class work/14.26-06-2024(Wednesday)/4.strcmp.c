#include<stdio.h>
main()
{
	char a[5],b[6];
	int n;
	
	printf("Enter string A : ");
	gets(a);
	printf("Enter String B : ");
	gets(b);
	
	n = strcmp(a,b);
	
	printf("%d",n);
}


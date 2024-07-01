#include<stdio.h>
main()
{
	char a[5],b[6];
	
	printf("Enter string A : ");
	gets(a);
	printf("Enter String B : ");
	gets(b);
	
	strcat(a,b);
	printf("string : %s",a);
}


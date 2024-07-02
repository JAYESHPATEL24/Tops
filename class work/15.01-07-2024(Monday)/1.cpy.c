#include<stdio.h>
main()
{
	char a[10],b[10];
	int i;
	
	printf("Enter any String : ");
	gets(a);
	
	for(i=0;a[i]!='\0';i++)
		b[i]=a[i];
	
	b[i]='\0';
	
	printf("copy String : ");
	puts(b);
}


#include<stdio.h>
main()
{
	char a[10],b[10];
	int i,j;
	
	printf("Enter any String 1 : ");
	gets(a);
	
	printf("Enter any String 2 : ");
	gets(b);
	
	for(i=0;a[i]!='\0';i++);
	
	for(j=0;b[j]!='\0';j++)
	{
		a[i]=b[j];
		i++;
	}
	a[i]='\0';
	
	printf("String Concat is : ");
	puts(a);
}


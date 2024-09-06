//C program to separate individual characters from a string.

#include<stdio.h>
main()
{
	char a[30];
	int i,l;
	
	printf("Enter a String : ");
	gets(a);			//Accept a string from user.
	
	printf("characters in string are : ");
	
	for(i=0; a[i]!='\0'; i++) // print all the characters seperately.
	{
		if(a[i]==' ')
			continue;
		else
			printf("\n %c ",a[i]);
	}
}


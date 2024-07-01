//C program to print individual characters of a string in reverse order. 

#include<stdio.h>
main()
{
	char a[30];
	int i,l=0;
	
	printf("Enter a String : ");
	gets(a);			//Accept a string from user.
	
	for(i=0;a[i]!='\0';i++)
		l++;
	
	
	printf("characters in string are : ");
	
	for(i=l-1;i>=0;i--) // print all the characters seperately in reverse.
	{
		if(a[i]==' ')
			continue;
		else
			printf("\n %c ",a[i]);
	}	
}


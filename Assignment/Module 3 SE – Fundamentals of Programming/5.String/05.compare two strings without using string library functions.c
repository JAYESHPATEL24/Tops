//C program to compare two strings without using string library functions. 

#include<stdio.h>
main()
{	
	char a[10],b[10];
	int i,j;
			//Accept two Strings from the user.
	printf(" Enter String A : ");
	gets(a);
	printf(" Enter String B : ");
	gets(b);
		
			//Check Equality of Strings 
	for(i=0;a[i]!='\0';i++)
	{
		if(a[i]==b[i])
			j=1;
		else 
		{
			j=0;
			break;
		}
	}
	
	if(j==1)
		printf("\n String A and String B Are Same Strings.");
	else
		printf("\n String A and String B Are not Same Strings.");
}


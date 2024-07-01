//C program to copy one string to another string.

#include<stdio.h>
main()
{
	char a[30],b[30];
	
			//Accept Two Strings from the user. 
	printf("Enter string A : ");
	gets(a);
	printf("Enter string B : ");
	gets(b);
	
	strcpy(b,a);	//Function for copy String from a to b.
	
	printf("\n\nAfter Copy String : \n");
		//print strings after copy string 
	printf("\nString A : %s",a);
	printf("\nString B : %s",b);
}


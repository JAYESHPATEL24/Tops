//C program to combine two strings manually.

#include<stdio.h>
main()
{
	char a[30],b[30];
	int i,j;
					
				//Accept Two strings from the user.
	printf("Enter String A : ");
	gets(a);
	printf("Enter String B : ");
	gets(b);
	
	for(i=0;a[i]!='\0';i++); //terminate 1st string
	
		//Combine 2nd strings with 1st string 
	for(j=0;b[j]!='\0';j++)	 
	{
		a[i]=b[j];
		i++;
	}
	a[i]='\0';
	
	printf("\nAfter Combine two Strings : %s",a);
}


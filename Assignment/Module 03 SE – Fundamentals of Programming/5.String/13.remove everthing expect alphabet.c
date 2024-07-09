//C program to remove characters from a string except alphabets. 

#include<stdio.h>
main()
{
	char a[30];
	int i,j;
	
	printf("Enter any String : ");
	gets(a);		//user input
	
	for(i=0;a[i]!='\0';i++)
	{
		//if character are not an alphabet then enter this loop
		while(!(a[i]>='a'&& a[i]<='z') && !(a[i]>='A'&& a[i]<='Z') && !(a[i]=='\0') && !(a[i]==' '))
		{
			for(j=i;a[j]!='\0';j++)
			{
				a[j] = a[j+1];	//remove characater
			}
			a[j]='\0';
		}
	}
	printf("\nAfter Removing all the Characters except Alphabets String : %s",a);
}


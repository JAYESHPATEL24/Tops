//C program to extract a substring from a given string  

#include<stdio.h>
main()
{
	char a[10],as[10];
	int i,j=0,l,s;
	
	printf("Enter a String : ");
	gets(a);			// input string from user.
	printf("Enter Starting Position for extract Substring : ");
	scanf("%d",&s);		// Staring word position from string given by user.
	printf("Enter length of Substring : ");
	scanf("%d",&l);	   //	length of substring given by user. 
	
	for(i=s-1;i<l+s-1;i++) //extract Sub string From the main String.
	{
		as[j] = a[i] ;
		j++;
	}
	a[j]='\0';
	
	printf("\nSubstring : %s",as);
}


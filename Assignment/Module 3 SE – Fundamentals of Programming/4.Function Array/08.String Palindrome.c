//C program to reverse a string and check that the string is palindrome or not 

#include<stdio.h>
main()
{
	char s[30],rs[30];
	int i,l=0,j;
	
	printf("Enter any String : ");
	gets(s);			//user input
	
	for(i=0;s[i]!='\0';i++)	//count length of String.
		l++;
	
	for(i=0;s[i]!='\0';i++) //Reverse a String
	{
		l--;
		rs[l]=s[i];	     //store reversed string in rs variable.
	}
	
	for(i=0;s[i]!='\0';i++)//Check String and reverse String are same or not
	{
		if(s[i]==rs[i])
			j=1;
		else 
		{
			j=0;
		}
	}
						//print String is palindrome or not
	if(j==1)
		printf("String is Palindrome.");
	else
		printf("String is not Palindrome.");
}


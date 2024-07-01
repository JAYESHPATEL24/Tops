/*C program to read a sentence and replace lowercase characters with
 uppercase and vice versa.*/ 

#include<stdio.h>
main()
{
	char s[30];
	int i;
	
	printf(" Enter a String : ");
	gets(s);	//user input
	
	for(i=0;s[i]!='\0';i++)
	{	
				//Convert upper case to lower case
		if(s[i]>='A' && s[i]<='Z')
			s[i] = s[i] + 32;
				//Convert lower case to upper case
		else if(s[i]>='a' && s[i]<='z')
			s[i] = s[i] - 32;
		else	//reamining is as it is.
			s[i] = s[i];
	}
	printf(" \nAfter replace lowercase characters with uppercase and uppercase characters with lowercase");
	printf(" String : %s",s);
}


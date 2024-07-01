//C program to find the number of times a given word 'is' appears in the given string.

#include<stdio.h>
main()
{
	char s[30];
	int i,count=0;
	
	printf(" Enter a String : ");
	gets(s); 		//user input
	
	for(i=0;s[i]!='\0';i++)
	{
			//calculate how many time "is" word appear in String.
		if(s[i]==' ' && s[i+1]=='i' && s[i+2] == 's' && (s[i+3]==' ' || s[i+3] == '\0' || s[i+3]=='.'))
			count++;
	}
	
	printf("\n %d times word 'is' appears in this string.",count);
}


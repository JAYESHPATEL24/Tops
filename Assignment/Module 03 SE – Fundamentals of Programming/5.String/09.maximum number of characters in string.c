//C program to find the maximum number of characters in a string. 

#include<stdio.h>
main()
{
	char s[10];
	int i,l=0;
	
	printf("Enter a String : ");
	gets(s);  // user input
	
	for(i=0;s[i]!='\0';i++)
	{
		if(s[i]==' ')	//skip space
			continue;
		else		//count characters
			l++;
	}
	printf("Number of Characters in String = %d",l);
}


//C program to count the total number of words in a string. 

#include<stdio.h>
main()
{
	char s[50];
	int i,count=1;
	
	printf("Enter a String : ");
	gets(s);			//user input
	
	for(i=0;s[i]!='\0';i++)	//count words in string
	{
		if(s[i]==' ' && s[i+1]!=' ')
		{
			count++;
		}
	}
	
	printf("%d",count);
}


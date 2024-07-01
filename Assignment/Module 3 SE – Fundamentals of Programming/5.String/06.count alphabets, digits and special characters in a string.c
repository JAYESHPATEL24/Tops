//C program to count the total number of alphabets, digits and special characters in a string.*/

#include<stdio.h>
main()
{
	char s[30];
	int i,al=0,d=0,sc=0;
	
	printf(" Enter a String : ");
	gets(s);	//user input
	
	for(i=0;s[i]!='\0';i++)
	{			
				//calculating alphabets
		if(s[i]>='A' && s[i]<='Z' || s[i]>='a' && s[i]<='z')
			al++;
				//calculate digits
		else if(s[i]>='0' && s[i]<='9')
			d++;
				//avoid spaces 
		else if(s[i] == ' ')
			continue;
		else	//Count special characters
			sc++;
	}
	printf(" \nNumber of Alphabets in String : %d",al);
	printf(" \nNumber of Digits in String : %d",d);
	printf(" \nNumber of Special Characters in String : %d",sc);
}


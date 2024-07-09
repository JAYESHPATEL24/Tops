//C to count the total number of vowels or consonants in a string. */

#include<stdio.h>
main()
{
	char s[30];
	int v=0,c=0,i;
	
	printf(" Enter a String : ");
	gets(s);		// user input
	
	for(i=0;s[i]!='\0';i++)
	{
		if(s[i]==' ')	//ignore the space
			continue;
			//count vowels
		else if(s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'||s[i]=='a'||s[i]=='e'||s[i]=='o'||s[i]=='i'||s[i]=='u')
			v++;
			//count Consonants
		else	
			c++;
	}
	
	printf("\n Numbers Vowels in string : %d",v);
	printf("\n Numbers Consonants in string : %d",c);
}


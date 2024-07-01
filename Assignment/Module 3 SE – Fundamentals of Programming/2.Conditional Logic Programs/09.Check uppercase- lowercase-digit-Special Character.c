//C Program to Check Uppercase or Lowercase or Digit or Special Character

#include<stdio.h>
main()
{
	char c;
	
	printf(" Enter any Character : ");
	scanf("%c",&c);
	
	if(c>='A' && c<='Z')  // condition for uppercase
		printf(" %c is Uppercase Alphabet.",c);
	
	else if(c>='a' && c<='z') // condition for lowercase
		printf(" %c is Lowercase Alphabet.",c);
		
	else if(c>='0' && c<='9') // condition for digit
		printf(" %c is Digit.",c);
	
	else 			 // remaining are special characters
		printf(" %c is Special Character.",c);									
}

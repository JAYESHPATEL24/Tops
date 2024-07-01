//C program for Find the Character Is Vowel or Not

#include<stdio.h>
main()
{
	char c;   //c:alphabet or character
	
	printf("Enter any character : ");
	scanf("%c",&c);
	
	if(c=='a'||c=='e'||c=='o'||c=='i'||c=='u') //vowel in lowercase
		printf("Character is Vowel.");
	else if(c=='A'||c=='E'||c=='O'||c=='I'||c=='U') //vowel in Uppercase
		printf("Character is Vowel.");
	else
		printf("Character is not Vowel.");
}

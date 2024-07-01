//C program to Convert country's name in abbreviate form

#include<stdio.h>

main()
{
	char c[30];
	
	printf("Enter your Country name : ");
	gets(c);		//user input 	
	
	//print abbreviated form of country name
	printf("%c%c%c",c[0],c[1],c[2]);
}


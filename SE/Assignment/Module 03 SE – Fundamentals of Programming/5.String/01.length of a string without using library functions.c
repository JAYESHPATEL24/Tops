/*C program to find the length of a string
 without using library functions.*/

#include<stdio.h>

main()
{	
	int i;
	char a[30];
	
	printf("Enter a String : ");
	gets(a);	// user input 
	
	for(i=0;a[i]!='\0';i++); //loop for Find Length
	
	printf("Length of String : %d",i);
}

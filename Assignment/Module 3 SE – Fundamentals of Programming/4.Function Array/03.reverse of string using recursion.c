//C program to find reverse of string using recursion 

#include <stdio.h>

// Function to print reverse of the passed string
void reverse(char *str) //function definitiom
{
    if (*str) 
		{
    	    reverse(str + 1);	//recursion
        	printf("%c", *str);
    	}
}

main() 
{
    char a[10]; 
    
    printf("Enter a String : ");
    gets(a);		//accept String from user
    
    printf("Reverse String : ");
    reverse(a);	   //call reverse Function.
    
}


//c program for Find character value from ascii

#include<stdio.h>
main()
{
	int a; 
	
	printf("Enter ascii value :  ");
	scanf("%d",&a);
	
		//because we have character from ascii value 0 to 255.
	if(a>=0 && a<256 ) 
		printf("The Character value of ascii %d is '%c'.",a,a);
			// print character value of ascii value.
	else
		printf("Incorrect ASCII value.");
}

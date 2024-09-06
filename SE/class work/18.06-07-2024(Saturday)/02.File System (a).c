#include<stdio.h>
main()
{
	FILE* fptr;
	fptr=(fopen("text.txt","a")); //a : append add text into file 
									//if file doesn't exists then create new file
	fprintf(fptr,"Set your heart ablaze.......");
	fclose(fptr);
}

#include<stdio.h>
main()
{
	FILE* fptr;
	fptr=(fopen("text.txt","r")); //r : read a saved file..
	char a[100];
	fgets(a,100,fptr);
	printf("%s",a);
	fclose(fptr);
}

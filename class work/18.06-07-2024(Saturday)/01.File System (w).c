#include<stdio.h>
main()
{
	FILE* fptr;
	fptr=(fopen("text.txt","w")); //w : write  create a new file
	fprintf(fptr,"Wake up to reality.....");
	fclose(fptr);
}

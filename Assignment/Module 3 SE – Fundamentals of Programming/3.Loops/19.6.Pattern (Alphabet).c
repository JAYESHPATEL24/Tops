//C program for followin pattern :
/* A
   AB
   ABC
   ABCD
   ABCDE   */

#include<stdio.h>
main()
{
	int i,j;
	
	for(i=1;i<=5;i++)		//rows
	{
		for(j=1;j<=i;j++)  //columns
		{	
			printf("%c",j+64);
		}
		printf("\n");
	}
}


//C program for followin pattern :
/*A
  BC
  DEF
  GHIJ
  KLMNO */
  
#include<stdio.h>
main()
{
	int i,j,n=65;
	
	for(i=1;i<=5;i++)		//rows
	{
		for(j=1;j<=i;j++)  //columns
		{	
			printf("%c",n);
			n++;
		}
		printf("\n");
	}
}


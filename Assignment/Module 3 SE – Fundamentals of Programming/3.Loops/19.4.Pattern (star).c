//C program for followin pattern :
/* *
   **
   ***
   ****
   *****
   ******
   *****
   ****
   ***
   **
   *			*/

#include<stdio.h>
main()
{
	int i,j,k;
	
	for(i=1;i<=11;i++)		//rows
	{
		if(i<=6)
		{
			for(j=1;j<=i;j++)  //columns for row 1 to row 6
			{	
				printf("*");
			}
		}
		
		else
		{	
			for(k=11;k>=i;k--) //columns for row 7 to row 11
			{
				printf("*");
			}
		}
		printf("\n");
	}
}


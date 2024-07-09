//C program for followin pattern :
/*    *
     * *
    * * *
   * * * *
  * * * * *   */

#include<stdio.h>
main()
{
	int i,j,k;
	
	for(i=1;i<=5;i++)		//rows
	{
		for(k=5;k>i;k--)	//space
		{
			printf(" ");
		}
		for(j=1;j<=i;j++)  //columns
		{	
			printf(" *");
		}
		printf("\n");
	}
}


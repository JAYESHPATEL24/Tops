//C program for followin pattern :
/*1
  10
  101
  1010
  10101 */	

#include<stdio.h>
main()
{
	int i,j;
	
	for(i=1;i<=5;i++)		//rows
	{
		for(j=1;j<=i;j++)  //columns
		{	
			if(j%2==1)
				printf("1");
			else
				printf("0");
		}
		printf("\n");
	}
}


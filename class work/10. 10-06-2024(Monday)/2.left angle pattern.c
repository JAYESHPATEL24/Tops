
#include<stdio.h>

main()
{
	int i,j,k; //data members
	
	
	for(i=1;i<=5;i++) //raw
	{
		for(k=1;k<=5-i;k++) // space
		{
			printf(" ");
		}
		for(j=1;j<=i;j++) //colum
		{
			printf("*");
		}	
		printf("\n");
	}	
}


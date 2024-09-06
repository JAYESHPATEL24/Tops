#include<stdio.h>

main()
{
	int i,j,n=65; //data members
	
	
	for(i=1;i<=5;i++) //raw
	{
		for(j=1;j<=i;j++) //colum
		{
			printf("%c",n);
		}	
		printf("\n");
	}
	
}


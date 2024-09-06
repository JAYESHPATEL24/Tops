#include<stdio.h>

main()
{
	int i,j,k,n=3;
	
	i=1;
	while(i<=5)
	{
		k=1;
		while(k<=5-i)
		{
			printf(" ");
			k++;
		}
		j=1;
		while(j<=i)
		{
			printf(" %c",n);
			j++;
		}		
		printf("\n");
		i++;
	}
}


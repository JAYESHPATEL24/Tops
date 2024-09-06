// c program for print a table.

#include<stdio.h>
main()
{
	int n,i;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=1;i<=10;i++)
		printf("\n\t%d * %d = %d\n",n,i,n*i);
		
}

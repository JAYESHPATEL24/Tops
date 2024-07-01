//C program to print table up to given numbers. 

#include<stdio.h>
main()
{
	int i,n,m; // m,n:number
	
	printf("Enter a Number : ");
	scanf("%d",&n);					//table of n number
	printf("You wants to print table upto No : ");
	scanf("%d",&m);					//table upto this(m) number
	
	printf("\nTable for No. %d from 1 to %d : \n",n,m);
	
	for(i=1;i<=m;i++) // multiplication table creation
	{
		printf("\n %d * %d = %d\n",n,i,n*i);
	}
}




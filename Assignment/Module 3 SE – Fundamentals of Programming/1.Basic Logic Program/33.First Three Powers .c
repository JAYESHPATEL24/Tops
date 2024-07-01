// C Program for Print First Three Powers (N^1, N^2, N^3) 

#include<stdio.h>
main()
{
	int n; //n:number
	
	printf(" Enetr a number : ");
	scanf("%d",&n);
	
	printf("\n %d^1 = %d \n",n,n); //n^1
	
	printf("\n %d^2 = %d \n",n,n*n); //n^2
	
	printf("\n %d^3 = %d \n",n,n*n*n);	//n^3
}


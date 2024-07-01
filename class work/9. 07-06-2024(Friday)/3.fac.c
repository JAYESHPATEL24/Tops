//c program for factorial

#include<stdio.h>
main()
{
	int i,n,sum=1;
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=n;i>1;i--)
		sum += i;
		
	printf("Factorial is : %d",sum);
}

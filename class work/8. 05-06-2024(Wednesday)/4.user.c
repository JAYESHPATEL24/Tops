#include<stdio.h>

main()
{
	int i=1,a; //intialize
	printf("Enter a Number : ");
	scanf("%d",&a);
	
	while(i<=a)		//condition
	{
		printf("%d\n",i);
		i++;		//increment
	}
}


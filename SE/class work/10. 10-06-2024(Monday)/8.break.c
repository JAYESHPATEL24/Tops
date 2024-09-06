//The purpose of break is for unconditional exit from the loop.. 

#include<stdio.h>

main()
{
	int n,i;
	
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		printf("%d\n",i);
		if(i==10)
			break;
	}
}


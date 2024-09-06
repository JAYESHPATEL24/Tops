/*continue statement is used to skip the remaining code 
after the continue statement within a loop and 
jump to the next iteration of the loop.*/ 

#include<stdio.h>

main()
{
	int i,n;
	
	printf("Enter a number : ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		if(i==5)
			continue;
		printf("%d\n",i);
	}
}


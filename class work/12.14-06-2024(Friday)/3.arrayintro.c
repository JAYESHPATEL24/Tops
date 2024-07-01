#include<stdio.h>

main()
{
	double a[5] = {00,20,30,40,50};
	
	int i;
	for(i=0;i<5;i++)
		printf("%02.0lf ",a[i]);
}


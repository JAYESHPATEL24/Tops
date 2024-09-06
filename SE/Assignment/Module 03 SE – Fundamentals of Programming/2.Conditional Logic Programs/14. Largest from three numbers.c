//C program for find the largest of three numbers. 

#include<stdio.h>
main()
{
	int a,b,c,max; //a,b,c:numbers max:largest number
	
	printf("Enter a number A : ");
	scanf("%d",&a);
	printf("Enter a number B : ");
	scanf("%d",&b);
	printf("Enter a number C : ");
	scanf("%d",&c); 
	
	max=a; 
			 //store largest number in max
	if(b>max)	
		max=b;
	if(c>max)
		max=c;
	
	printf("%d is largest Number.",max);
}


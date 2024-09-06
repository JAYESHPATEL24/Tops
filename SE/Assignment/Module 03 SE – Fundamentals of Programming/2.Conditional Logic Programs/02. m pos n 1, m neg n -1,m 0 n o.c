/*	C program for read the value of an integer m 
	and display the value of n is 1 when m is larger than 0,
	0 when m is 0 and -1 when m is less than 0 */
	
#include<stdio.h>
main()
{
	int m,n;   
	
	printf("Enter a integer number : ");
	scanf("%d",&m);	//user input
	
	if(m==0)
		n=0;		//m=0 n=0
	else if(m>0)
		n=1;		//m>o n=1
	else
		n=-1;		//m<0 n=-1
		
	printf("\nThe value of n is %d",n);
}

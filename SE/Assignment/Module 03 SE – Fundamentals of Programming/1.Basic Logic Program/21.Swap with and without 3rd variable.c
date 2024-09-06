/*Accept 2 numbers from user and swap 2 numbers with using 3rd variable
 and without using 3rd variable */
 
#include<stdio.h>
main()
{
 	int a,b,c,x,y;
 	
 	printf("Enter a Number A : ");
 	scanf("%d",&a);
 	printf("Enter a Number B : ");
 	scanf("%d",&b);
 	
 	c=a;
 	a=b;	//swapping with 3rd variable.
 	b=c;
 	
 	printf("\nAfter Swapping using 3rd variable : ");
 	printf("\nA : %d  B : %d ",a,b);
 	
 	printf("\n\n\nEnter a Number X : ");
 	scanf("%d",&x);
 	printf("Enter a Number Y : ");
 	scanf("%d",&y);
 
 	y=x+y-(x=y);	
 		// swapping without 3rd variable.
 		
 	printf("\nAfter Swapping without using 3rd variable : ");
 	printf("\nX : %d  Y : %d ",x,y);
}

//C Program of Armstrong Number Using For Loop. 

#include<stdio.h>
main()
{	
	int n,d=0,r,p,sum=0; //n:number d:no of digits p:power r:remiander sum:summation 
	int i,j;
		
	printf(" Enter a number : ");
	scanf("%d",&n);
	
	for(i=n;i>0;i/=10) //count digits of a number.
		d++;
		
	for(i=n;i>0;i/=10)
	{
		r = i%10;
		
		p=1;		
		for(j=1;j<=d;j++)	// power of digit
			p*=r;			
	
		sum += p;	//summation of powers.
	}
	
	if(sum==n)	//check  sum and use number is equal or not.
		printf("\n %d is an Armstrong Number.\n",n);
	else
		printf("\n %d is not an Armstrong Number.\n",n);
}


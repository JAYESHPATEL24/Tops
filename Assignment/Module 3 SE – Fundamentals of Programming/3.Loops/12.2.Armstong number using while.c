//C Program of Armstrong Number Using While Loop. 

#include<stdio.h>
main()
{	
	int n,d=0,r,p,sum=0; //n:number d:no of digits p:power r:remiander sum:summation 
	int i,j;
		
	printf(" Enter a number : ");
	scanf("%d",&n);
	
	i=n;
	while(i>0) //count digits of a number.
	{
		d++;
		i/=10;
	}
		
	i=n;
	while(i>0)
	{
		r = i%10;
		
		p=1;
		j=1;		
		while(j<=d)	// power of digit
		{
			p*=r;
			j++;
		}			
	
		sum += p;	//summation of powers.
		
		i/=10;
	}
	
	if(sum==n)	//check  sum and use number is equal or not.
		printf("\n %d is an Armstrong Number.\n",n);
	else
		printf("\n %d is not an Armstrong Number.\n",n);
}


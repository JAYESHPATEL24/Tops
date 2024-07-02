// menu driven factorial,prime,right angle pattern .

#include<stdio.h>

fact(int x)	//funtion for find factorial number
{
	int i,fact=1;
	for(i=x;i>0;i--)
	{
		fact *= i;
	}
	printf("\nFactorial of number %d = %d \n",x,fact);
	printf("\n------------------------------------\n");
}

prime(int y)	//function for check prime number
{
	int i,j=0;
	for(i=1;i<=y;i++)
	{
		if(y%i==0)
			j++;
	}
	if(j==2)
		printf("\n%d is prime number.\n",y);
	else
		printf("\n%d is not a prime number.\n",y);
	printf("\n------------------------------------\n");
}

right_angle(int z)	//function for print right angle pattern.
{
	int i,j;
	for(i=1;i<=z;i++)
	{
		for(j=1;j<=i;j++)
			printf("*");
		printf("\n");
	}
	
	printf("\n------------------------------------\n");
	
}

#include<stdio.h>
main()
{
	int ch,n;
	
	while(ch != 4)
	{				//print choices
		printf("\n********** Select any one *********\n");
		printf("1.Find factorial of number.\n");
		printf("2.Find number is Prime number or not.\n");
		printf("3.Print right angle pattern.\n");
		printf("4.Exit");
		
		printf("\n------------------------------------\n");
		
		printf("\nEnter your choice : ");
		scanf("%d",&ch);	//user choice from given options
		
		switch(ch)
		{
			case 1:
				printf("Enter a number : ");
				scanf("%d",&n);
				fact(n);		//call fact function
				break;
				
			case 2:
				printf("Enter a number : ");
				scanf("%d",&n);
				prime(n);	  //call prime function
				break;	
					
			case 3:
				printf("Enter a number : ");
				scanf("%d",&n);
				right_angle(n);
				break;		//call right_angle function
			
			case 4: 
				break;
				
			default:
				printf("\nXXXX INVALID CHOICE..");
				printf("\nPlease Enter correct choice....\n\n");
		}
	}
}


/*C program to accept 5 numbers from user and check 
entered number is even or odd using of array */

#include<stdio.h>
main()
{
	int n[5],i;
	
	printf("Enter 5 numbers : \n");
	
	for(i=0;i<5;i++)	//Accept 5 numbers from users.
	{
		printf(" %d. ",i+1);
		scanf("%d",&n[i]);
	}
	
	printf("\n\n\n");
	for(i=0;i<5;i++)
	{
		if(n[i]==0)		//number is zero.
			printf(" %d. %d is zero.\n",i+1,n[i]);
		else if(n[i]%2==0)	//Number is even.
			printf(" %d. %d is Even Number.\n",i+1,n[i]);
		else				//Number is odd.
			printf(" %d. %d is Odd Number.\n",i+1,n[i]);
	}
}


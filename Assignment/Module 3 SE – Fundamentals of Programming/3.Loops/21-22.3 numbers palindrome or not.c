/*C program for Accept 3 numbers from user using while loop and 
check each numbers palindrome */

#include<stdio.h>
main()
{
	int i=0,a[3],rvs,n;
	
	printf("Enter any 3 Numbers : \n");
	
	while(i<3)	//take 3 numbers from user
	{
		printf("No %d = ",i+1);
		scanf("%d",&a[i]);
		i++;
	}
	
	i=0;
	while(i<3)	//find number is palindrome or not
	{
		rvs=0;
		n = a[i];
		while(n>0)		//find reverse number.
		{
			rvs = rvs*10 + n%10;
			n /=10;
		}
		if(rvs==a[i])  //check reverse number and original number are equal or not.
			printf("\n%d is palindrome Number.",a[i]);
		else
			printf("\n%d is Not palindrome Number.",a[i]);
		i++;
	}
}


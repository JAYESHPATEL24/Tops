#include<stdio.h>

panipuri()
{	int a = 20;
	printf("\nYOU SELECTED PANIPURI........\n\n");
	return a;
}

dabeli()
{
	int a = 25;
	printf("\nYOU SELECTED DABELI........\n\n");
	return a;
}

vadapav()
{
	int a = 30;
	printf("\nYOU SELECTED VADAPAV........\n\n");
	return a;
}

main()
{
	int ch,amt,t_amt=0; 
	
	while(ch!=4 && ch!=5)
	{
		printf("\n********* welcome **********\n");
		printf("\n1. PANIPURI     RS=20\n");
		printf("\n2. DABELI       RS=25\n");
		printf("\n3. VADAPAV      RS=30\n");
		printf("\n4. BILL\n");
		printf("\n5. EXIT\n");
			
		printf("\nEnter your chooice : ");
		scanf("%d",&ch);
	
		if(ch==1)
		{
			amt = panipuri();
		}
		
		else if(ch==2)
		{
			amt = dabeli();
		}
		
		else if(ch==3)
		{
			amt = vadapav();
		}
		
		else if(ch==4)
		{
			printf("\n****************************\n");
			printf("Your Bill amount : %d ",t_amt);
			printf("\n****************************\n");
			printf("\nThank you for visiting\n");
			printf("\n****************************\n");
		}
		
		else if(ch==5)
		{
			printf("\n****************************\n");
			printf("\nThank you for visiting\n");
			printf("\n****************************\n");
		}
		
		else 
		{
			printf("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n");
			printf("\nInvalid choice.");
			printf("\nPlease Enter the right Choice ......\n\n");
		}
		t_amt += amt;
	}
}

#include<stdio.h>

main()
{
	int ch,n=16;
	
	printf("\n****** welcome to the game.******\n");
	
	while(1)
	{
		printf("\n******Guess the number between 1 to 50******\n");	
	
		printf("\nEnter your choice : ");
		scanf("%d",&ch);
		
		if(ch<n)
			printf("\n%d is less than original number.\n",ch);
		else if(ch>n && ch<=50)
			printf("\n%d is greater than original number.\n",ch);
		else if(ch==n)
		{
			printf("\nyou win!!\n");
			break;
		}	
		else
		{
			printf("\nInvalid choice.\n");
			break;
		}
	}	
}


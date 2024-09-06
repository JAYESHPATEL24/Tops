/*C program for Addition, Subtraction, Multiplication and Division 
using Switch case.(Must Be Menu Driven)*/ 

#include<stdio.h>
main()
{
	int a,b,ch; //a,b:numbers ch:choice
	
	while(ch!=5)
	{
		//print menu
		printf("\n******** Menu ******** \n");
		printf(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.division\n 5.EXIT\n");
		printf("---------------------- \n");
		
		printf("Enter your choice : ");
		scanf("%d",&ch); //user input choice
		
		if(ch>0 && ch<5)
		{					
						//take two numbers from user
			printf("Enter two numbers : \n No. 1 : ");
			scanf("%d",&a);
			printf(" No. 2 : ");
			scanf("%d",&b);
		}
		
		switch(ch)				
		{
			case 1:
				printf("Addition : \n %d + %d = %d \n",a,b,a+b);
				printf("---------------------- \n\n");
				break;
				
			case 2:
				printf("Subtraction : \n %d - %d = %d \n",a,b,a-b);
				printf("---------------------- \n\n");
				break;
				
			case 3:
				printf("Multiplication : \n %d x %d = %d \n",a,b,a*b);
				printf("---------------------- \n\n");
				break;
				
			case 4:
				printf("Division : \n %d / %d = %.2f \n",a,b,(float)a/b);
				printf("---------------------- \n\n");
				break;
				
			case 5:
				printf("\n\nThanks for visiting. \n");
				break;
				
			default:
				printf("\n\nxxxxx INCORRECT CHOICE. \n\n");
				printf("---------------------- \n\n");
		}
		
	}
}


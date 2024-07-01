//Food bill according to customer.
#include<stdio.h>

main()
{
	int choice,qnt,amt,t_amt=0,ch; 
	
	while(ch!=2)
	{
			//print the menu..
		printf("\n*************** Menu ***********************\n\n");
		printf("\n Items \t\t|  Price per Plate\n");
		printf("\n----------------|----------------------------\n");
		printf("\n 1.Panipuri \t|  Rs.40\n");
		printf("\n 2.Dabeli   \t|  Rs.20\n");
		printf("\n 3.Vadapav  \t|  Rs.30\n");
		printf("\n 4.Pizza    \t|  Rs.120\n");
		printf("\n 5.Bhajipav \t|  Rs.70\n");
		printf("\n 6.Idli     \t|  Rs.50\n");
		printf("\n 7.Dosa     \t|  Rs.100\n");
		printf("\n---------------------------------------------\n");
		
		Sleep(1000);
				//Customer selection from the menu
		printf("Enter your Choice : ");
		scanf("%d",&choice);
		printf("---------------------------------------------\n\n");
		
				//acording to customer choice show right order
				//also aking for how many plates customer wanna order.
				//calculate amount of selected order. 
		switch(choice)	
		{
			case 1:
				printf(" YOU HAVE SELECTED Panipuri....\n");
				printf(" Enter Quantity : ");
				scanf("%d",&qnt);
				amt = qnt*40;
				printf(" Amount : Rs.%d\n",amt);
				break;
							
			case 2:
				printf(" YOU HAVE SELECTED Dabeli....\n");
				printf(" Enter Quantity : ");
				scanf("%d",&qnt);
				amt = qnt*20;
				printf(" Amount : Rs.%d\n",amt);
				break;
				
			case 3:
				printf(" YOU HAVE SELECTED Vadapav....\n");
				printf(" Enter Quantity : ");
				scanf("%d",&qnt);
				amt = qnt*30;
				printf(" Amount : Rs.%d\n",amt);
				break;
				
			case 4:
				printf(" YOU HAVE SELECTED Pizza....\n");
				printf(" Enter Quantity : ");
				scanf("%d",&qnt);
				amt = qnt*120;
				printf(" Amount : Rs.%d\n",amt);
				break;
			
			case 5:
				printf(" YOU HAVE SELECTED Bhajipav....\n");
				printf(" Enter Quantity : ");
				scanf("%d",&qnt);
				amt = qnt*70;
				printf(" Amount : Rs.%d\n",amt);
				break;
				
			case 6:
				printf(" YOU HAVE SELECTED Idali....\n");
				printf(" Enter Quantity : ");
				scanf("%d",&qnt);
				amt = qnt*50;
				printf(" Amount : Rs.%d\n",amt);
				break;
				
			case 7:
				printf(" YOU HAVE SELECTED Dosa....\n");
				printf(" Enter Quantity : ");
				scanf("%d",&qnt);
				amt = qnt*100;
				printf(" Amount : Rs.%d\n",amt);
				break;
				
			default:
				printf(" XXX INCORRECT CHOICE.\n");
				printf(" Please Enter a CORRECT choice from the Menu..\n");
		}
		
		printf("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n");
		
		t_amt = t_amt + amt ; //calculate total amount of all orders.
		
		printf(" Total Bill Amount : Rs.%d",t_amt);
		
		printf("\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n\n");
		
		//Customer selection for he/she wanna place more orders or not.
		printf(" Do you Want place more orders ? \n");
		printf(" Enter 1 for YES \n Enter 2 for NO\n");
		printf(" Enter your choice : ");
		scanf("%d",&ch);
		
		if(ch==2)//customer doesn't want to order anything than print thanks and exit
		{
			printf("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n");
			printf(" Total Bill Amount : Rs.%d",t_amt);
			printf("\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n\n");
			printf("\n THANK U SO MUCH FOR VISITING ....%c%c\n",1,1);
			printf(" VISIT AGAIN ............!!!!\n");
			printf("\n*********************************************\n\n");
		}	
		
		 //in case customer select another choice instead of yes or no than again ask for choice.
		while(ch!=1 && ch!=2)
		{
			printf(" Enter correct choice (1 0r 2) : ");
			scanf("%d",&ch);
		}  
	}
}


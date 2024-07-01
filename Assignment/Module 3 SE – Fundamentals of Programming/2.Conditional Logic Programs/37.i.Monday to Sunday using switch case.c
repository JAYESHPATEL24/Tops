//C program for show i.Monday to Sunday using switch case 

#include<stdio.h>
main()
{
	int n; //n:day number
	
	printf(" Enter a week day no (1-7) : ");
	scanf("%d",&n);
	
	switch(n)
	{
		case 1: 
			printf(" MONDAY.");
			break;
		case 2: 
			printf(" TUESDAY.");
			break;
		case 3: 
			printf(" WEDNESDAY.");
			break;
		case 4: 
			printf(" THURSDAY.");
			break;
		case 5: 
			printf(" FRIDAY.");
			break;
		case 6: 
			printf(" SATURDAY.");
			break;
		case 7: 
			printf(" SUNDAY.");
			break;
		default:
			printf("INCORRECT NUMBER.");
	}
}


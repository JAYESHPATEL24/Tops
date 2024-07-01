#include<stdio.h>

main()
{
	char n;
	printf("Enter Character : ");
	scanf("%c",&n);
	
	switch(n)
	{
		case 'A':
			printf("\n\nVOWEL!!");
			break;
			
		case 'E':
			printf("\n\nVOWEL!!"); 
			break;   
			
		case 'I':
			printf("\n\nVOWEL!!");
			break;
			
		case 'O':
			printf("\n\nVOWEL!!");
			break;
		
		case 'U':
			printf("\n\nVOWEL!!");
			break;
			
		default:
			printf("\n\nConstant!!");
	}
}


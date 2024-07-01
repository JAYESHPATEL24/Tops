/*C program to input basic salary of an employee and 
calculate its Gross salary according to following: 
Basic Salary <= 10000 : HRA = 20%, DA = 80% 
Basic Salary <= 20000 : HRA = 25%, DA = 90% 
Basic Salary > 20000 : HRA = 30%, DA = 95% */

#include<stdio.h>
main()
{
	float bs,gs; //bs:Basic Salary gs:Gross Salary 
	
	printf("Enter your Basic Salary : Rs.");
	scanf("%f",&bs);
	
	if(bs<=10000)	//calculate gross salary according basic salary.
		gs = bs + (bs*20)/100 + (bs*80)/100;
		
	else if(bs<=20000)
		gs = bs + (bs*25)/100 + (bs*90)/100;
	
	else // basic salary more than 20000
		gs = bs + (bs*30)/100 + (bs*95)/100;
		
	printf("Gross Salary is : Rs.%.2f ",gs);
}


/*C program to input electricity unit charges and calculate
 total electricity bill according to the given condition: 
 For first 50 units Rs. 0.50/unit
 For next 100 units Rs. 0.75/unit 
 For next 100 units Rs. 1.20/unit 
 For unit above 250 Rs. 1.50/unit 
 An additional surcharge of 20% is added to the bill */

#include<stdio.h>
main()
{
	float u,amt,t; //u:unit amt:amount t:total amount
	
	printf(" Enter cosumed electricity units : ");
	scanf("%f",&u);
	
	// calculate bill according to conditions.
	if(u<=50)
	{
		amt = u*0.50;
	}
	
	else if(u<=150)
	{
		u=u-50;			// Already calculate 50 units = 25 rupees
		amt = 25 + u*0.75;
	}
	
	else if(u<=250)
	{
		u=u-150;		// Already calculate 150 units = 100 rupees
		amt = 100 + u*1.20;
	}
	
	else
	{
		u=u-250;		// Already calculate 250 units = 220 rupees
		amt = 220 + u*1.50;
	}
	
	t = amt + (amt*20)/100; // 20% additional surcharge
	
	printf("\n Amount of Electricity bill = Rs.%.2f",t);
}


/*C program to calculate and print the electricity bill of a given 
 customer. The customer ID, name, and unit consumed by the user should
 be captured from the keyboard to display the total amount to be paid 
 to the customer. The charge are as follow : 
		Unit						 Charge/unit
 	upto 350  							@1.20 
	350 and above but less than 600 	@1.50
  	600 and above but less than 800  	@1.80 
	800 and above  						@2.00 

If bill exceeds Rs. 800 then a surcharge of 18% will be charged and the minimum bill should be of Rs. 256/-
*/

#include<stdio.h>
main()
{
	char n[20];			//n:name
	int id;				//id:customer id
	float u,t;			//u:units t:total amount
	
	printf(" Enter a Customer Name : ");
	gets(n);
	
	printf(" Enter a Customer ID   : ");
	scanf("%d",&id);		
	
	printf(" Enter consummed units : ");
	scanf("%f",&u);
	
			//calculate total amount according to units.
	if(u<350)
		t=u*1.2;
	else if(u<600)
		t=u*1.5;
	else if(u<800)
		t=u*3.8;
	else 
		t=u*2;	
		
	
	if(t>800)		// amount is more than 800 than 15% super charge.
		t=t+((t*15)/100);
	if(t<256)		// minimum bill amount is 256.
		t=256;	
		
						//print Electicity Bill
	printf("\n\n\n******Electricity Bill******\n"); 
	printf("\n\n  Customer ID           : %d ",id);
	printf("\n\n  Customer Name         : %s ",n);
	printf("\n\n  Consummed unit        : %.0f",u);
	printf("\n\n  Net Amount to be paid : Rs.%.2f\n",t);
}


//C program to calculate profit and loss on a transaction. 

#include<stdio.h>

main()
{
	int cp,sp; //cp:cost price sp:selling price
	
	printf(" Enter a Cost Price : Rs.");
	scanf("%d",&cp);
	printf(" Enter a Selling Price : Rs.");
	scanf("%d",&sp);
	
	if(sp>cp) //selling price is more than cost prise so its profit
		printf("\n Profit : Rs.%d ",sp-cp);//profit= selling price - cost price

	else if(cp>sp) //cost pricr is more than Selling price so its loss
		printf("\n Loss : Rs.%d ",cp-sp);//loss= cost price - selling price

	else // in case of both prices are equal.
		printf("\n NO PROFIT AND NO LOSS.");
}



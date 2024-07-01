/* C program for accept the height of a person in centimeters and 
categorize the person according to their height */

#include<stdio.h>
main()
{
	int h; //h:height
	
	printf("Enter person's Height in centimeters : ");
	scanf("%d",&h);
	
	if(h<150) // consider less than 150cm height as short
		printf("Short person.");	
	
	else if(h<170) //Average height is between 150 cm and 170 cm.
		printf("Average height person");
	
	else //consider above 170 cm height is tall
		printf("Tall person.");
		
}

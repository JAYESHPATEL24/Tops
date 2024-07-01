/*C program to read temperature in centigrade and
 display a suitable message according to the temperature state below:
 Temp < 0 then Freezing weather 
 Temp 0-10 then Very Cold weather
 Temp 10-20 then Cold weather
 Temp 20-30 then Normal in Temp
 Temp 30-40 then Its Hot 
 Temp >=40 then Its Very Hot  */

#include<stdio.h>
main()
{
	int t; //t:temperature
	
	printf("Enter temperature in centigrade : ");
	scanf("%d",&t);
	
	if(t<0)			// all weather conditions 
		printf("Freezing weather.");
	else if(t<10)
		printf("Very Cold weather");
	else if(t<20)
		printf("Cold weather");
	else if(t<30)
		printf("Normal in Temp");
	else if(t<40)
		printf("Its Hot");
	else if(t>=40)
		printf("Its Very Hot");
}


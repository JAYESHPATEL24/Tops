// c program for Convert temperature Fahrenheit to Celsius.

#include<stdio.h>
main()
{
	float f,c; // c:Celsius f:Fahrenheit
	
	printf("Enter a temperature in Fahrenheit : ");
	scanf("%f",&f);
	
	c = (5*(f-32))/9;//formula for convert temperature Fahrenheit to Celsius.
	
	printf("\nTemperature in Celsius : %.2f ",c);	
} 

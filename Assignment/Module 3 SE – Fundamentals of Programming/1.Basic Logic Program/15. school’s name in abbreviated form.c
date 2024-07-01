//C program to convert school's name in abbreviated form 

#include<stdio.h>

main()
{
	int k=0,flag=1,i,l=0,j=0;
	char n[50];
	
	printf("Enter your school name : ");
	gets(n);		//user input (Ex.Shree Gannath Vidhyalay)
	
	for(i=0;n[i]!='\0';i++) //calculate the length of String
		l++;
		
	char a[l];
	
	for(i=l-1;i>=0;i--)
	{
		if(n[i]==' ')	//take character after space 
		{				//Ex. G. from Gannath	
			flag=0;
			if(k>0)
			{
				a[j]='.';
				j++;
				a[j]=n[i+1];
				j++;
			}
			k=1;
		}
		
		if(flag==1)
		{
			a[j]=n[i];	// Store last name in reverse.
			j++;		// (Ex.Vidyalay as yalaydiV)
		}
		
		if(i==0)	//store 1st latter (Ex. s. from Shree)
		{
			a[j]='.';	
			j++;
			a[j]=n[0];
		}
	}
	
	for(j;j>=0;j--)		//print abbreviated form of school name 
		printf("%c",a[j]);
}


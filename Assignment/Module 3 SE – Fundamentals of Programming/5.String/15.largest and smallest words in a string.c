//C program to find the largest and smallest words in a string.

#include<stdio.h>
main()
{
	char s[10],sub[10][10];
	int i,j,k=0,temp,min=0,max=0,minin=0,maxin=0;
	
	printf("Enter a String : ");
	gets(s);			//user input
	
	for(i=0;s[i]!='\0';i++) //break string into words.
	{
		j=0;
		while(s[i]!=' ' && s[i]!='\0')
		{
			sub[k][j] = s[i];
			i++;
			j++;
		}
		sub[k][j]='\0';
		k++;
	}
	
	/*consider length of 1st Substring as minimum and maximum length
		as length of smallest and largest words.*/
	for(i=0;sub[0][i]!='\0';i++)
	{
		min++;
		max++;
	}
	
	for(i=0;i<k;i++) //here k is number of words in string
	{
		temp=0;
				//find length of every substrings one by one.
		for(j=0;sub[i][j]!='\0';j++)
			temp++;
		
		if(temp>max)	//find largest word.
		{
			max = temp;
			maxin = i;
		}
		
		if(temp<max)	//find smallest word.
		{
			min = temp;
			minin = i;
		}
	}
	
	printf("\nlargest word  : %s",sub[maxin]);
	printf("\nsmallest word : %s",sub[minin]);
}


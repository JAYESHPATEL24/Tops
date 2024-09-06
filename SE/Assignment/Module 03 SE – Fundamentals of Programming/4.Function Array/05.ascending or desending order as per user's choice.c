/*C program to take two Array input from user and sort them in 
ascending or descending order as per user's choice */

#include<stdio.h>
main()
{
	int a[10],b[10],i,j,n,m,ch1,ch2,temp;
	
	printf("how many numbers you want to add in 1st array (max limit 10) : ");
	scanf("%d",&n);
	
	printf("Enter 1st Array : \n");
	
	for(i=0;i<n;i++) //user input for 1st array
	{
		printf("No. %d. ",i+1);
		scanf("%d",&a[i]);
	}
	
	printf("\nhow many numbers you want to add in 2nd array (max limit 10) : ");
	scanf("%d",&m);
	
	printf("Enter 2nd Array : \n");
	
	for(i=0;i<m;i++) //user input for 2nd array
	{
		printf("No. %d. ",i+1);
		scanf("%d",&b[i]);
	}
	
	printf("\n-------------------------------\n");
	printf(" Select 1 for Ascending order \n Select 2 for Descending Order\n");
	printf("-------------------------------\n\n");
	
			//ascending and descending order choices for both arrays
	printf("Enter your choice for 1st array : ");
	scanf("%d",&ch1);
	printf("Enter your choice for 2nd array : ");
	scanf("%d",&ch2);
	printf("\n-------------------------------\n");
	
	if(ch1==1) //print ascending order for 1st array
	{
		printf(" ASCENDING ORDER OF 1ST ARRAY  : ");
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(a[i]>a[j])
				{
					temp=a[i];
					a[i]=a[j];
					a[j]=temp;
				}
			}
			printf(" %d ",a[i]);
		}
	}
	
	else if(ch1==2) //print descending order for 1st array
	{
		printf(" DESCENDING ORDER OF 1ST ARRAY : ");
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(a[i]<a[j])
				{
					temp=a[i];
					a[i]=a[j];
					a[j]=temp;
				}
			}
			printf(" %d ",a[i]);
		}
	}
		
	else
	{
		printf("\n XXXX INCORRECT CHOICE FOR 1ST ARRAY.");
	}
	
	if(ch2==1) //print ascending order for 2nd array
	{
		printf("\n ASCENDING ORDER OF 2ND ARRAY  : ");
		for(i=0;i<m;i++)
		{
			for(j=i+1;j<m;j++)
			{
				if(b[i]>b[j])
				{
					temp=b[i];
					b[i]=b[j];
					b[j]=temp;
				}
			}
			printf(" %d ",b[i]);
		}
	}
	
	else if(ch2==2) //print descending order for 2nd array
	{
		printf("\n DESCENDING ORDER OF 2ND ARRAY : ");
		for(i=0;i<m;i++)
		{
			for(j=i+1;j<m;j++)
			{
				if(b[i]<b[j])
				{
					temp=b[i];
					b[i]=b[j];
					b[j]=temp;
				}
			}
			printf(" %d ",b[i]);
		}
	}
	
	else
	{
		printf("\n XXXX INCORRECT CHOICE FOR 2ND ARRAY.");
	}
	printf("\n-------------------------------\n");
}


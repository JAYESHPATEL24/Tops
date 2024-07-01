//C program for Accept 5 employees name and salary and count average and total salary.

#include<stdio.h>
main()
{
	char n1[10],n2[10],n3[10],n4[10],n5[10]; // n1-n5:name
	int s1,s2,s3,s4,s5,t; //s1-s5:salary t:total
	
	printf("Enter 5 Employee's name and salary : " );
	
	printf("\n 1.Name : ");
	scanf("%s",&n1);
	printf("   Salary : Rs.");
	scanf("%d",&s1);
		
	printf("\n 2.Name : ");
	scanf("%s",&n2);
	printf("   Salary : Rs.");
	scanf("%d",&s2);

	printf("\n 3.Name : ");
	scanf("%s",&n3);
	printf("   Salary : Rs.");
	scanf("%d",&s3);
	
	printf("\n 4.Name : ");
	scanf("%s",&n4);
	printf("   Salary : Rs.");
	scanf("%d",&s4);	
	
	printf("\n 5.Name : ");
	scanf("%s",&n5);
	printf("   Salary : Rs.");
	scanf("%d",&s5);	
	
	t = s1+s2+s3+s4+s5; // calculate total salary.
	
	printf("\n\n Average salary of 5 employees : Rs.%.2f",(float)(t/5));
							// calculate and print average salary.
							
	printf("\n\n Total salary of 5 employees : Rs.%d",t);
}



/*C program to determine eligibility for admission to a professional 
course based on the following criteria 
Eligibility Criteria : 
Marks in Maths >=65 & Marks in Phy >=55 & Marks in Chem>=50 & 
Total in all three subject >=190 or Total in Maths and Physics >=140
 -------------------------------------- 
Input the marks obtained in Physics :65 
Input the marks obtained in Chemistry :51 
Input the marks obtained in Mathematics :72 
Total marks of Maths, Physics and Chemistry : 188 
Total marks of Maths and Physics : 137 
output : The candidate is not eligible.*/

#include<stdio.h>
main()
{
	int mt,ph,ch; //marks in maths:mt, physics:ph, chemistry:ch
	int t1,t2; // t1:total of all subject t2:total of maths & physics.
	
	printf("To Check eligibility for admission to a professional course Enter your data : ");

	printf("\n Marks in Physics  : ");
	scanf("%d",&ph);
	
	printf(" Marks in Chemistry: ");
	scanf("%d",&ch);

	printf(" Marks in Maths    : ");
	scanf("%d",&mt);
		
	t1 = mt + ph + ch ; //total of all subject
	t2 = mt + ph;	//total of maths & physics
	
	printf(" Total marks of Maths, Physics and Chemistry : %d",t1);
	printf("\n Total marks of Maths and Physics : %d\n",t2);

	if(mt>=65 && ph>=55 && ch>=50) // check all the conditions for eligiblity.
	{
		if(t1>=190 || t2>=140)
			printf(" The candidate is eligible.");
		else
			printf(" The candidate is not eligible.");
	}
	else
		printf(" The candidate is not eligible.");
}


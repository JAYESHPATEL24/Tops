//C program to show difference between Structure and Union.

#include <stdio.h> 
#include <string.h> 
  
			// declaring structure 
struct struct_example
{ 
    int integer; 
    float decimal; 
    char name[20]; 
}; 
  
			// declaring union 
union union_example 
{ 
    int integer; 
    float decimal; 
    char name[20]; 
}; 
  
void main() 
{ 
	//deference 1 : Structure->several members can initilize at once.
		//			union -> only 1st member can be intilized.	  
     // creating variable for structure and initializing values
    struct struct_example s = { 18, 38, "INDIA" }; 
  
    // creating variable for union and initializing values 
    union union_example u = { 18, 38, "INDIA" };  
  
	printf(" structure data:\n integer: %d\n decimal: %.2f\n name: %s\n",s.integer, s.decimal, s.name); 
    printf("\n union data:\n integer: %d\n decimal: %.2f\n name: %s\n",u.integer, u.decimal, u.name); 
  
    /* difference 2 :Structure->compiler allocates the memory for each member. 
				  				The size of structure is greater than or equal to the sum of 
								sizes of its members.
 					 Union->Memory allocated is shared by individual members of union.
 					 		compiler allocates the memory by considering the size of the largest memory. 
							So, size of union is equal to the size of largest member.
 */
    printf("\nsizeof structure : %d\n", sizeof(s)); 
    printf("sizeof union : %d\n", sizeof(u)); 
  
    // difference 3 :Structure->Individual member can be accessed at a time.
    //				 union->Only one member can be accessed at a time.
    printf("\n Accessing all members at a time:\n"); 
    s.integer = 183; 
    s.decimal = 90; 
    strcpy(s.name, "GUJARAT"); 
  
    printf("structure data:\n integer: %d\n decimal: %.2f\n name: %s\n",s.integer, s.decimal, s.name); 
  
    u.integer = 183; 
    u.decimal = 90; 
    strcpy(u.name, "GUJARAT"); 
  
    printf("\nunion data:\n integer: %d\n decimal: %.2f\n name: %s\n",u.integer, u.decimal, u.name); 
  
    printf("\n Accessing one member at time:"); 
  
    printf("\n structure data:"); 
    s.integer = 240; 
    printf("\ninteger: %d", s.integer); 
  
    s.decimal = 120; 
    printf("\ndecimal: %f", s.decimal); 
  
    strcpy(s.name, "AHMEDABAD"); 
    printf("\nname: %s\n", s.name); 
  
    printf("\n union data:"); 
    u.integer = 240; 
    printf("\ninteger: %d", u.integer); 
  
    u.decimal = 120; 
    printf("\ndecimal: %f", u.decimal); 
  
    strcpy(u.name, "AHMEDABAD"); 
    printf("\nname: %s\n", u.name); 
  
    // difference 4:Stucture->Altering the value of a member will not affect other members values.
    //				Union->Altering the value of any of the member will alter other member values.

    printf("\nAltering a member value:\n"); 
    s.integer = 1218; 
    printf("structure data:\n integer: %d\n decimal: %.2f\n name: %s\n",s.integer, s.decimal, s.name); 
  
    u.integer = 1218; 
    printf("union data:\n integer: %d\n decimal: %.2f\n name: %s\n",u.integer, u.decimal, u.name); 
}

 /*C program for structure for five employees, that provides 
 the following information -print and display 
 employee number (empno), employee name (empname), address, and age: */

#include <stdio.h>

// Define the structure for an employee
struct Employee 
{
    int empno;
    char empname[50];
    char address[100];
    int age;
};

main() 
{
    // Create an array of structures to store employee details
    struct Employee employees[5];
    int i;

    // Input details for each employee
    for (i = 0; i < 5; i++) 
	{
        printf("\nEnter details for Employee %d:\n", i + 1);
        printf("Employee Number (empno): ");
        scanf("%dn", &employees[i].empno);
        getchar();
        printf("Employee Name (empname): ");
        gets(employees[i].empname);
        printf("Address: ");
        gets(employees[i].address);
        printf("Age: ");
        scanf("%d", &employees[i].age);
    }

    // Display details for each employee
    printf("\nEmployee Details:\n");
    for (i = 0; i < 5; ++i) 
	{
        printf("Employee %d:--\n", i + 1);
        printf("EmpN   : %d\n", employees[i].empno);
        printf("EmpName: %s\n", employees[i].empname);
        printf("Address: %s\n", employees[i].address);
        printf("Age    : %d\n", employees[i].age);
        printf("\n");
    }
}

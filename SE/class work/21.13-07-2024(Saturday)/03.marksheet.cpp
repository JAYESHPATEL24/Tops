#include<iostream>
using namespace std;

class School
{
	public:
	intro()
	{
		cout<<"Welcome to our School."<<endl;
	}
	
};

class Student : public School
{
	public:
	string name;
	int roll;
	Name()
	{
		cout<<"Enter Student's Name : ";
		cin>>name;
		cout<<"Enter Roll number    : ";
		cin>>roll;
	}
};

class Marksheet : public Student
{
	public:
	marks()
	{
	
		cout<<endl<<endl<<"Student's Name : "<<name;
		cout<<endl<<"Roll No        : "<<roll;
		cout<<endl<<endl<<"%%%% MArksheet %%%%%"<<endl;
		cout<<"Maths     :  60/ 70"<<endl;
		cout<<"Physics   :  55/ 70"<<endl;
		cout<<"Chemestry :  65/ 70"<<endl;
		cout<<"Total     : 180/210"<<endl;
		cout<<"Percentage: 85.71 %";
	}
};

main()
{
	
	Marksheet m;
	m.intro();
	m.Name();
	m.marks();
}




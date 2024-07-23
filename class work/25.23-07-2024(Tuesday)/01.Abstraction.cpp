#include<iostream>
using namespace std;

class Employer{
	
	public:
		virtual salary()=0; // pure virtual function
};

class Lucky : public Employer{
	
	public:
		salary()
		{
			cout<<"Lucky got Rs.200"<<endl;
		}
};

class Himanshu : public Employer{
	
	public:
		salary()
		{
			cout<<"Himanshu got Rs.150"<<endl;
		}
};

class Vishal : public Employer{
	
	public:
		salary()
		{
			cout<<"Vishal got Rs.500"<<endl;
		}
};

main()
{
	Lucky l;
	Himanshu h;
	Vishal v;
	
	l.salary();
	h.salary();
	v.salary();
}



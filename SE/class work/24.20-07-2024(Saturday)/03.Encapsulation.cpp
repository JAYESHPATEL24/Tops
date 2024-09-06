#include<iostream>
using namespace std;

class A{
	
	string name;
	int id;
	
	public:
		getname(string name)
		{
			this->name = name;
	 	} 
	 	setname()
	 	{
	 		cout<<"Name   : "<<this->name;
		}
		getid(int id)
		{
			this->id=id;
		}
		setid()
		{
			cout<<endl<<"Number : "<<this->id;
		}
		~A()
		{
			cout<<endl<<"datebayoooo..";
		}
};

main()
{
	A a;
	a.getname("NARUTO UZUMAKI");	
	a.setname();
	a.getid(7);
	a.setid();
}

#include<iostream>
using namespace std;

class A
{
	protected:
	int a,b,c;
	A()
	{
		cout<<"Hybrid inheritance "<<endl;
	}	
};

class B : public virtual A{
	public:
	funb()
	{
		cout<<"Class B "<<endl;
		cout<<"Enter A : ";
		cin>>a;
		cout<<"A : "<<a<<endl<<endl; 	
	}
};

class C : public virtual A{
	public:
	func()
	{
		cout<<"Class C "<<endl;
		cout<<"Enter B : ";
		cin>>b;
		cout<<"B : "<<b<<endl<<endl; 	
	}
};

class D : public B,public C{
	public:
	fund()
	{
		cout<<"Class D "<<endl;
		cout<<"Enter C : ";
		cin>>c;
		cout<<"C : "<<c<<endl; 	
	}
};

main()
{
	D d;
	d.funb();
	d.func();
	d.fund();
}



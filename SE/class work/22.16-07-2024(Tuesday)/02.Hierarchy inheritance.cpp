#include<iostream>
using namespace std;

class A
{
	protected:
		int x,y;
	A()
	{
		cout<<"I am Robot."<<endl;
	}
	public:
	fu()
	{
		cout<<"Enter a number X :";
		cin>>x;
		
	}
	fu1()
	{
		cout<<"Enter a number y:";
		cin>>y;	
	}
};

class B : public A
{
	public:
	fun1()
	{
		cout<<"Enter X : "<<x<<endl;
	}	
};

class C : public A
{
	public:
	fun2()
	{
		cout<<"Enter y : "<<y<<endl;
	}
};
main()
{
	C c;
	B b;
	b.fu();
	b.fun1();
	c.fu1();
	c.fun2();
}

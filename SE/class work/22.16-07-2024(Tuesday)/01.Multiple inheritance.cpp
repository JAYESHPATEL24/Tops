#include<iostream>
using namespace std;

class A
{
	protected:
		int a,b;
	
	A()
	{
		cout<<"This is a Constructor"<<endl;
	}
};

class B
{
	public:
	fun1()
	{
		cout<<"Function of class B"<<endl;	
	}	
};

class C : public A, public B
{
	public:
	
	fun2()
	{
		cout<<"Enter a number A : ";
		cin>>a;
		cout<<"Enter a number B : ";
		cin>>b;
		cout<<"A : "<<a<<endl<<"B : "<<b;
	}
};
main()
{
	C o;
	o.fun1();
	o.fun2();
}

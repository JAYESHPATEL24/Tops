#include<iostream>
using namespace std;

class A
{
	public:
	fun1()
	{
		cout<<"Parent class"<<endl;
	}
};

class B: public A
{
	public:
	fun2()
	{
		cout<<"Child class"<<endl;	
	}	
};

main()
{
	B b;
	b.fun1();
	b.fun2();
}



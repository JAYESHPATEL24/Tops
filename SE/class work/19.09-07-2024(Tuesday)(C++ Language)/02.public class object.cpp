#include<iostream>
using namespace std;

class Myclass
{
	public:
	int a,b;
	
	fun1()
	{
		cout<<"Enter A : ";
		cin>>a;
		cout<<"Enter B : ";
		cin>>b;
		cout<<"Addition : "<<a+b<<endl<<endl;	
	}
	
	fun2()
	{
		cout<<"Enter A : ";
		cin>>a;
		cout<<"Enter B : ";
		cin>>b;
		cout<<"Subtraction : "<<a-b<<endl<<endl;
	}
	
	fun3()
	{
		cout<<"Enter A : ";
		cin>>a;
		cout<<"Enter B : ";
		cin>>b;
		cout<<"Multipliction : "<<a*b<<endl<<endl;	
	}
	
	fun4()
	{
		cout<<"Enter A : ";
		cin>>a;
		cout<<"Enter B : ";
		cin>>b;
		cout<<"Division : "<<a/b<<endl<<endl;	
	}	
};

main()
{
	Myclass obj;
	obj.fun1();
	obj.fun2();
	obj.fun3();
	obj.fun4();
}



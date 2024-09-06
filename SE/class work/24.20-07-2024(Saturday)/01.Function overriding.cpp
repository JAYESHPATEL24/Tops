#include<iostream>
using namespace std;

class A{
	
	public:
		fun()
		{
			cout<<"Hay Hay" <<endl<<"Oye Hoy"<<endl;
		}
};

class B : public A{
	
	public:
		fun()
		{
			A::fun();         //scope resolution operator	
			cout<<"Bado bati bado bati";
		}
};

main()
{
		B b;
		b.fun();	
}



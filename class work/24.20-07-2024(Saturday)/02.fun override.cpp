#include<iostream>
using namespace std;

class A{
	
	public:
		fun()
		{
			cout<<"Hay Hay" <<endl<<"Oye Hoy"<<endl;
		}
};

class B{
	
	public:
		fun()
		{	
			cout<<"Bado bati bado bati"<<endl;
		}
};

class C : public A,public B{
	
	public:
		fun()
		{	
			B::fun();
			A::fun();
			cout<<"Ankh ladi bado bati"<<endl;
		}
};

main()
{
		C c;
		c.fun();	
}



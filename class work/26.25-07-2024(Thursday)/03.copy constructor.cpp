#include<iostream>
using namespace std;

class A{
	
	int x,y;
	
	public:
		
		A(int a, int b)		//parameterised constructor
		{
			x = a;
			y = b;
		}
		
		A(A &f)			//copy constructor
		{
			cout<<"A : "<<f.x<<endl;
			cout<<"B : "<<f.y;
		}
};

main()
{
	A o(50,100);
	A b(o);
}



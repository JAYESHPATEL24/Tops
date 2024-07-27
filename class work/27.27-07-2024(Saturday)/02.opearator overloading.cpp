#include<iostream>
using namespace std;

class Sub{
	
	int a,b;
	
	public:
		
		Sub(int x=0, int y=0)
		{
			a = x;
			b = y;
		}
		
		Sub operator-(Sub const &s)
		{
			Sub u;
			u.a = a - s.a;
			u.b = b - s.b;
			return u; 
		}
		
		display()
		{
			cout<<"a : "<<a<<"b : "<<b;
		}
};

main()
{
	Sub s1(10,20),s2(1,2),s3;
	s3 = s1-s2;
	s3.display();
}



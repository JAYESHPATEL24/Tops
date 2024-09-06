#include<iostream>
using namespace std;

class X
{
	public:
	X(int y)
	{
		int fact=1,i;
		for(i=1;i<=y;i++)
			fact *= i;
		cout<<"Factorial is : "<<fact;
	}
};

main()
{
	X O(7);
}



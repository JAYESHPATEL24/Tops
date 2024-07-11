#include<iostream>
#include<windows.h>
using namespace std;

class Xyz
{
	public:
	Xyz()			//default costructor
	{
		cout<<"WAKE UP TO REALITY......."<<endl;
	}
	
	Xyz(int a)		//parameterized constructor
	{
		int i,j;
		for(i=1;i<=a;i++)
		{
			for(j=1;j<=i;j++)
			{
				Sleep(100);
				cout<<"%";
			}
			cout<<endl;
		}
	}
};

main()
{
	Xyz o;			// call defualt constructor
	Xyz p(10);		// Call parameterized constructor
}



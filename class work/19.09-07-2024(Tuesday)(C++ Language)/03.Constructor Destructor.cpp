#include<iostream>
using namespace std;

class Hello
{
	public:
	Hello() //Constructor
	{
		cout<<"Welcome to our Website."<<endl<<endl;
	}
	
	prime()
	{
		int i,n,c;
		
		cout<<"Enter a Number : ";
		cin>>n;
		
		for(i=1;i<=n;i++)
		{
			if(n%i==0)
				c++;
		}
		if(c==2)
			cout<<"Numeber is prime."<<endl<<endl;
		else
		 	cout<<"Number is not prime."<<endl<<endl;
	}
	
	~Hello()
	{
		cout<<"Thank you."<<endl<<endl;
	}
};
main()
{
	Hello obj;
	obj.prime();
}



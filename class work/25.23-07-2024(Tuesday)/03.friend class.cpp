#include<iostream>
using namespace std;

class A{
	private:
		int a,b,c[5],d[5];
		
		friend class B;
};

class B{
	
	public:
		fun1(A& a)
		{
			cout<<"Enter Number A : ";
			cin>>a.a;
			cout<<"Enter Number B : ";
			cin>>a.b;
			
			cout<<"Addition = "<<a.a + a.b;
		}
		
		fun2(A& b)
		{
			cout<<endl<<endl<<"Enter Array Elements : "<<endl;
			int i;
			for(i=0; i<5 ; i++)
			{
				cout<<i+1<<". : ";
				cin>>b.c[i];
			}
			
			cout<<endl<<endl<<"Enter Array Elements : "<<endl;
			for(i=0; i<5 ; i++)
			{
				cout<<i+1<<". : ";
				cin>>b.d[i];
			}
			
			cout<<endl<<"Array Elements after addition of two arrays : "<<endl;
			for(i=0; i<5; i++)
			{
				cout<<i+1<<". : "<<b.c[i] + b.d[i] <<endl;
			}
		}
};

main()
{
	A a;
	B b;
	b.fun1(a);
	b.fun2(a);
}



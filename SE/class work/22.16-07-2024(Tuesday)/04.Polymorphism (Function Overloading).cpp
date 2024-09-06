#include<iostream>
using namespace std;
class A
{
	public:
		
	fun1()
	{
		cout<<"Hello"<<endl;
	}
	fun1(int a)
	{
		cout<<"hi"<<endl;
	}
	fun1(string s)
	{
		cout<<"Aati kya khandala..";
	}
};
main()
{
	A a;
	a.fun1();
	a.fun1(10);
	a.fun1("Yes");
}	



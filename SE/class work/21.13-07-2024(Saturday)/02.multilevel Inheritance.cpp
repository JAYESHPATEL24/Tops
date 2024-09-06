#include<iostream>
using namespace std;

class Grandparent
{
	public:
	home()
	{
		cout<<"GrandParent purchase a home."<<endl;
	}
};

class Parent : public Grandparent
{
	public:
	car()
	{
		cout<<"Parents purchase a Car."<<endl;
	}
};

class Child : public Parent
{
	public:
	mohmaya()
	{
		cout<<"Sub Moh Maya he........";
	}
};

main()
{
	Child x;
	x.home();
	x.car();
	x.mohmaya();
}



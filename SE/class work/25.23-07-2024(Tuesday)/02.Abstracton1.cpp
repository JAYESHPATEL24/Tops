#include<iostream>
using namespace std;

class Wheel{
	
	public:
					//pure virtual functions
		virtual tyre()= 0 ;
		virtual colour()=0;		
};

class Car : public Wheel{
	
	public:
		
		tyre()
		{
			cout<<"Car has 4 tyres."<<endl;
		}
		colour()
		{
			cout<<"Colour of Car is Red."<<endl<<endl;
		}
};

class Bike : public Wheel{
	
	public:
		
		tyre()
		{
			cout<<"Bike has 2 tyres."<<endl;
		}
		colour()
		{
			cout<<"Colour of Bike is Black."<<endl<<endl;
		}
};

class Truck : public Wheel{
	
	public:
		
		tyre()
		{
			cout<<"Truck has 6 tyres."<<endl;
		}
		colour()
		{
			cout<<"Colour of TRuck is Yellow."<<endl<<endl;
		}
};

main()
{
	Car c;
	Bike b;
	Truck t;
	
	c.tyre();
	c.colour();
	
	b.tyre();
	b.colour();
	
	t.tyre();
	t.colour();
}



#include<iostream>
using namespace std;

class arr{
	
	private:
		int a[5];
		
		friend descending(arr& x); //declare friend function
};

descending(arr& x)			//friend function definition
{
	int i,j;
	
	cout<<"Enter 5 numbers : "<<endl;
	
	for(i=0;i<5;i++)
	{
		cout<<i+1<<". : ";
		cin>>x.a[i];
	}
	
	cout<<endl<<"Desending order : "<<endl;
	
	for(i=0;i<5;i++)
	{
		for(j=i+1;j<5;j++)
		{
			if(x.a[j]>x.a[i])	
			{
				int temp = x.a[i];
				x.a[i] = x.a[j];
				x.a[j] = temp;
			}
		}
		cout<<x.a[i]<<" ";	
	}
}

main()
{
	arr y;
	descending(y); //friend function call	
}



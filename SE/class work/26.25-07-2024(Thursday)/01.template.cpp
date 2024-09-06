#include<iostream>
using namespace std;

template<typename T>
T Maximum(T a, T b)
{
	return((a>b)?a:b);
}

template<t

main()
{
	cout<<Maximum<int>(10,50)<<endl;
	cout<<Maximum<char>('a','x')<<endl;
}



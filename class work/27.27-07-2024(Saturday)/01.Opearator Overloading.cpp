#include<iostream>
using namespace std;

class Image{
	
	int height, width;
	
	public:
		
		Image(int h = 0, int w = 0)
		{
			height = h;
			width = w;
		}
		
		Image operator+(Image &i)
		{
			Image r;
			r.height = height + i.height;
			r.width = width + i.width;
			return r;
		}
		
		display()
		{
			cout<<"Heighth : "<<height << "    Width : "<<width;
		}
};

main()
{
	Image i1(5,10),i2(50,100),i3;
	
	i3 = i1 + i2;
	
	i3.display();
}



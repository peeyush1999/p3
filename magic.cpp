#include<stdio.h>


int &f(int a)
{	int y;
	y=y+a;
	return y;
}

int main()
{
	int x=100;
	int i =50,d=10;
	int y;
	f(x) = i+d;
	
	printf("%d %d",x,y);
}

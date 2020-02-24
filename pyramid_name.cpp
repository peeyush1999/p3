#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>

using namespace std;
int main()
{
	int temp;
	char str[]="ramanclasses";
	int len = sizeof(str)/sizeof(char) -1;

	for(int i=0;i<len;i++)
	{	
		temp=i;
		
		while(temp--)
			cout<<" ";
		for(int j=i;j<len;j++)
		{
			cout<<str[j];
			
		}
		cout<<endl;
		len--;
	}
}

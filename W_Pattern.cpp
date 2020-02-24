#include<stdio.h>
#include<iostream>
#include<math.h>

using namespace std;
int main()
{
	int num_rows;
	char str[]="Ramanclasses";
	cin>>str;
	cin>>num_rows;
	
	int len=sizeof(str)/sizeof(char) - 1;
	int mark[len]={-1};
	
	int counter = -1*(num_rows-1);
	
	
	for(int i=0;i<len;i++)
	{
		if(counter >= (num_rows-1))
		{
			counter = -1*(num_rows-1);
			//cout<<counter<<endl;
		}
		mark[i] = abs(counter);
		counter++;
	}
	/*for(int i=0;i<len;i++)
	{
		cout<<mark[i]<<" ";
	}*/
	
	for(int i=num_rows-1;i>=0;i--)
	{
		for(int j=0;j<len;j++)
		{
			if(mark[j]==i)
			{
				cout<<str[j];
			}
			else
			{
				cout<<" ";
			}
		}
		cout<<endl;
	}
	
	
	
}

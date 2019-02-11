#include<stdio.h>
#include<conio.h>
#include<string.h>

#define AND &&

bool myIsDigit(char s)
{
		
		bool flag = false;
		
		
			if(s-'0'<=9 && s-'0'>=0 )
			{
				flag=true;
			
			}
			
		
		return flag;
		
} 


int main()
{
	char s='?';
	if(myIsDigit(s))
	{
		printf("Yes");
	}
	else
	{
		printf("No");
	}
	return 0;
	
}

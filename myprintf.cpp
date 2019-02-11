#include<stdio.h>
#include<conio.h>
#include<string.h>

bool mypalindrome(char *s)
{
		int len=strlen(s);
		int i=0;
		int j=len-1;
		bool flag = true;
		
		while(i<j)
		{
			if(s[i]!=s[j])
			{
				flag=false;
				break;
			}
				i++;
				j--;	
		}
		
		return flag;
		
} 


int main()
{
	char s[]="abcbaa";
	if(mypalindrome(s))
	{
		printf("Yes");
	}
	else
	{
		printf("No");
	}
	return 0;
	
}

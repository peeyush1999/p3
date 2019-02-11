#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>

bool myStringUpper(char *s)
{
		int len=strlen(s);
		int i=0;
		
		bool flag = true;
		
		while(i<len)
		{	
			if(islower(s[i]))
			s[i] = s[i] + 'A' -'a';
			i++;		
		}
		
		return flag;
		
} 


int main()
{
	char s[]="abcbaaZ#$%aBZ";
	
	myStringUpper(s);
	
	printf("%s",s);
	
	return 0;
	
}

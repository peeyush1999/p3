#include<stdio.h>
#include<string.h>

void subString(char *s)
{
	int len = strlen(s);
	int i=0,j;
	char out[500];
	int count=0;
	
	while(s[i]!=0)
	{	
		count=0;
		
		for(j=i;j<len;j++)
		{
			out[count] = s[j];
			count++;
			out[count]=0;
			printf("%s\n",out); 
		}
		
		i++;
	}
	 
}
int main()
{	char *str ="ikra";
	subString(str);
	return 0;
}


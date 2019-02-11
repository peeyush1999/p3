#include<stdio.h>
#include<string.h>

void mystrrev(char *str)
{
	int len = strlen(str);
	int i = 0 ;
	int j = len-1;
	char temp;
	
	while(i<j)
	{	
		temp = str[i];
		str[i] = str[j];
		str[j] = temp;
		
		i++;
		j--;	
	}
	
		
}

int main()
{
	char str[1000];
	scanf("%s",str);
	
	mystrrev(str);
	printf("%s",str);
	
	return 0;	
}

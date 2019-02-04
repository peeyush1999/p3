#include<stdio.h>

#define MAX 100000

int A[MAX][MAX];

int main()
{
	
	int i,j,k,num;
	
	int numR,numC,sum,count=0;
	
	scanf("%d",&numR);
	scanf("%d",&numC);
	
	k = numR+numC-1;
	
		
	for(i=0;i<numR;i++)
	{
		for(j=0;j<numC;j++)
		{
			scanf("%d",&A[i][j]);	
		}	
	}	

while(count<k)
{
	
	if(count%2==0)
	{
		for(i=0;i<numR;i++)
		{
			for(j=0;j<numC;j++)
			{
				if(i+j == count)
					printf("%d ",A[j][i]);	
			}	
		}
	
	}
	else
	{
		for(i=0;i<numR;i++)
		{
			for(j=0;j<numC;j++)
			{
				if(i+j == count)
					printf("%d ",A[i][j]);	
			}	
		}
	
	}
	count++;		
		
}

return 0;
}

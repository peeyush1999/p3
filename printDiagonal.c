#include<stdio.h>

#define MAX 100000

int A[MAX][MAX];

int main()
{
	
	int i,j,k,num;
	
	int numR,numC,sum;
	k=0;
	
	scanf("%d",&numR);
	scanf("%d",&numC);
		
	for(i=0;i<numR;i++)
	{
		for(j=0;j<numC;j++)
		{
			scanf("%d",&A[i][j]);	
		}	
	}
	
	printf("Enter Diagonal NUmber:");
	scanf("%d",&sum);
	
	for(i=0;i<numR;i++)
	{
		for(j=0;j<numC;j++)
		{
			if(i+j == sum)
				printf("%d ",A[i][j]);	
		}	
	}

	

return 0;
}

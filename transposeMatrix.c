#include<stdio.h>

#define MAX 100000

int A[MAX][MAX];

int main()
{
	
	int i,j,k,num;
	
	int numR,numC,sum,temp;
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
	
	
	
	for(i=0;i<numR;i++)
	{
		for(j=0;j<numC;j++)
		{
			if(i<j)
			{
				temp = A[i][j];
			 A[i][j] = A[j][i];
			 A[j][i] = temp;	
			}
			 
			 printf("%d ",A[i][j]);	
			 	
		}	
		printf("\n");
	}

	
	

return 0;
}

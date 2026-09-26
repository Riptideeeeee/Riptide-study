#include<stdio.h>
int main(){
	int sum=0,s=0;
	int matrix[3][3];
	for (int i =0;i<3;i++){
		for (int j =0;j<3;j++){
			scanf("%d",&matrix[i][j]);
			sum+=matrix[i][j];
		}
	}
	s=matrix[0][0] + matrix[1][1] + matrix[2][2];
	printf("%d , %d",sum,s);
}

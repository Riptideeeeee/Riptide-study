#include<stdio.h>
int main(){
	int list[5];
	for (int i=0;i<5;i++){
		scanf("%d",&list[i]);
	}
	for (int i=4;i>=0;i--){
		printf("%d ",list[i]);
	}
	return 0;
}

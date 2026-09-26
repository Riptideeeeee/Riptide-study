#include<stdio.h>
#include<stdlib.h>
int main(){
	int *list=(int *)malloc(3*sizeof(int));
	if (list==NULL){
		printf("List Fail!");
		return 1;
	}
	list[0]=10;list[1]=20;list[2]=30;
	int *new_list=(int *)realloc(list,5*sizeof(int));
	if (new_list==NULL){
		printf("New_list Fail!");
		free(list);
		return 1;
	}
	list=new_list;
	list[3]=40;list[4]=50;
	for (int i =0;i<5;i++){
		printf("%d ",list[i]);
	}
	free(list);
	return 0;
}

#include<stdio.h>
void print_name(char *name){
	printf("\n%s",name);
}
int main(){
	char *names[]={"张三", "李四", "王五", "赵六", "孙七"};
	for (int i=0;i<5;i++){
		print_name(names[i]);
	}
	return 0;
}

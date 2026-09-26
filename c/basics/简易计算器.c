#include<stdio.h>
int main(){
	printf("char:");
	char op;int a,b;
	scanf("%c",&op);
	printf("\nnumber a is :");
	scanf("%d",&a);
	printf("\nnumber b is :");
	scanf("%d",&b);
	printf("\n");
	switch (op){
		case '+':
			printf("the answer is %d",a+b);
			break;
		case '-':
			printf("the answer is %d",a-b);
			break;
		case '*':
			printf("the answer is %d",a*b);
			break;
		case '/':
			if (b==0){
				printf("b cannot be 0");
				break;
			}else{
			printf("the answer is %d",a+b);
			break;
			}
		default:
			printf("the char is not in +-*/");
	}
	return 0;
}

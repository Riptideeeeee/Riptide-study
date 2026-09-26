#include<stdio.h>
void is_even(int n){
	if (n%2==1){
		printf("\nThis is an odd num");
	}else{
		printf("\nThis is an even num");
	}
}
int main(){
	int n;
	scanf("%d",&n);
	is_even(n);
	return 0;
}

#include<stdio.h>
int main(){
	int n;int ans=0;
	scanf("%d",&n);
	for (int i =0;i<=n;i++){
		ans+=i;
		if (i==n){
			printf("%d = %d",i,ans);
		}else{
			printf("%d +",i);
		}
	} 
	return 0;
}

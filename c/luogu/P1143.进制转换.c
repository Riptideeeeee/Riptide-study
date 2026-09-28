#include<stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	char num[100];
	scanf("%s",num);
	int m;
	scanf("%d",&m);
	int num10=0;
	for (int i=0;num[i]!='\0';i++){
		if ('0'<=num[i] && num[i]<='9'){
			num10=num10*n+(num[i]-'0');
		}else{
			num10=num10*n+(num[i]-'A'+10);
		}
	}
	char ans[100];
	ans[99]='\0';
	int times=98;
	while(num10!=0){
		int temp=num10%m;
		if (0<=temp && temp<=9){
			ans[times]='0'+temp;
		}else{
			ans[times]='A'+temp-10;
		}
		num10=num10/m;
		times--;
	}
	printf("%s\n",ans+times+1);
	return 0;
}

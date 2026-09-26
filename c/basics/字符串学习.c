#include<stdio.h>
#include<string.h>
int main(){
	char a[99];
	char b[99];
	int c=0;
	scanf("%s",a);
	scanf("%s",b);
	printf("The first String's length is %d\n",strlen(a));
	printf("The second String's length is %d\n",strlen(b));
	c=strcmp(a,b);
	strcat(a,b);
	printf("Result: %s\n",a);
	if (c==0){
		printf("The two strings are the same string\n");
	}else{
		printf("The two strings are not the same\n");
	}
	return 0;
}

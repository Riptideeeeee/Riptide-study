#include <stdio.h>

bool isPalindrome(int x) {
    int original=x;
    int reverse=0;
    int temp=0;
    if (x<0){
        return false;
    }
    while(x==0){
        temp=x%10;
        reverse=reverse*10+temp;
        x=(int)(x/10);
    }
    if (original==reverse){
        return true;
    }else{
        return false;
    }
}

int main(){
    printf("reverse:");
    int x=0;
    scanf("%d",&x);
    printf("\n%d",isPalindrome(x));
    scanf(" ");
    return 0;
}
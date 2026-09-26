#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node* next;
};
struct stack{
	struct node *top;
};
struct stack *init_stack(int value){
	struct stack *s=(struct stack*)malloc(sizeof(struct stack));
	struct node *add=(struct node*)malloc(sizeof(struct node));
	add->next=NULL;
	add->data=value;
	s->top=add;
	return s;
}
void push(struct stack *s, int value){
	struct node *new_top=(struct node*)malloc(sizeof(struct node));
	new_top->next=s->top;
	new_top->data=value;
	s->top=new_top;
}
int pop(struct stack *s){
	if (s->top->next==NULL){
		printf("this stack only has one element,you can't delete it\n");
		return s->top->data;
	}
	struct node *temp=s->top;
	s->top=s->top->next;
	return temp->data;
}
void print_stack(struct stack *s){
	struct node *current=s->top;
	printf("!!!\n");
	while (current!=NULL){
		printf("%d\n",current->data);
		current=current->next;
	}
}
int peek(struct stack *s){
	return s->top->data;
}
int main(){
	struct stack *s=init_stack(1);
	push(s,2);
	push(s,211);
	push(s,22);
	push(s,4);
	print_stack(s);
	for (int i =0;i<5;i++){
		printf("%d\n",pop(s));
	}
	push(s,211);
	push(s,22);
	push(s,4);
	printf("%d\n",peek(s));
	return 0;
}

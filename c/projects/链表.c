#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node* next;
};
struct Node* create_new_node(int data){
	struct Node* new_node=(struct Node*)malloc(sizeof(struct Node));
	new_node->data=data;
	new_node->next=NULL;
	return new_node;//这里会创造一个空节点，需要输入data一个值 
}
struct Node* create_head_node(int data,struct Node* head){
	struct Node* new_node=(struct Node*)malloc(sizeof(struct Node));
	new_node->data=data;
	new_node->next=head;
	return new_node;//这里在开头创造节点，需要输入data和head 
}
struct Node* create_tail_node(int data,struct Node* head){
	struct Node* new_node=(struct Node*)malloc(sizeof(struct Node)),*current=head;
	while (current->next!=NULL){
		current=current->next;
	}
	new_node->data=data;
	new_node->next=NULL;
	current->next=new_node;
	return head;//这里在尾部创造节点，需要data和head
}
//struct Node* create_insert_node(int data,struct Node* place){
//	struct Node* new_node=(struct Node*)malloc(sizeof(struct Node));
//	new_node->data=data;
//	new_node->next=place->next;
//	place->next=new_node;
//	return new_node;//这里插入节点，需要data和插入位置的上一个节点 
//}
struct Node* delete_node(int target,struct Node *head){
	struct Node* current=head,*temp;
	if (head->data==target){
		temp=head;
		head=temp->next;
		free(temp);
		return head;
	}
	while (current->next!=NULL){
		if (current->next->data==target){
			struct Node* temp=current->next;
			current->next=current->next->next;
			free(temp);
			return head;
		}
		current=current->next;
	}
	printf("Fail to find the node with value '%d'.\n",target);
	return head;
}
struct Node* print_list(struct Node* head){
	struct Node* current=head;
	while (current->next!=NULL){
		printf("%d ",current->data);
		current=current->next;
	}
	printf("%d \n",current->data);
}
void free_list(struct Node* head){
	struct Node* current=head;
	while (current!=NULL){
		struct Node* temp=current;
		current=current->next;
		free(temp);
	}
	printf("The list is free!\n");
}
int main(){
	struct Node* head=create_new_node(10);
	struct Node* current=head;
	for (int i=20;i<=100;i+=10){
		current=create_tail_node(i,current);
	}
	print_list(head);
	head=delete_node(10,head);
	print_list(head);
	head=create_tail_node(40,head);
	print_list(head);
	head=create_head_node(1,head);
	print_list(head);
	free_list(head);
	return 0;
}

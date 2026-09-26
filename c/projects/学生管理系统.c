#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct Student {
    int id;
    char name[20];
    float score;
    struct Student *next;
};
struct Student* add_student(struct Student *head, int id, char *name, float score){
	struct Student* current=head;
	if (head==NULL){
		struct Student* new_node = (struct Student*)malloc(sizeof(struct Student));
		new_node->id=id;
		strcpy(new_node->name,name);
		new_node->score=score;
		new_node->next=NULL;
		return new_node;
	}else{
		struct Student* temp=(struct Student*)malloc(sizeof(struct Student));
		while(current->next!=NULL){
			current=current->next;
		}
		current->next=temp;
		temp->id=id;
		strcpy(temp->name,name);
		temp->score=score;
		temp->next=NULL;
		return head;
	}
	
}
struct Student* delete_student(struct Student *head, int id){
	struct Student *current=head;
	char confirm;
	if (current->id==id){
			printf("ÊÇ·ñÒªÉ¾³ý£¿\nY/N:");
			scanf(" %c",&confirm);
			if (confirm=='Y'||confirm=='y'){
				struct Student *temp=current;
				current=current->next;
				free(temp);
				printf("É¾³ý³É¹¦!");
				return current;
			}else if(confirm=='N'||confirm=='n'){
				return head;
			}else{
				printf("´íÎóÊäÈë£¬È¡ÏûÉ¾³ý.");
				return head;
			}
		}
	while (current->next!=NULL){
		if (current->next->id==id){
			printf("ÊÇ·ñÒªÉ¾³ý£¿\nY/N:");
			scanf(" %c",&confirm);
			if (confirm=='Y'||confirm=='y'){
				struct Student *temp=current->next;
				current->next=current->next->next;
				free(temp);
				printf("É¾³ý³É¹¦!");
				return head;
			}else if(confirm=='N'||confirm=='n'){
				return head;
			}else{
				printf("´íÎóÊäÈë£¬È¡ÏûÉ¾³ý.");
				return head;
			}
		}
		current=current->next;
	}
	printf("´íÎóid£¬È¡ÏûÉ¾³ý\n");
	return head;
}
void find_student(struct Student *head, int id){
	struct Student* current=head;
	while (current!=NULL){
		if (current->id==id){
			printf("\n¸ÃÑ§ÉúÃû×ÖÊÇ%s, Ñ§ºÅÊÇ%d, ³É¼¨Îª%.1f\n",current->name,current->id,current->score);
			return;
		}
		current=current->next;
	}
	printf("\nÎ´ÕÒµ½¸ÃÑ§Éú\n");
	return;
}
struct Student* update_score(struct Student *head, int id, float new_score){
	struct Student* current=head;
	while(current!=NULL){
		if (current->id==id){
			current->score=new_score;
			printf("ÐÞ¸Ä³É¹¦!");
			return head;
		}
		current=current->next;
	}
	printf("Î´ÕÒµ½¸ÃÑ§Éú£¡");
	return head;
}
void print_all(struct Student *head){
	struct Student* current=head;
	while(current!=NULL){
		printf("%d , %s , %.2f\n",current->id,current->name,current->score);
		current=current->next;
	}
}
float calc_average(struct Student *head){
	struct Student* current=head;
	float all_score=0.0;
	int student_num=0;
	while(current!=NULL){
		all_score+=current->score;
		student_num++;
		current=current->next;
	}
	return (all_score/student_num);
}
void save_to_file(struct Student *head){
	struct Student *current=head;
	FILE *fp=fopen("stu.txt","w");
	while (current!=NULL){
		fprintf(fp,"%d %s %.2f\n",current->id,current->name,current->score);
		current=current->next;
	}
	fclose(fp);
	printf("±£´æ³É¹¦!\n");
}
struct Student* load_from_file(struct Student* head){
	FILE *fp=fopen("stu.txt","r");
	int id;
    char name[20];
    float score;
	while (fscanf(fp,"%d %s %f",&id,name,&score)==3){
		head=add_student(head,id,name,score);
	}
	fclose(fp);
	return head;
}
void free_all(struct Student *head){
	struct Student *current=head;
	while (current!=NULL){
		struct Student *temp=current;
		current=current->next;
		free(temp);
	}
	printf("ÒÑÊÍ·ÅÄÚ´æ!\n");
}
int main(){
	FILE *fp=fopen("stu.txt","r");
	struct Student* head=NULL;
	int choise,delete_id,find_id;
	int new_id;
	char new_name[20],enter;
	float new_score;
	if (fp==NULL){
		FILE *fp=fopen("stu.txt","w");
		fprintf(fp,"1001 Alice 85.5\n1002 Bob 92.0\n1003 Cindy 78.5");
		fclose(fp);
	}else{
		int ch = fgetc(fp);  // ¶ÁÈ¡µÚÒ»¸ö×Ö·û
    	if (ch == EOF) {
        	// ÎÄ¼þÎª¿Õ£¬Ð´Èë³õÊ¼Êý¾Ý
        	fclose(fp);
        	fp = fopen("stu.txt", "w");
        	fprintf(fp, "1001 Alice 85.5\n1002 Bob 92.0\n1003 Cindy 78.5");
        	fclose(fp);
    	}else{
    		fclose(fp);
		}
	}//ÅÐ¶ÏÎÄ¼þÊÇ·ñ´æÔÚ£¬²»´æÔÚÔòÐ´Èë³õÊ¼Êý¾Ý
	head=load_from_file(head);
	do {
		system("cls");
		printf("================================\n"
			   "   Ñ§Éú³É¼¨¹ÜÀíÏµÍ³\n"
			   "================================\n"
			   "1. Ìí¼ÓÑ§Éú\n"
			   "2. É¾³ýÑ§Éú\n"
			   "3. ²éÕÒÑ§Éú\n"
			   "4. ÐÞ¸Ä³É¼¨\n"
			   "5. ÏÔÊ¾È«²¿\n"
			   "6. ¼ÆËãÆ½¾ù·Ö\n"
			   "7. ±£´æµ½ÎÄ¼þ\n"
			   "8. ´ÓÎÄ¼þ¶ÁÈ¡\n"
			   "0. ÍË³ö\n"
			   "================================\n"
			   "ÇëÑ¡Ôñ£º");
		scanf("%d",&choise);
		switch (choise){
			case 1://1. Ìí¼ÓÑ§Éú
				printf("ÊäÈëÑ§ÉúÑ§ºÅ: ");
				scanf("%d",&new_id);
				printf("ÊäÈëÑ§ÉúÐÕÃû(ÇëÊäÈëÓ¢ÎÄ): ");
				scanf("%s",new_name);
				printf("ÊäÈëÑ§Éú³É¼¨: ");
				scanf("%f",&new_score);
				add_student(head,new_id,new_name,new_score);
				save_to_file(head);
				printf("Ìí¼Ó³É¹¦!\n°´»Ø³µ¼ü¼ÌÐø...");
				getchar();
				getchar();
				break;
			case 2://2. É¾³ýÑ§Éú
				printf("Ï£ÍûÉ¾³ýÄÄ¸öÑ§Éú£¬ÇëÊäÈëÑ§ºÅ£º");
				scanf("%d",&delete_id);
				head=delete_student(head,delete_id);
				save_to_file(head);
				printf("\n°´»Ø³µ¼ü¼ÌÐø...");
				getchar();
				getchar();
				break;
			case 3://3. ²éÕÒÑ§Éú
				printf("ÇëÊäÈë¸ÃÑ§ÉúÑ§ºÅ£º");
				scanf("%d",&find_id);
				find_student(head,find_id);
				printf("\n°´»Ø³µ¼ü¼ÌÐø...");
				getchar();
				getchar();
				break;
			case 4://4. ÐÞ¸Ä³É¼¨
				printf("ÇëÊäÈë¸ÃÑ§ÉúÑ§ºÅ£º");
				scanf("%d",&find_id);
				printf("ÇëÊäÈë¸ÃÑ§ÉúÐÂµÄ³É¼¨£º");
				scanf("%f",&new_score);
				head=update_score(head,find_id,new_score);
				save_to_file(head);
				printf("\n°´»Ø³µ¼ü¼ÌÐø...");
				getchar();
				getchar();
				break;
			case 5://5. ÏÔÊ¾È«²¿
				print_all(head);
				printf("\n°´»Ø³µ¼ü¼ÌÐø...");
				getchar();
				getchar();
				break;
			case 6://6. ¼ÆËãÆ½¾ù·Ö
				printf("Õâ¸ö°àÆ½¾ù·ÖÎª%.2f\n",calc_average(head));
				printf("\n°´»Ø³µ¼ü¼ÌÐø...");
				getchar();
				getchar();
				break;
			case 7://7. ±£´æµ½ÎÄ¼þ
				save_to_file(head);
				printf("\n°´»Ø³µ¼ü¼ÌÐø...");
				getchar();
				getchar();
				break;
			case 8://8. ´ÓÎÄ¼þ¶ÁÈ¡
				head=load_from_file(head);
				break;
			case 0:
				break;
			default:
				printf("ÎÞÐ§Ñ¡Ïî\n");
		}
	}while(choise!=0);
	save_to_file(head);
	free_all(head);
	printf("¸ÐÐ»Ê¹ÓÃ!\n");
	return 0;
}

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
			printf("是否要删除？\nY/N:");
			scanf(" %c",&confirm);
			if (confirm=='Y'||confirm=='y'){
				struct Student *temp=current;
				current=current->next;
				free(temp);
				printf("删除成功!");
				return current;
			}else if(confirm=='N'||confirm=='n'){
				return head;
			}else{
				printf("错误输入，取消删除.");
				return head;
			}
		}
	while (current->next!=NULL){
		if (current->next->id==id){
			printf("是否要删除？\nY/N:");
			scanf(" %c",&confirm);
			if (confirm=='Y'||confirm=='y'){
				struct Student *temp=current->next;
				current->next=current->next->next;
				free(temp);
				printf("删除成功!");
				return head;
			}else if(confirm=='N'||confirm=='n'){
				return head;
			}else{
				printf("错误输入，取消删除.");
				return head;
			}
		}
		current=current->next;
	}
	printf("错误id，取消删除\n");
	return head;
}
void find_student(struct Student *head, int id){
	struct Student* current=head;
	while (current!=NULL){
		if (current->id==id){
			printf("\n该学生名字是%s, 学号是%d, 成绩为%.1f\n",current->name,current->id,current->score);
			return;
		}
		current=current->next;
	}
	printf("\n未找到该学生\n");
	return;
}
struct Student* update_score(struct Student *head, int id, float new_score){
	struct Student* current=head;
	while(current!=NULL){
		if (current->id==id){
			current->score=new_score;
			printf("修改成功!");
			return head;
		}
		current=current->next;
	}
	printf("未找到该学生！");
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
	printf("保存成功!\n");
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
	printf("已释放内存!\n");
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
		int ch = fgetc(fp);  // 读取第一个字符
    	if (ch == EOF) {
        	// 文件为空，写入初始数据
        	fclose(fp);
        	fp = fopen("stu.txt", "w");
        	fprintf(fp, "1001 Alice 85.5\n1002 Bob 92.0\n1003 Cindy 78.5");
        	fclose(fp);
    	}else{
    		fclose(fp);
		}
	}//判断文件是否存在，不存在则写入初始数据
	head=load_from_file(head);
	do {
		system("cls");
		printf("================================\n"
			   "   学生成绩管理系统\n"
			   "================================\n"
			   "1. 添加学生\n"
			   "2. 删除学生\n"
			   "3. 查找学生\n"
			   "4. 修改成绩\n"
			   "5. 显示全部\n"
			   "6. 计算平均分\n"
			   "7. 保存到文件\n"
			   "8. 从文件读取\n"
			   "0. 退出\n"
			   "================================\n"
			   "请选择：");
		scanf("%d",&choise);
		switch (choise){
			case 1://1. 添加学生
				printf("输入学生学号: ");
				scanf("%d",&new_id);
				printf("输入学生姓名(请输入英文): ");
				scanf("%s",new_name);
				printf("输入学生成绩: ");
				scanf("%f",&new_score);
				add_student(head,new_id,new_name,new_score);
				save_to_file(head);
				printf("添加成功!\n按回车键继续...");
				getchar();
				getchar();
				break;
			case 2://2. 删除学生
				printf("希望删除哪个学生，请输入学号：");
				scanf("%d",&delete_id);
				head=delete_student(head,delete_id);
				save_to_file(head);
				printf("\n按回车键继续...");
				getchar();
				getchar();
				break;
			case 3://3. 查找学生
				printf("请输入该学生学号：");
				scanf("%d",&find_id);
				find_student(head,find_id);
				printf("\n按回车键继续...");
				getchar();
				getchar();
				break;
			case 4://4. 修改成绩
				printf("请输入该学生学号：");
				scanf("%d",&find_id);
				printf("请输入该学生新的成绩：");
				scanf("%f",&new_score);
				head=update_score(head,find_id,new_score);
				save_to_file(head);
				printf("\n按回车键继续...");
				getchar();
				getchar();
				break;
			case 5://5. 显示全部
				print_all(head);
				printf("\n按回车键继续...");
				getchar();
				getchar();
				break;
			case 6://6. 计算平均分
				printf("这个班平均分为%.2f\n",calc_average(head));
				printf("\n按回车键继续...");
				getchar();
				getchar();
				break;
			case 7://7. 保存到文件
				save_to_file(head);
				printf("\n按回车键继续...");
				getchar();
				getchar();
				break;
			case 8://8. 从文件读取
				head=load_from_file(head);
				break;
			case 0:
				break;
			default:
				printf("无效选项\n");
		}
	}while(choise!=0);
	save_to_file(head);
	free_all(head);
	printf("感谢使用!\n");
	return 0;
}

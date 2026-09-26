#include<stdio.h>
struct student_information{
	int id;
	char name[20];
	float score;
};
void write_stuinf(struct student_information students[5]){
	FILE *fp=fopen("student_information.txt","w");
	for (int i=0;i<5;i++){
		fprintf(fp,"%d %s %.2f\n",students[i].id,students[i].name,students[i].score);
	}
	fclose(fp);
	printf("Finished!");
}
void read_stuinf(struct student_information new_information[]){
	FILE *fp=fopen("student_information.txt","r");
	if (fp==NULL){
		printf("The file is not exist!");
	}else{
		for (int a=0;a<5;a++){
			fscanf(fp," %d %s %.2f",&new_information[a].id,new_information[a].name,&new_information[a].score);
		}
		printf("Finished!");
	}
}
int main (){
	int choise;
	struct student_information students[5]={
		{1001,"Alice",85.5},
		{1002,"Bob",92.0},
		{1003,"Cindy",78.5},
		{1004,"David",66.0},
		{1005,"Emily",89.5},
	};	
	struct student_information new_information[5];
	printf("1. Write students' information into student_information.txt\n2. Read students' information from student_information.txt\nChoose the function you need:");
	scanf("%d",&choise);
	if (choise==1){
		write_stuinf(students);
	}else if(choise==2){
		read_stuinf(new_information);
	}else{
		printf("This choise is not in the list!");
	}
	return 0;
}

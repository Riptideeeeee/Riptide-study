#include<stdio.h>
struct student_information{
	int id;
	char name[20];
	float score;
};
float calc_average(struct student_information students[]){
	float sum=0.0;
	for (int i =0;i<5;i++){
		sum+=students[i].score;
	}
	return sum/5;
}
void print_above_average(struct student_information students[],float average){
	for (int i =0;i<5;i++){
		if (students[i].score>=average){
			printf("%s\n",students[i].name);
		}
	}
}
int main (){
	struct student_information students[5]={
		{1001,"Alice",85.5},
		{1002,"Bob",92.0},
		{1003,"Cindy",78.5},
		{1004,"David",66.0},
		{1005,"Emily",89.5},
	};	
	float average=calc_average(students);
	print_above_average(students,average);
	return 0;
}

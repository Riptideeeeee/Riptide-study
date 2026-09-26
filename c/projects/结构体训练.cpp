#include<stdio.h>
struct Robot {
	char name[20];
	float speed;
	int battery;
};
int main(){
	struct Robot Turtle={"TurtleBot", 1.5, 80};
	printf("Name is %s\n",Turtle.name);
	printf("Speed is %.2fm/s\n",Turtle.speed);
	printf("Battery is %d%%\n",Turtle.battery);
	return 0;
}

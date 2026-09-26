#include <stdio.h>

struct Student {
    int id;
    char name[20];
    float score;
};

int main() {
    struct Student students[3] = {
        {1001, "Alice", 85.5},
        {1002, "Bob", 92.0},
        {1003, "Cindy", 78.5}
    };

    // 打开文件（写模式）
    FILE *fp = fopen("students.txt", "w");
    if (fp == NULL) {
        printf("文件打开失败！\n");
        return 1;
    }

    // 写入数据
    for (int i = 0; i < 3; i++) {
        fprintf(fp, "%d %s %.1f\n", students[i].id, students[i].name, students[i].score);
    }

    // 关闭文件
    fclose(fp);
    printf("写入成功！\n");

    return 0;
}

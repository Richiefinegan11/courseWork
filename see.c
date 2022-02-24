#include <stdio.h>

int main(void){
    char name[20];
    printf("What is your name? ");
    scanf("%s", name);
    printf("Hello there, %s", name);
}

#include <stdio.h>
#include "header.h"

int main(void) {

    int *p_int;
    printf("Hello, World!\n");
    // printf("The size of myStruct is %ld\n", sizeof(byte));
    printf("Size of a pointer is %ld\n", sizeof(p_int));

    char *string;
    string = "hello";
    printf("The size of string is %ld\n", sizeof(string));

    return 0;
}
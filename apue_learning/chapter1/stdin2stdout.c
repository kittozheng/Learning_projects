/*************************************************************************
 > File Name: stdin2stdout.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月15日 星期三 14时57分53秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUFFERSIZE 4096

void std2stdin1();
void std2stdin2();

void 
stdin2stdout1(){
    int n;
    char buf[BUFFERSIZE];
    
    /* 
     *  #include <unistd.h>
     *  #define STDIN_FILENO 0
     *  #define STDOUT_FILENO 1
     *
     *  read() function read a bytes_counted integer, while read error return -1
     */
    while((n = read(STDIN_FILENO, buf, BUFFERSIZE)) > 0){
        if(write(STDOUT_FILENO, buf, n) != n){
            fprintf(stderr, "write error..");
            exit(1);
        }
        break;
    }
    if(n < 0){
        fprintf(stderr, "read error");
        exit(1);
    } 
}

void 
stdin2stdout2(){
    int c;
    while((c = getc(stdin)) != EOF){
        if(putc(c, stdout) == EOF){
            fprintf(stderr, "output error..");
            exit(1);
        }
    }

    if(ferror(stdin)){
        printf("input error..");
        exit(1);
    }
}

void 
test(){
    printf("======================================================\n");
    printf("stdin to stdout, using original unix code..\n");
    stdin2stdout1();
    printf("stdin to stdout, using getc and putc function..\n");
    stdin2stdout2();
    printf("======================================================\n");
}

int
main(){   
    test();
    exit(0);
}
 

/*************************************************************************
 > File Name: exec_cmd_from_stdin.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月15日 星期三 15时52分38秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

#define MAXLINE 4096

int
main(){
    char buf[MAXLINE];
    pid_t pid;
    int status;
    printf("%%");
    
    while(fgets(buf, MAXLINE, stdin) != NULL){
        if(buf[strlen(buf) - 1] == '\n'){
            /* replace newlinew with null */
            buf[strlen(buf) - 1] = 0;
        }
        
        /*
         *  execlp() run cmd for once and stop the process
         *  In order to make execlp run more than once 
         *  we can use fork() to create child process,and
         *  let child process handle the execlp so that
         *  child process end but parent process keep going.
         * */
        if((pid = fork()) <  0){
            fprintf(stderr, "fork error..");
            exit(1);
        }else if(pid == 0){
            /* child process */
            /*
             * int execlp(const char *file, const char *arg, ...);
             */
            execlp(buf, buf, (char *)0);
            fprintf(stderr, "couldn't execute: %s\n", buf);
        }

        /* parent process */
        if((pid = waitpid(pid, &status, 0)) < 0){
            fprintf(stderr, "waitpid error..\n");
            exit(1);
        }
        printf("%%");
    }
    exit(0);
}

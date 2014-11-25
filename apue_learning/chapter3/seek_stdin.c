/*************************************************************************
 > File Name: seekfile.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月16日 星期四 17时01分41秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int
main(){
    if(lseek(STDIN_FILENO, 0, SEEK_CUR) == -1)
        printf("seek error..\n");
    else
        printf("seek ok\n");

    exit(0);
}

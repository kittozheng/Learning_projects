/*************************************************************************
 > File Name: printpid.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月15日 星期三 15时23分15秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int
main(){
    printf("APUE from process ID %d\n", getpid());
    exit(0);
}

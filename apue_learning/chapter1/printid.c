/*************************************************************************
 > File Name: printid.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月15日 星期三 16时23分26秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int
main(){
    printf("uid = %d, gid = %d\n", getuid(), getpid());
    exit(0);
}


/*************************************************************************
 > File Name: printerror.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月15日 星期三 16时19分08秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

int
main(int argc, char *argv[]){
    fprintf(stderr, "EACCES: %s\n", strerror(EACCES));
    errno = EACCES;
    perror(argv[0]);
    exit(0);
}

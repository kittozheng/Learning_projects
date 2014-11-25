/*************************************************************************
 > File Name: locate_route.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月16日 星期四 11时27分59秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>
#include <errno.h>

#ifdef PATH_MAX
static int pathmax = PATH_MAX;
#else 
static int pathmax = 0;
#endif

#define PATH_MAX_GUESS 1024

int get_pathmax(void){
    if(pathmax == 0){
        errno = 0;
        if((pathmax = pathconf("/", _PC_PATH_MAX)) < 0){
            if(errno == 0){
                pathmax = PATH_MAX_GUESS;
            }else{
                fprintf(stderr, "sysconf error for _SC_OPEN_MAX..\n");
            }
        }else{
            pathmax++;
        }
    }
    return pathmax;
}

int
main(void){
    printf("pathmax = %d\n", get_pathmax());
    exit(0);
}

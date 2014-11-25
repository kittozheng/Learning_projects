/*************************************************************************
 > File Name: get_openmax.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月16日 星期四 13时20分55秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

#ifdef OPEN_MAX
static int long openmax = OPEN_MAX;
#else
static int long openmax = 0;
#endif

#define OPEN_MAX_GUESS 256

int get_openmax(void){
    if(openmax == 0){
        errno = 0;
        if((openmax = sysconf(_SC_OPEN_MAX)) < 0){
            if(errno == 0){
                openmax = OPEN_MAX_GUESS;
            }else{
                fprintf(stderr, "sysconf error for SC_OPEN_MAX..");
            }
        }
    }

    return openmax;
}

int
main(){
    printf("openmax = %d\n", get_openmax());
    return 0;
}


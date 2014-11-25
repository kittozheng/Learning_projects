/*************************************************************************
 > File Name: printconf.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月16日 星期四 11时07分10秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <limits.h>

static void
pr_sysconf(char *, int);

static void
pr_pathconf(char *, const char *, int);

int
main(int argc, char *argv[]){
    if(argc != 2){
        printf("Usage: printconf <dirname>\n");
        exit(0);
    }
#ifdef ARG_MAX
    printf("ARG_MAX defined to be %d\n", ARG_MAX+0);
#else
    printf("No symbol for ARG_MAX\n");
#endif

#ifdef MAX_CANON
    printf("MAX_CANON defined to be %d\n", MAX_CANON+0);
#else
    printf("No symbol for MAX_CANON");
#endif

    pr_sysconf(argv[0], argc);
    pr_pathconf(argv[0], argv[1], argc);
    return 0;
}

static void
pr_sysconf(char *mesg, int name){
    long val;

    fputs(mesg, stdout);
    errno = 0;

    if((val = sysconf(name)) < 0){
        if(errno != 0){
            if(errno == EINVAL){
                fputs("(not supported) \n", stdout);
            }else{
                fprintf(stderr, "sysconf error\n");
            }
        }else{
            fputs("(no limit)\n", stdout);
        }
    }else{
        printf("%ld\n", val);
    }
}

static void
pr_pathconf(char *mesg, const char *path, int name){
    long val;

    fputs(mesg, stdout);
    errno = 0;

    if((val = pathconf(path, name)) < 0){
        if(errno != 0){
            if(errno == EINVAL){
                fputs("(not supported)\n", stdout);
            }else{
                fprintf(stderr, "pathconf error, path = %s\n", path);
            }
        }else{
            fputs("(no limit)\n", stdout);
        }
    }else{
        printf("%ld\n", val);
    }
}




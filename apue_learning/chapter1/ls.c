/*************************************************************************
 > File Name: ls.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月15日 星期三 14时20分26秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dirent.h>

#define PATH_SIZE 1024

int
main(int argc, char *argv[]){
    DIR *dp = NULL;
    struct dirent *dirp = NULL;
    char *path = NULL;
    
    /* Get ls path */
    if(argc > 2){
        printf("Usage: ls <directory_name>");
        exit(1);
    }else if(argc == 1){
        path = (char *)malloc(PATH_SIZE);
        if(getcwd(path, PATH_SIZE) == NULL){
            fprintf(stderr, "getcwd error..\n");
            exit(1);
        }
    }else{
        path = argv[1];
    }
    
    /*
     * #include <sys/types.h>
     * #include <dirent.h>
     *
     * DIR *opendir(const char *dirname);
     * struct dirent *readdir(DIR *dirp);
     * int closedir(DIR *dirp)
     */
    if((dp = opendir(path)) == NULL){
        fprintf(stderr, "can't open %s", path);
        exit(1);
    }
    while((dirp = readdir(dp)) != NULL){
        printf("%s\n", dirp->d_name);
    }

    closedir(dp);
    dp = NULL;

    if(argc == 1){
        free(path);
    }

    exit(0);
}

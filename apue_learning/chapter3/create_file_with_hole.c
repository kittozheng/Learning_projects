/*************************************************************************
 > File Name: create_file_with_hole.c
 > Author: kitto Zheng
 > Mail: kittoszu@gmail.com
 > Created Time: 2014年10月16日 星期四 17时27分27秒
 ************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

char buf1[] = "abcdefghij";
char buf2[] = "ABCDEFGHIJ";

#define FILE_MODE ()
int
main(){
    int fd;

    if((fd = create("file.hole", FILE_MODE)) < 0){
        fprintf(stderr, "create error..");
        exit(1);
    }

    if(write(fd,  buf1, 10) != 10){
        fprintf(stderr, "buf1 write error..");
        exit(1);
    }

    if(lseek(fd, 16384, SEEK_SET) == -1){
        /* offset now = 16384 */
        fprintf(stderr, "lseek_error..");
        exit(1);
    }

    if(write(fd, buf2, 10) != 10){
        /* offset now = 16394 */
        fprintf(stderr, "buf2 write error..");
        exit(1);
    }

    exit(0);
}

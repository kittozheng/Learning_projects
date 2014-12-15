/****************************************************************
     > File Name:test.c
     > Author:
     > Mail:
     > Created Time:2014年12月11日 星期四 23时41分50秒
****************************************************************/

#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

#define MYFILE "missing.txt"

main(){
    /*
    * Catch error when no file exists  
    */
    FILE *fin;

    fin = fopen(MYFILE, "r");

    if(fin == (FILE *)NULL){
        printf("%s: %s\n", MYFILE, strerror(errno));
        exit(-1);
    }

    fclose(fin);
    
}



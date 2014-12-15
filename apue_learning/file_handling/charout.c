/****************************************************************
     > File Name:charout.c
     > Author:
     > Mail:
     > Created Time:2014年12月11日 星期四 23时51分06秒
****************************************************************/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int
main(){

    int i;
    FILE *fout;

    const char string[] = {"This\r \nis a test\r\nfile.\r\n\0"};

    fout = fopen("inpfile.txt", "w");

    if(fout == (FILE *)NULL)
        exit(-1);
    
    i = 0;
    while(string[i] != NULL){
        fputc((int)string[i], fout);
        i++;
    }

    fclose(fout);

    return 0;

}

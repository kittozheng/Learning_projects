## File Handling

File Handling in GNU/Linux

### File Handling API

#### Create A File Handle

#inlcude <stdio.h>
FILE *fp;

#### Opening A File

File *fopen(const char *filename,const char *mode);

mode={'r', 'w', 'a', 'rw'}

#### Reading and Writing Data

##### Character interface

int fputc(int c, FILE *stream);
int fgetc(FILE *stream);





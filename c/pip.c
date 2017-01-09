#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// pipe use two elements array p[2]
// p[0] for read 
// p[1] for write

int main(){
    int p[2];
    pipe(p);
    write(p[1],"HelloWorld",10);
    close(p[1]);
    char buf[128];
    memset(buf,'\0',128);
    int ret=-1;
    ret=read(p[0],buf,128);
    printf("buf=%s\n",buf);
}

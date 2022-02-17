#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    //declare variables
	char tag[10];
    int length,check;

    //read user input (tag)
    scanf("%s",&tag);

    //checks if third value is a vowel and even numbers
    if(tag[2] == 'A' || tag[2] == 'E' || tag[2] == 'I' || tag[2] == 'O' || tag[2] == 'U' || tag[2] == 'Y'
    || (tag[0] + tag[1]) % 2 != 0 || (tag[3] + tag[4]) % 2 != 0 || (tag[4] + tag[5]) % 2 != 0 || (tag[7] + tag[8]) % 2 !=0){
        printf("invalid");
    }

    else{
        printf("valid");
    }
    return 0;
}
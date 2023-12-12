#include <stdio.h>
#include <string.h>

init_str(char str[])
{
    strcpy(str, "ciao");
    return 0;
}

int main(int argc, char const *argv[])
{
    char str1[5];
    char str2[5];

    init_str(str1);
    printf("%s\n", str1);
    gets(str2);
    int valid = 0;
    if (strncmp(str1, str2, 5) == 0)
        valid = 1;
    printf("buffer1: str1(%s), str2(%s), valid(%d)\n", str1, str2, valid);

    return 0;
}

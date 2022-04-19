#include <stdio.h>

int main() {
    int my_list[2][2];

    my_list[0][1] = 2;
    my_list[1][0] = 3;
    my_list[0][0] = 1;
    my_list[1][1] = 4;

    for(int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++){
            // my_list[i][j] = 1;
            printf("%d", my_list[i][j]);
        }
        printf("\n");
    }

    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main() {
    int number = 14, temp, unit, temp_unit, copy_temp, copy_num, find=0;
    temp = number;
    while(1) {
        temp++;
        copy_num = number;
        find = 0;
        while (copy_num != 0) {
            unit = copy_num%10;
            copy_num = (copy_num - unit) / 10;
            copy_temp = temp;
            while (copy_temp != 0) {
                temp_unit = copy_temp % 10;
                copy_temp = (copy_temp - temp_unit) / 10;
                if (unit == temp_unit) {
                    find = 1;
                    break;
                }
            }
            if (find == 1) {
                break;
            }
        }
        if (find==0) {
            printf("\n%d is the number for %d!\n", temp, number);
            break;
        }
    }
    return 0;
}
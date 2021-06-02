# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# void printArea(int num);
 
# int main() {
#     int num;
#     scanf("%d", &num);
#     printArea(num);
 
#     return 0;
# }
 
# void printArea(int num) {
#     printf("%0.2f\n", 3.14 * num * num);
# }
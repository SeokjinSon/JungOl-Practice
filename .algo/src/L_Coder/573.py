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
#     int value = 1;
#     for (int i = 0; i < num; i++) {
#         for (int l = 0; l < num; l++)
#             printf("%d ", value++);
#         printf("\n");
#     }
# }
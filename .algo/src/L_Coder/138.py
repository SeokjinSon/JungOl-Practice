# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int number;
#     scanf("%d", &number);
 
#     for (int i = 1; i <= number; i++) {
#         for (int l = 1; l <= number; l++)
#             printf("(%d, %d) ", i, l);
#         printf("\n");
#     }
 
#     return 0;
# }
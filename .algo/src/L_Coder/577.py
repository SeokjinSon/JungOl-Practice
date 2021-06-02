# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# #include <stdlib.h>
 
# void printResult(int* num1, int* num2);
 
# int main() {
#     int num1, num2;
 
#     scanf("%d %d", &num1, &num2);
#     printResult(&num1, &num2);
#     printf("%d %d\n", num1, num2);
 
#     return 0;
# }
 
# void printResult(int* num1, int* num2) {
#     if (*num1 > *num2) {
#         *num1 /= 2;
#         *num2 *= 2;
#     }
#     else {
#         *num2 /= 2;
#         *num1 *= 2;
#     }
# }
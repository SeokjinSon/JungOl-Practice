# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# #include <stdlib.h>
 
# int printValue(int num1, int num2);
 
# int main() {
#     int num1, num2, result;
 
#     scanf("%d %d", &num1, &num2);
#     printf("%d\n", printValue(num1, num2));
 
#     return 0;
# }
 
# int printValue(int num1, int num2) {
#     int result = 1;
 
#     for (int i = 0; i < num2; i++)
#         result *= num1;
 
#     return result;
# }
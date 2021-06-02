# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# #include <stdlib.h>
 
# void printResult(int num1, int num2, char ch);
 
# int main() {
#     int num1, num2;
#     char ch;
 
#     scanf("%d %c %d", &num1, &ch, &num2);
#     printResult(num1, num2, ch);
 
#     return 0;
# }
 
# void printResult(int num1, int num2, char ch) {
#     if (ch == '+')
#         printf("%d + %d = %d\n", num1, num2, num1 + num2);
#     else if(ch == '-')
#         printf("%d - %d = %d\n", num1, num2, num1 - num2);
#     else if (ch == '*')
#         printf("%d * %d = %d\n", num1, num2, num1 * num2);
#     else if (ch == '/')
#         printf("%d / %d = %d\n", num1, num2, num1 / num2);
#     else
#         printf("%d %c %d = 0\n", num1, ch, num2);
# }
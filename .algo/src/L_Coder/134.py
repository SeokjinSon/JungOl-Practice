# C Code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int number = 0;
#     int even = 0, odd = 0;
#     for (int i = 0; i < 10; i++) {
#         scanf("%d", &number);
#         if (number % 2 == 0)
#             even++;
#         else
#             odd++;
#     }
#     printf("even : %d\n", even);
#     printf("odd : %d\n", odd);
 
#     return 0;
# }
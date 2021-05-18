# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int arr[10] = { 0, };
#     int sum1 = 0; // 짝수
#     int sum2 = 0; // 홀수
 
#     for (int i = 0; i < 10; i++) {
#         scanf("%d", &arr[i]);
#         if ((i + 1) % 2 != 0) // 홀수 번째
#             sum2 += arr[i];
#         else
#             sum1 += arr[i];
#     }
 
#     printf("odd : %d\n", sum2);
#     printf("even : %d\n", sum1);
 
#     return 0;
# }
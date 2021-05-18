# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int N, mid;
 
#     scanf("%d", &N);
#     if (N > 100 || N < 0 || (N % 2 == 0)) {
#         printf("INPUT ERROR!\n");
#         return;
#     }
 
#     mid = N / 2;
#     for (int i = 0; i < N; i++) {
#         if (i <= mid) {
#             for (int l = 0; l < i; l++)
#                 printf(" ");
#             for (int k = 0; k < i * 2 + 1; k++)
#                 printf("*");
#             printf("\n");
#         }
#         else {
#             for (int l = i; l < N-1; l++)
#                 printf(" ");
#             for (int k = 0; k < 2 * (N - i) - 1; k++)
#                 printf("*");
#             printf("\n");
#         }
#     }
 
#     return 0;
# }
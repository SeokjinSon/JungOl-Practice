# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int n1, n2;
 
#     scanf("%d %d", &n1, &n2);
 
#     if (n1 < n2) {
#         for (int i = 1; i <= 9; i++) {
#             for (int l = n1; l <= n2; l++) {
#                 printf("%d * %d = %2d   ", l, i, i * l);
#             }
#             printf("\n");
#         }
#     }
#     else {
#         for (int i = 1; i <= 9; i++) {
#             for (int l = n1; l >= n2; l--) {
#                 printf("%d * %d = %2d   ", l, i, i * l);
#             }
#             printf("\n");
#         }
#     }
 
#     return 0;
# }
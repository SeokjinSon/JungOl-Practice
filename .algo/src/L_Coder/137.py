# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int n1, n2, value;
#     scanf("%d %d", &n1, &n2);
 
#     for (int i = 1; i <= n1; i++) {
#         value = 0;
#         for (int l = 0; l < n2; l++) {
#             value += i;
#             printf("%d ", value);
#         }
#         printf("\n");
#     }
 
#     return 0;
# }
# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int arr[5] = { 0, };
#     int sum = 0;
 
#     for (int i = 0; i < 5; i++) {
#         scanf("%d", &arr[i]);
#         if ((i + 1) % 2 != 0)
#             sum += arr[i];
#     }
 
#     printf("%d\n", sum);
 
#     return 0;
# }
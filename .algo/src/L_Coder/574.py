# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# #include <stdlib.h>
 
# int printArea(int* arr);
 
# int main() {
#     int* arr = (int)malloc(sizeof(int) * 3);
#     int max;
 
#     for (int i = 0; i < 3; i++)
#         scanf("%d", &arr[i]);
#     printf("%d\n", printArea(arr));
 
#     return 0;
# }
 
# int printArea(int* arr) {
#     int max = arr[0];
 
#     for (int i =1; i < 3; i++) {
#         if (arr[i] > max)
#             max = arr[i];
#     }
#     return max;
# }
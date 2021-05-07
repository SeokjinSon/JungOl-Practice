# C Code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int number, sum=0;
#     double avg;
#     int* arr;
#     scanf("%d", &number);
#     arr = (int)malloc(sizeof(int) * number);
 
#     for (int i = 0; i < number; i++) {
#         scanf("%d", &arr[i]);
#         sum += arr[i];
#     }
 
#     avg = (double)sum / number;
#     printf("%0.2f\n", avg);
 
#     return 0;
# }
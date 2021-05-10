# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int N, K, cnt=0;
#     int* arr;
#     scanf("%d %d", &N, &K);
#     arr = (int)malloc(sizeof(int) * N);
 
#     for (int i = 1; i <= N; i++) {
#         if (N % i == 0)
#             arr[cnt++] = i;
#     }
 
#     if (cnt < K)
#         printf("0\n");
#     else
#         printf("%d\n", arr[K - 1]);
 
#     return 0;
# }
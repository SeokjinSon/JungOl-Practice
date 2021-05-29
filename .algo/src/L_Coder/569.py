# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     // 사용할 배열 초기화
#     int** arr = (int**)malloc(sizeof(int*) * 5);
#     int cnt = 0, sum = 0;
 
#     for (int i = 0; i < 5; i++)
#         arr[i] = (int*)malloc(sizeof(int) * 4);
 
#     for (int i = 0; i < 5; i++) {
#         for (int l = 0; l < 4; l++)
#             scanf("%d", &arr[i][l]);
#     }
 
#     // 최종 출력
#     for (int i = 0; i < 5; i++) {
#         sum = 0;
#         for (int l = 0; l < 4; l++)
#             sum += arr[i][l];
#         if (((double)sum / 4) >= 80) {
#             printf("pass\n");
#             cnt++;
#         }
#         else
#             printf("fail\n");
#     }
#     printf("Successful : %d\n", cnt);
#     return 0;
# }
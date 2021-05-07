# C Code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
 
# int main() {
#     int n1, n2, sum=0, cnt=0;
#     scanf("%d %d", &n1, &n2);
 
#     if (n1 < n2) {
#         for (int i = n1; i <= n2; i++) {
#             if ((i % 3 == 0) || (i % 5 == 0)) {
#                 sum += i;
#                 cnt++;
#             }
#         }
#     }
#     else {
#         for (int i = n1; i >= n2; i--) {
#             if ((i % 3 == 0) || (i % 5 == 0)) {
#                 sum += i;
#                 cnt++;
#             }
#         }
#     }
 
     
#     printf("sum : %d\n", sum);
#     printf("avg : %0.1f\n", (double)sum/cnt);
 
#     return 0;
# }
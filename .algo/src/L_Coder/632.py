# C Code

# #include <stdio.h>
 
# int main() {
#     int num1, num2, num3, min;
#     scanf("%d %d %d" ,&num1, &num2, &num3);
 
#     min = (num1<num2 ? num1:num2);
#     min = (min<num3 ? min:num3);
 
#     printf("%d\n", min);
#     return 0;
# }
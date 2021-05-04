# C code

# #include <stdio.h>

# int main() {
#   int input, odd=0, even=0;
#   while(1) {
#     scanf("%d", &input);
#     if(input==0) {
#       printf("odd : %d\n", odd);
#       printf("even : %d\n", even);
#       break;
#     }
#     if(input%2==0)
#       even++;
#     else
#       odd++;
#   }
#   return 0;
# }
# C Code

# #include <stdio.h>

# int main() {
#   int input, count=0, sum=0;
#   while(1) {
#     scanf("%d", &input);
#     sum+=input;
#     count++;
#     if(input>=100) {
#       printf("%d\n", sum);
#       printf("%0.1f\n", (double)sum/(double)count);
#       break;
#     }
#   }
#   return 0;
# }
# C code

# #include <stdio.h>

# int main() {
#   int input, sum=0, count=0;

#   while(1) {
#     scanf("%d", &input);
    
#     if(input<0 || input>100) {
#       printf("sum : %d\n", sum);
#       printf("avg : %0.1f\n", (double)sum/(double)count);
#       break;
#     }
#     sum+=input;
#     count++;
#   }
  
#   return 0;
# }
# C Code

# #include <stdio.h>
 
# int main() {
#   int input, count=0;
 
#   while(1) {
#     scanf("%d", &input);
 
#     if(input==0) {
#       printf("%d\n", count);
#       break;
#     }
#     if(input%3!=0 && input%5!=0)
#       count++;
#   }
   
#   return 0;
# }
# C Code

# #include <stdio.h>

# int main() {
#   double weight;
#   scanf("%lf", &weight);

#   if(weight<=50.80) 
#     printf("Flyweight\n");
#   else if(weight>50.80 && weight<=61.23)
#     printf("Lightweight\n");
#   else if(weight>61.23 && weight<=72.57)
#     printf("Middleweight\n");  
#   else if(weight>72.57 && weight<=88.45)
#     printf("Cruiserweight\n");
#   else if(weight>88.45)
#     printf("Heavyweight\n");

#   return 0;
# }
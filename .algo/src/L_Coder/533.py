# C Code

# #include <stdio.h>

# int main() {
#   char gender;
#   int age;
#   scanf("%c %d", &gender, &age);

#   if(age>=18) {
#     if(gender == 'M')
#       printf("MAN\n");
#     else
#       printf("WOMAN\n");
#   } else {
#     if(gender == 'M')
#       printf("BOY\n");
#     else
#       printf("GIRL\n");
#   }
  
#   return 0;
# }
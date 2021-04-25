### c언어 코드 ###
# include <stdio.h>
# include <stdlib.h>

# int main() {
#   int input;
#   int start=1;
#   int** m;
#   scanf("%d", &input);
#   m = malloc(sizeof(int*)*input);

#   for(int i=0; i<input; i++)
#     m[i] = malloc(sizeof(int)*input);

#   for(int i=0; i<input; i++) {
#     for(int l=0; l<input; l++) {
#       m[l][i] = start;
#       start++;
#     }
#   }

#   for(int i=0; i<input; i++) {
#     for(int l=0; l<input; l++)
#       printf("%d ", m[i][l]);
#     printf("\n");
#   }
#   return 0;
# }
  
# C code

# #include <stdio.h>
# #include <stdlib.h>

# int main() {
#   int N, ch, idx;
#   int** triangle;

#   scanf("%d", &N);
#   triangle = (int**)malloc(sizeof(int*)*N);

#   for(int i=0; i<N; i++)
#     triangle[i] = (int*)malloc(sizeof(int)*N);

#   for(int i=0; i<N; i++) {
#     for(int l=0; l<N; l++)
#       triangle[i][l] = ' ';
#   }

#   ch = 'A';

#   for(int i=0; i<N; i++) {
#     idx=N-1;
#     for(int l=i; l<N; l++) {
#       if(ch > 'Z')
#         ch = 'A';
#       triangle[l][idx] = ch++;
#       idx=idx-1;
#     }
#   }

#   for(int i=0; i<N; i++) {
#     for(int l=0; l<N; l++)
#       printf("%c ", triangle[i][l]);
#     printf("\n");
#   }
  
#   return 0;
# }
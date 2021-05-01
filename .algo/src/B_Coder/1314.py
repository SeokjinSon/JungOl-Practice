# C code

# #include <stdio.h>
# #include <stdlib.h>
 
# int main() {
#   int n, k=0;
#   char result = 'A';
#   scanf("%d", &n);
#   char** sqr = (char**)malloc(sizeof(char*)*n);
 
#   for(int i=0; i<n; i++)
#     sqr[i] = (char*)malloc(sizeof(char)*n);
 
#   for(int i=0; i<n; i++) {
#     if(k==0) {
#       for(int l=k; l<n; l++) {
#         if(result > 'Z')
#           result = 'A';
#         sqr[l][i] = result;
#         k++;
#         result++;
#       }
#     } else {
#       for(int l = k-1; l>=0; l--) {
#         if(result > 'Z')
#           result = 'A';
#         sqr[l][i] = result;
#         k--;
#         result++;
#       }
#     }
     
#   }
 
#   for(int i=0; i<n; i++) {
#     for(int l=0; l<n; l++)
#       printf("%c ", sqr[i][l]);
#     printf("\n");
#   }  
 
#   return 0;
# }
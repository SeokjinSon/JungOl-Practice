# C code

# #include <stdio.h>
# #include <stdlib.h>

# int main() {
#   int n, m;
#   int start=1;
#   scanf("%d %d", &n, &m);
    
#   int** arr = (int**)malloc(sizeof(int*)*n);
#   for(int i=0; i<n; i++)
#     arr[i] = (int*)malloc(sizeof(int)*n);

#   switch(m){
#     start=1;
#     case 1:
#       for(int i=0; i<n; i++) {
#         for(int l=0; l<n; l++)
#           printf("%d ", start);
#         start++;
#         printf("\n");
#       }
#       break;
#     case 2:
#       for(int i=0; i<n; i++) {
#         if(i%2==0) {
#           for(int l=0; l<n; l++) {
#             arr[i][l]=start;
#             start++;
#           }
#         }
#         else {
#           for(int l=0; l<n; l++) {
#             start--;
#             arr[i][l]=start;
#           }
#         }    
#       }
#       for(int i=0; i<n; i++) {
#         for(int l=0; l<n; l++)
#           printf("%d ", arr[i][l]);
#         printf("\n");
#       }
#       break;
#     case 3:
#       for(int i=0; i<n; i++) {
#         for(int l=0; l<n; l++) {
#           if(l==0)
#             arr[i][l] = start;
#           else
#             arr[i][l] = arr[i][l-1] + start;
#         }
#         start++;
#       }
#       for(int i=0; i<n; i++) {
#         for(int l=0; l<n; l++)
#           printf("%d ", arr[i][l]);
#         printf("\n");
#       }
#       break;
#   }
#   return 0;
# }
  
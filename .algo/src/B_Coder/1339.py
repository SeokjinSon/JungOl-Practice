# C Code(N의 홀수 조건은 했지만 1보다 작거나 100보다 큰 조건은 안 적용해서 에러 계속 났음)

# #include <stdio.h>
# #include <stdlib.h>

# int main() {
#     int N, input, seq, seq2;
#     scanf("%d", &N);

#     if(N%2==0 || N<1 || N>100) {
#       printf("INPUT ERROR\n");
#       return 0;
#     }
      
#     int** arr = (int**)malloc(sizeof(int*)*N);

#     for(int i=0; i<N; i++)
#       arr[i] = (int*)malloc(sizeof(int)*N);

#     for(int i=0; i<N; i++) {
#       for(int l=0; l<N; l++)
#         arr[i][l] = 32;
#     }

#     seq=1;
#     input=65;
#     for(int i=N/2; i>=0; i--) {
#       seq2 = i;
#       for(int l=0; l<seq; l++) {
#         if(input>'Z')
#           input=65;
#         arr[seq2][i] = input++;
#         seq2++;
#       }
#       seq+=2;
#     }
  
#     for(int i=0; i<N; i++) {
#       for(int l=0; l<N; l++)
#         printf("%c ", arr[i][l]);
#       printf("\n");
#     }
  
#     return 0;
# }
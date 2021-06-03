# Java code

# import java.util.Scanner;
 
# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         int num = sc.nextInt();
#         int[][] arr = new int[num][num];
#         int row, col, value=2;
         
#         arr[0][0]=1;
#         for(int i=1; i<num*2-1; i++) { // 1 2 3 4 5 6 7 8
#             if(i<num) {
#                 // 홀수(위로)
#                 if(i%2!=0) {
#                     row=i;
#                     col=0;
#                     while(row>=0) {
#                         arr[row--][col++] = value;
#                         value++;
#                     }
#                 } else {
#                     // 짝수(아래로)
#                     row=0;
#                     col=i;
#                     while(col>=0) {
#                         arr[row++][col--] = value;
#                         value++;
#                     }
#                 }               
#             } else {
#                 // 홀수(위로)
#                 if(i%2!=0) {
#                     row=num-1;
#                     col=i-num+1;
#                     while(col<num) {
#                         arr[row--][col++] = value;
#                         value++;
#                     }
#                 } else {
#                     // 짝수(아래로)
#                     row=i-num+1;
#                     col=num-1;
#                     while(row<num) {
#                         arr[row++][col--] = value;
#                         value++;
#                     }
#                 }   
#             }
#         }       
         
#         for(int i=0; i<num; i++) {
#             for(int l=0; l<num; l++)
#                 System.out.print(arr[i][l] + " ");
#             System.out.println();
#         }
#     }
# }
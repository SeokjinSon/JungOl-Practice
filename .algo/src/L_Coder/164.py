# Java code

# import java.util.Scanner;
 
# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         int[][] arr = new int[4][3];
#         int[] sum = new int[4];
         
#         for(int i=0; i<4; i++) {
#             System.out.printf("%dclass? ", i+1);
#             for(int l=0; l<3; l++) {
#                 arr[i][l] = sc.nextInt();
#                 sum[i]+=arr[i][l];
#             }
#         }
         
#         for(int i=0; i<4; i++)
#             System.out.printf("%dclass : %d\n", i+1, sum[i]);
#     }
# }
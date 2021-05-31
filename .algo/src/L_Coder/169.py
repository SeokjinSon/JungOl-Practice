# Java code

# import java.util.Scanner;
 
# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         char[][] arr = new char[3][5];
         
#         for(int i=0; i<3; i++) {
#             for(int l=0; l<5; l++) {
#                 arr[i][l] = sc.next().charAt(0);
#             }
#         }
#         for(int i=0; i<3; i++) {
#             for(int l=0; l<5; l++)
#                 System.out.printf("%c ", arr[i][l]+32);
#             System.out.println();
#         }
#     }
# }
# Java code

# import java.util.Scanner;
 
# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         int num = sc.nextInt();
#         printNum(num);
#     }
#     public static void printNum(int num) {
#         for(int i=1; i<=num; i++) {
#             for(int l=1; l<=num; l++)
#                 System.out.print(i*l + " ");
#             System.out.println();
#         }
#     }
# }
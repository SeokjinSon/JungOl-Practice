# Java code

# import java.util.Scanner;
 
# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         int num1 = sc.nextInt();
#         int num2 = sc.nextInt();
#         System.out.println(printNum(num1, num2));  
#     }
#     public static int printNum(int num1, int num2) {
#         int big, small;
#         if(num1<num2) {
#             big=num2;
#             small=num1;
#         } else {
#             big=num1;
#             small=num2;
#         }
         
#         return (big*big)-(small*small);
#     }
# }
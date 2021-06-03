# Java code

# import java.util.Scanner;
 
# public class Main {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         int num = sc.nextInt();
#         System.out.println(printSum(num));
#     }
#     public static int printSum(int num) {
#         int sum = 0;
#         for(int i=1; i<=num; i++)
#             sum+=i;
#         return sum;
#     }
# }
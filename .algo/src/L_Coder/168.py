# Java code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int num = sc.nextInt();
		
# 		int[][] arr = new int[num][num];
		
# 		for(int i=0; i<num; i++) {
# 			for(int l=0; l<num; l++)
# 				arr[i][l] = 1;
# 		}
# 		for(int i=2; i<num; i++) {
# 			for(int l=1; l<i; l++) 
# 				arr[i][l] = arr[i-1][l-1] + arr[i-1][l];
# 		}
# 		for(int i=num-1; i>=0; i--) {
# 			for(int l=0; l<=i; l++)
# 				System.out.print(arr[i][l] + " ");
# 			System.out.println();
# 		}
# 	}
# }
# Java Code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int[][] arr = new int[4][2];
# 		int sum=0;
		
# 		for(int i=0; i<4; i++) {
# 			for(int l=0; l<2; l++)
# 				arr[i][l] = sc.nextInt();
# 		}
		
# 		for(int i=0; i<4; i++) {
# 			sum = sum + arr[i][0] + arr[i][1];
# 			System.out.print((arr[i][0] + arr[i][1])/2 + " ");
# 		}
# 		System.out.println();
# 		for(int i=0; i<2; i++)
# 			System.out.print((arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i])/4 + " ");
# 		System.out.println();
# 		System.out.println(sum/8);
# 	}
# }
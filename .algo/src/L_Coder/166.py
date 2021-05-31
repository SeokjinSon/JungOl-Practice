# Java code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int[][] arr1 = new int[2][3];
# 		int[][] arr2 = new int[2][3];
# 		int[][] arr3 = new int[2][3];

# 		System.out.println("first array");
# 		for(int i=0; i<2; i++) {
# 			for(int l=0; l<3; l++)
# 				arr1[i][l] = sc.nextInt();
# 		}
# 		System.out.println("second array");
# 		for(int i=0; i<2; i++) {
# 			for(int l=0; l<3; l++)
# 				arr2[i][l] = sc.nextInt();
# 		}
		
# 		for(int i=0; i<2; i++) {
# 			for(int l=0; l<3; l++)
# 				arr3[i][l] = arr1[i][l]*arr2[i][l];
# 		}
# 		for(int i=0; i<2; i++) {
# 			for(int l=0; l<3; l++)
# 				System.out.print(arr3[i][l] + " ");
# 			System.out.println();
# 		}		
# 	}
# }
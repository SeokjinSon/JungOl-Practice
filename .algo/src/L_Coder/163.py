# Java code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		int sum=0;
# 		int[][] arr = {
# 				{3, 5, 9}, 
# 				{2, 11, 5}, 
# 				{8, 30, 10}, 
# 				{22, 5, 1}
# 		};
# 		for(int i=0; i<4; i++) {
# 			for(int l=0; l<3; l++)
# 				sum+=arr[i][l];
# 		}
# 		for(int i=0; i<4; i++) {
# 			for(int l=0; l<3; l++)
# 				System.out.print(arr[i][l] + " ");
# 			System.out.println();
# 		}
# 		System.out.println(sum);
# 	}
# }
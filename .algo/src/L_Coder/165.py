# Java Code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int[][] arr = new int[5][5];
		
# 		arr[0][0]=1;
# 		arr[0][2]=1;
# 		arr[0][4]=1;
		
# 		for(int i=1; i<5; i++) {
# 			for(int l=0; l<5; l++) {
# 				if(l==0)
# 					arr[i][l] = arr[i-1][l+1];
# 				else if(l==4)
# 					arr[i][l] = arr[i-1][l-1];
# 				else
# 					arr[i][l] = arr[i-1][l-1] + arr[i-1][l+1];
# 			}
# 		}
# 		for(int i=0; i<5; i++) {
# 			for(int l=0; l<5; l++)
# 				System.out.print(arr[i][l] + " ");
# 			System.out.println();
# 		}	
# 	}
# }
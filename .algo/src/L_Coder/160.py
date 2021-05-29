# Java code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int[] arr = new int[6];
# 		int num=0;
		
# 		for(int i=0; i<10; i++) {
# 			num = sc.nextInt();
# 			arr[num-1]++;
# 		}
# 		for(int i=0; i<6; i++ )
# 			System.out.printf("%d : %d\n", i+1, arr[i]);
# 	}
# }
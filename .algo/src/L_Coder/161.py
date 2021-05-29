# Java code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int[] arr = new int[11];
# 		int num=0;
		
# 		while(true) {
# 			num = sc.nextInt();
# 			if(num==0)
# 				break;
# 			else
# 				arr[num/10]++;
# 		}
# 		for(int i=arr.length-1; i>=0; i--) {
# 			if(arr[i]!=0)
# 				System.out.printf("%d : %d person\n", i*10, arr[i]);
# 		}
# 	}
# }
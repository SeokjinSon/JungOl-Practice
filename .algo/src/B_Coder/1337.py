
# Java code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int num = sc.nextInt();
# 		int row = 0, col = 0, val = 0;
# 		int[][] arr = new int[num][num];
# 		int swp = num;
		
# 		for(int i=0; i<num; i++) {
# 			for(int l=0; l<num; l++)
# 				arr[i][l] = -1;
# 		}
		
# 		int hei = (int) Math.pow(num, 2) + (int) Math.pow(num, 2);
# 		int cnt = (int)(Math.sqrt(hei)/2);
		
# 		for(int idx=0; idx<cnt; idx++) {
# 			for(int i=0; i<num; i++) {
# 				if(val>9)
# 					val = 0;
# 				if(arr[row][col]==-1) {
# 					arr[row++][col++] = val;
# 					val++;
# 				} else
# 					break;
# 			}
# 			row--;
# 			col=col-2;
# 			num--;
# 			for(int i=0; i<num; i++) {
# 				if(val>9)
# 					val = 0;
# 				if(arr[row][col]==-1) {
# 					arr[row][col--] = val;
# 					val++;
# 				} else
# 					break;
# 			}
# 			col++;
# 			row--;
# 			num--;
# 			for(int i=0; i<num; i++) {
# 				if(val>9)
# 					val = 0;
# 				if(arr[row][col]==-1) {
# 					arr[row--][col] = val;
# 					val++;
# 				}
					
# 				else
# 					break;
# 			}
# 			row=row+2;
# 			col++;
# 		}
# 		for(int i=0; i<swp; i++) {
# 			for(int l=0; l<=i; l++)
# 				System.out.print(arr[i][l] + " ");
# 			System.out.println();
# 		}
# 	}
# }
# Java code

# import java.util.Scanner;

# public class Main {
# 	public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int num = sc.nextInt();
# 		int len = num*2-1;
# 		int center = num-1;
# 		int col = center;
# 		int row = 0;
# 		char ch = 'A';
# 		int swp = num;
# 		char[][] arr = new char[len][len];
		
# 		for(int i=0; i<len; i++) {
# 			for(int l=0; l<len; l++)
# 				arr[i][l] = ch;
# 		}
		
# 		for(int i=0; i<swp; i++) {
# 			for(int l=0; l<num; l++) {
# 				if(ch>'Z')
# 					ch = 'A';
# 				arr[row++][col--] = ch;
# 				ch++;
# 			}
# 			col+=2;
			
# 			for(int l=0; l<num-1; l++) {
# 				if(ch>'Z')
# 					ch = 'A';
# 				arr[row++][col++] = ch;
# 				ch++;
# 			}
# 			row-=2;
			
# 			for(int l=0; l<num-1; l++) {
# 				if(ch>'Z')
# 					ch = 'A';
# 				arr[row--][col++] = ch;
# 				ch++;
# 			}
# 			col-=2;
			
# 			for(int l=0; l<num-2; l++) {
# 				if(ch>'Z')
# 					ch = 'A';
# 				arr[row--][col--] = ch;
# 				ch++;
# 			}
# 			row+=1;						
# 			num--;
# 		}
			
# 		for(int i=0; i<swp; i++) {
# 			for(int k=0; k<center-i; k++)
# 				System.out.print("  ");
# 			for(int l=center-i; l<=center+i; l++)
# 				System.out.print(arr[i][l] + " ");
# 			System.out.println();
# 		}
		
# 		for(int i=len-center; i>1; i--) {
# 			for(int k=0; k<=center-i+1; k++)
# 				System.out.print("  ");			
# 			for(int l=center-i+2; l<center+i-1; l++)
# 				System.out.print(arr[len-i+1][l] + " ");
# 			System.out.println();
# 		}	
# 	}
# }
# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# void recur(int n1, int n2) {
# 	printf("%d ", n1 - n2);
# 	if (n1 - n2 < 0)
# 		return;
# 	recur(n2, n1 - n2);
# }

# int main() {
# 	int num1 = 100;
# 	int num2;

# 	scanf("%d", &num2);

# 	printf("%d %d ", num1, num2);
# 	recur(num1, num2);
	
# 	return 0;
# }
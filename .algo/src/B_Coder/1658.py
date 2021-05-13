# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() { 
# 	int n1, n2, gcd=1, lcm=1, min;

# 	scanf("%d %d", &n1, &n2);

# 	if (n1 < n2)
# 		min = n1;
# 	else
# 		min = n2;

# 	while(1) {

# 		for (int i = 2; i <= min; i++) {
# 			if (n1 % i == 0 && n2 % i == 0) { // 나누어 떨어짐
# 				gcd*=i;
# 				lcm*=i;
# 				n1/=i;
# 				n2/=i;
# 				break;
# 			}
# 			else { 
# 				if (i == min) {
# 					printf("%d\n", gcd);
# 					printf("%d\n", lcm*n1*n2);
# 					return;
# 				}
# 			}
# 		}
# 	}
# 	return 0;
# }
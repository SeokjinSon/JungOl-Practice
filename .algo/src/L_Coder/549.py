# C Code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, sum = 0, cnt = 0;
# 	scanf("%d", &n);

# 	for (int i = 1; i <= n; i++) {
# 		if (i % 2 != 0) {
# 			if (sum >= n) {
# 				printf("%d %d\n", cnt, sum);
# 				break;
# 			}
# 			else {
# 				cnt++;
# 				sum += i;
# 			}
# 		}
# 	}

# 	return 0;
# }
# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int arr[26] = { 0, };
# 	char ch;
# 	int startCh = 65;

# 	while (1) {
# 		scanf(" %c", &ch);
# 		if (ch >= 'A' && ch <= 'Z')
# 			arr[ch % 'A']++;
# 		else
# 			break;
# 	}

# 	for (int i = 0; i < 26; i++) {
# 		if (arr[i] != 0) 
# 			printf("%c : %d\n", startCh, arr[i]);
# 		startCh++;
# 	}
	
# 	return 0;
# }
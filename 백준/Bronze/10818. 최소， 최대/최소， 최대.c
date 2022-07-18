#include <stdio.h>

int main(void) {
	int N;

	scanf("%d", &N);

	int x[1000000] = { 0 };

	for (int i = 0; i < N; i++)
		scanf("%d", &x[i]);

	int max = x[0], min = x[0];

	for (int i = 0; i < N; i++) {
		if (max < x[i]) max = x[i];
		if (min > x[i]) min = x[i];
	}

	printf("%d %d", min, max);

	return 0;
}
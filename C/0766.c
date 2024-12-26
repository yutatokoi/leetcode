#include <stdio.h>

bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    for (int i = 0; i < matrixSize; i++) {
        int r = i, c = 0;
        int val = matrix[r][c];
        r++, c++;

        while (r < matrixSize && c < *matrixColSize) {
            if (matrix[r][c] != val) {
                return 0;
            }
            r++, c++;
        }
    }

    for (int i = 0; i < *matrixColSize; i++) {
        int r = 0, c = i;
        printf("c = %d\n", c);
        int val = matrix[r][c];
        r++, c++;

        while (r < matrixSize && c < *matrixColSize) {
            if (matrix[r][c] != val) {
                return 0;
            }
            r++, c++;
        }
    }

    return 1;
}

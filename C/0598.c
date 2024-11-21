int min(int a, int b);

int maxCount(int m, int n, int** ops, int opsSize, int* opsColSize) {
    for (int i = 0; i < opsSize; i++) {
        int *op = ops[i];
        m = min(m, op[0]);
        n = min(n, op[1]);
    }

    return m * n;
}

int min(int a, int b) {
    if (a < b) {
        return a;
    }

    return b;
}

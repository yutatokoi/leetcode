int arrangeCoins(int n) {
    int rows = 0, i = 1;

    while (n >= i) {
        n -= i;
        i++;
        rows++;
    }

    return rows;
}

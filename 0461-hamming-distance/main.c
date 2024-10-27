int hammingDistance(int x, int y) {
    int distance = 0, xor = x ^ y;

    while (xor) {
        int remainder = xor % 2;
        if (remainder == 1) {
            distance++;
        }
        xor /= 2;
    }

    return distance;
}

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int count = 0;

    for (int i = 0; i < flowerbedSize; i++) {
        if (flowerbed[i] == 0) {
            int empty_left = (i == 0) || (flowerbed[i-1] == 0);
            int empty_right = (i == flowerbedSize - 1) || (flowerbed[i+1] == 0);

            if (empty_left && empty_right) {
                flowerbed[i] = 1;
                if (++count >= n) return 1;
            }
        }
    }

    return count >= n;
}

bool judgeCircle(char* moves) {
    int x = 0, y = 0;
    int len = strlen(moves);

    for (int i = 0; i < len; i++) {
        if (moves[i] == 'U') {
            y++;
        } else if (moves[i] == 'D') {
            y--;
        } else if (moves[i] == 'R') {
            x++;
        } else {
            x--;
        }
    }

    return (x == 0 && y == 0);
}

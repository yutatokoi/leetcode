// attempt1: naive recursive solution
int fib(int n){
    if (n == 0) return 0;
    if (n == 1) return 1;

    return fib(n - 1) + fib(n - 2);
}

// attempt2: DP (?) solution
int fib(int n){
    int numbers[31] = {0};
    numbers[1] = 1;

    for (int i = 2; i < n + 1; i++) numbers[i] = numbers[i-1] + numbers[i-2];

    return numbers[n];
}

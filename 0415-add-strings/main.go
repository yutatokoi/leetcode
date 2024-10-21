func addStrings(num1 string, num2 string) string {
    if len(num1) < len(num2) {
        num1, num2 = num2, num1
    }
    
    i1, i2 := len(num1) - 1, len(num2) - 1
    s := []byte{}
    remainder := 0
    
    for i1 >= 0 || i2 >= 0 {
        x1, x2 := 0, 0
        if i1 >= 0 {
            x1 = int(num1[i1] - '0')
        }
        
        if i2 >= 0 {
            x2 = int(num2[i2] - '0')
        }
        
        remainder += x1 + x2
        s  = append(s, byte(remainder % 10) + '0')
        remainder /= 10
        i1--
        i2--
    }

    if remainder > 0 {
        s = append(s, byte(remainder % 10) + '0')
    }

    for i, j := 0, len(s) - 1; i < j; i, j = i + 1, j - 1 {
        s[i], s[j] = s[j], s[i]
    }

    return string(s)
}

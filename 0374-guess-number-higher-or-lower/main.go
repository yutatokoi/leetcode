/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    left, right := 1, n
    mid := 0

    for (left <= right) {
        mid = (left + right) >> 1
        if g := guess(mid); g == -1 {
            right = mid - 1
        } else if g == 1 {
            left = mid + 1
        } else {
            break
        }
    }

    return mid
}

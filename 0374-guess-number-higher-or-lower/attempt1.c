/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

int guessNumber(int n){
	long long left = 0, right = n, mid;

    while (left <= right) {
        mid = (left + right) / 2;
        if (guess(mid) == -1) {
            right = mid - 1;
        } else if (guess(mid) == 1) {
            left = mid + 1;
        } else {
            break;
        }
    }

    return mid;
}

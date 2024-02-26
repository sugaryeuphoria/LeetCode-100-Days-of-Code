/*Reverse Integer */
public class Day58 {
    
    // Method declaration
    public int reverse(int x) {
// Initialize a long variable to store the reversed number
        long ans = 0;
// Iterate until the input number becomes 0
        while (x != 0) {

// Multiply the current reversed number by 10 and add the last digit of the input number
            ans = ans * 10 + x % 10; 
        }
    }
}

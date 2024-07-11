import java.util.Stack;

public class Day178 {
    public String reverseParentheses(String s) {
        // Stack to store the indices of the '(' characters
        Stack<Integer> stack = new Stack<>();
        char[] chars = s.toCharArray();
         // Traverse the string
         for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(') {
                 // Push the index of the '(' onto the stack
                 stack.push(i);
                } else if (chars[i] == ')') {
    }
}

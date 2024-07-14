/*726. Number of Atoms
 * Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
*/

import java.util.Stack;

public class Day179 {
    public String countOfAtoms(String formula) {
        // Initialize a StringBuffer to build a processed formula string
        StringBuffer sb = new StringBuffer();
        // Append the first character of the formula to sb
        sb.append(formula.charAt(0));
        // Store the first character as prevC
        char prevC = formula.charAt(0);
        // Get the length of the formula
        int length = formula.length();
         // Iterate through the formula starting from the second character
         for (int i = 1; i < length; i++) {
            // Get the current character
            char c = formula.charAt(i);
            // Check if current character is a lowercase letter or both current and previous are digits
            boolean flag = Character.isLowerCase(c) || (Character.isDigit(c) && Character.isDigit(prevC));
            // If flag is false, append a space before the current character
            if (!flag)
                sb.append(' ');
                // Append the current character
                sb.append(c);
                // Update prevC to the current character
                prevC = c;
         }
         // Split the processed string into array by spaces
        String[] array = sb.toString().split(" ");
        // Initialize a stack to process the elements
         Stack<String> stack = new Stack<String>();
         // Get the length of the array
         int arrayLength = array.length;
    }

}

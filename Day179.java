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

import java.util.Set;
import java.util.Stack;
import java.util.TreeMap;

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
         // Iterate through the array elements
        for (int i = 0; i < arrayLength; i++) {
            String str = array[i]; // Get the current string element
            
            if (str.equals(")")) { // If the current string is a closing parenthesis
                if (i < arrayLength - 1 && Character.isDigit(array[i + 1].charAt(0))) // Check if the next element is a digit
                    stack.push(str); // Push the closing parenthesis to the stack
                else { // If next element is not a digit
                    Stack<String> tempStack = new Stack<String>(); // Temporary stack to hold elements inside parentheses
                    while (!stack.peek().equals("(")) // Pop elements until an opening parenthesis is found
                        tempStack.push(stack.pop());
                    stack.pop(); // Pop the opening parenthesis
                    while (!tempStack.isEmpty()) // Push back elements from tempStack to the main stack
                        stack.push(tempStack.pop());
                }
            } else if (Character.isDigit(str.charAt(0))) { // If the current string is a digit
                int count = Integer.parseInt(str); // Convert the string to an integer count
                String prev = stack.pop(); // Pop the previous element from the stack
                
                if (prev.equals(")")) { // If the previous element is a closing parenthesis
                    Stack<String> tempStack = new Stack<String>(); // Temporary stack to hold elements inside parentheses
                    while (!stack.peek().equals("(")) { // Pop elements until an opening parenthesis is found
                        String element = stack.pop();
                        int index = element.indexOf(','); // Find the index of comma in the element
                        if (index >= 0) { // If comma is found
                            String atom = element.substring(0, index); // Extract the atom name
                            int atomCount = Integer.parseInt(element.substring(index + 1)) * count; // Multiply the count
                            tempStack.push(atom + "," + atomCount); // Push the updated element to tempStack
                        } else
                            tempStack.push(element + "," + str); // If no comma, append count to element and push
                    }
                    stack.pop(); // Pop the opening parenthesis
                    while (!tempStack.isEmpty()) // Push back elements from tempStack to the main stack
                        stack.push(tempStack.pop());
                } else { // If previous element is not a closing parenthesis
                    String curStr = prev + "," + str; // Combine the element with count
                    stack.push(curStr); // Push the combined string to the stack
                }
            } else
                stack.push(str); // If current string is neither closing parenthesis nor digit, push it to the stack
        }
        
        // Create a TreeMap to store atom counts in sorted order
        TreeMap<String, Integer> map = new TreeMap<String, Integer>();
        while (!stack.isEmpty()) { // Process elements from the stack
            String atomCount = stack.pop(); // Pop the top element from the stack
            int index = atomCount.indexOf(','); // Find the index of comma
            if (index >= 0) { // If comma is found
                String atom = atomCount.substring(0, index); // Extract the atom name
                int count = Integer.parseInt(atomCount.substring(index + 1)); // Extract the count
                count += map.getOrDefault(atom, 0); // Add to the existing count in the map
                map.put(atom, count); // Update the map with the new count
            } else {
                int count = map.getOrDefault(atomCount, 0) + 1; // If no comma, increment the count in the map
                map.put(atomCount, count); // Update the map
            }
        }
        
        // Build the output string in the required format
        StringBuffer output = new StringBuffer();
        Set<String> keySet = map.keySet(); // Get the set of keys (atom names) from the map
        for (String atom : keySet) { // Iterate through the atom names
            int count = map.get(atom); // Get the count of the current atom
            output.append(atom); // Append the atom name to the output
            if (count > 1) // If count is greater than 1
                output.append(count); // Append the count to the output
        }
        
        return output.toString(); // Return the final output string
    }

}

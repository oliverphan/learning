class Solution {
    
    // <Key, Value>
    private HashMap<Character, Character> mappings;
    
    public Solution() { // Constructor for the class, closing bracket key with opening value
        this.mappings = new HashMap<Character, Character>();
        this.mappings.put(')', '(');
        this.mappings.put('}', '{');
        this.mappings.put(']', '[');
    }
    
    public boolean isValid(String s) {
        // Utilise the stack structure
        // The problem implies that every closing bracket encountered should have a matching             opening bracket
        
        //Init Stack
        Stack<Character> stack = new Stack<Character>();
        
        // Iterate through the string
        for (int i = 0; i < s.length(); i++) {
            
            // Case: Closing bracket
            if (this.mappings.containsKey(c)) {
                
                // Get the top element of the stack. If the stack is empty, set a dummy value of '#'
                // topElement is assigned the result of the ternary operator
                char topElement = stack.empty() ? '#' : stack.pop();

                if (topElement != this.mappings.get(c)) {
                    return false;
                }
            } else {
                // Case: opening bracket. Push to the stack
                stack.push(c);
            }
        }
        // Expression invalid if stack isn't empty here
        return stack.isEmpty();
    }
}
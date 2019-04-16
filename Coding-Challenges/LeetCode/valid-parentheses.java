// Rule 1: An opening can't be followed by a closing of a different
// Rule 2: Opening brackets need to be matched by an equal number of closing of the same type
//  + Consequence:

class Solution {
    public boolean isValid(String s) {
        int i;
        // Could probably improve to remove these shitty switch statements
        for (i = 0; i < s.length() - 1; i++) {
            // System.out.println(s.length());
            switch (s.charAt(i)) {

                case '(':
                    if (s.charAt(i+1) == ']' || s.charAt(i+1) == '}') {
                        return false;
                    }
                    break;

                case '[':
                    if (s.charAt(i+1) == ')' || s.charAt(i+1) == '}') {
                        return false;
                    }
                    break;

                case '{':
                    if (s.charAt(i+1) == ')' || s.charAt(i+1) == ']') {
                        return false;
                    }
                    break;
            }
        }
        return true;
    }
}
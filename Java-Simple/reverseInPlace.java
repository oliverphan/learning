import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class reverseInPlace {
    public static void main(String [] args) {
        List<String> colors = new ArrayList<>(Arrays.asList("RED", "BLUE", "BLACK"));

        System.out.println(colors);
        
        reverseRecursive(colors);
        System.out.println(colors);
        
        reverseIterative(colors);
        System.out.println(colors);
    }
    
    // Reverse a list in place, recursively.
    public static <T> void reverseRecursive(List<T> list) {
        if (list == null || list.size() <= 1) {
            return;
        }

        T first = list.remove(0);

        reverseRecursive(list);

        list.add(first);
    }

    public static <T> void reverseIterative(List<T> list) {
        if (list == null || list.size() <= 1) {
            return;
        }

        int start = 0;
        int end = list.size() - 1;
        T temp;

        while (start < end) {
            temp = list.get(start);
            list.set(start, list.get(end));
            list.set(end, temp);

            start++;
            end--;
        }
    }
}
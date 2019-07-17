public class stackArray {
    static final int MAX = 1000;
    int[] arr = new int[MAX];
    int topIndex;

    // Constructor
    public stackArray() {
        this.topIndex = -1;
    }

    boolean isEmpty() {
        return (this.topIndex < 0);
    }

    boolean push(int x) {
        if (topIndex >= MAX - 1) {
            System.out.println("Stack overflow");
            return false;
        }   

        System.out.println("Push: " + x);
        topIndex++;
        arr[topIndex] = x;
        return true;
    }

    int pop() {
        if (this.topIndex < 0) {
            System.out.println("Stack underflow");
            return -1;
        }
        int temp = arr[this.topIndex];
        this.topIndex--;
        return temp;
    }

    int peekTop() {
        if (this.topIndex < 0) {
            System.out.println("Stack underflow");
            return -1;
        }
        return this.arr[this.topIndex];
    }

    public static void main (String[] args) 
    { 
        stackArray stack = new stackArray(); 
  
        stack.push(10); 
        stack.push(20); 
        stack.push(30); 
        System.out.println(stack.pop() + " Popped from stack"); 
        System.out.println("Top: " + stack.peekTop());
    } 
}
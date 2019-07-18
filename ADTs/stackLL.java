// import static java.lang.System;
// import java.lang.String;

class stackLL {
    // A singly linked list used. Dynamic sizing.
    class Node {
        int value;
        Node prev;

        Node() {
            value = -1;
            prev = null;
        }    
    }

    Node top;

    // Constructor
    public stackLL() {
        this.top = null;
    }

    boolean isEmpty() {
        return (this.top == null);
    }

    void push(int x) {
        Node temp = new Node();
        temp.value = x;
        temp.prev = top;
        this.top = temp;
    }

    int pop() {
        int temp = top.value;
        top = top.prev;
        return temp;
    }

    int peekTop() {
        return top.value;
    }

    public static void main (String[] args) 
    { 
        stackLL stack = new stackLL(); 
  
        stack.push(10); 
        stack.push(20); 
        stack.push(30); 
        System.out.println(stack.pop() + " Popped from stack"); 
        System.out.println("Top: " + stack.peekTop());
    } 
}
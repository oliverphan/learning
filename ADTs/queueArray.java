public class queueArray {
    int front, rear, size;
    int capacity;
    int array[];

    public static void main(String[] args) {
        queueArray q = new queueArray(10);

        q.enqueue(10);
        q.enqueue(30);
        q.enqueue(20);
        q.enqueue(40);

        System.out.println(q.dequeue() +  
                     " dequeued from queue\n"); 
        
        System.out.println("Front item is " +  
                               q.front()); 
           
        System.out.println("Rear item is " +  
                                q.rear());
    }

    public queueArray(int capacity) {
        this.capacity = capacity;
        this.front = this.size = 0; // the first item
        this.rear = capacity - 1; // the last item
        this.array = new int[this.capacity];
    }

    boolean isFull() {
        return (this.size == this.capacity);
    }

    boolean isEmpty() {
        return (this.size == 0);
    }

    // Modulo for circular tracking of indices
    void enqueue(int x) {
        if (this.isFull()) {
            return;
        }

        this.rear = (this.rear + 1) % this.capacity;
        array[this.rear] = x;
        this.size += 1;
        System.out.println("item queued :" + x);
    }

    // Remove from front
    int dequeue() {
        if (this.isEmpty()) {
            return Integer.MIN_VALUE;
        }

        int item = array[this.front];
        this.front = (this.front + 1) % this.capacity;
        // this.array[this.front] = null; this line doesn't work because array was declared array of INT
        this.size -= 1;
        return item;
    }

    int front() {
        if (this.isEmpty()) {
            return Integer.MIN_VALUE;
        }

        return this.array[this.front];
    }
    int rear() { 
        if (this.isEmpty()) {
            return Integer.MIN_VALUE; 
        }
        return this.array[this.rear]; 
    } 
}
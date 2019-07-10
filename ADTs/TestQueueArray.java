import queueArray;

public class TestQueueArray {
    
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
}
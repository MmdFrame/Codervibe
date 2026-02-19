class CircularQueue:
    def __init__(self, capacity=100):
        self.data = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % len(self.data) == self.front

    def enqueue(self, x):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % len(self.data)

        self.data[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        k = self.data[self.front]

        if self.front == self.rear:  # فقط یک عنصر
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.data)

        return k
    
    
    
    
    


class C_Queue:
    def __init__(self, max):
        self.list = [None] * max   # اصلاح شد
        self.front = -1
        self.rear = -1

    def insert(self, x):
        if self.is_full():
            print("Queue is full")
            return

        if self.front == -1:   # صف خالی است
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % len(self.list)

        self.list[self.rear] = x

    def delete(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        k = self.list[self.front]

        if self.front == self.rear:   # فقط یک عنصر
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.list)

        return k

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % len(self.list) == self.front






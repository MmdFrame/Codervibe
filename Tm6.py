class CircularQueue:
    def __init__(self, max_size=100):
        self.data = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % len(self.data) == self.front

    def insert(self, x):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.data[0] = x
            return

        self.rear = (self.rear + 1) % len(self.data)
        self.data[self.rear] = x

    def delete(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        k = self.data[self.front]

        if self.front == self.rear:   # فقط یک عنصر داشت
            self.front = -1
            self.rear = -1
            return k

        self.front = (self.front + 1) % len(self.data)
        return k

    # نمایش عناصر معتبر (داخل صف)
    def show_valid(self):
        if self.is_empty():
            print("Queue is empty")
            return

        i = self.front
        while True:
            print(self.data[i])
            if i == self.rear:
                break
            i = (i + 1) % len(self.data)

    # نمایش خانه‌های نامعتبر (بیرون صف)
    def show_invalid(self):
        if len(self.data) == 0:
            return

        if self.is_empty():
            for i in range(len(self.data)):
                print(self.data[i])
            return

        i = (self.rear + 1) % len(self.data)
        while i != self.front:
            print(self.data[i])
            i = (i + 1) % len(self.data)

    # پیدا کردن اندیس یک مقدار در صف (اگر نبود None)
    def find(self, x):
        if self.is_empty():
            return None

        i = self.front
        while True:
            if self.data[i] == x:
                return i
            if i == self.rear:
                break
            i = (i + 1) % len(self.data)

        return None

    # جایگزینی همه‌ی x ها با y
    def replace(self, x, y):
        if self.is_empty():
            return

        i = self.front
        while True:
            if self.data[i] == x:
                self.data[i] = y
            if i == self.rear:
                break
            i = (i + 1) % len(self.data)

























        






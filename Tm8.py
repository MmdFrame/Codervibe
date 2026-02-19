class Stack:
    def __init__(self, limit=1000):
        self.data = []
        self.limit = limit

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return len(self.data) >= self.limit

    def push(self, x):
        if self.is_full():
            print("Stack is full")
            return -1
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self.data[-1]


# همه اندیس‌های x را چاپ کند
def print_all_indexes(self, x):
    found = False
    for i in range(len(self.st)):
        if self.st[i] == x:
            print(i)
            found = True
    if not found:
        print("not found")


# اولین اندیس شامل x را چاپ کند
def print_first_index(self, x):
    for i in range(len(self.st)):
        if self.st[i] == x:
            print(i)
            return
    print("not found")


# آخرین اندیس شامل x را چاپ کند (از آخر به اول)
def print_last_index(self, x):
    for i in range(len(self.st) - 1, -1, -1):
        if self.st[i] == x:
            print(i)
            return
    print("not found")


# آخرین اندیس شامل x را چاپ کند (روش دوم: از اول به آخر)
def print_last_index_v2(self, x):
    p = -1
    for i in range(len(self.st)):
        if self.st[i] == x:
            p = i
    if p == -1:
        print("not found")
    else:
        print(p)


# جایگزینی: همه‌ی x ها را با y عوض کند
def replace_all(self, x, y):
    for i in range(len(self.st)):
        if self.st[i] == x:
            self.st[i] = y






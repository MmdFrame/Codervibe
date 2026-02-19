class node:
    def __init__(self, d):
        self.Data = d
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    # درج اول
    def insert_first(self, x):
        a = node(x)
        a.next = self.head
        self.head = a

    # درج آخر
    def insert_last(self, x):
        a = node(x)
        if self.head is None:
            self.head = a
            return

        c = self.head
        while c.next:
            c = c.next
        c.next = a

    # درج بعد از اولین نودی که Data == x
    def insert_after(self, x, y):
        if self.head is None:
            print("list is empty")
            return

        c = self.head
        while c:
            if c.Data == x:
                a = node(y)
                a.next = c.next
                c.next = a
                return
            c = c.next

        print("not found")

    # درج قبل از اولین نودی که Data == x
    def insert_before(self, x, y):
        if self.head is None:
            print("list is empty")
            return

        if self.head.Data == x:
            self.insert_first(y)
            return

        c = self.head
        while c.next:
            if c.next.Data == x:
                a = node(y)
                a.next = c.next
                c.next = a
                return
            c = c.next

        print("not found")
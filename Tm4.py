class dnode:
    def __init__(self, x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list:
    def __init__(self):
        self.head = None

    def ins_frist(self, x):
        a = dnode(x)
        a.next = self.head
        if self.head:
            self.head.back = a
        self.head = a

    def ins_last(self, x):
        if self.head is None:
            self.ins_frist(x)
            return

        c = self.head
        while c.next:
            c = c.next

        a = dnode(x)
        c.next = a
        a.back = c

    def ins_after(self, x, y):
        if self.head is None:
            print("error")
            return

        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.ins_last(y)
                    return

                a = dnode(y)
                a.next = c.next
                a.back = c
                c.next.back = a
                c.next = a
                return

            c = c.next

        print("not found")

    def ins_befor(self, x, y):
        if self.head is None:
            print("error")
            return

        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    self.ins_frist(y)
                    return

                a = dnode(y)
                a.next = c
                a.back = c.back
                c.back.next = a
                c.back = a
                return

            c = c.next

        print("not found")

    def del_first(self):
        if self.head is None:
            print("error")
            return

        c = self.head
        self.head = c.next
        if self.head:
            self.head.back = None
        del c

    def del_last(self):
        if self.head is None:
            print("error")
            return

        c = self.head
        while c.next:
            c = c.next

        if c.back is None:
            self.del_first()
            return

        c.back.next = None
        del c

    def del_befor(self, x):
        if self.head is None:
            print("error")
            return
        if self.head.Data == x:
            print("error")
            return

        c = self.head
        while c:
            if c.Data == x:
                a = c.back  # نود قبل از x که باید حذف شود

                # اگر نود حذف‌شونده head است (یعنی x در نود دوم بوده)
                if a.back is None:
                    self.head = c
                    c.back = None
                    del a
                    return

                # حالت معمولی (نود حذف‌شونده وسط لیست است)
                c.back = a.back
                a.back.next = c
                del a
                return

            c = c.next

        print("x not found")

                                                   





class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # حذف نود بعد از اولین نودی که value == x
    def remove_after(self, x):
        if self.head is None:
            print("error: empty list")
            return

        cur = self.head
        while cur:
            if cur.value == x:
                if cur.next is None:
                    print("error: no node after x")
                    return

                target = cur.next
                cur.next = target.next
                if target.next:
                    target.next.prev = cur
                return

            cur = cur.next

        print("not found")

    # حذف اولین نودی که value == x
    def remove_value(self, x):
        if self.head is None:
            print("error: empty list")
            return

        cur = self.head
        while cur:
            if cur.value == x:
                # اگر نود سر لیست بود
                if cur.prev is None:
                    self.head = cur.next
                    if self.head:
                        self.head.prev = None
                    return

                # اگر نود وسط یا آخر بود
                cur.prev.next = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return

            cur = cur.next

        print("not found")
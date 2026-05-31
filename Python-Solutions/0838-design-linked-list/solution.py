class MyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.data

    def addAtHead(self, val: int) -> None:
        newnode = self.Node(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newnode = self.Node(val)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newnode
            
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index == 0:
            self.addAtHead(val)
            return
            
        newnode = self.Node(val)
        cur = self.head
        for i in range(index - 1):
            cur = cur.next
            
        newnode.next = cur.next
        cur.next = newnode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
       
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head

            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

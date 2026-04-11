class ListNode:
    def __init__(self, key = int):
        self.key = key
        self.next = None #points to next
class MyHashSet:

    def __init__(self): #constructor to pre-allocate the memory which is going to be array in this case
        self.set = [ListNode(0) for i in range(10**4)] #dummy node for every position in array  
    
    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index] # current point is a head of the linkedlist and wwe also want iterate through the end of the linkedlist to insert new node with this key

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)


    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index] 

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index] 

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
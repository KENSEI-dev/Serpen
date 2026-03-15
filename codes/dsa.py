class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class dsa:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print('None')
    
    def deleteFromFirst(self):
        if self.head is None:
            print("List is empty! No node to delete.")
            return
        print(f"Deleting node from first: {self.head.data}")
        self.head = self.head.next  

    def deleteFromLast(self):
        if self.head is None:
            print("List is empty! No node to delete.")
            return
        if self.head.next is None:
            print(f"Deleting only node in list: {self.head.data}")
            self.head = None
            return
        temp = self.head
        while temp.next.next: 
            temp = temp.next
        print(f"Deleting node from last: {temp.next.data}")
        temp.next = None  

    def deleteFromAny(self, pos):
        if self.head is None:
            print("List is empty! No node to delete.")
            return
        
        if pos <= 1:
            self.deleteFromFirst()
            return
        temp = self.head
        count = 1
        while temp.next and count < pos - 1:
            temp = temp.next
            count += 1
        if temp.next is None:
            print("Position out of range!")
            return
        print(f"Deleting node at position {pos}: {temp.next.data}")
        temp.next = temp.next.next  

    def reverseList(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def mergeSortedLists(l1, l2):
        dummy = Node(0)
        current = dummy
        l1 = l1.head
        l2 = l2.head
        while l1 and l2:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        merged = ll.LinkedList()
        merged.head = dummy.next
        return merged

    def addPolynomials(p1, p2):
        result = ll.LinkedList()
        t1 = p1.head
        t2 = p2.head
        while t1 and t2:
            coeff = t1.data[0] + t2.data[0]
            power = t1.data[1]  
            result.insertAtEnd((coeff, power))
            t1 = t1.next
            t2 = t2.next
        while t1:
            result.insertAtEnd(t1.data)
            t1 = t1.next
        while t2:
            result.insertAtEnd(t2.data)
            t2 = t2.next
        return result

    def pairwiseSwap(self):
        temp = self.head
        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    def detectLoop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

ll=dsa()
for value in [10,20,30,40]:
    ll.insert_at_end(value)
ll.insert_at_end(50)
ll.traverse()
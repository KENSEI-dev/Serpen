class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head= None
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("NULL")
    def insert(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def del_second_node(self):
        temp=self.head
        if temp.next is None or temp is None:
            return temp
        temp.next=temp.next.next
        return temp
ll=LinkedList()
for value in [10,20,30,40]:
    ll.insert(value)
ll.traverse()
ll.del_second_node()
ll.traverse()
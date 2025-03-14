class Node:
    def __init__(self, data, next=None):
        self.data = next
        self.next = next

class LinkedList:
    def __init__(self,head= None):
        self.head = head
    def add(self, data):
        new = Node(data)
        if (self.head):
            temp = self.head
            while (temp.next!=None) : 
                temp=temp.next
            temp.next = new
        else:
            self.head =new

    def list(self, first=None):
      self.first = first
      first = self.head
      while(first):
        print(first)
        first = first.next

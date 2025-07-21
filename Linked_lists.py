class Node:
    def __init__(self, data, pre = None, next = None):
        self.data = data
        self.next = next
        self.pre = pre

class LinkedList:
    def __init__(self):
        self.linkedlist = []
    def Insertion(self, data, position = -1):
        node = Node(data)
        if not self.linkedlist :
                self.linkedlist.append(node)
        else :
            if position == 0 :
                node.next = self.linkedlist[0]
            elif position == -1 :
                last = self.linkedlist[0]
                while last.next != None :
                    last = last.next
                last.next = node
                node.pre = last
                self.linkedlist.append(last)
            else:
                last = self.linkedlist[0]
                while last.data != data:
                    last = last.next
                node.next = last.next
                node.pre = last
                self.linkedlist.append(last)
        
    def Deletion(self,position=-1):
        if not self.linkedlist:
            print('list is empty')
            return
        if position == 0 :
            node = self.linkedlist[0]
            node.next.pre = None
            node.next = None
            self.linkedlist.remove(0)
            return
        elif position == -1 :
            last = self.LinkedList[0]
            while last.next != None :
                last = last.next
            last.pre.next = None
            self.linkedlist.remove(last)
            return
        else:
            last = self.linkedlist[0]
            while last.data != position:
                last = last.next
            last.pre.next = last.next
            last.next.pre = last.pre
            self.linkedlist.remove(last)
            return
        
    def showLinkedList(self):
        last = self.linkedlist[0]
        while last :
            print(last.data, end= ' --> ')
            last = last.next


lsit = LinkedList()
lsit.Insertion(10,0)
lsit.Insertion(20,-1)
lsit.Insertion(30,-1)
lsit.Insertion(40,-1)
lsit.Insertion(50,-1)
lsit.Insertion(60,-1)
lsit.showLinkedList()
lsit.Deletion(30)
lsit.showLinkedList()
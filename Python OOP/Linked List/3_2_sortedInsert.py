# Sorted Insert in a Linked List

class LinkedList:
    class Node:
        def __init__(self, value):
           self.value = value
           self.next = None
    
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def sortedInsert(self, value):
        if self.isEmpty():
            self.head = self.Node(value)
            self.size += 1
        else:
            if value < self.head.value:
                node = self.Node(value)
                node.next = self.head
                self.head = node
                self.size += 1
                return value

            prev = self.head
            curr = self.head.next
            while curr:
                if value < curr.value:
                    node = self.Node(value)
                    node.next = curr
                    prev.next = node
                    self.size += 1
                    return value
                prev = curr
                curr = curr.next
            else:
                prev.next = self.Node(7)
            
            self.size += 1
        return value

    def remove(self, value):
        if self.isEmpty():
            return False
        else:
            if self.head.value == value:
                self.head = self.head.next
                self.size -= 1
                return True
            else:
                prev = self.head
                curr = self.head.next

                while curr:
                    # print 'Previous: %d, Current %d' % (prev.value, curr.value)
                    if curr.value == value:
                        prev.next = curr.next
                        self.size -= 1
                        return True
                    prev = curr
                    curr = curr.next

                return False

                    

    def traverse(self):
        pointer = self.head
        print "\nTraversing Linked List:", 
        while pointer:
            print pointer.value, " ",
            pointer = pointer.next

def removeHelper(ll, value):
    print "\n\nTrying to remove %d..." % value
    if ll.remove(value):
        print "Success!!!"
    else:
        print "Unsuccessful!!!"




     


if __name__ == '__main__':
    ll = LinkedList()
    
    print "Inserting %d" % ll.sortedInsert(7)
    print "Inserting %d" % ll.sortedInsert(6)
    print "Inserting %d" % ll.sortedInsert(3)
    print "Inserting %d" % ll.sortedInsert(9)
    print "Inserting %d" % ll.sortedInsert(2)
    print "Inserting %d" % ll.sortedInsert(5)
    ll.traverse()
    
    removeHelper(ll, 7)
    removeHelper(ll, 8)
    removeHelper(ll, 2)
    ll.traverse()
    
    removeHelper(ll, 5)
    ll.traverse()

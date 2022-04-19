# Linked List
# Singly Linked List
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insertAtBeginning(self, data):
        node = Node(data, self.head)        # Create node with data, next value is current head
        self.head = node                    # Set new node as head

    # Insert at end
    def insertAtEnd(self, data):
        node = Node(data)
        if self.head == None:               # If there is no head, set node as head
            self.head = node
            return
        value = self.head
        while value.next != None:           # While there is still next element, set value as next element
            value = value.next
        value.next = node                   # Set new node as last element's next value 

    # Insert at middle
    def insertAtMiddle(self, middleNode, data):
        if middleNode == None:              # If there is no middle node, pass
            pass
        else:
            node = Node(data)               
            node.next = middleNode.next     # Set middle node's next as new node's next
            middleNode.next = node          # Set node as middle node's next

    # Remove Data
    def removeData(self, dataToRemove):
        value = self.head
        if value != None:                   
            if value.data == dataToRemove:  # If head is data to remove, set next element as head
                value.next = self.head
                value = None
                return
        while value != None:
            if value.data == dataToRemove:  # Find value to remove
                break
            previousValue = value           # Set current value as previous value
            value = value.next              # Set next value as current value
        if value == None:                   # If data to remove cannot be found, return
            return
        previousValue.next = value.next     # Set current value's next as previous value's next

    # Remove Beginning
    def removeBeginning(self):              
        value = self.head                   # Set head as value
        self.head = value.next              # Set next value as head

    # Remove End
    def removeEnd(self):
        value = self.head
        while value.next != None:           # Find last element
            previousValue = value           
            value = value.next
        previousValue.next = None           # Set previous element's next as None

    # Get Index
    def getIndex(self, index):
        count = 0
        value = self.head
        while count < index:                # While count < index, move to next element
            if value.next == None:          # If index outside of bounds, break
                break
            else:
                value = value.next
                count += 1
        print(value.data)

    # Print List
    def printList(self):
        value = self.head                   # Set head as value to be printed
        while value != None:                # While there is still value, print data
            print(value.data)            
            value = value.next              # Set next node as the value

linkedList = LinkedList()

# Set elements [10, 20, 40]
linkedList.head = Node(10)
element2 = Node(20)
element3 = Node(40)
element2.next = element3
linkedList.head.next = element2

# Insert elements
linkedList.insertAtBeginning(0)
linkedList.insertAtBeginning(5)
linkedList.insertAtMiddle(element2, 30)
linkedList.insertAtEnd(50)
linkedList.insertAtEnd(60)
linkedList.insertAtEnd(70)

# Remove elements
linkedList.removeBeginning()
linkedList.removeData(35)
linkedList.removeEnd()

# Print linked list
print("Linked List:")
linkedList.printList()
print("\nGet Index 3:")
linkedList.getIndex(3)
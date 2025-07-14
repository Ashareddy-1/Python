#In LinkedList class that we implemented in our tutorial add following two methods,
#def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

#def remove_by_value(self, data):
    # Remove first node that contains data
#Now make following calls,

    #ll = LinkedList()
    #ll.insert_values(["banana","mango","grapes","orange"])
    #ll.print()
    #ll.insert_after_value("mango","apple") # insert apple after mango
    #ll.print()
    #ll.remove_by_value("orange") # remove orange from linked list
    #ll.print()
    #ll.remove_by_value("figs")
    #ll.print()
    #ll.remove_by_value("banana")
    #ll.remove_by_value("mango")
    #ll.remove_by_value("apple")
    #ll.remove_by_value("grapes")
    #ll.print()

#LinkedList Class Code:  
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#Purpose: Represents a single node in the linked list.
#Attributes:
#data: Stores the value of the node.
#next: A pointer to the next node in the list, initialized to None.

class LinkedList:
    def __init__(self):
        self.head = None

#Purpose: Manages the linked list.
#Attributes:
#head: A pointer to the first node in the list, initialized to None.

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

#Purpose: Prints the elements of the linked list.
#Steps:
#Check if the list is empty. If it is, print a message and return.
#Traverse the list, appending each node's data to a string.
#Print the string representation of the list.

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

#Purpose: Returns the number of nodes in the list.
#Steps:
#Initialize a counter to 0.
#Traverse the list, incrementing the counter for each node.
#Return the counter.

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

#Purpose: Inserts a new node at the beginning of the list.
#Steps:
#Create a new node with the given data, pointing to the current head.
#Update the head to the new node.

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

#Purpose: Inserts a new node at the end of the list.
#Steps:
#If the list is empty, set the head to the new node.
#Otherwise, traverse to the last node.
#Set the next pointer of the last node to the new node.

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

#Purpose: Inserts a new node at the specified index.
#Steps:
#Check if the index is valid. If not, raise an exception.
#If the index is 0, insert at the beginning.
#Otherwise, traverse to the node just before the specified index.
#Insert the new node at the specified index.

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

#Purpose: Removes the node at the specified index.
#Steps:
#Check if the index is valid. If not, raise an exception.
#If the index is 0, update the head to the next node.
#Otherwise, traverse to the node just before the specified index.
#Remove the node at the specified index.
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

#Purpose: Inserts multiple values into the list.
#Steps:
#Clear the list by setting the head to None.
#Insert each value from the data list at the end of the list.

##def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

#def remove_by_value(self, data):
# Remove first node that contains data

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

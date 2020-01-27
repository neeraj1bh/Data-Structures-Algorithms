class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class CircularLinkedList:

    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last == None:
            print("List is empty")
            return

        p = self.last.link

        while True:
            print(p.info, " ", end = "")
            p = p.link
            if p == self.last.link:
            	break
        print()

    def insert_at_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_in_empty_list(self, data):
    	temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_at_end(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp
        
    def create_list(self):
        n = int(input("Enter the no of nodes : "))
        if n == 0:
            return
        data = int(input("Enter the element to be inserted : "))
        self.insert_in_empty_list(data)

        for i in range(n-1):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.last.link

        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
            	break

        if p == self.last.link and p.info != x:
            print(x, "is not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if p == self.last:
            	self.last = temp

    def delete_node(self, x):

        if self.last is None:
            print("List is empty")
            return

        # Deletion of only node
        if self.last.link == self.last and self.last.info == x:
            self.last = None
            return

        # Deletion of first node
        if self.last.link.info == x:
            self.last.link = self.last.link.link
            return

        # Deletion in between or at the end
        p = self.last.link
        while p.link is not self.last.link:
            if p.link.info == x:
                break
            p = p.link

        if p.link is self.last.link:
            print("Element ", x, "not in list")
        else:
            p.link = p.link.link
            if self.last.info == x:
            	self.last = p

    def delete_first_node(self):

        if self.last is None: # List is empty
            return
        if self.last.link == self.last:
            self.last = None
            return    
        self.last.link = self.last.link.link

    def delete_last_node(self):

        if self.last is None:
            return

        if self.last.link is self.last:
            self.last = None
            return

        p = self.last.link
        while p.link is not self.last:
            p = p.link
        p.link = self.last.link
        self.last = p        

list1 = CircularLinkedList()
list1.create_list()

while True:
    print("1. Display list")
    print("2. Insert in empty list")
    print("3. Insert a node at the beginning of the list")
    print("4. Insert a node at the end of the list")
    print("5. Insert a node after a specified node")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Delete any node")
    print("9. Quit")

    option = int(input("Enter your choice:"))
    if option == 1:
        list1.display_list()
    elif option == 2:
        data1 = int(input("Enter the element to be inserted:"))
        list1.insert_in_empty_list(data1)
    elif option == 3:
        data1 = int(input("Enter the element to be inserted:"))
        list1.insert_at_beginning(data1)
    elif option == 4:
        data1 = int(input("Enter the element to be inserted:"))
        list1.insert_at_end(data1)
    elif option == 5:
        data1 = int(input("Enter the element to be inserted:"))
        x1 = int(input("Enter the element after which to insert:"))
        list1.insert_after(data1, x1)
    elif option == 6:
        list1.delete_first_node()
    elif option == 7:
        list1.delete_last_node()
    elif option == 8:
        data1 = int(input("Enter the element to be deleted:"))
        list1.delete_node(data1)
    elif option == 9:
        break
    else:
        print("Wrong Option")
    print()

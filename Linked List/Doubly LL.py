class Node:

    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is :  ")
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.next
            print()

    def insert_at_beginning(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input("Enter the no of nodes : "))
        if n == 0:
            return
        data = int(input("Enter the first element to be inserted: "))
        self.insert_in_empty_list(data)

        for i in range(n-1):
            data = int(input("Enter the next element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print(x, "is not present in the list")
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp  # should not be done when p refers to last node
            p.next = temp

    def insert_before(self, data, x):
        # If list is empty
        if self.start is None:
            print("List is empty")
            return

        # x is in first node, new node is to inserted before first node
        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return

        # Find reference to predecessor of node containing x
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print(x, " not present in the list")
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_first_node(self):

        if self.start is None:  # List is empty
            return
        if self.start.next is None:  # List has only one node
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last_node(self):

        if self.start is None:  # List is empty
            return

        if self.start.next is None:  # List has only one node
            self.start = None
            return

        p = self.start
        while p.next is not None:
            p = p.next
        p.prev.next = None

    def delete_node(self, x):

        if self.start is None:  # List is empty
            print("List is empty")
            return

        if self.start.next is None:  # List has only one node
            if self.start.info == x:
                self.start = None
            else:
                print(x, "not found")
            return

        # Deletion of first node
        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start.next
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None:  # Node to be deleted is in between
            p.prev.next = p.next
            p.next.prev = p.prev
        else:  # prefers to the last node
            if p.info == x:  # Node to be deleted is at the end
                p.prev.next = None
            else:
                print(x, " not found")

    def reverse_list(self):

        if self.start is None:  # List is empty
            return

        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1


list1 = DoubleLinkedList()
list1.create_list()

while True:
    print("1. Display list")
    print("2. Insert in empty list")
    print("3. Insert a node at the beginning of the list ")
    print("4. Insert a node at the end of the list")
    print("5. Insert a node after a specified node")
    print("6. Insert a node before a specified node")
    print("7. Delete first node")
    print("8. Delete last node")
    print("9. Delete any node")
    print("10. Reverse the list")
    print("11. Quit")

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
        data1 = int(input("Enter the element to be inserted:"))
        x1 = int(input("Enter the element before which to insert:"))
        list1.insert_before(data1, x1)
    elif option == 7:
        list1.delete_first_node()
    elif option == 8:
        list1.delete_last_node()
    elif option == 9:
        data1 = int(input("Enter the element to be deleted:"))
        list1.delete_node(data1)
    elif option == 10:
        list1.reverse_list()
    elif option == 11:
        break
    else:
        print("Wrong Option")
    print()

class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:

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
                p = p.link
            print()

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:  # Insert a new node in an empty list
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the no of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def concatenate(self, list2):
        # If list is empty
        if self.start is None:
            self.start = list2.start
            return

        if list2.start is None:
            return

        p = self.start
        while p.link is not None:
            p = p.link

        p.link = list2.start


lists1 = SingleLinkedList()
lists2 = SingleLinkedList()

print("Enter first list")
lists1.create_list()
print("Enter second list")
lists2.create_list()

print("First", end=" ")
lists1.display_list()
print("Second", end=" ")
lists2.display_list()

lists1.concatenate(lists2)
print("Concatenated", end=" ")
lists1.display_list()

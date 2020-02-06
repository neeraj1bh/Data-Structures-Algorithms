
class EmptyQueueError(Exception):
    pass


class Node:

    def __init__(self, value, pr):
        self.info = value
        self.priority = pr
        self.link = None


class Queue:

    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def size(self):
        n = 0
        p = self.front
        while p is not None:
            n += 1
            p = p.link
        return n

    def enqueue(self, data, data_priority):
        temp = Node(data, data_priority)
        # If queue is empty or element to be added has priority more than first element
        if self.is_empty() or data_priority < self.front.priority:
            temp.link = self.front
            self.front = temp
        else:
            p = self.front
            while p.link is not None and p.link.priority <= data_priority:
                p = p.link
            temp.link = p.link
            p.link = temp

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.front.info
        self.front = self.front.link
        return x

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            print("Queue is :  ")
            p = self.front
            while p is not None:
                print(p.info, "     ", p.priority)
                p = p.link
            print()


##########################################################################

if __name__ == "__main__":
    qu = Queue()

    while True:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Size")
        print("4. Display")
        print("5. Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x1 = int(input("Enter the element to be pushed : "))
            pr1 = int(input("Enter it's priority : "))
            qu.enqueue(x1, pr1)
        elif choice == 2:
            x1 = qu.dequeue()
            print("Element deleted from the queue is : ", x1)
        elif choice == 3:
            print("Size of Queue : ", qu.size())
        elif choice == 4:
            qu.display()
        elif choice == 5:
            break
        else:
            print("Wrong Choice")
        print()

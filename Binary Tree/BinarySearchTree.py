class TreeEmptyError(Exception):
    pass


class Node:

    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild, x)
        else:
            print(x, " already present in the tree")
        return p

    def insert1(self, x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
            else:
                print(x, " already present in the tree")
                return

        temp = Node(x)

        if par is None:
            self.root = temp
        elif x < par.info:
            par.lchild = temp
        else:
            par.rchild = temp

    def search(self, x):
        return self._search(self.root, x) is not None

    def _search(self, p, x):
        if p is None:
            return None  # key not found
        if x < p.info:  # Search in left subtree
            return self._search(p.lchild, x)
        if x > p.info:  # Search in right subtree
            return self._search(p.rchild, x)
        return p  # key found

    def search1(self, x):
        p = self.root
        while p is not None:
            if x < p.info:
                p = p.lchild  # Move to left child
            elif x > p.info:
                p = p.rchild  # Move to right child
            else:  # x found
                return True
        return False

    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, p, x):
        if p is None:
            print(x, " not found")
            return p

        if x < p.info:  # Delete from left subtree
            p.lchild = self._delete(p.lchild, x)
        elif x > p.info:  # Delete from right subtree
            p.rchild = self._delete(p.rchild, x)
        else:
            # key to be deleted is not found
            if p.lchild is not None and p.rchild is not None:
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild, s.info)

            else:  # 1 child or no child
                if p.lchild is not None:  # only left child
                    ch = p.lchild
                else:  # only right child no left child
                    ch = p.rchild
                p = ch
        return p

    def delete1(self, x):
        p = self.root
        par = None

        while p is not None:
            if x == p.info:
                break
            par = p
            if x < p.info:
                p = p.lchild
            else:
                p = p.rchild

        if p is None:
            print(x, " not found")
            return

        # Case C: 2 children
        # Find Inorder successor and its parent

        if p.lchild is not None and p.rchild is not None:
            ps = p
            s = p.rchild

            while s.lchild is not None:
                ps = s
                s = s.lchild
            p.info = s.info
            p = s
            par = ps

        # Case B and Case A : 1 or no child
        if p.lchild is not None:  # Node to be deleted has left child
            ch = p.lchild
        else:  # Node to be deleted has right child or no child
            ch = p.rchild

        if par is None:  # Node to be deleted is self.root node
            self.root = ch
        elif p == par.lchild:  # Node is the left child of its parent
            par.lchild = ch
        else:  # Node is the right child of its parent
            par.rchild = ch

    def min1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.lchild is not None:
            p = p.lchild
        return p.info

    def max1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.info

    def min2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._min2(self.root).info

    def _min2(self, p):
        if p.lchild is None:
            return p
        return self._min2(p.lchild)

    def max2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._max2(self.root).info

    def _max2(self, p):
        if p.rchild is None:
            return p
        return self._max2(p.rchild)

    def display(self):
        self._display(self.root, 0)
        print()

    def _display(self, p, level):
        if p is None:
            return
        self._display(p.rchild, level + 1)
        print()

        for i in range(level):
            print("        ", end='')
        print(p.info)
        self._display(p.lchild, level + 1)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, p):
        if p is None:
            return
        print(p.info, " ", end='')
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info, " ", end='')
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info, " ", end='')

    def height(self):
        return self._height(self.root)

    def _height(self, p):
        if p is None:
            return 0

        hleft = self._height(p.lchild)
        hright = self._height(p.rchild)

        if hleft > hright:
            return 1 + hleft
        else:
            return 1 + hright


##########################################################################
bst = BinarySearchTree()

while True:
    print("1. Display Tree")
    print("2. Search (Iterative)")
    print("3. Search (Recursive)")
    print("4. Insert a new node (Iterative)")
    print("5. Insert a new node (Recursive)")
    print("6. Delete a node (Iterative)")
    print("7. Delete a node (Recursive)")
    print("8. Find Minimum key (Iterative)")
    print("9. Find Minimum key (Recursive)")
    print("10. Find Maximum key (Iterative)")
    print("11. Find Maximum key (Recursive)")
    print("12. Preorder Traversal")
    print("13. Inorder Traversal")
    print("14. Postorder Traversal")
    print("15. Height of Tree")
    print("16. Quit")
    choice = int(input("Enter your Choice : "))

    if choice == 1:
        bst.display()
    elif choice == 2:
        x1 = int(input("Enter the key to be searched: "))
        if bst.search1(x1):
            print("Key found")
        else:
            print("Key not found")
    elif choice == 3:
        x1 = int(input("Enter the key to be searched: "))
        if bst.search(x1):
            print("Key found")
        else:
            print("Key not found")
    elif choice == 4:
        x1 = int(input("Enter the key to be inserted: "))
        bst.insert1(x1)
    elif choice == 5:
        x1 = int(input("Enter the key to be inserted: "))
        bst.insert(x1)
    elif choice == 6:
        x1 = int(input("Enter the element to be deleted: "))
        bst.delete1(x1)
    elif choice == 7:
        x1 = int(input("Enter the element to be deleted: "))
        bst.delete(x1)
    elif choice == 8:
        print(" Minimum key is : ", bst.min1())
    elif choice == 9:
        print(" Minimum key is : ", bst.min2())
    elif choice == 10:
        print(" Maximum key is : ", bst.max1())
    elif choice == 11:
        print(" Maximum key is : ", bst.max2())
    elif choice == 12:
        bst.preorder()
    elif choice == 13:
        bst.inorder()
    elif choice == 14:
        bst.postorder()
    elif choice == 15:
        print(" Height of Tree is : ", bst.height())
    elif choice == 16:
        break
    else:
        print("Wrong choice")
    print()

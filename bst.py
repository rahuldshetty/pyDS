class Node:
    def __init__(self,value = None):
        self.__value = value
        self.__left =  None
        self.__right = None

    def get_value(self):return self.__value

    def get_left(self):return self.__left

    def get_right(self):return self.__right

    def set_left(self,node):
        self.__left = node 

    def set_right(self,node):
        self.__right = node 

    def set_value(self,value):
        self.__value = value
    


class BST:
    def __init__(self):
        self.__root = Node()

    def get_root(self):return self.__root

    def add(self,value):
        if self.search(value) == True:
            return
        temp = Node(value)
        self.__root = BST.insert(self.get_root(),temp)
    
    @staticmethod
    def insert(root,node):
        if root.get_value() is None:
            return node
        else:
            if root.get_value() < node.get_value():
                if root.get_right() is None:
                    root.set_right(node)
                else:
                    right = BST.insert(root.get_right(),node)
                    root.set_right(right)
            else:
                if root.get_left() is None:
                    root.set_left(node)
                else:
                    left = BST.insert(root.get_left(),node)
                    root.set_left(left)
        return root

    def search(self,value):
        temp = self.get_root()
        while temp!= None and  temp.get_value() != None:
            if temp.get_value() == value:
                return True
            elif temp.get_value() > value:
                temp = temp.get_left()
            else:
                temp = temp.get_right()
        return False


    def call_inorder(self):
        print("Inorder Traversal:",end="")
        self.inorder(self.get_root())
        print("\n")

    def inorder(self,root):
        if root != None and root.get_value() != None:
            if root.get_left()!=None:
                self.inorder(root.get_left())
            print(root.get_value(),end=" ")
            if root.get_right() != None:
                self.inorder(root.get_right())

if __name__ == "__main__":
    root = BST()
    while True:
        s = input("1.Add 2.Search 3.Inorder 4.Exit\nEnter option:")  
        if s == "4":break
        elif s == "1":
            v = int(input("Add value:"))
            root.add(v)
        elif s == "3":
            root.call_inorder()
        else:
            v =  int(input("Search value:"))
            print(root.search(v))
      

        
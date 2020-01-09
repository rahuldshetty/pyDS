from graph_utils import *

class Node:
    def __init__(self,node_value = None,edge_value = None):
        self.__node_value = node_value
        self.__edge_value = edge_value
        self.__children = []
        self.__node_count = 1

    def add_child(self,node):
        self.__children.append(node)
        self.__node_count += node.get_node_count()   

    def get_node_count(self):
        return self.__node_count

    def get_child_count(self):
        return len(self.__children)
    
    def get_node(self,index):
        if index < len(self.__children):
            return self.__children[index]
        else:
            raise Exception("Unknown Index")
    
    def update_node(self,node,index):
        if index < len(self.__children):
            self.__children[index] = node 
        else:
            raise Exception("Unknown index")
    
    def is_leaf(self):
        if len(self.__children) == 0:
            return True
        return False

    def get_edge_value(self):
        return self.__edge_value

    def get_node_value(self):
        return self.__node_value

    def print_values(self):
        print("Node Value:",self.get_node_value(),"Edge Value:",self.get_edge_value())

    def add_childs(self,values):
        self.__children += values
        for node in values:
            self.__node_count += node.get_node_count()


if __name__ == "__main__":
    root = Node(1)
    root.add_child(Node(0))
    root.add_child(Node(2))
    print(root.get_node_count())
    inorder_traversal(root)
    
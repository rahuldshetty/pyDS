def inorder_traversal(node):
    if node.is_leaf():
        print(node.get_node_value())
        return 
    else:
        printed = False
        for i in range(node.get_child_count()):
            child = node.get_node(i)
            inorder_traversal(child)
            if printed == False:
                print(node.get_node_value())
                printed = True



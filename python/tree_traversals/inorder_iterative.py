class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def inorder(self):
        result = []
        stack = []
        curr = self.root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2); 
tree.root.right = Node(3); 
tree.root.left.left = Node(4); 
tree.root.left.right = Node(5); 
print(tree.inorder())
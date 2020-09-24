# In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
# To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal is reversed can be used.

# Approach: 
# 1. Take the root node and put it into the stack
# 2. Iterate to reach the leftmost node while adding every visited node to the stack
# 3. Take the leaf node and push it into the result, explore the nodes right child 

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
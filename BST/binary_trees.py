# binary_trees.py

class BSTNode:
    """A node class for binary search trees. Contains a value, a
    reference to the parent node, and references to two child nodes.
    """
    def __init__(self, data):
        """Construct a new node and set the value attribute. The other
        attributes will be set when the node is added to a tree.
        """
        self.value = data
        self.prev = None        # A reference to this node's parent node.
        self.left = None        # self.left.value < self.value
        self.right = None       # self.value < self.right.value


class BST:
    """Binary search tree data structure class.
    The root attribute references the first node in the tree.
    """
    def __init__(self):
        """Initialize the root attribute."""
        self.root = None

    def find(self, data):
        """Return the node containing the data. If there is no such node
        in the tree, including if the tree is empty, raise a ValueError.
        """
        # Define a recursive function to traverse the tree.
        def _step(current):
            """Recursively step through the tree until the node containing
            the data is found. If there is no such node, raise a Value Error.
            """
            if current is None:                     # Base case 1: dead end.
                raise ValueError(str(data) + " is not in the tree.")
            if data == current.value:               # Base case 2: data found!
                return current
            if data < current.value:                # Recursively search left.
                return _step(current.left)
            else:                                   # Recursively search right.
                return _step(current.right)

        # Start the recursion on the root of the tree.
        return _step(self.root)

    def insert(self, data):
        """Insert a new node containing the specified data.

        Raises:
            ValueError: if the data is already in the tree.
        """
        # Initialize the data as a BST node
        new_node = BSTNode(data)

        # Base case: If the tree is empty, set the root to the new_node
        if self.root is None:
            self.root = new_node
        
        # Insert the node
        else:
            # Find the parent
            def _find_parent(parent, new_node):

                # If the data is already in the tree, raise a Value Error
                if parent.value == new_node.value:
                    raise ValueError(str(data) + " is already in the BST")
                
                # If the data is less than the parent, and the parent has no left child, link parent and new_node
                # Else call the function again on the left child
                elif parent.value > new_node.value:
                    if parent.left is None:
                        parent.left = new_node
                        new_node.prev = parent
                        return
                    _find_parent(parent.left, new_node)

                # If the data is greater than the parent, and the parent has no right child, link parent and new_node
                # Else call the function again on the right child
                elif parent.value < new_node.value:
                    if parent.right is None:
                        parent.right = new_node
                        new_node.prev = parent
                        return
                    _find_parent(parent.right, new_node)

            return _find_parent(self.root, new_node)
            
    def remove(self, data):
        """Remove the node containing the specified data.

        Raises:
            ValueError: if there is no node containing the data, including if
                the tree is empty.
        """
        # Find the node to remove. If the tree is empty or if the data is not in any node, find raises a ValueError
        target = self.find(data)

         # Initialize the children
        left_child = target.left
        right_child = target.right

        # If target has no children, remove the node and update the neighbors
        if left_child is None and right_child is None:
            if target is self.root:
                self.root = None
            elif target.prev.value < target.value:
                target.prev.right = None
            elif target.prev.value > target.value:
                target.prev.left = None

        # If target has one child
        elif left_child is None or right_child is None:
            
            # Set child to the one that is not None
            child = right_child
            if right_child is None:
                child = left_child

            # If the target is the root, set the root to its child and child.prev to None
            if target is self.root:
                self.root = child
                child.prev = None

            # If the target is to the right of its parent, update parent.right to child and child.prev to parent 
            elif target.prev.value < target.value:
                target.prev.right = child
                child.prev = target.prev
            
            # If the target is to the left of its parent, update parent.left to child and child.prev to parent
            elif target.prev.value > target.value:
                target.prev.left = child
                child.prev = target.prev
        
        # If the target has two children
        elif left_child != None and right_child != None:
            
            # Find the predecessor by going all the way to the right from the left child
            def _find_predecessor(node):
                if node.right is None:
                    return node
                return _find_predecessor(node.right)
            
            predecessor = _find_predecessor(target.left)

            # Save the predecessor value and remove that value, then set the target node to the predecessor value
            predecessor_value = predecessor.value
            self.remove(predecessor_value)
            target.value = predecessor_value
        return

    def __str__(self):
        """String representation: a hierarchical view of the BST."""
        if self.root is None:                       # Empty tree
            return "[]"
        out, current_level = [], [self.root]        # Nonempty tree
        while current_level:
            next_level, values = [], []
            for node in current_level:
                values.append(node.value)
                for child in [node.left, node.right]:
                    if child is not None:
                        next_level.append(child)
            out.append(values)
            current_level = next_level
        return "\n".join([str(x) for x in out])

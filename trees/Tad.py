import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
        self.center = None
    
class TernaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node_helper(self.root, new_node)

    def insert_node_helper(self, root, new_node):
        if new_node.value < root.value:
            if root.left is None:
                root.left = new_node
            else:
                self.insert_node_helper(root.left, new_node)
        elif new_node.value > root.value:
            if root.right is None:
                root.right = new_node
            else:
                self.insert_node_helper(root.right, new_node)
        else:  
            if root.center is None:
                root.center = new_node
            else:
                self.insert_node_helper(root.center, new_node)
                 
    def pre_order(self):
        return self.pre_order_helper(self.root)
    
    def pre_order_helper(self, node):
        if node is None:
            return []
        return [node.value] + self.pre_order_helper(node.left) + self.pre_order_helper(node.center) + self.pre_order_helper(node.right)

    def in_order(self):
        return self.in_order_helper(self.root)
    
    def in_order_helper(self, node):
        if node is None:
            return []
        return self.in_order_helper(node.left) + [node.value] + self.in_order_helper(node.center) + self.in_order_helper(node.right)

    def post_order(self):
        return self.post_order_helper(self.root)
    
    def post_order_helper(self, node):
        if node is None:
            return []
        return self.post_order_helper(node.left) + self.post_order_helper(node.center) + self.post_order_helper(node.right) + [node.value]

    def search(self, value):
        return self.search_helper(self.root, value)

    def search_helper(self, root, value):
        if root is None:
            return f'Value {value} not found in the tree'
        elif root.value == value:
            return f'Value: {value} is in the tree'
        elif value < root.value:
            return self.search_helper(root.left, value)
        elif value > root.value:
            return self.search_helper(root.right, value)
        else:  
            return self.search_helper(root.center, value)

    def remove(self, value):
        self.root = self.remove_helper(self.root, value)
  
    def remove_helper(self, root, value):
        if root is None:
            return None
        elif value < root.value:
            root.left = self.remove_helper(root.left, value)
        elif value > root.value:
            root.right = self.remove_helper(root.right, value)
        else:
            if root.center is not None:
                root.center = self.remove_helper(root.center, value)
            elif root.left is None and root.right is None:
                root = None
            elif root.right is not None:
                root.value = self.successor(root)
                root.right = self.remove_helper(root.right, root.value)
            else:
                root.value = self.predecessor(root)
                root.left = self.remove_helper(root.left, root.value)
        return root
    
    def successor(self, root):
        root = root.right
        while root.left is not None:
            root = root.left
        return root.value
    
    def predecessor(self, root):
        root = root.left 
        while root.right is not None:
            root = root.right
        return root.value
    
    def add_edges(self, node, graph, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.value, pos=(x, y))
            if node.left:
                graph.add_edge(node.value, node.left.value)
                l = x - 1 / layer
                self.add_edges(node.left, graph, pos, x=l, y=y-1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.value, node.right.value)
                r = x + 1 / layer
                self.add_edges(node.right, graph, pos, x=r, y=y-1, layer=layer + 1)
            if node.center:
                graph.add_edge(node.value, node.center.value)
                c = x
                self.add_edges(node.center, graph, pos, x=c, y=y-1, layer=layer + 1)

    def draw_tree(self):
        graph = nx.DiGraph()
        pos = {}
        self.add_edges(self.root, graph, pos)
        pos = nx.get_node_attributes(graph, 'pos')
        labels = {node: node for node in graph.nodes()}
        nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False)
        plt.show()


tree = TernaryTree()
tree.insert_node(30)
tree.insert_node(20)
tree.insert_node(40)
tree.insert_node(10)
tree.insert_node(8)
tree.insert_node(8)


print("Pre-order:", tree.pre_order())
print("In-order:", tree.in_order())
print("Post-order:", tree.post_order())
print(tree.search(8))
print(tree.search(0))


tree.remove(8)
print("In-order after removing 8:", tree.in_order())

tree.draw_tree()

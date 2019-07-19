# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children
                     if child is not child_node]

  def traverse(self):
    print(self.value)
    for child in self.children:
      child.traverse()

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Head of Engineer")
first_grandchild = TreeNode('Engineer Manager')
second_grandchild = TreeNode('Project Manager')

third_child.add_child(first_grandchild)
third_child.add_child(second_grandchild)

root.add_child(first_child)
root.add_child(second_child)
root.add_child(third_child)
# root.remove_child(second_child)

root.traverse()


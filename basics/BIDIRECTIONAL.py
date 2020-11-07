import queue

class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = None
    self.visited_right = False  
    self.visited_left = False  
    self.parent_right = None  
    self.parent_left = None  


def bidirectional(s, t):

  def extract_path(node):
    node_copy = node
    path = []

    while node:
      path.append(node.value)
      node = node.parent_right

    path.reverse()
    del path[-1]  

    while node_copy:
      path.append(node_copy.value)
      node_copy = node_copy.parent_left
    return path


  q = queue.Queue()
  q.put(s)
  q.put(t)
  s.visited_right = True
  t.visited_left = True

  while not q.empty():
    n = q.get()

    if n.visited_left and n.visited_right:  
      return extract_path(n)

    for node in n.neighbors:
      if n.visited_left == True and not node.visited_left:
        node.parent_left = n
        node.visited_left = True
        q.put(node)
      if n.visited_right == True and not node.visited_right: 
        node.parent_right = n
        node.visited_right = True
        q.put(node)

  return False



n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n0.neighbors = [n1, n2]
n1.neighbors = [n2]
n2.neighbors = [n3]
n3.neighbors = [n1, n2]

print(bidirectional(n0, n3))
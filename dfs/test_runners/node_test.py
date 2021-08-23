class Node(object):
  def __init__(self, left, right, val):
    self.left, self.right, self.val = left, right, val

def run_test(func_to_test):
  node_1 = Node(None, None, 10)
  node_2 = Node(None, None, -2)
  node_3 = Node(None, None, 6)
  node_4 = Node(None, None, 8)
  node_5 = Node(None, None, -4)
  node_6 = Node(None, None, 7)
  node_7 = Node(None, None, 5)
  
  node_1.left = node_2
  node_1.right = node_3
  node_2.left = node_4
  node_2.right = node_5
  node_3.left = node_6
  node_3.right = node_7
  
  print("Testing for")
  print('''
                  10
               /      \\
             -2        6
           /   \\      /  \\ 
         8     -4    7    5''')
         
  func_to_test(node_1)
  
  # assert node_1.val == 20
  # assert node_2.val == 4
  # assert node_3.val == 12
  # assert node_4.val == 0
  # assert node_5.val == 0
  # assert node_6.val == 0
  # assert node_7.val == 0
  # print("Output passes. Looks like")

  # print('''
  #               20
  #            /      \\
  #          4         12
  #        /   \\      /  \\ 
  #      0      0    0    0''')
  
from test_runners.node_test import Node, run_test

class Solution:
  def __init__(self):
    pass

  def dfs(self,root):
    # Base case
    if root is None:
      return
    
    # Do something
    print(root.val)
    
    # Traverse
    self.dfs(root.left)
    self.dfs(root.right)
    
def main():
  sol = Solution()
  run_test(sol.dfs)

if __name__ == '__main__':
  main()
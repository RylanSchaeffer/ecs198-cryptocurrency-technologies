import hashlib
import sys

def main(input):
  with open(input) as f:
    lines = f.read().splitlines()
  curTree = lines
  x = len(curTree)
  while  x != 0 and x & (x - 1) != 0:
    curTree.append("null")
    x = x + 1
  tree = []
  i = 0
  while  i < len(curTree):
    curTree[i] = (hashlib.sha256(curTree[i]))
    i = i + 1
  while len(curTree) != 1:
    tree = []
    i = 0
    while  i < len(curTree):  
      m = hashlib.sha256(curTree[i].hexdigest())
      m.update(curTree[i+1].hexdigest())
      tree.append(m)
      i = 2 + i  
    curTree = tree 
        
  return curTree[0].hexdigest()

if __name__ =="__main__": 
  main(str(sys.argv[1]))

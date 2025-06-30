import sys
sys.setrecursionlimit(10 ** 6)

def bst(inorder):
    if not inorder:
        return None
    mid = len(inorder) // 2
    root = {
        'val': inorder[mid],
        'left': bst(inorder[:mid]),
        'right': bst(inorder[mid+1:])
    }
    return root

def postorder(node):
    if node is None:
        return
    postorder(node['left'])
    postorder(node['right'])
    print(node['val'], end=' ')

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.remove(-1)
arr.append(x)
arr.sort()
root = bst(arr)

postorder(root)
print()
import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

graph = {}
n = int(input())

for _ in range(n):
    node, left, right = input().split()
    graph[node] = (left, right)

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
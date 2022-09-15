# Notes: Week 3

## Coding Drills: Find Height of Binary Tree Variations

Important question for the interviewer:

> When determining the height of a binary tree, are we counting edges or vertices?

TODO: Review BFS on a binary tree

### Problem: Determining the height of a binary tree using breadth-first-search

```python
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

from collections import deque

def findHeightBFS(node):
    if node is None:
        return
    queue = deque([node])
    count = 0
    while len(queue):
        length = len(queue)
        count += 1
        for i in range(length):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return count
```

## BFS - Searching a tree to determine if a value exists

```python
create a queue
add the head node into the queue
while the queue is not empty:
    pop the next node
    if the node matches the value:
        you can return the node, the value,
            or true / false depending on the problem
        add the left child if it exists
        add the right child, if it exists
return false # if it gets to this point, you have iterated
through the whole tree without finding the value


def bfs(head: TreeNode, value: int):
    queue = [head]

    while len(queue):
        node = queue.pop(0)
        if node.value == value:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False
```

## Algo Blitz

### Problem: Given a binary tree, return the nodes when facing the tree from the right hand side:

Leetcode question: https://leetcode.com/problems/binary-tree-right-side-view/

```python
def rightSideView(, root: Optional[TreeNode]) -> List[int]:
        result = []
        def bfs(root,level):
            if root:
                if len(result) > level:
                    result[level].append(root.val)
                else:
                    result.append([root.val])
            bfs(root.left,level + 1)
            bfs(root.right,level + 1)
    bfs(root,0)
    return [i[-1] for i in result]
```

### Bubble Sort

I was asked a question regarding bubble sort on Algo Blitz.

Here is an implementation:
https://www.geeksforgeeks.org/bubble-sort/

### Linked List reversal:

I didn't know how to do this at the moment. I had the right idea but was tripped up on a certain point

```python
def reverse(list):
    previous = None
    current list
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous
```

### Selection Sort

Don't know how to do this either... Review this and try to memorize it

```python
def solution(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array
```

geeksforgeeks article: https://www.geeksforgeeks.org/selection-sort/

### Find the midpoint of a sorted array

```python
def solution(array, target):
    
    def helper(array, lo, hi):
        nonlocal target
        if lo > hi:
            return -1
        
        mid = (hi + lo) // 2
        if array[mid] == target:
            return mid
        
        if array[mid] > target:
            return helper(array, lo, mid-1)
        return helper(array, mid+1, hi)
    
    return helper(array, 0, len(array) - 1)
```

# Week 4 Notes

> Print values from a list in level order

```python
from collections import deque

class TreeNode:
    def __init__(self, value, left = 0, right = 0):
        self.value = value
        self.left = left
        self.right = right


def toListLevelOrder(head: TreeNode):
    # my solution
    if not head:
        return []
    
    result = []

    def bfs(node: TreeNode, children):

        queue = [node]
        children.append(node.value)

        while len(queue) > 0:
            currentLevel = []
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return children

        
    
    bfs(head, result)
    return result


def DonaldBFS(root: TreeNode):
    # his solution
    queue = deque()

    queue.append(root)
    ans = []

    while queue:
        currentLevel = []
        #"Level Order Traversal"
        for _ in range(len(queue)):
            node = queue.popleft()
            currentLevel.append(node.value)
            #print(currentLevel)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(currentLevel)

    return ans

tree1 = TreeNode(1, TreeNode(2), TreeNode(3))

print(toListLevelOrder(tree1))
```

## Trie

* Trie is a tree data structure used for storing collections of strings.
* If two strings have a common prefix then they will have the same ancestor in the tree.
* Tries are ideal for storing words found in a dictionary (book, not a python dictionary).
* Tries can also be used to perform perfect space search and you can sort the strings lexographically.

### Data Structure

```python
class TrieNode:
    def __init__(self):
        self.map = {} # key = character, value = parent
        self.endOfWord = Boolean # character representing the TrieNode is the end of word
```

### Example

Watch [this](https://www.youtube.com/watch?v=AXjmTQ8LEoI) video for a description and example.

## Runtime reading

### Linear runtime

$n$ runtime. As the input grown by $n$ the amount of work necessary also increases by $n$.

Note: $n$ more elements doesn't always need exactly $n$ more work. As long as the amount of work grows linearly, the runtime will be $O(n)$

> Finding the sum of the first 5 elements in an array

Constant? We're only ever concerned with the first 5 elements, no matter the size of n. $O(5)$.

> Finding the sum of the first 5% of the elements in an array

%O(n)%. We will always be finding $5%$ of $O(n)$

> Summing two linked lists of the same length

$O(m x n)$ where $n$ is the number of elements in a linked list.

### $k \cdot n$ Runtime

Multiple variables may exist in the runtime analysis.

The example is finding the sum of k arrays, each of n length.

> Find the runtime: Find the array with the largest first element

$O(n)$ where $n$ is the number of arrays to be searched.

> Find the runtime: Find the array that has the largest sum

$O(k \cdot n)$ where $k$ is the number of arrays and $n$ is the length of an array

> Find the sum of the first array

$O(n)$ where $n$ is the length of the array

> 1. Return the number of times that elements from array2 appear in array1, without creating any new data structures.

Is this a count of the total number of repeats? If yes $O(n)$

If no, then I'm not sure how to solve the problem without a new data structure

The solution is to iterate over the longer array, and check each of its element against every element of the smaller (or equal sized) array. $O(m \cdot n)$ is the runtime where m is the number of elements in the first array and n is the number of elements in the second array.

> 2. Return the array that has the largest element (this one is a bit of a trick question)

$O(m \cdot n)$ where $m$ is the number of arrays to be searched and $n$ is the number of elements in each array

> 3. Return true if there are any elements in array1 and array2 that match, without creating any new data structures

$O(n)$ where n represents the number of elements in the shortest array.

### Quadratic

#### Selection sort

Loop through an array
Find the smallest element, swap that element with the element at position 0
Repeat the process on the rest of the array

> What is the runtime of finding the smallest element in the array?

$O(n)$ where n is the number of elements in the array

> How many times do you have to find the smallest element in the array?

$O(n)$

> Given the above answers, what is the total runtime?

$O(n^2)$

#### Practice problems. Which is $O(n^2)$

> 1. Finding the largest element across two unsorted arrays.

$O(n)$

> 2. Finding the sum of two arrays of equal length.

$O(m + n)$

> 3. Creating a matrix given an input array by repeating the input array n times, where n is the length of the input array.

$O(n^2)$ where $n$ is the number of elements in the input array.

### Common Pitfalls:

## Right tree view:

>Given a binary tree t, return its right view. To understand what the right view of the tree means, imagine yourself standing on the right side of the tree: The right view will be all the vertices that you can see. For example, imagine the following tree:

See [here](https://www.scaler.com/topics/right-view-of-a-binary-tree/) for solution descriptions.

### DFS Solution

```python
def solution(t):
    def helper(root: Tree, last_printed_level, curr_level, results):
        if not root:
            return
        if last_printed_level[0] < curr_level:
            results.append(root.value)
            last_printed_level[0] = curr_level
        helper(root.right, last_printed_level, curr_level + 1, results)
        helper(root.left, last_printed_level, curr_level + 1, results)
        return
    
    current_level = 1
    last_printed_level = [0]
    results = []
    
    helper(t, [0], 1, results)
    return results
```


## Level order traversal of a binary tree

```python
from collections import deque

def solution(node):
    queue = deque()
    queue.append(node)
    answer = []
    while len(queue):
        currentLevel = []
        for _ in range(len(queue)):
            node = queue.popleft()
            currentLevel.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        answer.append(currentLevel)
    return answer
```

Note: I need to memorize this solution. It's come up a few times and it's a simple solution compared to
the typical google search.


## Given a string, representing a binary tree, determine the max depth

```javascript
/*
You are given a binary tree that is represented by a string. Nodes have no value. 

A 0 represents null and a (00) represents a leaf node. 

((00)0) would represent a tree where the root has one left node and no right node. 
maxDepth = Math.max(maxDepth, currentDepth)
currentDepth = 0
((00)(00))
         i
  

q = '((00) 0)'
      
00 lvl = 0
       lvl1 = 
Max(i, j) 
   0
  / 
 0    
((00)(00)) represents a tree with one left and one right node.
  0
 / \
0   0
Given this representation of the tree, return an Int representing the depth of the tree.

Examples

(((00)0)0) represents this tree:
  0
 0
0


       0
     /
   0
  /
0
This would return 3.

Empty tree: "0"

(0(00)) represets:
0
 \
  0


perfect tree 
(((00)((00))((00)(00)))
*/

// an additional challenge would be to write a parser which would convert the string
// into a tree

function findMaxDepth(tree) {
  let maxDepth = 0
  let currentDepth = 0;

  for(let i = 0; i < tree.length; i++){
    let char = tree[i]    //)
    if(char === '(') currentDepth+=1      //1
    else if(char === '0') continue
    else {
      currentDepth-=1
    }
    maxDepth = Math.max(maxDepth, currentDepth);    //1
  }

  return maxDepth; //1
}
```
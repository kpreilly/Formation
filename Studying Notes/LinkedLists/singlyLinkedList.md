# Notes: Singly Linked Lists

## Data Structure

Linked Lists consist of nodes. Nodes use at least the following two fields:

* Data: holds the data type which the list will store.
* Next: A pointer to the next node in the linked list

```python
class Node:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

```

Note: The last node in a singly linked list will have a `next` field value of None, indicating that the end of the list has been reached.

Linked Lists are stored at random locations in memory. This is different from arrays, which are stored in contiguous "blocks" of memory. This is why pointers are important, so we can reliably find the list elements

### Common language:

`head` is typically a pointer which points to the start of a linked list.

### Time Complexity

* `LinkedList.insert(0)` or `LinkedList.deleteAt(`: When we're inserting at the start of the list, the operation will be $O(1)$.
* `LinkedList.insert(idx)`: Accessing the element at index `idx` in the linked list will be $O(n)$. We must traverse the list elements in order.

`LinkedList.delete` will require the same time complexity as `insert`.

### Insertion

Insertion covers three main cases:

1. `append` - add the node to the end of the list $O(n)$
2. `prepend` - add the node to the beginning of the list $O(1)$
3. `insert` - add the node to some position between the list head and end

#### `append`

```python
# LinkedList class
def append(self, data):
    new_node = Node(data)
    # empty list
    if self.head is None:
        self.head = new_node
        return
    # non-empty list
    last_node = self.head
    while last_node.next:
        last_node = last_last.next
    last_node.next = new_node
```

#### `prepend`

```python
# LinkedList class
def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

#### `insert`

Here, we want to insert an element after a given node.

```python
# LinkedList class
def insert(self, prev_node, data):
    if not prev_node:
        return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
```

#### `__str__`

```python
# LinkedList class
def __str__(self):
    return str(self.data) + ' -> ' + self.next.__str__()
```

### Deletion by Value

```python
# LinkedList class

def delete_node(self, key):
    # Case 1: delete head
    cur_node = self.head
    if cur_node and cur_node.data == key:
        self.head = cur_node.next
        cur_node = None
        return
    # Case 2: delete a node which isn't head
    prev = None
    # traverse the list
    while cur_node and cur_node.data != key:
        prev = cur_node
        cur_node = cur_node.next
    if cur_node is None:
        return
    prev.next = cur_node.next
    cur_node = None
```

### Deletion by Position

```python
# LinkedList class
def delete_node_at_position(self, pos):
    if self.head:
        cur_node = self.head
        if pos == 0:
            # Case 1: Delete at head
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        count = 0
        while cur_node and count != pos:
            # Case 2: Delete at any other location
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        
        if cur_node is None:
            return
        
        prev.node= cur_node.next
        cur_node = None
```

### Finding the length of the list

We can get the length of the list using an iterative as well as a recursive approach.

#### Iteration

```python
# LinkedList class
def len_iterative(self):
    count = 0
    cur_node = self.head
    while cur_node:
        count += 1
        cur_node = cur_node.next
    return count
```

#### Recursion

```python
# LinkedList class
def len_recursive(self, node):
    return 0 if node is None else 1 + self.len_recursive(node.next)
```

### Swapping nodes

```python
#LinkedList class
def swap_nodes(self, key_1, key_2):
    if key_1 == key_2:
        return

    # find the first node
    prev_1 = None
    curr_1 = self.next
    while curr_1 and curr_1.data != key_1:
        prev_1 = curr_1
        curr_1 = curr_1.next
    
    # find the second node
    prev_2 = None
    curr_2 = self.head
    while curr_2 and curr_2.data != key_2:
        prev_2 = curr_2
        curr_2 = curr_2.next
    
    # if either of the nodes aren't found, leave the function
    if not curr_1 or not curr_2:
        return
    
    # check to see if curr_1 is head node (curr_1 is the head if it lacks a previous node)
    if prev_1:
        prev_1.next = curr_2 # set the node preceding curr_1 to point to curr_2 (first part of the swap)
    else:
        self.head = curr_2 # if curr_1 is the head, make curr_2 the head

    # check to see if curr_2 is head node
    if prev_2:
        prev_2.next = curr_1
    else:
        self.head = curr_1
    
    # second part of the swap, set each node's next value to point to the other
    curr1.next, curr_2.next = curr_2.next, curr_1.next
```

### Reverse a Linked List

$A => B => C => D => X$
$D => C => B => A => X$

#### Iterative Implementation

```python
# LinkedList class
def reverse(self):
    prev = None
    cur = self.head
    while cur:
        nxt = cur.next  # temporary storage
        cur.next = prev # swap the pointer
        prev = cur 
        cur = nxt
    self.head = prev
```

#### Recursive Implementation

```python
# LinkedList class
def reverse_recursive(self, cur, prev):
    
    def _reverse_recursive(cur, prev):
        # swap one pair of nodes
        if not cur:
            return prev
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        return _reverse_recursive(cur, prev)
    
    self.head = _reverse_recursive(cur=self.head, prev=None)
```

### 

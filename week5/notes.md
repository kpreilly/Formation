# Notes: Week 5

## Trie implementation

```python
'''
Problem Statement

The programming interface for a legacy motor controller accepts commands as binary strings of variable length. 
The console has a very primitive autocomplete autocorrect feature: 
given an incomplete command, it will display possible commands that has the incomplete command as a prefix. 

For example, if '1010' is a possible command and the user enters '10', the interface should return '1010' as a possible autocomplete result.

Implement a data structure that will allow us to efficiently query possible autocomplete results given an incomplete input.

Examples
Possible commands = ['000', '1110', '01', '001', '110', '11', '0']

Input -> Output
'0' → ['000', '01', '001']
'1' → ['1110', '110', '11']
'00' → ['000', '001']
'1111' → []
'11' -> ['11']

Function Signature
Candidates should implement a class which should be initialized with a list of possible commands. The class should have the following public method:
           *
        0       1
      0   1*   0* 1*
    0*  1*          1
                  0*
class Autocomplete:
    __init__(dictionary: List[String]) -> None
    autocomplete(input: String) → List[String]

TrieNode:
    value: char/string
    children: Dict[string, node]
    isWord: Optional[str]

Trie:
    root_node: TrieNode
    AddCommand(command: str) -> None:
    SearchCommand(prefix: str) -> List[str]
'''

class TrieNode:
    def __init__(self, value='None'):
        self.value = value
        self.children = dict()
        self.isWord = ''

class Trie:
    def __init__(self, root):
        self.root = root
    
    def add_command(self, command):
        '''
        iterate through the command, char by char
        move through the tree, node by node
            move to next char node if it exists
            otherwise, create node
        set isWord to the command
        '''
        current = self.root
        
        for char in command:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]

        current.isWord = command
    
    def search_command(self, prefix):
        '''
        Iterate through the prefix, char by char
        Move through the tree, node by node
            If you can't find the char in prefix, return empty list
            Otherwise: 
                Go to the node corresponding to the last character in the prefix
                Do some traversal to look at every node under it
                Add each isWord node to the return list
        '''
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        output = []
        def helper(root):
            if not root: return
            
            if root.isWord:
                output.append(root.isWord)
            
            for child in root.children.values:
                helper(child)

        helper(current)
        return output
        
from typing import List

class Autocomplete():
    def __init__(self, dictionary: List[str]):
        self.root = Trie(TrieNode())
        
        for command in dictionary:
            self.root.add_command(command)

    def autocomplete(self, prefix):
        return self.root.search_command(prefix)
```

Related Leetcode question:

```python
class Trie:

    def __init__(self):
        self.child = {}

    def insert(self, word: str) -> None:
        current = self.child
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['#'] = 1

    def search(self, word: str) -> bool:
        current = self.child
        for l in word:
            if l not in current:
                return False
            current = current[l]
        return '#' in current

    def startsWith(self, prefix: str) -> bool:
        current = self.child
        for l in prefix:
            if l not in current:
                return False
            current = current[l]
        return True
```

## Binary Search

```python
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        pos = 0
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            pos = midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return (pos, found)
```

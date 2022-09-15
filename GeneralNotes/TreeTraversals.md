# Tree Traversals

Trees are a subset of the graph data structure.

## Trie

26-ary tree where each node represents a letter in English. The root node is empty.

### data structure

```python
class Node:
    def __init__(self, letter, isEndOfWord=False):
        self.letter = letter
        self.children = set()
        self.isEndOfWord = isEndOfWord
```

## Syntax Trees/ Parse Trees

Tree which structure a nested math equation.

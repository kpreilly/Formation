'''
PARTICIPANTS:
- Chris
- Kyle
- Ziran
- Uyen

PROBLEMS (ON LINKED LISTS):
1)*** function reduce(head, accumulator, initialVal) - returns single value
2)*** function map(head, mapper) - returns new list
3) function any(head, test) - returns true if at least one value passes the test function
4) *function all(head, test) - returns true if ALL of the values in the list pass the test function
5) ** BONUS: function filter(head, test) - modifies list and returns new head

'''
class LinkedNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + '->' + str(self.next.__repr__())
    
    def __str__(self):
        pass


lambda x, y: x + y

# head = 1 > 2 > 3
# accumulator = sum, init = 0
#  >> sum = 6

# empty >> initialVal
# 1> 2> 3 >> mult = 6, init = 1
# 8 > 4 > 2 >> div = 1, init = 64

def reduce(head,accumulator,initialVal):
    output = initialVal
    while head:
        output = accumulator(output,head.value)
        head = head.next
    return output

# 1 -> 5 -> 3 -> 9 -> x
# test = isEven
# None

# head == None -> None
# 

def filter(head, test):
    result = LinkedNode()
    resultPtr = result
    while head:
        if test(head.value):
            resultPtr.next = LinkedNode(head.value)
            resultPtr = resultPtr.next
        head = head.next
    return result.next

def map(head, f):
    result = LinkedNode()
    pointer = result
    while head:
        pointer.next = LinkedNode(f(head.value))
        pointer = pointer.next
        head = head.next
    return result.next

# 1->2->3->None
# f = double
# 2->4->6->None

# 1->2->3->None
# f = square
# 1->4->9->None

# test if isOdd
isOdd = lambda x: x % 2 != 0
oddList = LinkedNode(1, LinkedNode(3, LinkedNode(5)))
happyList = LinkedNode(1, LinkedNode(2, LinkedNode(4)))



print(filter(oddList, isOdd))
print(filter(happyList, isOdd))


node1 = LinkedNode(1)
node2 = LinkedNode(2)
node3 = LinkedNode(3)
node1.next = node2
node2.next = node3

accumulator = lambda x, y: x + y
mult = lambda x, y: x * y
div = lambda x, y: x // y # is this the type of division we want?

initialVal = 1

# print(reduce(node1,mult,initialVal), "should be 6")

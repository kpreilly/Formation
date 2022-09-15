'''
filter, map, and reduce notes.
'''
from functools import reduce

'''
functools.reduce(function, iterable[, initializer])
apply function of two arguments cumulatively to the items of sequence, from left to right, so as to reduce the sequence to a single value.

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
* calculates: ((((1+2)+3)+4)+5)
* x, is the accumulated value.
* y, is the update value from the sequence.

reduce implements a mathematical technique called folding (or reduction).
* useful when you need to apply a function to an iterable and reduce it to a single cumulative value.

* Apply a function (or callable) to the first two items in an iterable and generate a parital result.
* Use the partial result, together with the third item in the iterable, to generate another partial result.
* Repeat the process until the iterable is exhausted and then return a single cumulative value.
'''

# Notes for Formation: Concept Drills: Arrays
# 8-1-2022

'''
Notes: Array Concept Drill

array: contiguous block of memory
Accessing specific elements is quick. O(1)

doubling array size:

javascript: shift remove something from the beginning of the array

accumulator pattern:
find the sum of the elements of an array
Write these out in multi-line vs a one-line solution.
This will avoid confusion. As an aside: it will be good
to know how to do the one line solution.

Find Best Answer:
Example: Find the maximum of of the array:

JavaScript array talk:
javascript stores arrays as a hash table.
Javascript has no queue data structure

'''


'''
Notes: Coding Drills: Number of Unique Elements Variations

look up defaultdict. Useful for interviews

look up unittest boilerplate

import unittest

class TestExactlyTwoOccurrences(unittest.TestCase):
    def test_foo(self):
        arr = [1,2,3]
        self.assertEquals(3, exactly_two_occurrences(arr))

look up: itertools, functools, collections

itertools allow us to use iterators

iterator:
* an iterable is something that can be looped over
* in python an object is iterable if it has the function: __iter__()
    * __iter__() is a dunder, or magic method.
* an iterator is an object which keeps track of
where it is in the current iteration
* iterators can be added to your own class to make it an iterable.

look this up: https://realpython.com/python-hash-table/

Resume Review:

Next job: keep track of all projects you worked on

Compress resume to one page
Write the resume for November:
* give project ideas
* Add school projects
* future state, current state, gap analysis. Fill the gap between now and next

Format, content
Check out university resources for resume formatting

Professional
Apply for middle positions - if you're unable to do it, downgrade to junior
System design portion

Previous musician experience: soft-skills
* 1 to 1 mentoring
* interpersonal communication
* soft skills
    * good communication skills
    * leadership skills - Band management

Future resume: fill the gaps, softskills
Add musician skills! They are useful soft skills

Create a full resume which encompasses all of your experience. Then make small edits to adjust the resume over time.

Print resume and put it in front of you.
value your non-software engineering skills

prepare to explain about gpa not present
Nailed all courses =
'''
"""
Question: Find all anagrams in a list of words:

# original solution:
# NOTE: THIS DID NOT WORK
def solution(words):
    if len(words) < 1: return 0
    groups = []
    # look at each word in the list
    # for a given word, check if it is an anagram of the first element of every group
    #   a word is an anagram if the sorted versions of both words are the same
    # if the word is an anagram, add it to the current group
    # otherwise add it to a new group
    for word in words:
        if len(groups) < 1:
            groups.append[[word]]
        else:
            added = False
            for group in groups:
                for group_word in group:
                    if sorted(word) == sorted(group_word):
                        group.append(word)
                        added = True
                        break
                if added: break
            if added == False:
                groups.append([word])
    return len(groups)

# Ending solution: Remember to sort items in the future!
# This also threw an error of TypeError: Object of type set is not JSON serializable when I simply tried to count the number of elements in the set. So we have to convert a set to a list and then take it's length
def solution(words):
    if len(words) < 1: return 0
    return len(list(set([''.join(sorted(word)) for word in words])))

count letters in a string

letters = {}
for letter in str:
    letters[letter] = letters.get(letter,0) + 1


Session: Coding Drills First To K Variations
always important to relate n in O(n) to something.
In this case, O(n) relates to the number of elements in a string

interview: classic technique
clarifying questions,
edge cases
decide on data structure, confer with interviewer
Pseudocode first solution
code out the solution
"""
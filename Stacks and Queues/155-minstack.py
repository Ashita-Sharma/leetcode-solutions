'''Description: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.'''

'''Approach: First, we initialize a stack named minstack. The each element in minstack will have two data associated 
 with it-- the value itself, as well as the minimum value currently. This allows us to get the minimum value in 
 constant time. When we push a new value, we check it against our current minimum value and update it accordingly. 
 The pop, top and getmin are self-explanatory.'''


class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, value: int) -> None:
        min_val = self.getMin()
        if min_val is None or min_val > value:
            min_val = value

        self.minstack.append([value, min_val])

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1][0] if self.minstack else None

    def getMin(self) -> int:
        return self.minstack[-1][1] if self.minstack else None

#Time Complexity: O(1) for each function used
#Space complexity: O(1) for each function used
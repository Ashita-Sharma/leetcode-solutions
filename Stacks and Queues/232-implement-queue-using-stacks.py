#Description: Implement a first in first out (FIFO) queue using only two stacks. The implemented queue
#should support all the functions of a normal queue (push, peek, pop, and empty).
#Implement the MyQueue class:
#
#void push(int x) Pushes element x to the back of the queue.
#int pop() Removes the element from the front of the queue and returns it.
#int peek() Returns the element at the front of the queue.
#boolean empty() Returns true if the queue is empty, false otherwise

#Approach: Starting with the easiest to implement-
#empty() just returns true if queue does not contain anything and false otherwise.
#peek() returns the firstmost element (denoted by queue[-1])
#pop() removes the topmost element and returns it.
#push() directly appends the element if queue is empty, otherwise it shifts all elements to a different stack
#until queue is empty, then pushes the required value and then pops and pushes the elements from the
#temporary stack.


class MyQueue:

    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, x: int) -> None:
        if not self.queue:
            self.queue.append(x)
        else:
            while self.queue:
                self.stack.append(self.queue.pop())
            self.queue.append(x)
            while self.stack:
                self.queue.append(self.stack.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False
#Time Complexity: O(2n) for pushing, O(1) otherwise.
#Space complexity: O(n), because of stack

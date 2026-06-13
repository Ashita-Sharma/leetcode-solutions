#Description: Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support
#all the functions of a normal stack (push, top, pop, and empty).
#Implement the MyStack class:
#
#void push(int x) Pushes element x to the top of the stack.
#int pop() Removes the element on the top of the stack and returns it.
#int top() Returns the element on the top of the stack.
#boolean empty() Returns true if the stack is empty, false otherwise.

#Approach: Starting with the easiest to implement-
#empty() just returns true if stack does not contain anything and false otherwise.
#peek() returns the firstmost element (denoted by stack[0])
#pop() removes the topmost element and returns it.
#push() directly appends the element if stack is empty, otherwise it shifts all elements to a different queue
#until stack is empty, then pushes the required value and then pops and pushes the elements from the
#temporary queue.


class MyStack:

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
        else:
            while self.stack:
                self.queue.append(self.stack.pop(0))
            self.stack.append(x)
            while self.queue:
                self.stack.append(self.queue.pop(0))
    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack

#Time Complexity: O(2n) for pushing, O(1) otherwise.
#Space complexity: O(n), because of stack
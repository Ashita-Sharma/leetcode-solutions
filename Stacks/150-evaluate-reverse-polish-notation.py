#Description: You are given an array of strings tokens that represents an arithmetic expression in a
#Reverse Polish Notation. Evaluate the expression. Return an integer that represents the value of
#the expression.

#Approach Description: Let us iterate through each token in tokens. If token is a number,
#i.e. not an operator, we push it onto the stack. If it is an operator, we pop out last two elements,
#naming them b and a, and operate accordingly.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    stack.append(int(a / b))

        return stack[0]

#Time Complexity: O(n)
#Space complexity: O(n), because of stack

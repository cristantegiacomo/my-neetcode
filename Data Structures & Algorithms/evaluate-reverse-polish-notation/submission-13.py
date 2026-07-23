class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i,t in enumerate(tokens):
            if t in ('+','-','*','/'):
                y=int(stack.pop())
                x=int(stack.pop())
                if t=='+':   stack.append(x+y)
                elif t=='-': stack.append(x-y)
                elif t=='*': stack.append(x*y)
                elif t=='/': stack.append(int(x/y))
            else:
                stack.append(t)
        return int(stack[-1])

# soluzione più pulita
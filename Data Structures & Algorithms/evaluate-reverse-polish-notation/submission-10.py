class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i,t in enumerate(tokens):
            if t not in ('+','-','*','/'):
                stack.append(t)
            elif t=='+':
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(x+y)
            elif t=='-':
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(x-y)
            elif t=='*':
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(x*y)
            elif t=='/':
                y=int(stack.pop())
                x=int(stack.pop())
                stack.append(x/y)
        return int(stack[-1])



    
# 1,2,3,+,*,6,- = 1*(2+3)-6
# 1, 2, 3, 6
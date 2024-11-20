class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        notations = {"+","-","*","/"} 
        stack = []
        num = 0

        for t in tokens: 
            if t in notations:
                val = stack.pop() 
                
                if t == "+":
                    stack[-1] = stack[-1] + val 
                elif t == "-":
                    stack[-1] = stack[-1] - val 
                elif t == "*":
                    stack[-1] = stack[-1] * val
                elif t == "/":
                    stack[-1] = int(stack[-1] / val)
            
            else:
                #if t.isdigit(): can't handle nagative number
                stack.append(int(t)) 
        return sum(stack)

class Solution: 
    def isValid(self, s): 
        checker = {")":"(", "}":"{", "]":"["}
        stack = []
        for _s in s:
            if _s in checker:
                if stack == []:
                    return False
                    
                last = stack.pop() 
                if checker[_s] != last:
                    return False 
            else:
                stack.append(_s)
        
        return len(stack)==0
            

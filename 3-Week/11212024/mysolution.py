class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        ans = []  
        def BT(open_count, close_count, path):
            if len(path) == n*2:
                ans.append("".join(path))
                return 
            if open_count < n:
                path.append("(")
                BT(open_count + 1,close_count, path) 
                path.pop() 
            if close_count < open_count:
                path.append(")")
                BT(open_count,close_count +1, path)  
                path.pop() 
            
        BT(0,0,[])
        return ans

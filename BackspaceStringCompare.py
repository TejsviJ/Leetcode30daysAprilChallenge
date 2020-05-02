class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sk=[]
        tk=[]
        for i in range (len(S)):
            if S[i]!='#':
                sk.append(S[i])
            elif sk:
                sk.pop(-1)
        
        
        for i in range (len(T)):
            if T[i]!='#':
                tk.append(T[i])
            elif tk:
                tk.pop(-1)
        if tk==sk:
            return True
        else:
            return False
                

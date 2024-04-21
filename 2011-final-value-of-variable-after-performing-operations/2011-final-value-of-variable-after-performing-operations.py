class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        init = 0
        for i in operations:
            if i == "++X" or i == "X++":
                init = init + 1
            if i == "--X" or i == "X--":
                init = init - 1
        return init
                
        
        
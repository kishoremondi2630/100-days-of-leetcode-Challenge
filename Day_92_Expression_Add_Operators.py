class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        n = len(num)
        
        def dfs(index, path, value, prev):
            if index == n:
                if value == target:
                    result.append(path)
                return
            
            curr_num = 0
            for i in range(index, n):
                # No leading zero for multi-digit numbers
                if i > index and num[index] == '0':
                    return
                    
                curr_num = curr_num * 10 + int(num[i])
                curr_str = str(curr_num)
                
                if index == 0:
                    # First number
                    dfs(i + 1, curr_str, curr_num, curr_num)
                else:
                    # Addition
                    dfs(i + 1, path + '+' + curr_str, value + curr_num, curr_num)
                    # Subtraction
                    dfs(i + 1, path + '-' + curr_str, value - curr_num, -curr_num)
                    # Multiplication
                    dfs(i + 1, path + '*' + curr_str, value - prev + prev * curr_num, prev * curr_num)
        
        dfs(0, "", 0, 0)
        return result

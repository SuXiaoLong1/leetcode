# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics 数组 回溯 👍 1560 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        n = len(candidates)
        if n==1:
            if candidates[0]==target:
                return [candidates]
            else:
                return []
        candidates.sort()
        res=[]
        for i in range(n):
            if i>0 and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]<target:
                mid=self.combinationSum2(candidates[i+1:],target-candidates[i])
                for j in mid:
                    res.append([candidates[i]]+j)
            elif candidates[i]==target:
                res.append([candidates[i]])
                break
        return res

# leetcode submit region end(Prohibit modification and deletion)

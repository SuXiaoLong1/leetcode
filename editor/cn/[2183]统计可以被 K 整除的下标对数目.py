# 给你一个下标从 0 开始、长度为 n 的整数数组 nums 和一个整数 k ，返回满足下述条件的下标对 (i, j) 的数目： 
# 
#  
#  0 <= i < j <= n - 1 且 
#  nums[i] * nums[j] 能被 k 整除。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3,4,5], k = 2
# 输出：7
# 解释：
# 共有 7 对下标的对应积可以被 2 整除：
# (0, 1)、(0, 3)、(1, 2)、(1, 3)、(1, 4)、(2, 3) 和 (3, 4)
# 它们的积分别是 2、4、6、8、10、12 和 20 。
# 其他下标对，例如 (0, 2) 和 (2, 4) 的乘积分别是 3 和 15 ，都无法被 2 整除。    
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,2,3,4], k = 5
# 输出：0
# 解释：不存在对应积可以被 5 整除的下标对。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i], k <= 10⁵ 
#  
# 
#  Related Topics 数组 数学 数论 👍 62 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
# leetcode submit region end(Prohibit modification and deletion)

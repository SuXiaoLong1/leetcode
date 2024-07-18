# 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。 
# 
#  点的坐标 pi 表示为 [xi, yi] 。 输入没有任何顺序 。 
# 
#  一个 有效的正方形 有四条等边和四个等角(90度角)。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# 输出：false
#  
# 
#  示例 3: 
# 
#  
# 输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# 输出：true
#  
# 
#  
# 
#  提示: 
# 
#  
#  p1.length == p2.length == p3.length == p4.length == 2 
#  -10⁴ <= xi, yi <= 10⁴ 
#  
# 
#  Related Topics 几何 数学 👍 180 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        l1=dist(p1,p2)
        l2=dist(p1,p3)
        l3=dist(p1,p4)
        l4=dist(p2,p3)
        l5=dist(p2,p4)
        l6=dist(p3,p4)
        l=[l1,l2,l3,l4,l5,l6]
        l=sorted(l)
        if l[0]==l[1]==l[2]==l[3] and l[4]==l[5] and l[0]!=0:
            return True
        return False
# leetcode submit region end(Prohibit modification and deletion)

# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


class Solution:
    def reverseBits(self, num: int) -> int:
        mid = [0]
        n = 1
        while num != 0:
            a = num % 2
            if a == 1:
                mid[-1] += 1
            else:
                mid.append(0)
                n += 1
            num = num // 2

        res = mid[0]

        for i in range(1, n):
            res = max(res, mid[i - 1]+ mid[i])

        return res + 1


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    print(1)
    num=2147482622
    a=Solution()
    print(a.reverseBits(num))
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


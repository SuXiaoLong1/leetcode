# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        if n<2:
            return 0
        if n<=10:
            return 1
        res=0
        ninety=0
        flag=1
        m=0
        while n!=0:
            k=n%10
            n=n//10

            if k<2:
                res=res+k*ninety
            elif k==2:
                res=res+m+1+k*ninety
            else:
                res=res+k*ninety+flag
            ninety=10*ninety+flag
            m += k * flag
            flag*=10

        return res



# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    import sys

    try:
        while True:
            line = sys.stdin.readline()
            n = int(line[:-1])
            triangle = [[1], [1, 1, 1]]
            for i in range(2, n):
                triangle.append([])
                for j in range(i + 1):
                    if j == 0:
                        triangle[i].append(1)
                    elif j == 1:
                        triangle[i].append(i)
                    else:
                        triangle[i].append(triangle[i - 1][j - 2] + triangle[i - 1][j-1] + triangle[i - 1][j])
                for j in range(i):
                    triangle[i].append(triangle[i][i - j - 1])
            flag = -1
            for num in range(n-1):
                if triangle[n-1][num] % 2 == 0:
                    flag = num + 1
                    break
            print(flag)



    except:
        pass

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


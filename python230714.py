# 代码文件: ch88/ch8_5.py

# 创建全局变量x
x=20
def printvalue():
    global x
    x = 10
    print("函数中x = {0}".format(x))
printvalue()
print("全局变量x = {0}".format(x))
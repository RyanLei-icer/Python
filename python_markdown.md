# python_markdown

```python {cmd=true matplotlib=true}
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show() # show figure
```

```python {cmd=true matplotlib=true}
import math
import matplotlib.pyplot as plt
# x = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
x = [x/100 for x in range(0, 1001)]
y = [math.sin(i) for i in x]
plt.plot(x, y)
plt.grid(True, color="red", linestyle="--")
# 显示网格线，颜色为红色，样式为虚线
plt.show() # show figure
```

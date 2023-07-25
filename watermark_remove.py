from PIL import Image
import fitz
import os

from PyPDF4 import PdfFileReader,PdfFileWriter
from PyPDF4.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_

def get_file_dir():
    # gui输入文件地址
    import tkinter as tk
    from tkinter import filedialog
    import ctypes
    root = tk.Tk()  #创建窗口，root可替换成自己定义的窗口
    root.withdraw() #将窗口隐藏到屏幕外，但仍然保持窗口对象的存在

    # 高分屏dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  #调用api设置成由应用程序缩放
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0) #调用api获得当前的缩放因子
    root.tk.call('tk', 'scaling', ScaleFactor/75)   #设置缩放因子
    file_dir = filedialog.askopenfilename()
    # 将路径中的正斜杠替换为反斜杠
    file_dir = file_dir.replace("/", "\\")
    print(file_dir)
    return file_dir


output = PdfFileWriter()
RD_dir = get_file_dir()
# 分离出文件名和路径
file_dir, file_name = os.path.split(RD_dir)
WR_dir = os.path.join(file_dir,"removed_"+file_name)
pdf = PdfFileReader(RD_dir)
pdf1=pdf.getPage(195)
# 获取pdf一页的内容
content_object = pdf1.getContents()
content = ContentStream(content_object, pdf)
for operands, operator in content.operations:
    # 根据要去除的水印格式是“Tj”文本
    if operator == b_("University"):
        # 将获取的文本替换为空
        operands[0] = TextStringObject('')
# 转换原来的内容对象
pdf1.__setitem__(NameObject('/Contents'), content)
# 增加到新的pdf上
output.addPage(pdf1)

# 输入新的pdf文件
with open(WR_dir, "wb") as outputStream:
    output.write(outputStream)

with open("WR_dir",'wb') as ouf:
    output.write(ouf)

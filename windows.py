import main
import tkinter as tk
from tkinter import *

windows = tk.Tk()
windows.title('总之就是非常好用')
windows.geometry('678x341')
windows.resizable(0,0)
Label1=tk.Label(windows,text="目录:")
Label1.place(height = 39,width = 77,x = 6,y = 11)
rootBox=tk.Entry(windows)
rootBox.place(height = 39,width = 502,x = 87,y = 11)
output=tk.Text(windows)
output.place(height = 254,width = 650,x = 6,y = 69,)


def Find():
    root = rootBox.get()
    videolist = main.FindAllVideo(root)
    output.text = '共找到%d个视频请稍等...' % len(videolist)
    for one in videolist:
        output.insert(END,'正在编码:'+one['title'] + '\n')
        output.insert(END,main.CodeVideo([one],root))
        #output.insert(END,main.CodeVideo([one],root))

Findbutton=tk.Button(windows,text = '寻找',command = Find)
Findbutton.place(height = 39,width = 76,x = 592,y = 11)

windows.mainloop()

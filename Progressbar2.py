from tkinter import *
import tkinter.ttk as ttk
import time, threading
from tkinter import messagebox
root = Tk()

bar = ttk.Progressbar(root, mode="determinate")
bar.pack()

def progress():
	for i in range(20):
		bar['value'] += i
		time.sleep(.1)
		if bar['value'] == 20:
			messagebox.showinfo('title', 'DONE!)')

threading.Thread(target=progress).start()
root.mainloop()

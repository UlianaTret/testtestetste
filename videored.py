import moviepy.editor
from tkinter import *

def icheckkkk():
	file_name = str(edit2.get())
	video = moviepy.editor.VideoFileClip(file_name + '.mp4')
	audio = video.audio
	audio.write_audiofile( file_name +'.mp3')
	t3.config(text = 'YOUR FILE IS READY)')

##########dialog_windows##########################
win = Tk()
win.geometry('500x200')
win.resizable(width = False, height = False)

t1 = Label(win, text = 'from mp4 to mp3', fg = 'black')
t1.config(font=('courier new', 15))
t1.pack()

t2 = Label(win, text = 'write name file\nfor example: singer - Song', fg = 'grey')
t2.config(font=('courier new', 15))
t2.pack()
edit2 = Entry (win, width = 50, bg = 'Lavender')
edit2.pack()

t31 = Label(win, text = '')
t31.pack()

but = Button(win, text = 'get audio file', command = icheckkkk)
but.config(font=('courier new', 10))
but.pack()

t3 = Label(win, text = '', fg = 'purple')
t3.config(font=('courier new', 15))
t3.pack()

win.mainloop()
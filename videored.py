import moviepy.editor #import *
from tkinter import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#videored.py
#SKAM France S6 - Teaser
def icheckkkk():
	file_name = str(edit2.get())
	t_start = edit3.get()
	t_end = edit4.get()
	if (t_start != '' and t_end != ''):
		video = ffmpeg_extract_subclip(file_name + '.mp4', int(t_start), int(t_end), targetname="testtt.mp4")
		video = moviepy.editor.VideoFileClip('testtt.mp4')
	else:
		video = moviepy.editor.VideoFileClip(file_name +'.mp4')
	audio = video.audio
	audio.write_audiofile( file_name +'.mp3')
	t32.config(text = 'YOUR FILE IS READY)')

##########dialog_windows##########################
win = Tk()
win.geometry('500x500')
win.resizable(width = False, height = False)

t1 = Label(win, text = 'from mp4 to mp3', fg = 'black')
t1.config(font=('courier new', 15))
t1.pack()

t2 = Label(win, text = 'write name file\nfor example: singer - Song', fg = 'grey')
t2.config(font=('courier new', 15))
t2.pack()
edit2 = Entry (win, width = 50, bg = 'Lavender')
edit2.pack()

t3 = Label(win, text = 'time start with', fg = 'black')
t3.config(font=('courier new', 15))
t3.pack()
edit3 = Entry (win, width = 50, bg = 'Lavender')
edit3.pack()

t4 = Label(win, text = 'time end with', fg = 'black')
t4.config(font=('courier new', 15))
t4.pack()
edit4 = Entry (win, width = 50, bg = 'Lavender')
edit4.pack()

t31 = Label(win, text = '')
t31.pack()

but = Button(win, text = 'get audio file', command = icheckkkk)
but.config(font=('courier new', 10))
but.pack()

t32 = Label(win, text = '', fg = 'purple')
t32.config(font=('courier new', 15))
t32.pack()

win.mainloop()

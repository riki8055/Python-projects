from moviepy.editor import *
import os
from tkinter import messagebox, filedialog

def browse1(source_Directory):
	source_Directory = filedialog.askopenfilename(initialdir="E:\\")	# This can be optional/user based
	return source_Directory

def browse2(dest):
	destination_Directory = filedialog.asksaveasfilename(initialdir="E:\\")		# This can be optional/user based
	dest = destination_Directory+".mp3"		# Adding '.mp3' at the end of the file to avoid any confusion
	return dest

def convert(mp4, mp3):
	video = VideoFileClip(os.path.join(mp4))
	video.audio.write_audiofile(os.path.join(mp3))

	### BONUS STEP ###
	index_pos = len(mp3) - mp3[::-1].index("/") - 1
	destination_Folder = mp3[:index_pos:]
	name = mp3[index_pos+1:]

	messagebox.showinfo("FINISHED!" ,"Successfully converted and saved in "+destination_Folder+" as "+name)		#Displaying a confirmation message

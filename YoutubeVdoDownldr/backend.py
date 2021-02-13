from tkinter import messagebox, filedialog
from pytube import YouTube

# Defining Browse() to select a
# destination folder to save the video
def browse(download_Directory):
	# Presenting user with a pop-up for 
	# directory selection. initialdir  
	# argument is optional Retrieving the 
	# user-input destination directory and 
	# storing it in downloadDirectory 
	download_Directory = filedialog.askdirectory(initialdir="E:\Videos")

	# Displaying the directory in the
	# directory textbox
	return download_Directory

# Defining Download() to download
# the video
def download(yt_link, download_Folder):
	# # Getting user input Youtube link
	# yt_link = e2_value.get()

	# # Select the optimal location for
	# # saving file
	# download_Folder = d2_value.get()

	# Creating object of YouTube()
	getVdo = YouTube(yt_link)

	# Getting all the available streams of the 
	# youtube video and selecting the first 
	# from the list
	vdoStream = getVdo.streams.first()

	# Downloading the video to the
	# destination directory
	vdoStream.download(download_Folder)

	# Displaying the message
	messagebox.showinfo("FINISHED!" ,"Successfully downloaded and saved in "+download_Folder)
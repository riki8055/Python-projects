from tkinter import *
import backend as bck

# Declaring a class
class Converter:

	# The source() command will ask for the source directory
	# to pick the MP4 version (as '.mp4')
	def source(self):
		self.e1_value.set(bck.browse1(self.e1_value.get()))

	# The destination() command will ask for the directory
	# where to save the MP3 version (as '.mp3')
	def destination(self):
		self.e2_value.set(bck.browse2(self.e2_value.get()))

	# The conv() command will convert MP4 version to the MP3 version
	def conv(self):
		bck.convert(self.e1_value.get(), self.e2_value.get())

	# Initializing the frame
	def __init__(self, root):
		self.f = Frame(root, width=300, height=300, bg='#2f3e46')
		self.f.propagate(0)		# avoid frame to propagate
		self.f.pack()

		self.l1 = Label(self.f, text='Source', font=('Calibri', -24))
		self.l1.pack(pady=10)

		self.e1_value = StringVar()
		self.e1 = Entry(self.f, textvariable=self.e1_value, font=('Body+'))
		self.e1.pack()

		self.b1 = Button(self.f, text='Browse', width=6,
			bg='#4895ef', command=self.source)
		self.b1.pack(pady=5)

		self.l2 = Label(self.f, text='Destination', font=('Calibri', -24))
		self.l2.pack(pady=10)

		self.e2_value = StringVar()
		self.e2 = Entry(self.f, textvariable=self.e2_value, font=('Body+'))
		self.e2.pack()

		self.b2 = Button(self.f, text='Browse', width=6,
			bg='#4895ef', command=self.destination)
		self.b2.pack(pady=5)

		self.b3 = Button(self.f, text='Convert', width=10, font='Calibri',
			cursor='hand2', bg='#06d6a0', command=self.conv)
		self.b3.pack(pady=15)

root = Tk()
root.title('MP4 Converter')
root.wm_iconbitmap('icon.ico')
root.resizable(False, False)	# Restrict the resizable property
mb = Converter(root)	# Making the class 'Converter' an object
root.mainloop()

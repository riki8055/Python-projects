from tkinter import *
import backend as bck

class YTVD:

	def btn(self, n):
		if n==1:
			self.e2_value.set(bck.browse(self.e2_value.get()))
			# print('Browse')
		if n==2:
			bck.download(self.e1_value.get(), self.e2_value.get())
			# print('RISHI')

	def __init__(self, root):
		self.f = Frame(root, width=350, height=300, bg='#606c38')
		self.f.propagate(0)
		self.f.pack()

		self.l1 = Label(self.f, text='Video link', font=('Calibri', -20))
		self.l1.pack(pady=10)

		self.e1_value = StringVar()
		self.e1 = Entry(self.f, textvariable=self.e1_value, font=('Body+'), width=28)
		self.e1.pack()

		self.l2 = Label(self.f, text='Destination', font=('Calibri', -20))
		self.l2.pack(pady=10)

		self.e2_value = StringVar()
		self.e2 = Entry(self.f, textvariable=self.e2_value, font=('Body+'))
		self.e2.pack()

		self.b1 = Button(self.f, text='Browse', font=('Calibri', -13),
			bg='#8a817c', fg='#ffffff', command=lambda:self.btn(1))
		self.b1.place(x=237, y=160)

		self.b2 = Button(self.f, text='Download', font=('Calibri', -20),
			cursor='hand2', bg='#9bf6ff', command=lambda:self.btn(2))
		self.b2.pack(pady=50)

root = Tk()
root.title('YouTube Video Downloader')
root.resizable(False, False)
yt = YTVD(root)
root.mainloop()
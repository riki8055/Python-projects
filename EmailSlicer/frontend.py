from tkinter import *
import backend as bck

class EmailSlicer:

	def Slice(self):
		self.t1.delete('1.0', END)
		for row in bck.username(self.e1_value.get()):
			self.t1.insert(END, row)

		self.t2.delete('1.0', END)
		for row in bck.domain(self.e1_value.get()):
			self.t2.insert(END, row)

	def __init__(self, root):
		self.f = Frame(root, width=300, height=350, bg='#293241')
		self.f.propagate(0)
		self.f.pack()

		self.l1 = Label(self.f, text='Email', font=('Calibri', -20))
		self.l1.pack(pady=10)
		
		self.e1_value = StringVar()
		self.e1 = Entry(self.f, textvariable=self.e1_value, font=('Calibri'), width=25)
		self.e1.pack()

		self.b = Button(self.f, text='Slice', font=('Calibri'), cursor='hand2',
			bg='#588157', fg='#e2eafc', width=10, command=self.Slice)
		self.b.pack(pady=10)

		self.l2 = Label(self.f, text='Username', font=('Calibri', -18))
		self.l2.pack(pady=10)
		self.t1 = Text(self.f, font=('Calibri'), width=20, height=1)
		self.t1.pack()
		self.l3 = Label(self.f, text='Domain', font=('Calibri', -18))
		self.l3.pack(pady=10)
		self.t2 = Text(self.f, font=('Calibri'), width=20, height=1)
		self.t2.pack()

root = Tk()
root.title('Email Slicer')
root.resizable(False, False)
mb = EmailSlicer(root)
root.mainloop()

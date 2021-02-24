from tkinter import *
import backend as bck
import time

class DictionaryApp:

	def btn(self, n):
		if n==1:
			print('Yes')
			time.sleep(0.25)
			self.lbl.destroy()
			self.btnY.destroy()
			self.btnN.destroy()
			# self.e1_value.set()
		if n==2:
			time.sleep(0.25)
			self.lbl.destroy()
			self.btnY.destroy()
			self.btnN.destroy()
			self.m = Label(self.f, text="The word doesn't exist.\nPlease double-check it!",
				font=('Calibri', 14), bg='#3a0ca3', fg='#ced4da')
			self.m.place(x=50, y=130)
			self.m.after(4000, self.m.destroy)

	def click(self):

		self.t1.delete('1.0', END)

		if(len(self.e1_value.get()) > 0):
			word = self.e1_value.get()
			
			output = bck.translate(word)

			if type(output) == list:
				for item in output:
					txt = '• ' + item + '\n'
					self.t1.insert(END, txt)
			else:
				self.lbl = Label(self.f, text=output, font=('Calibri', 16),
					bg='#3a0ca3', fg='#ced4da')
				# self.lbl.pack()
				self.lbl.place(x=50, y=130)
				self.btnY = Button(self.f, text="Yes", bg='#06d6a0', font=('Calibri', 12),
					cursor='hand2', command=lambda:self.btn(1))
				self.btnN = Button(self.f, text="No", bg='#ffd166', font=('Calibri', 12),
					cursor='hand2', command=lambda:self.btn(2))
				self.btnY.place(x=210, y=165)
				self.btnN.place(x=250, y=165)
				# self.t1.insert(END, output)
				# self.lbl.insert(END, output)
		else:
			self.m = Message(self.f, text='Nothing in there!!', font=('Calibri', 14),
				bg='#3a0ca3', fg='#ced4da')
			self.m.place(x=50, y=130)
			self.m.after(4000, self.m.destroy)

	def __init__(self, root):

		self.f = Frame(root, width=370, height=400, bg='#3a0ca3')
		self.f.propagate(0)
		self.f.pack()

		self.l1 = Label(self.f, text='Enter a Word', font=('Calibri', 18))
		self.l1.pack(pady=2.5)
		# self.l1.place(x=115, y=10)

		self.e1_value = StringVar()
		self.e1 = Entry(self.f, textvariable=self.e1_value, font=('Body', 20))
		self.e1.pack(pady=2.5)
		# self.e1.place(x=33, y=52)

		self.b1 = Button(self.f, text='Click', font=('Calibri'), width=5,
			cursor='hand2', bg='#8d99ae', command=self.click)
		self.b1.pack(pady=2.5)

		self.l2 = Label(self.f, text='Definition', font=('Calibri', 18))
		# self.l2.pack(pady=2.5)
		self.l2.place(x=134, y=206)

		self.t1 = Text(self.f, height=6, width=31, font=('Body'))
		# self.t1.pack(pady=2.5)
		self.t1.place(x=12, y=247)

root = Tk()

root.title('The Ultimate Dictionary')

root.resizable(False, False)

da = DictionaryApp(root)

root.mainloop()
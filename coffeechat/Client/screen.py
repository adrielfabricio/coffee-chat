from tkinter import *


def window(root):

	root.title("CoffeeChat")
	width = 500
	heigth = 340
	x = (root.winfo_screenwidth() // 2) - (width // 2)
	y = (root.winfo_screenheight() // 2) - (heigth // 2)
	root.geometry('{}x{}+{}+{}'.format(width, heigth, x, y))


def set_user(username):

	user = username
	Label(frame_side, text=username, wraplength=20, anchor="w",
	      justify=LEFT).pack()


def set_message(event):

	message = entry.get()

	if message.isspace():

		Label(scrollable_frame,
		      text=user,
		      wraplength=370,
		      anchor="w",
		      justify=LEFT,
		      width='50').pack()
		Label(scrollable_frame,
		      text=message,
		      wraplength=370,
		      anchor="w",
		      justify=LEFT,
		      width='50').pack()
		Label(
		    scrollable_frame,
		    text=
		    '_______________________________________________________________________',
		    wraplength=370,
		    anchor="w",
		    justify=LEFT,
		    width='50').pack()

		return message

	return " "


def clear_message(event):

	# print("You clicked the fucking entry")
	entry.delete(0, END)


def start_screen():

	global scrollable_frame
	global entry
	global user
	global frame_side

	win = Tk()
	window(win)
	win.resizable(height=False, width=False)

	# FRAME
	frame = Frame(win)
	frame_side = Frame(frame, bg='white')

	# TITULO - PRINCIPAL
	label = Label(win,
	              text="Redes - CoffeeChat",
	              font="Helvetica 16 bold italic")

	# TITULO - LADO
	label_side = Label(frame_side,
	                   text="Usuários",
	                   font="Helvetica 10 bold italic",
	                   justify='left')

	# CANVAS SCROLL
	canvas = Canvas(frame)
	scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
	scrollable_frame = Frame(canvas)
	scrollable_frame.bind(
	    "<Configure>",
	    lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

	canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
	canvas.configure(yscrollcommand=scrollbar.set)

	# MENSAGEM
	entry = Entry(win,
	              width='85',
	              borderwidth=18,
	              bg='#ccc',
	              relief=FLAT,
	              font='Times 10')

	# PACK - BINDA AS TELAS
	label.pack()
	frame.pack()
	frame_side.pack(fill='both', side=RIGHT)
	label_side.pack()

	canvas.pack(side="left", fill="both", expand=True)
	scrollbar.pack(side="right", fill="both")
	entry.pack()

	# EXTRA - BINDING ETC ...
	entry.insert(0, "Digite algo e aperte enter ...")
	entry.bind('<Return>', set_message)
	entry.bind('<Button-1>', clear_message)

	# STARTA A TELA PRINCIPAL
	win.mainloop()
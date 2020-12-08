import argparse
import threading
import tkinter as tk
import coffeechat.Client as Client


def main(host, port):
	
 	#JANELA
	client = Client.Client(host, port)
	receive = client.start()
	window = tk.Tk()
	window.title('CoffeeChat')
	window.resizable(height=False, width=False)
 
	# COMPONENTES
	frm_messages = tk.Frame(master=window)
	scrollbar = tk.Scrollbar(master=frm_messages)
	messages = tk.Listbox(master=frm_messages, yscrollcommand=scrollbar.set)
	scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
	messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

	client.messages = messages
	receive.messages = messages

	# IMAGEM E FORM
	frm_messages.grid(row=0, column=0, columnspan=2, sticky="nsew")
	# img = tk.PhotoImage(file='logo.png')
	# label = tk.Label(window, image=img,borderwidth=0)
	
	#INPUT
	frm_entry = tk.Frame(master=window)
	text_input = tk.Entry(master=frm_entry)
	text_input.pack(fill=tk.BOTH, expand=True)
	text_input.bind("<Return>", lambda x: client.send(text_input))
	text_input.insert(0, "Digite algo e aperte enter, ou clique enviar.")
	text_input.bind("<Button-1>", lambda x: text_input.delete(0,tk.END))
	text_input.focus()
	
	btn_send = tk.Button(master=window,
	                     text='Enviar',
	                     command= lambda:client.send(text_input),
                       relief='flat',
                       bg='#ddd')
	#PACK OU GRID
	frm_entry.grid(row=1, column=0, padx=10, sticky="ew")
	btn_send.grid(row=1, column=1, pady=10, sticky="ew")
	# label.place(in_=window, anchor="c", relx=.5, rely=.5)

	#CONFIG
	window.rowconfigure(0, minsize=500, weight=1)
	window.rowconfigure(1, minsize=50, weight=0)
	window.columnconfigure(0, minsize=500, weight=1)
	window.columnconfigure(1, minsize=200, weight=0)

	window.mainloop()

def redirect(host, port, window):
	
	host = host_input.get()
	window.destroy()
	main(host, 1060)



if __name__ == "__main__":
  
	window = tk.Tk()
	window.title('Cliente - Conexão ao Host')
	host_input = tk.Entry(master=window, width='50', borderwidth=18,
								bg='#ccc', relief=tk.FLAT, font='Times 10')
	host_input.pack(fill=tk.BOTH, expand=True)
	host_input.bind("<Return>", lambda x: redirect(host_input.get(), 1060, window) )
	host_input.insert(0, "Digite o endereço de Host que deseja se Conectar, ex: localhost")
	host_input.bind("<Button-1>", lambda x: host_input.delete(0,tk.END))
	host_input.focus()

	width = 450
	heigth = 50
	x = (window.winfo_screenwidth()//2) - (width//2)
	y = (window.winfo_screenheight()//2) - (heigth//2)
	window.geometry('{}x{}+{}+{}'.format(width, heigth, x, y))

	window.mainloop()
	# parser = argparse.ArgumentParser(description='CoffeChat Client')
	# parser.add_argument('host', help='Interface the server listens at')
	# parser.add_argument('-p',
	#                     metavar='PORT',
	#                     type=int,
	#                     default=1060,
	#                     help='TCP port (default 1060)')
	# args = parser.parse_args()

	# Create and start server thread
	# main(args.host, args.p)
	# client = Client.Client(args.host, args.p)
	# client.start()

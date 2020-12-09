"""Inicialização do cliente e sua interface GUI"""
import os
import argparse
import threading
import tkinter as tk
import coffeechat.Client as Client


def main(host, port):
	"""
	Configuração do cliente e inicializa a interface gráfica.
	
	Attributes:
		host (str): Endereço IP do socket.
		port (int): Número da porta do socket.
	"""
	# Janela
	client = Client.Client(host, port)
	receive = client.start()
	window = tk.Tk()
	window.title('CoffeeChat')
	window.resizable(height=False, width=False)
	if os.name == 'nt':
		window.iconbitmap('logo_2.ico')
	window.config(background='#3c3939')

	# Componentes
	frm_messages = tk.Frame(master=window, bg='#3c3939')
	scrollbar = tk.Scrollbar(master=frm_messages)
	messages = tk.Listbox(master=frm_messages,
	                      yscrollcommand=scrollbar.set,
	                      fg='white',
	                      bg='#3c3939',
	                      borderwidth=0,
	                      highlightthickness=0,
	                      selectbackground="Red",
	                      highlightcolor="Green")
	scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
	messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

	client.messages = messages
	receive.messages = messages

	# Imagem & Formulario
	frm_messages.pack(fill='both', expand=True, padx=10, pady=10)
	# img = tk.PhotoImage(file='logo.png')
	# label = tk.Label(window, image=img,borderwidth=0)

	# Input
	frm_entry = tk.Frame(master=window)
	text_input = tk.Entry(master=frm_entry,
	                      borderwidth=18,
	                      bg='#524f4f',
	                      fg='white',
	                      relief=tk.FLAT,
	                      font='Times 10')
	text_input.pack(fill=tk.BOTH, expand=True)
	text_input.bind("<Return>", lambda x: client.send(text_input))
	text_input.insert(0, "Digite algo e aperte enter.")
	text_input.bind("<Button-1>", lambda x: text_input.delete(0, tk.END))
	text_input.focus()

	# Pack ou Grid
	frm_entry.pack(fill='both')

	# Configs
	width = 450
	heigth = 550
	x = (window.winfo_screenwidth() // 2) - (width // 2)
	y = (window.winfo_screenheight() // 2) - (heigth // 2)
	window.geometry('{}x{}+{}+{}'.format(width, heigth, x, y))

	window.mainloop()


def redirect(host, port, window):
	"""
	Redireciona o usuário para a sala de bate-papo.

	Attributes:
		host (str): Endereço IP do socket.
		port (int): Número da porta do socket.
		window (tk.Frame): Objeto tk.Frame que contém a interface GUI que será destruida para criação da tela da sala de bate papo.
	"""
	host = host_input.get()
	window.destroy()
	main(host, 1060)


if __name__ == "__main__":

	window = tk.Tk()
	window.title('Cliente - Conexão ao Host')
	window.resizable(height=False, width=False)
	if os.name == 'nt':
		window.iconbitmap('logo_2.ico')
	host_input = tk.Entry(master=window,
	                      width='50',
	                      borderwidth=18,
	                      bg='#ccc',
	                      relief=tk.FLAT,
	                      font='Times 10')
	host_input.pack(fill=tk.BOTH, expand=True)
	host_input.bind("<Return>",
	                lambda x: redirect(host_input.get(), 1060, window))
	host_input.insert(
	    0, "Digite o endereço de Host que deseja se Conectar, ex: localhost")
	host_input.bind("<Button-1>", lambda x: host_input.delete(0, tk.END))

	width = 450
	heigth = 50
	x = (window.winfo_screenwidth() // 2) - (width // 2)
	y = (window.winfo_screenheight() // 2) - (heigth // 2)
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

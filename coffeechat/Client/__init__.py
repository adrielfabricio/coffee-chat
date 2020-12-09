"""Configuração do cliente"""
import socket
import tkinter as tk
from datetime import datetime
from coffeechat.Client.send import *
from coffeechat.Client.receive import *


def get_name(entry, window, obj):
	"""
	Captura o nome do usuário pela interface gráfica.
	
	Attributes:
		entry (tk.Entry): Campo de entrada para o nome do usuário.
		window (tk.Frame): Janela da interface gráfica onde é localizado o campo de entrada.
		obj (Client): Objeto do tipo Client.
	"""
	obj.name = entry.get()
	window.destroy()


class Client:
	"""
	Oferece suporte ao gerenciamento de conexões cliente-servidor e integração com a GUI.

	Attributes:
		host (str): Endereço IP do socket de escuta do servidor.
		port (int): Número da porta do socket de escuta do servidor.
		sock (socket.socket): Objeto socket conectado.
		name (str): Nome de usuário do cliente.
		messages (tk.Listbox): Objeto tk.Listbox que contém todas as mensagens exibidas na GUI.
    """
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.name = None
		self.messages = None

	def start(self):
		"""
		Estabelece a conexão cliente-servidor. Reúne a entrada do usuário para o nome de usuário,
		cria e inicia as threads de envio e recebimento e notifica outros clientes conectados.

		Returns:
			Um objeto Receive que representa o segmento de recebimento.
		"""
		print(f'Tentando se conecatar com {self.host}:{self.port}...')
		self.sock.connect((self.host, self.port))
		print(f'Conectado com sucesso a {self.host}:{self.port}\n')

		# INTERFACE
		window = tk.Tk()
		window.title('Cliente - Nome')
		window.resizable(height=False, width=False)
		if os.name == 'nt':
			window.iconbitmap('img/logo_2.ico')
		host_input = tk.Entry(master=window,
		                      width='50',
		                      borderwidth=18,
		                      bg='#ccc',
		                      relief=tk.FLAT,
		                      font='Times 10')
		host_input.pack(fill=tk.BOTH, expand=True)
		host_input.bind("<Return>",
		                lambda x: get_name(host_input, window, self))
		host_input.insert(0,
		                  "Digite o nome desejado sem caracteres especiais.")
		host_input.bind("<Button-1>", lambda x: host_input.delete(0, tk.END))

		width = 350
		heigth = 50
		x = (window.winfo_screenwidth() // 2) - (width // 2)
		y = (window.winfo_screenheight() // 2) - (heigth // 2)
		window.geometry('{}x{}+{}+{}'.format(width, heigth, x, y))

		window.mainloop()

		# self.name = input('Your name: ')

		print(
		    f'\nBem Vindo, {self.name}! Preparando para enviar mensagens...'
		)

		# create send and receive threads
		send = Send(self.sock, self.name)
		receive = Receive(self.sock, self.name)

		# start send and receive threads
		send.start()
		receive.start()

		self.sock.sendall('Server: {} acabou de se juntar ao chat, diga ola!'.format(
		    self.name).encode('ascii'))
		print("\rTudo pronto! Voce pode sair do chat digitando QUIT.\n")
		print(f'{self.name}: ', end='')

		return receive

	def send(self, text_input):
		"""
		Envia dados text_input da GUI. Este método deve ser vinculado a text_input e
		quaisquer outros widgets que ativem uma função semelhante, por exemplo, botões.
		Digitar 'QUIT' fechará a conexão e sairá do aplicativo.

		Args:
			text_input(tk.Entry): Objeto tk.Entry destinado à entrada de texto do usuário.
		"""

		# current date and time
		now = datetime.now()
		timestamp = now.strftime("%H:%M:%S")

		message = text_input.get()
		text_input.delete(0, tk.END)
		self.messages.insert(
		    tk.END,
		    '{}: {}'.format('(' + str(timestamp) + ')' + ' ' + self.name,
		                    message).encode('ascii'))

		if message == 'QUIT':
			self.sock.sendall('Server: {} saiu do chat.'.format(
			    self.name).encode('ascii'))

			print('\n Saindo...')
			self.sock.close()
			os._exit(0)
		else:
			self.sock.sendall('{}: {}'.format(self.name,
			                                  message).encode('ascii'))

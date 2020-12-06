import socket
import tkinter as tk
from coffeechat.Client.send import *
from coffeechat.Client.receive import *


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
		print(f'trying to connect to {self.host}:{self.port}...')
		self.sock.connect((self.host, self.port))
		print(f'successfully connected to {self.host}:{self.port}\n')

		self.name = input('Your name: ')

		print(
		    f'\nWelcome, {self.name}! Getting ready to send and receive messages...'
		)

		# create send and receive threads
		send = Send(self.sock, self.name)
		receive = Receive(self.sock, self.name)

		# start send and receive threads
		send.start()
		receive.start()

		self.sock.sendall('server: {} has joined the chat. Say hi!'.format(
		    self.name).encode('ascii'))
		print("\rAll set! Leave the chatroom anytime by typing 'QUIT'\n")
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
		message = text_input.get()
		text_input.delete(0, tk.END)
		self.messages.insert(
		    tk.END, '{}: {}'.format(self.name, message).encode('ascii'))

		if message == 'QUIT':
			self.sock.sendall('server: {} has left the chat.'.format(
			    self.name).encode('ascii'))

			print('\nquitting...')
			self.sock.close()
			os._exit(0)
		else:
			self.sock.sendall('{}: {}'.format(self.name,
			                                  message).encode('ascii'))

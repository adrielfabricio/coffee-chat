import os
import socket
import threading


class Send(threading.Thread):
	'''
	Thread de envio que espera a entrada do usuário na CLI.

	Attributes:
		sock (socket.socket): Objeto socket conectado.
		name (str): Nome de usuário fornecido pelo usuário.
	'''
	def __init__(self, sock, name):
		super().__init__()
		self.sock = sock
		self.name = name

	def run(self):
		'''
		Espera a entrada do usuário na CLI e a envia ao servidor.
		Digitar 'QUIT' fechará a conexão e sairá do aplicativo.
		'''
		while True:
			message = input('{}: '.format(self.name))
			# leave of app typing 'QUIT'
			if message == 'QUIT':
				self.sock.sendall('Server: {} has left the chat.'.format(
				    self.name).encode('ascii'))
				break
			else:
				self.sock.sendall('{}: {}'.format(self.name,
				                                  message).encode('ascii'))

		print('\nQuitting...')
		self.sock.close()
		os._exit(0)

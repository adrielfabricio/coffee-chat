import os
import socket
import threading


class Receive(threading.Thread):
	"""
	A thread de recebimento escuta as mensagens recebidas do servidor.

	Attributes:
		sock (socket.socket): Objeto socket conectado.
		name (str): Nome de usuário fornecido pelo usuário.
		messages (tk.Listbox): Objeto tk.Listbox que contém todas as mensagens exibidas na GUI.
	"""
	def __init__(self, sock, name):
		super().__init__()
		self.sock = sock
		self.name = name

	def run(self):
		"""
		Recebe dados do servidor e os exibe na GUI.
		Sempre escuta os dados de entrada até que uma das extremidades feche o socket.
		"""
		while True:
			message = self.sock.recv(1024).decode('ascii')

			if message:
				print('\r{}\n{}: '.format(message, self.name), end='')
			else:
				# Server has closed the socket, exit the program
				print('\nOh no, we have lost connection to the server!')
				print('\nQuitting...')
				self.sock.close()
				os._exit(0)
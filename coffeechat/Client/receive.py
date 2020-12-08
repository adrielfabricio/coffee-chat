import os
import socket
import threading
import tkinter as tk
from winsound import *
from win10toast import ToastNotifier
from datetime import datetime

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
		self.messages = None

	def run(self):
		"""
		Recebe dados do servidor e os exibe na GUI.
		Sempre escuta os dados de entrada até que uma das extremidades feche o socket.
		"""
		while True:
			message = self.sock.recv(1024).decode('ascii')

			if message:
     
				if self.messages:
										
					# current date and time
					now = datetime.now()
					timestamp = now.strftime("%H:%M:%S")
					self.messages.insert(tk.END, '(' + str(timestamp) +')' +' '+message)
					
					#SOM DE NOTIFICAÇÃO
					PlaySound('notification.wav', SND_FILENAME)
					#NOTIFICAÇÃO WINDOWS
					if os.name == 'nt':
						toaster = ToastNotifier()
						toaster.show_toast(message)

					print('\r{}\n{}: '.format(message, self.name).encode('ascii'),end='')
				else:
					print('\r{}\n{}: '.format(message,self.name).encode('ascii'),end='')
			else:
				# Server has closed the socket, exit the program
				print('\nOh não, perdemos conexão com o server.')
				print('\nQuitting...')
				self.sock.close()
				os._exit(0)
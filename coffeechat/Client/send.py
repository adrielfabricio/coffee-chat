"""Configuração da classe resposável por enviar mensagens para o servidor"""
import os
import sys
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
			message = input(f'{self.name}: ')
			sys.stdout.flush()
			message = sys.stdin.readline()[:-1]

			# leave of app typing 'QUIT'
			if message == 'QUIT':
				self.sock.sendall(f'Server: {self.name} saiu do chat.')
				break
			else:
				self.sock.sendall(f'{self.name}: {message}')

		print('\nSaindo...')
		self.sock.close()
		os._exit(0)

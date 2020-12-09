"""Configuração do servidor"""
import os
import socket
import threading
from coffeechat.Server.ServerSocket import *


class Server(threading.Thread):
	"""
	Suporta gerenciamento de conexões de servidor.

	Attributes:
		connections (list): Lista de objetos ServerSocket que representam as conexões ativas.
		host (str): Endereço IP do socket de escuta.
		port (int): Número da porta do socket de escuta.
	"""
	def __init__(self, host, port):
		super().__init__()
		# list of server sockets objects representing active client connections
		self.connections = []
		self.host = host
		self.port = port

	def run(self):
		"""
		Cria o socket de escuta. O socket de escuta usará a opção SO_REUSEADDR para
		permitir a ligação a um endereço de socket usado anteriormente. Este é um aplicativo de pequena escala que
		suporta apenas uma conexão em espera por vez.
		Para cada nova conexão, um thread ServerSocket é iniciado para facilitar a comunicação com
		aquele cliente específico. Todos os objetos ServerSocket são armazenados no atributo connections.
		"""
		# AF_INET: address family, for IP networking
		# SOCK_STREAM: socket type, for reliable flow-controlled data stream
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind((self.host, self.port))

		sock.listen(1)
		print(f'listening at {sock.getsockname()}')

		# listen for new client connections
		while True:
			# new connection
			sc, sockname = sock.accept()
			print(
			    f'new connection from {sc.getpeername()} to {sc.getsockname()}'
			)

			# new thread
			server_socket = ServerSocket(sc=sc, sockname=sockname, server=self)
			# start thread
			server_socket.start()

			# add thread to active connections
			self.connections.append(server_socket)
			print(f'ready to receive messages from {sc.getpeername()}')

	def broadcast(self, message, source):
		"""
		Envia uma mensagem para todos os clientes conectados,
		exceto a origem da mensagem.
		
		Args:
			message (str): Mensagem a ser transmitida.
			source (tuple): Endereço de socket do cliente de origem.
		"""
		for connection in self.connections:
			if connection.sockname != source:
				connection.send(message)

	def remove_connection(self, connection):
		"""
		Remove uma thread ServerSocket do atributo connections.
		
		Args:
			connection (ServerSocket): Thread ServerSocket a ser removida.
		"""
		self.connections.remove(connection)
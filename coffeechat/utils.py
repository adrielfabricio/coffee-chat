import os


def exit(server):
	"""
	Permite que o administrador do servidor desligue o servidor.
	Digitar 'q' na linha de comando fechará todas as conexões ativas e sairá do aplicativo.

	Attributes:
		server (Server): Servidor que será desligado.
	"""
	while True:
		ipt = input('')
		if (ipt == 'q'):
			print('closing all connections...')
			for connection in server.connections:
				connection.sc.close()
			print('shutting down the server')
			os._exit(0)
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
			print('Fechando todas as conexoes...')
			for connection in server.connections:
				connection.sc.close()
			print('Desligando o servidor ...')
			os._exit(0)
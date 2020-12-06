import argparse
import threading
import coffeechat.Server as Server
import coffeechat.utils as utils

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='CoffeChat Server')
	parser.add_argument('host', help='Interface the server listens at')
	parser.add_argument('-p',
	                    metavar='PORT',
	                    type=int,
	                    default=1060,
	                    help='TCP port (default 1060)')
	args = parser.parse_args()

	# Create and start server thread
	server = Server.Server(args.host, args.p)
	server.start()

	exit = threading.Thread(target=utils.exit, args=(server, ))
	exit.start()

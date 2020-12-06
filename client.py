import argparse
import threading
import coffeechat.Client as Client

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='CoffeChat Client')
	parser.add_argument('host', help='Interface the server listens at')
	parser.add_argument('-p',
	                    metavar='PORT',
	                    type=int,
	                    default=1060,
	                    help='TCP port (default 1060)')
	args = parser.parse_args()

	# Create and start server thread
	client = Client.Client(args.host, args.p)
	client.start()

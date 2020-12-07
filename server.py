import argparse
import threading
import coffeechat.Server as Server
import coffeechat.utils as utils
import tkinter as tk

def start_server(host, window):
  
	window.destroy()
	server = Server.Server(host, 1060)
	server.start()

	exit = threading.Thread(target=utils.exit, args=(server, ))
	exit.start()

if __name__ == "__main__":
  
	window = tk.Tk()
	window.title('Conexão do Server')
	host_input = tk.Entry(master=window, width='50', borderwidth=18,
								bg='#ccc', relief=tk.FLAT, font='Times 10')
	host_input.pack(fill=tk.BOTH, expand=True)
	host_input.bind("<Return>", lambda x: start_server(host_input.get(),window) )
	host_input.insert(0, "Digite o endereço de host para o servidor: localhost")
	host_input.bind("<Button-1>", lambda x: host_input.delete(0,tk.END))
	host_input.focus()

	width = 450
	heigth = 50
	x = (window.winfo_screenwidth()//2) - (width//2)
	y = (window.winfo_screenheight()//2) - (heigth//2)
	window.geometry('{}x{}+{}+{}'.format(width, heigth, x, y))

	window.mainloop()
	# parser = argparse.ArgumentParser(description='CoffeChat Server')
	# parser.add_argument('host', help='Interface the server listens at')
	# parser.add_argument('-p',
	#                     metavar='PORT',
	#                     type=int,
	#                     default=1060,
	#                     help='TCP port (default 1060)')
	# args = parser.parse_args()
 

	# Create and start server thread


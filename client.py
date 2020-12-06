import argparse
import threading
import tkinter as tk
import coffeechat.Client as Client


def main(host, port):
	client = Client.Client(host, port)
	receive = client.start()

	window = tk.Tk()
	window.title('CoffeeChat')

	frm_messages = tk.Frame(master=window)
	scrollbar = tk.Scrollbar(master=frm_messages)
	messages = tk.Listbox(master=frm_messages, yscrollcommand=scrollbar.set)
	scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
	messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

	client.messages = messages
	receive.messages = messages

	frm_messages.grid(row=0, column=0, columnspan=2, sticky="nsew")

	frm_entry = tk.Frame(master=window)
	text_input = tk.Entry(master=frm_entry)
	text_input.pack(fill=tk.BOTH, expand=True)
	text_input.bind("<Return>", lambda x: client.send(text_input))
	text_input.insert(0, "Your message here.")

	btn_send = tk.Button(master=window,
	                     text='Send',
	                     command=lambda: client.send(text_input))

	frm_entry.grid(row=1, column=0, padx=10, sticky="ew")
	btn_send.grid(row=1, column=1, pady=10, sticky="ew")

	window.rowconfigure(0, minsize=500, weight=1)
	window.rowconfigure(1, minsize=50, weight=0)
	window.columnconfigure(0, minsize=500, weight=1)
	window.columnconfigure(1, minsize=200, weight=0)

	window.mainloop()


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
	main(args.host, args.p)
	# client = Client.Client(args.host, args.p)
	# client.start()

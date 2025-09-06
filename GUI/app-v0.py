import tkinter as tk
import requests

'''
Convenções de nomenclatura

Classe Widget	Prefixo de nome variável	Exemplo
Label			lbl							lbl_name
Button			btn							btn_submit
Entry			ent							ent_age
Text			txt							txt_notes
Frame			frm							frm_address
'''

def window_manager(operacao):
	if operacao == "cadastro":
		janela_cadastro = WindowCad()
		janela_cadastro.show()
	elif operacao == "login":
		janela_login = WindowLogin()
		janela_login.show()


class WindowLogin:

	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Login")

		frame_menu = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1, width=80, height=40)
		frame_middle = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
		frame_botton = tk.Frame(master=self.window, relief=tk.RAISED, width=80, height=40)
		frame_log =	tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)

		frame_menu.pack(fill="x", padx=4, pady=2)
		frame_middle.pack(padx=4, pady=2)
		frame_botton.pack(fill="x", padx=4, pady=2)
		frame_log.pack(fill="x", padx=4, pady=2)

		for j in range(5):
			frame = tk.Frame(master=frame_menu, relief=tk.RAISED, borderwidth=1)
			frame.grid(row=0, column=j)
			btn = tk.Button(master=frame, text="btn")
			btn.pack(fill="x")		


		self.rep = tk.StringVar()
		self.rep.set("Log")
		lbl_log = tk.Label(master=frame_log, textvariable=self.rep, height=3)
		lbl_user = tk.Label(master=frame_middle, text="user:")
		self.ent_user = tk.Entry(master=frame_middle, width=25)
		lbl_password = tk.Label(master=frame_middle, text="password:")
		self.ent_password = tk.Entry(master=frame_middle, width=25)

		self.ent_user.bind("<Return>", self.evtGetEntry)
		self.ent_password.bind("<Return>", self.evtGetEntry)

		lbl_log.pack()
		lbl_user.pack()
		self.ent_user.pack()
		lbl_password.pack()
		self.ent_password.pack()

		btn_login = tk.Button(master=frame_botton, text="login", command=self.btnGetEntry)
		btn_cad = tk.Button(master=frame_botton, text="cadastro", command=lambda : window_manager("cadastro"))
		btn_login.pack(side="left")
		btn_cad.pack(side="right")

	def start(self):
		self.window.mainloop()

	def show(self):
		self.window.mainloop()

	def quit(self):
		self.window.destroy()

	def exit(self):
		self.window.destroy()

	def evtGetEntry(self, event):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"1"})
		print("---->  Status code:", response.status_code)

		if response.text == "OK" :
			self.rep.set("login bem sucedido!")
		else:
			self.rep.set("Credenciais Invalidas!")

	def btnGetEntry(self):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"1"})
		print("---->  Status code:", response.status_code)
		
		if response.text == "OK" :
			self.rep.set("login bem sucedido!")
		else:
			self.rep.set("Credenciais Invalidas!")
	
class WindowCad:

	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Cadastro")

		frame_menu = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1, width=80, height=40)
		frame_middle = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
		frame_botton = tk.Frame(master=self.window, relief=tk.RAISED, width=80, height=40)
		frame_log =	tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)

		frame_menu.pack(fill="x", padx=4, pady=2)
		frame_middle.pack(padx=4, pady=2)
		frame_botton.pack(fill="x", padx=4, pady=2)
		frame_log.pack(fill="x", padx=4, pady=2)

		for j in range(5):
			frame = tk.Frame(master=frame_menu, relief=tk.RAISED, borderwidth=1)
			frame.grid(row=0, column=j)
			btn = tk.Button(master=frame, text="btn")
			btn.pack()

		self.rep = tk.StringVar()
		self.rep.set("Log_cad")
		lbl_log = tk.Label(master=frame_log, textvariable=self.rep, height=3)

		lbl_user = tk.Label(master=frame_middle, text="user:")
		self.ent_user = tk.Entry(master=frame_middle, width=25)
		lbl_password = tk.Label(master=frame_middle, text="password:")
		self.ent_password = tk.Entry(master=frame_middle, width=25)

		self.ent_user.bind("<Return>", self.evtGetEntry)
		self.ent_password.bind("<Return>", self.evtGetEntry)

		lbl_log.pack()
		lbl_user.pack()
		self.ent_user.pack()
		lbl_password.pack()
		self.ent_password.pack()

		btn_sub = tk.Button(master=frame_botton, text="Submit", command=self.btnGetEntry)
		btn_sub.pack()
		

	def start(self):
		self.window.mainloop()

	def show(self):
		self.window.mainloop()

	def quit(self):
		self.window.destroy()

	def exit(self):
		self.window.destroy()

	def evtGetEntry(self, event):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"2"})
		print("---->  Status code:", response.status_code)

		if response.text == "OK" :
			self.rep.set("Cad OK")
		else:
			self.rep.set("Cad fail!")

	def btnGetEntry(self):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"2"})
		print("---->  Status code:", response.status_code)
		
		if response.text == "OK" :
			self.rep.set("Cad OK")
		else:
			self.rep.set("Cad fail!")

if __name__ == "__main__" :

	janela_login = WindowLogin()
	janela_login.show()
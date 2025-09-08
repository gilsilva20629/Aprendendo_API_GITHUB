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

class Window:
	def __init__(self, name:str)-> None:
		self.window = tk.Tk()
		self.window.title(name)
		text_log = tk.StringVar()
		text_log.set("report log")

		frame_menu = tk.Frame(master=self.window, background="white", relief=tk.RAISED, borderwidth=1, width=240, height=40)
		frame_middle = tk.Frame(master=self.window, background="white", relief=tk.RAISED, borderwidth=1, width=640, height=450)
		frame_middle_left = tk.Frame(master=frame_middle, background="gray80", relief=tk.RAISED, borderwidth=1, width=160, height=450)
		frame_middle_center = tk.Frame(master=frame_middle, background="gray80", relief=tk.RAISED, borderwidth=1, width=320, height=450)
		frame_middle_right = tk.Frame(master=frame_middle, background="gray80", relief=tk.RAISED, borderwidth=1, width=160, height=450)
		frame_botton = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1, width=240, height=80)
		frame_log = tk.LabelFrame(master=self.window, relief=tk.RAISED, borderwidth=1, width=240, height=40, text="Log")
		lbl_log = tk.Label(master=frame_log, textvariable=text_log, borderwidth=1)

		frame_menu.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle_left.pack(expand=True, fill="both", side="left", anchor="w", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle_center.pack(expand=True, fill="both", side="left", anchor="center", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle_right.pack(expand=True, fill="both", side="left", anchor="e", padx=2, pady=4, ipadx=1, ipady=1)
		frame_botton.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		frame_log.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		lbl_log.pack()
		
		######## Lidando com grid de botoes ##############

		text_label_frame = ["shop", "stock", "car", "finance", "gear"]
		images = ["images/shop.png", "images/stock.png", "images/car.png", "images/finance.png", "images/gear.png"]
		img_ref_list = []
		btn_ref_list = []
		window_list = ["shop", "stock", "car", "finance", "gear"]
		current_window = window_list[0]

		for j in range(5):
			frame = tk.LabelFrame(master=frame_menu, text=text_label_frame[j])
			frame.grid(row=0, column=j, ipadx=2, ipady=2, padx=2, pady=2, sticky="nsew")	#-column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
			btn = tk.Button(master=frame, command=lambda : identifier_button(btn))

			foto = tk.PhotoImage(master=label, file=images[j], width=35, height=35) 
			btn["image"] = foto

			#gpt confesso que nao entedi as duas linhas abaixo para prevenir garbage collector
			btn.image = foto	# Armazena a referência à imagem
			img_ref_list.append(foto)
			btn_ref_list.append(btn)	# Adiciona à lista para manter a referência

			btn.pack(fill="x", padx=2, pady=2, ipadx=2, ipady=2)

		for j in range(5):
			frame_menu.grid_columnconfigure(j, weight=1)  # Ajuste o peso das colunas ao expandir

		######## Fim de grid de botoes ##############


	def identifier_button(selfn, btn: tk.Button)-> None:

		match btn:
			case btn_ref_list[0]:
				print("BOTÃO SHOP")
			case btn_ref_list[1]:
				print("BOTÃO STOCK")
			case btn_ref_list[2]:
				print("BOTÃO CAR")
			case btn_ref_list[3]:
				print("BOTÃO FINANCE")
			case btn_ref_list[4]:
				print("BOTÃO GEAR")
			case "_":
				pass

	def start(self):
		self.window.mainloop()

	def show(self):
		self.window.mainloop()

	def quit(self):
		self.window.destroy()

	def exit(self):
		self.window.destroy()

	def teste(self):
		raise NotImplementedError("Este método deve ser implementado pelas filhas/subclasses.")


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
			frame.grid(expand=True, row=0, column=j)
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

	#janela_login = WindowLogin()
	#janela_login.show()

	janela_principal = Window("inicio")
	janela_principal.show()
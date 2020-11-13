from os import system
from datetime import datetime
import random

def view_menu():
	system("cls")
	menu = """
	APLIKASI Tiket Kereta Api
	[A] - Reservasi Tiket
	[B] - Beli Tiket
	[C] - Tampilkan Jadwal
	[D] - Informasi Tiket Anda
	[E] - Batalkan Tiket
	[Q] - KELUAR
	"""
	print(menu)

def create_id_data():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = random.randint(2,999)
	id_contact = str("%4d%2d%2d-T%3d" % (year, month, hari, counter))
	return id_data

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def print_data(id_data = None, all_fields = False):
	if id_data != None and all_fields == False:
		print(f"""
		-Data Founded-
	ID \t : {id_data}
	Name \t:{data[id_data]["nama"]}
	Telp \t:{data[id_data]["telp"]}
			""")
	elif all_fields == True:
		for id_data in data:
					nama = data[id_data]["nama"]
					telp = data[id_data]["telp"]
					print(f"ID:{id_data}\tName :{nama}\tTELP:{telp}\t")

def jadwal_hari():
	Senin1 = "Senin : [1] 07.00, [2] 12.00, [3] 17.00, [4] 22.00"
	Selasa1 = "Selasa : [1] 05.30, [2] 10.30, [3] 15.30 ,[4] 20.30"
	Rabu1 = "Rabu : [1] 08.30, [2] 12.45, [3] 18.15,[4] 22.00"
	Kamis1 = "Kamis : [1] 06.00, [2] 09.30, [3] 18.00, [4] 20.00"
	Jumat1 = "Jumat : [1] 10.00, [2] 15.00, [3] 18.30, [4] 21.30"
	Sabtu1 = "Sabtu : [1] 04.30, [2] 09.15, [3] 15.15, [4] 19.45"
	Minggu1 = "Minggu : [1] 05.00, [2] 11.00, [3] 16.15, [4] 22.45"
	Senin1, Selasa1, Rabu1, Kamis1 = float(Senin1), float(Selasa1), float(Rabu1), float(Kamis1)
	Jumat1, Sabtu1, Minggu1 = float(Jumat1), float(Sabtu1), float(Minggu1)

def jadwal():
	print("Jadwal Kereta Api : ")
	print(Senin1)
	print(Selasa1)
	print(Rabu1)
	print(Kamis1)
	print(Jumat1)
	print(Sabtu1)
	print(Minggu1)

def reservasi():
	print_header("-Reservasi Tiket Kereta-")
	print("Senin : [1] 07.00, [2] 12.00, [3] 17.00, [4] 22.00\tSelasa : [1] 05.30, [2] 10.30, [3] 15.30 ,[4] 20.30\tRabu : [1] 08.30, [2] 12.45, [3] 18.15,[4] 22.00\tKamis : [1] 06.00, [2] 09.30, [3] 18.00, [4] 20.00\tJumat : [1] 10.00, [2] 15.00, [3] 18.30, [4] 21.30")
	print("Sabtu : [1] 04.30, [2] 09.15, [3] 15.15, [4] 19.45\tMinggu : [1] 05.00, [2] 11.00, [3] 16.15, [4] 22.45")
	nama = input("NAMA\t: ")
	telp = input("TELP\t: ")

	user_ans = input("Reservasi Tiket Hari Apa : ")
	
	if user_ans == "Senin":
		print("Senin : [1] 07.00, [2] 12.00, [3] 17.00, [4] 22.00")
		user_ans2 = input("Pilih Waktu Yang Mana : ")
		if user_ans2 == "1":
			user_ans3 = input("Tekan Y untuk menyimpan(Y/N) : ")
			if verify_ans(user_ans3): #refactoring function
				id_data = create_id_data()
				print("Menyimpan Data ...")
				print("Data Tersimpan")
				data[id_data] = {"07.00"
					"nama" : nama,
					"telp" : telp
				}
		elif user_ans2 == "2":
			user_ans3 = input("Tekan Y untuk menyimpan(Y/N) : ")
			if verify_ans(user_ans3): #refactoring function
				id_data = create_id_data()
				print("Menyimpan Data ...")
				print("Data Tersimpan")
				data[id_data] = {"12.00"
					"nama" : nama,
					"telp" : telp
				}
		elif user_ans2 == "3":
			user_ans3 = input("Tekan Y untuk menyimpan(Y/N) : ")
			if verify_ans(user_ans3): #refactoring function
				id_data = create_id_data()
				print("Menyimpan Data ...")
				print("Data Tersimpan")
				data[id_data] = {"17.00"
					"nama" : nama,
					"telp" : telp
				}
		elif user_ans2 == "4":
			user_ans3 = input("Tekan Y untuk menyimpan(Y/N) : ")
			if verify_ans(user_ans3): #refactoring function
				id_data = create_id_data()
				print("Menyimpan Data ...")
				print("Data Tersimpan")
				data[id_data] = {"22.00"
					"nama" : nama,
					"telp" : telp
				}
			else:
				print("Data Batal Disimpan")
			input("Tekan ENTER Untuk Kembali ke MENU")
	elif user_ans == "Selasa":
		print("Selasa : [1] 05.30, [2] 10.30, [3] 15.30 ,[4] 20.30")
	elif user_ans == "Rabu":
		print("Rabu : [1] 08.30, [2] 12.45, [3] 18.15,[4] 22.00")
	elif user_ans == "Kamis":
		print("Kamis : [1] 06.00, [2] 09.30, [3] 18.00, [4] 20.00")
	elif user_ans == "Jumat":
		print("Jumat : [1] 10.00, [2] 15.00, [3] 18.30, [4] 21.30")
	elif user_ans == "Sabtu":
		print("Sabtu : [1] 04.30, [2] 09.15, [3] 15.15, [4] 19.45")
	elif user_ans == "Minggu":
		print("Minggu : [1] 05.00, [2] 11.00, [3] 16.15, [4] 22.45")
	else:
		input("Tekan ENTER Untuk Kembali ke MENU")

def print_header(msg):
	system("cls")
	print(msg)



data = {
	"21102020-T001" : {
		'nama' : 'Zebra',
		'telp' : '081223839848'
	}
}
stop = False

def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		reservasi()
	elif char == "B":
		beli()
	elif char == "C":
		jadwal()
	elif char == "D":
		info_tiket()
	elif char == "E":
		batal_tiket()

while not stop:
	view_menu()
	user_input = input("Pilihan : ")
	stop = check_input(user_input)
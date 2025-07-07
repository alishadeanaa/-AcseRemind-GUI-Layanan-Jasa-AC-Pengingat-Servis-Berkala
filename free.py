# import smtplib

# def sent_email(self):
#     gmail_user = "alishadeana.23244@mhs.unesa.ac.id"
#     gmail_app_password = input(str("masukkan password gmail:"))


#     sent_from = gmail_user
#     sent_to = input(str("masukkan gmail penerima:"))
#     sent_subject = input(str("masukkan subject email:"))
#     sent_body = input(str("masukkan pesan yg akan dikirim lalu enter"))


#     email_text = """\
#     From : %s
#     To: %s
#     Subject: %s

#     %s
#     """ % (sent_from,"," .join(sent_to), sent_subject, sent_body)

#     try:
#         server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#         server.ehlo()
#         server.login(gmail_user, gmail_app_password)
#         server.sendmail(sent_from,sent_to, email_text)
#         print("email berhasil dikirim")
#     except Exception as exception:
#         print("Error: %s!\n\n" % exception

# import customtkinter
# from tkinter import *
# from PIL import ImageTk
# master = Tk()
# class DashboardCustomTKbutton(customtkinter.CTkButton):
#     image = ImageTk.PhotoImage(file="logo apps.png")
#     def __init__(self, master, width=20, height=20, fg_color="white", text="", border_width=2, corner_radius=8, image=image, hover_color="grey", hover=True, *args, **kwargs):
#         super().__init__(master, width=width, height=height, fg_color=fg_color, text=text, border_width=border_width, corner_radius=corner_radius, image=image)
# gui = DashboardCustomTKbutton(master)
# master.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk

# class TransparentFrame(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Transparent Frame Example")
#         self.geometry("400x300")

#         # Set transparent background
#         self.attributes("-alpha", 0.8)

#         # Load an image with an alpha channel (transparency)
#         image = Image.open("logo.png")  # Ganti dengan path gambar transparan Anda
#         photo = ImageTk.PhotoImage(image)

#         # Create a label with the transparent image
#         label = tk.Label(self, image=photo)
#         label.place(x=0, y=0, relwidth=1, relheight=1)

#         # Make the label transparent
#         # label.image = photo
#         # label.config(bg="-transparentcolor")  # Set background to transparent

# if __name__ == "__main__":
#     app = TransparentFrame()
#     app.mainloop()
#
# import pandas as pd
# from datetime import date
# SHEET_ID = "1-WKAR8pPL65turHDlzNMpXgUigZiwfexJYoAhcAneiw"
# SHEET_NAME = "Sheet1"
# URL = f"https://docs.google.com/spreadsheets/d/1-WKAR8pPL65turHDlzNMpXgUigZiwfexJYoAhcAneiw/edit?hl=id#gid=0"
        
# def load_df(URL):
#             parse_dates = ["last service", "reminder date"]
#             df = pd.read_csv(URL, parse_dates=parse_dates)
#             return df

# print(load_df(URL))

# from datetime import datetime, timedelta

# def add_three_months(input_date):
#     # Konversi input_date ke objek datetime
#     date_object = datetime.strptime(input_date, '%d/%m/%y')

#     # Tambahkan 3 bulan menggunakan timedelta
#     new_date = date_object + timedelta(days=3*30)

#     # Format ulang tanggal baru ke format dd/mm/yy
#     new_date_formatted = new_date.strftime('%d/%m/%y')

#     return new_date_formatted

# # Contoh penggunaan
# input_date = '02/12/21'  # Ganti dengan tanggal awal yang diinginkan
# result_date = add_three_months(input_date)
# print(f"Tanggal awal: {input_date}")
# print(f"Tanggal setelah ditambah 3 bulan: {result_date}")
# 

# import tkinter as tk

# def on_button_click():
#     print("Tombol ditekan!")
#     # Mengganti nilai menjadi 1
#     value.set(1)
#     if value.get() >= 1:
#         print("hallow")
    
# # Membuat jendela Tkinter
# window = tk.Tk()

# # Variabel untuk menyimpan nilai
# value = tk.IntVar()

# # Membuat tombol di jendela

# button = tk.Button(window, text="Tekan Saya!", command=on_button_click)
# buttonb = tk.Button(window, text="Tekan Saya!", command=on_button_click).pack()
# # Menempatkan tombol di jendela
# button.pack()

# # Memulai siklus utama Tkinter
# window.mainloop()

# # Setelah jendela ditutup, Anda dapat mengakses nilai dengan value.get()
# print("Nilai setelah tombol ditekan:", value.get())







# import tkinter as tk
# import customtkinter as ct
# window = tk.Tk()
# window.size("100x400")

# def on_button_click( button_id):
#     print(f"Tombol {button_id} ditekan!")
#     if button_id == 1:
#           button1()
#     if button_id == 2: 
#           button2()
           
# # Membuat jendela Tkinter

# def button1():
#         print("p")
# def button2():
#     a= print("oj")
#     # return a
# # Membuat tombol di jendela
# button_1 = tk.Button(window, text="Tombol 1", command=lambda: on_button_click(1))
# button_2 = tk.Button(window, text="Tombol 2", command=lambda: on_button_click(2))
# entry_nama_jasa =ct.CTkLabel(window, text="ACTECH Service", width=250, corner_radius=20, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
# entry_nama_jasa.place(x=50, y=370)
# # Menempatkan tombol di jendela
# button_1.pack()
# # button_2.pack()

# Memulai siklus utama Tkinter
# window.mainloop()




# import tkinter as tk

# class CustomRadioButton(tk.Radiobutton):
#     def __init__(self, master=None, value=None, **kwargs):
#         super().__init__(master, value=value, **kwargs)
#         self.config(command=self.on_radiobutton_click)

#     def on_radiobutton_click(self):
#         print(f"Radio button dengan nilai {self.value} dipilih.")

# # Membuat jendela Tkinter
# window = tk.Tk()

# # Membuat daftar RadioButtons kustom
# radio_buttons = []
# values = ["A", "B", "C", "D", "E"]
# selected_value = tk.StringVar()

# for value in values:
#     custom_radio_button = CustomRadioButton(window, text=f"Option {value}", value=value, variable=selected_value)
#     radio_buttons.append(custom_radio_button)
#     custom_radio_button.pack()

# # Memulai siklus utama Tkinter
# window.mainloop()










# 

# import tkinter as tk

# def on_checkbutton_1_click():
#     print("Checkbutton 1 dipilih")

# def on_checkbutton_2_click():
#     print("Checkbutton 2 dipilih")

# # Membuat jendela Tkinter
# window = tk.Tk()

# # Membuat dua Checkbuttons di jendela
# checkbutton_1 = tk.Checkbutton(window, text="Checkbutton 1", command=on_checkbutton_1_click)
# checkbutton_2 = tk.Checkbutton(window, text="Checkbutton 2", command=on_checkbutton_2_click)

# # Menempatkan Checkbuttons di jendela
# checkbutton_1.pack()
# checkbutton_2.pack()

# # Memulai siklus utama Tkinter
# window.mainloop()



# import tkinter as tk

# def on_radio_button_1_click():
#     print("Radio button 1 dipilih")

# def on_radio_button_2_click():
#     print("Radio button 2 dipilih")

# # Membuat jendela Tkinter
# window = tk.Tk()

# # Membuat variabel StringVar untuk melacak nilai Radio button yang dipilih
# selected_radio = tk.StringVar()

# # Membuat dua Radio buttons di jendela
# radio_button_1 = tk.Radiobutton(window, text="Radio button 1", variable=selected_radio, value="1", command=on_radio_button_1_click)
# radio_button_2 = tk.Radiobutton(window, text="Radio button 2", variable=selected_radio, value="2", command=on_radio_button_2_click)

# # Radio button tanpa command
# radio_button_default = tk.Radiobutton(window, text="Radio button Default", variable=selected_radio, value="default")

# # Menempatkan Radio buttons di jendela
# radio_button_1.pack()
# radio_button_2.pack()
# radio_button_default.pack()

# # Memulai siklus utama Tkinter
# window.mainloop()

# 

# from tkinter import Tk, IntVar, Radiobutton

# root = Tk()

# # Variabel terkait
# selected_option = IntVar()

# # Radio buttons
# radio_button1 = Radiobutton(root, text="Option 1", variable=selected_option, value=1)
# radio_button2 = Radiobutton(root, text="Option 2", variable=selected_option, value=2)

# # Menampilkan radio buttons
# radio_button1.pack()
# radio_button2.pack()

# root.mainloop()

# from tkinter import Tk, IntVar, Radiobutton

# class YourApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("300x500")
#         self.master.title("Pilih Metode Pembayaran")

#         self.pemilihanpay = IntVar()

#         checkbutton_A = Radiobutton(master, text="CASH", value="CASH", variable=self.pemilihanpay, bg="#1679ad")
#         checkbutton_A.place(x=50, y=425)

#         checkbutton_B = Radiobutton(master, text="QRIS", value="QRIS", variable=self.pemilihanpay, bg="#1679ad")
#         checkbutton_B.place(x=170, y=425)

# if __name__ == "__main__":
#     root = Tk()
#     app = YourApp(root)
#     root.mainloop()

# from tkinter import Tk, IntVar, Radiobutton

# class YourApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("300x500")
#         self.master.title("Pilih Metode Pembayaran")

#         self.pemilihanpay = IntVar()

#         checkbutton_A = Radiobutton(master, text="CASH", value="CASH", variable=self.pemilihanpay)
#         checkbutton_A.place(x=50, y=425)

#         checkbutton_B = Radiobutton(master, text="QRIS", value="QRIS", variable=self.pemilihanpay,command=self.click)
#         checkbutton_B.place(x=170, y=425)

#     def click(self):
#      if self.pemilihanpay.get() == int("QRIS"):
#             print("anyyeong")
# if __name__ == "__main__":
#     root = Tk()
#     app = YourApp(root)
    # root.mainloop()



# from tkinter import *

# class YourApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("300x500")
#         self.master.title("Pilih Metode Pembayaran")

#         # Dictionary untuk memetakan nilai radio button ke representasi string
#         self.radio_values = {1: "CASH", 2: "QRIS"}

#         value = IntVar()
#         self.pemilihanpay = IntVar()
#         checkbutton_A = Radiobutton(master, text="CASH", value=1, variable=self.pemilihanpay)
#         checkbutton_A.place(x=50, y=425)

#         checkbutton_B = Radiobutton(master, text="QRIS", value=2, variable=self.pemilihanpay)
#         checkbutton_B.place(x=170, y=425)

#         # Tombol untuk menampilkan nilai yang dipilih
#         show_button = Button(master, text="Show Selected Value", command=self.show_selected_value)
#         show_button.place(x=50, y=470)

#     def show_selected_value(self):
#         selected_value = self.pemilihanpay.get()
#         if selected_value in self.radio_values:
#               self.pemilihanpayyy =  self.radio_values[selected_value]
            
#     # else:
#     #         print("Invalid value selected")

# if __name__ == "__main__":
#     root = Tk()
#     app = YourApp(root)
#     root.mainloop()

# from tkinter import *

# class YourApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("300x500")
#         self.master.title("Pilih Metode Pembayaran")

#         self.pemilihanpay = StringVar()

#         checkbutton_A = Radiobutton(master, text="CASH", value="CASH", variable=self.pemilihanpay)
#         checkbutton_A.place(x=50, y=425)

#         checkbutton_B = Radiobutton(master, text="QRIS", value="QRIS", variable=self.pemilihanpay)
#         checkbutton_B.place(x=170, y=425)

#         # Button to trigger the check and action
#         check_button = Button(master, text="Check and Calculate", command=self.check_and_calculate)
#         check_button.place(x=50, y=470)

#     def check_and_calculate(self):
#         selected_value = self.pemilihanpay.get()

#         if selected_value == "CASH":
#             # Do something specific for CASH
#             print("Selected: CASH")
        
#         else:
#             # Call a local function in the else block
#             self.local_function()

#     def local_function(self):
#         # Your local function logic here
#         print("This is a local function.")

#     def calculate_price(self):
#         # Your calculation logic here
#         print("Calculating price...")

# if __name__ == "__main__":
#     root = Tk()
#     app = YourApp(root)
#     root.mainloop()

# import cv2
# from pyzbar.pyzbar import decode

# def detect_and_decode_qr_code(image_path):
#     # Baca gambar dari path
#     image = cv2.imread("p.png")

#     # Konversi gambar ke grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Temukan dan dekode QR code
#     decoded_objects = decode(gray)

#     # Loop melalui setiap objek yang ditemukan
#     for obj in decoded_objects:
#         # Ambil nilai data dari QR code
#         qr_data = obj.data.decode('utf-8')
#         print(f"QR Code Detected: {qr_data}")

#         # Tampilkan QR code pada gambar
#         points = obj.polygon
#         if len(points) > 4:
#             hull = cv2.convexHull(points, clockwise=False)
#             cv2.polylines(image, [hull], True, (0, 255, 0), 2)

#     # Tampilkan gambar dengan QR code yang terdeteksi
#     cv2.imshow('QR Code Detection', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Contoh pemanggilan fungsi dengan gambar sebagai argumen
# detect_and_decode_qr_code('p.png')



# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/payment-notification', methods=['POST'])
# def handle_payment_notification():
#     try:
#         # Dapatkan data notifikasi dari sistem pembayaran
#         payment_data = request.json

#         # Lakukan verifikasi keaslian notifikasi (sesuai dengan dokumentasi sistem pembayaran)
#         # Verifikasi nomor pesanan, jumlah pembayaran, dan lainnya

#         # Jika verifikasi berhasil, perbarui status transaksi dalam sistem Anda
#         update_transaction_status(payment_data['order_number'], 'PAID')

#         return {'status': 'success'}
#     except Exception as e:
#         return {'status': 'error', 'message': str(e)}

# def update_transaction_status(order_number, status):
#     # Logika untuk memperbarui status transaksi dalam sistem Anda
#     print(f"Order {order_number} status updated to {status}")

# if __name__ == '__main__':
#     app.run(port=5000)

# import tkinter as tk

# class GFormLinkApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Link to Google Form")

#         # Link Google Form
#         self.gform_link = "https://docs.google.com/forms/d/e/your_form_id/viewform"

#         # Label untuk menampilkan link
#         self.link_label = tk.Label(master, text="Click here to open Google Form", fg="blue", cursor="hand2")
#         self.link_label.pack(pady=20)
#         self.link_label.bind("<Button-1>", self.open_gform)

#     def open_gform(self, event):
#         import webbrowser
#         webbrowser.open(self.gform_link)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = GFormLinkApp(root)
#     root.mainloop()

# import tkinter as tk

# class YourApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Main App")

#         # Tombol untuk menjalankan fungsi tanpa menampilkan frame
#         btn_run_operation = tk.Button(master, text="Run Operation", command=self.run_operation)
#         btn_run_operation.pack(pady=20)

#         # Frame yang seharusnya tidak ditampilkan
#         self.hidden_frame = tk.Frame(master)
#         self.hidden_frame.withdraw()  # Menyembunyikan frame

#     def run_operation(self):
#         # Panggil fungsi operasi dari luar frame
#         self.hidden_operation()

#     def hidden_operation(self):
#         # Operasi yang ingin dilakukan tanpa menampilkan frame
#         print("Hidden Operation Executed")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YourApp(root)
#     root.mainloop()

# import tkinter as tk

# class YourApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Main App")

#         # Tombol untuk menjalankan fungsi tanpa menampilkan frame
#         btn_run_operation = tk.Button(master, text="Run Operation", command=self.run_operation)
#         btn_run_operation.pack(pady=20)

#         # Frame yang seharusnya tidak ditampilkan
#         self.hidden_frame = tk.Frame(master)

#     def run_operation(self):
#         # Panggil fungsi operasi dari luar frame
#         self.hidden_operation()

#     def hidden_operation(self):
#         # Operasi yang ingin dilakukan tanpa menampilkan frame
#         print("Hidden Operation Executed")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YourApp(root)
#     root.mainloop()


# from tkinter import Tk, Label, Text
# import csv

# class NamaKelasAnda:
#     def __init__(self):
#         # ... (kode __init__ lainnya)

#         # Anggap self.frame_riwayat sudah didefinisikan di __init__
#         self.text_widget = Text(self.frame_riwayat, wrap=word, width=50, height=10)
#         self.text_widget.place(x=80, y=200)

#     def riwayat_ghaib(self):
#         username = self.username.get()
#         booking_history = []  # Anggap ini adalah daftar kamus dengan informasi pemesanan
#         with open('booking_data.csv', mode='r') as file:
#             csv_reader = csv.DictReader(file)
#             for row in csv_reader:
#                 if row['Username'] == username:
#                     booking_history.append(row)

#         if not booking_history:
#             # Jika tidak ada riwayat pemesanan, tampilkan label
#             no_booking_label = Label(self.frame_riwayat, text="Anda belum pernah booking.", font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
#             no_booking_label.place(x=80, y=170)
#         else:
#             # Tampilkan informasi pemesanan di widget teks
#             for booking in booking_history:
#                 booking_text = (
#                     f"• Username = {booking['Username']},\n• Tanggal = {booking['Booking Date']},"
#                     f"\n• Jasa = {booking['Service Name']},\n• Layanan = {booking['Selected Services']},"
#                     f"\n• Harga = {booking['Service Price']}\n\n============================================\n\n"
#                 )
#                 self.text_widget.insert('end', booking_text)

# # Contoh penggunaan
# root = Tk()
# app = NamaKelasAnda()
# app.riwayat_ghaib()
# root.mainloop()

# import tkinter as tk
# import customtkinter as ct

# def main():
#     # Membuat jendela utama
#     root = tk.Tk()
#     root.title("Contoh Entry dengan CustomTKinter")

#     # Menggunakan custom style untuk entri
#     custom_entry =ct.CTkEntry(root,bg_color="#ecf0f3", corner_radius=9,height=8,text_color="#0370a9",border_color="#0370a9",fg_color="white")
#     custom_entry.pack(padx=10, pady=10)  # Menambahkan padding sesuai kebutuhan

#     # Menjalankan aplikasi
#     root.mainloop()

# if __name__ == "__main__":
#     main()


# import tkinter as tk

# def main():
#     # Membuat jendela utama
#     root = tk.Tk()
#     root.title("Meninggikan Entry Tkinter")

#     # Membuat entri dengan tinggi (height) 3
#     entry_with_height = tk.Entry(root, height=3)
#     entry_with_height.pack(padx=10, pady=10)

#     # Menjalankan aplikasi
#     root.mainloop()

# if __name__ == "__main__":
#     main()

# import tkinter as tk
# from customtkinter import CTkFrame, Label

# class YourClass:
#     def __init__(self):
#         # ... inisialisasi lainnya

#     def konsul2(self):
#         # Ganti 'window' dengan objek Tkinter yang sesuai
#         self.frame_konsul.destroy()
#         frame_konsul1 = CTkFrame(window, corner_radius=20, bg_color='black', fg_color='white', width=500, height=530)
#         frame_konsul1.place(x=740, y=140)

#         masalah_ac = []
#         if self.konsultasi == "AC tidak Dingin":
#             masalah = "AC Tidak dingin:\nAda beberapa faktor yang bisa menyebabkan udara yang dikeluarkan AC menjadi tidak dingin. Beberapa di antaranya yaitu daya kerja AC yang tidak sesuai dengan luas ruangan, pengaturan remote AC yang tidak sesuai, hingga kondisi ruangan yang sering terpapar sinar matahari.\n"
#             masalah_ac.append(masalah)
#         elif self.konsultasi == "udara AC panas":
#             masalah = "Udara AC panas: \n Penyebabnya bisa karena ada komponen AC yang rusak, seperti bocornya sistem AC, atau tekanan pada freon yang terlalu tinggi."
#             masalah_ac.append(masalah)

#         # Menggunakan widget Text untuk menampilkan beberapa baris teks
#         text_widget = tk.Text(frame_konsul1, wrap=tk.WORD, bg='black', fg='white', font=("Helvetica", 12))
#         text_widget.insert(tk.END, ''.join(masalah_ac))
#         text_widget.place(x=50, y=50, width=400, height=400)

# if __name__ == "__main__":
#     # Ganti 'window' dengan objek Tkinter yang sesuai
#     window = tk.Tk()
#     your_instance = YourClass()
#     your_instance.konsul2()tki

# from tkinter import *
# from customtkinter import *

# class YourClass:
#     def __init__(self):
#         # ... inisialisasi lainnya
#         self.konsultasi = "AC tidak Dingin"  # Gantilah dengan nilai yang sesuai

#     def konsul2(self):
#         # self.frame_konsul.destroy()
#         frame_konsul1 = CTkFrame(window, corner_radius=20, bg_color='black', fg_color='white', width=500, height=530)
#         frame_konsul1.place(x=740, y=140)

#         masalah_ac = []
#         if self.konsultasi == "AC tidak Dingin":
#             masalah = "AC Tidak dingin:\nAda beberapa faktor yang bisa menyebabkan udara yang dikeluarkan AC menjadi tidak dingin. Beberapa di antaranya yaitu daya kerja AC yang tidak sesuai dengan luas ruangan, pengaturan remote AC yang tidak sesuai, hingga kondisi ruangan yang sering terpapar sinar matahari.\n"
#             masalah_ac.append(masalah)
#         elif self.konsultasi == "udara AC panas":
#             masalah = "Udara AC panas: \n Penyebabnya bisa karena ada komponen AC yang rusak, seperti bocornya sistem AC, atau tekanan pada freon yang terlalu tinggi."
#             masalah_ac.append(masalah)

#         # Menggunakan widget Text untuk menampilkan beberapa baris teks
#         text_widget = Text(frame_konsul1, wrap=WORD, bg='black', fg='white', font=("Helvetica", 12))
#         text_widget.insert(END, ''.join(masalah_ac))
#         text_widget.config(state=DISABLED)  # Membuat teks tidak dapat diedit
#         text_widget.place(x=50, y=50, width=400, height=400)

#         # # Menambahkan Label untuk menampilkan masalah AC di label
#         # label_masalah_ac = Label(frame_konsul1, text=masalah_ac[0], fg="white", font=("Helvetica", 12))
#         # label_masalah_ac.place(x=50, y=460)

# if __name__ == "__main__":
#     window = Tk()
#     your_instance = YourClass()
#     your_instance.konsul2()
#     window.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# class QuizApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Quiz App")
#         self.master.geometry("300x200")

#         self.descriptions = []  # Daftar untuk menyimpan deskripsi jawaban ya
#         self.create_widgets()

#     def create_widgets(self):
#         self.label_question1 = tk.Label(self.master, text="Apakah Anda suka pemrograman?")
#         self.label_question1.pack(pady=10)

#         self.answer_var1 = tk.StringVar()
#         self.answer_var1.set("Tidak")

#         self.radio_yes1 = tk.Radiobutton(self.master, text="Ya", variable=self.answer_var1, value="Ya")
#         self.radio_yes1.pack(side=tk.LEFT, padx=10)
#         self.radio_no1 = tk.Radiobutton(self.master, text="Tidak", variable=self.answer_var1, value="Tidak")
#         self.radio_no1.pack(side=tk.RIGHT, padx=10)

#         self.button_next = tk.Button(self.master, text="Selanjutnya", command=self.next_question)
#         self.button_next.pack(pady=10)

#     def next_question(self):
#         # Menyembunyikan elemen-elemen pertanyaan pertama
#         self.label_question1.pack_forget()
#         self.radio_yes1.pack_forget()
#         self.radio_no1.pack_forget()
#         self.button_next.pack_forget()

#         # Menampilkan pertanyaan kedua
#         self.label_question2 = tk.Label(self.master, text="Apakah Anda suka Python?")
#         self.label_question2.pack(pady=10)

#         self.answer_var2 = tk.StringVar()
#         self.answer_var2.set("Tidak")

#         self.radio_yes2 = tk.Radiobutton(self.master, text="Ya", variable=self.answer_var2, value="Ya")
#         self.radio_yes2.pack(side=tk.LEFT, padx=10)
#         self.radio_no2 = tk.Radiobutton(self.master, text="Tidak", variable=self.answer_var2, value="Tidak")
#         self.radio_no2.pack(side=tk.RIGHT, padx=10)

#         self.button_show_descriptions = tk.Button(self.master, text="Tampilkan Deskripsi", command=self.show_descriptions)
#         self.button_show_descriptions.pack(pady=10)

#     def show_descriptions(self):
#         # Menyembunyikan elemen-elemen pertanyaan kedua
#         self.label_question2.pack_forget()
#         self.radio_yes2.pack_forget()
#         self.radio_no2.pack_forget()
#         self.button_show_descriptions.pack_forget()

#         # Menambahkan deskripsi dari jawaban ya ke dalam daftar
#         if self.answer_var1.get() == "Ya":
#             self.descriptions.append("Anda suka pemrograman!")

#         if self.answer_var2.get() == "Ya":
#             self.descriptions.append("Anda suka Python!")

#         # Menampilkan deskripsi dari jawaban ya
#         if self.descriptions:
#             description_text = "\n".join(self.descriptions)
#             messagebox.showinfo("Deskripsi Jawaban Ya", description_text)
#         else:
#             messagebox.showinfo("Deskripsi Jawaban Ya", "Tidak ada deskripsi.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = QuizApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import END, DISABLED, WORD, Scrollbar

# class YourClass:
#     def __init__(self):
#         # ... inisialisasi lainnya
#         self.konsultasi = "AC tidak Dingin"  # Gantilah dengan nilai yang sesuai

#     def konsul2(self):
#         # self.frame_konsul.destroy()
#         frame_konsul1 = tk.Frame(window, bg='black', width=500, height=530)
#         frame_konsul1.place(x=740, y=140)

#         masalah_ac = []
#         if self.konsultasi == "AC tidak Dingin":
#             masalah = "AC Tidak dingin:\nAda beberapa faktor yang bisa menyebabkan udara yang dikeluarkan AC menjadi tidak dingin. Beberapa di antaranya yaitu daya kerja AC yang tidak sesuai dengan luas ruangan, pengaturan remote AC yang tidak sesuai, hingga kondisi ruangan yang sering terpapar sinar matahari.\n"
#             masalah_ac.append(masalah)
#         elif self.konsultasi == "udara AC panas":
#             masalah = "Udara AC panas: \n Penyebabnya bisa karena ada komponen AC yang rusak, seperti bocornya sistem AC, atau tekanan pada freon yang terlalu tinggi."
#             masalah_ac.append(masalah)

#         # Menggunakan widget Text untuk menampilkan beberapa baris teks
#         text_widget = tk.Text(frame_konsul1, wrap=WORD, bg='black', fg='white', font=("Helvetica", 12))
#         text_widget.insert(END, ''.join(masalah_ac))
#         text_widget.config(state=DISABLED)  # Membuat teks tidak dapat diedit
#         text_widget.place(x=50, y=50, width=400, height=400)

#         # Menambahkan Scrollbar
#         scrollbar = Scrollbar(frame_konsul1, command=text_widget.yview)
#         scrollbar.place(x=450, y=50, height=400)
#         text_widget.config(yscrollcommand=scrollbar.set)

#         # Menandai atau menstabilo teks tertentu
#         text_widget.tag_add("highlight", "1.0", "1.14")  # Menstabilo teks dari posisi 1.0 hingga 1.14
#         text_widget.tag_config("highlight", background="yellow")

# if __name__ == "__main__":
#     window = tk.Tk()
#     your_instance = YourClass()
#     your_instance.konsul2()
#     window.mainloop()



# 
# import tkinter as tk
# import time

# def update_clock():
#     current_time = time.strftime('%H:%M:%S')
#     current_date = time.strftime('%d-%m-%Y')
#     clock_label.config(text=current_time)
#     date_label.config(text=current_date)
#     root.after(1000, update_clock)

# root = tk.Tk()
# root.title("Jam dan Tanggal")

# clock_label = tk.Label(root, font=('Arial', 50))
# clock_label.pack(pady=20)

# date_label = tk.Label(root, font=('Arial', 20))
# date_label.pack()

# update_clock()

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# class EmailApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Aplikasi Pengiriman Email Yahoo")
#         self.setup_gui()

#     def setup_gui(self):
#         # Label dan Entry untuk alamat email pengirim
#         ttk.Label(self.root, text="Email Pengirim:").grid(row=0, column=0, padx=5, pady=5)
#         self.sender_email_entry = ttk.Entry(self.root, width=30)
#         self.sender_email_entry.grid(row=0, column=1, padx=5, pady=5)

#         # Label dan Entry untuk kata sandi email pengirim
#         ttk.Label(self.root, text="Kata Sandi:").grid(row=1, column=0, padx=5, pady=5)
#         self.password_entry = ttk.Entry(self.root, show="*", width=30)
#         self.password_entry.grid(row=1, column=1, padx=5, pady=5)

#         # Label dan Entry untuk alamat email penerima
#         ttk.Label(self.root, text="Email Penerima:").grid(row=2, column=0, padx=5, pady=5)
#         self.receiver_email_entry = ttk.Entry(self.root, width=30)
#         self.receiver_email_entry.grid(row=2, column=1, padx=5, pady=5)

#         # Label dan Entry untuk subjek email
#         ttk.Label(self.root, text="Subjek:").grid(row=3, column=0, padx=5, pady=5)
#         self.subject_entry = ttk.Entry(self.root, width=30)
#         self.subject_entry.grid(row=3, column=1, padx=5, pady=5)

#         # Label dan Text untuk isi email
#         ttk.Label(self.root, text="Isi Email:").grid(row=4, column=0, padx=5, pady=5)
#         self.message_text = tk.Text(self.root, wrap="word", width=30, height=5)
#         self.message_text.grid(row=4, column=1, padx=5, pady=5)

#         # Tombol untuk mengirim email
#         send_button = ttk.Button(self.root, text="Kirim Email", command=self.send_email)
#         send_button.grid(row=5, column=0, columnspan=2, pady=10)

#     def send_email(self):
#         # Ambil nilai dari input pengguna
#         sender_email = self.sender_email_entry.get()
#         password = self.password_entry.get()
#         receiver_email = self.receiver_email_entry.get()
#         subject = self.subject_entry.get()
#         message = self.message_text.get("1.0", tk.END)

#         # Setup email
#         email = MIMEMultipart()
#         email["From"] = sender_email
#         email["To"] = receiver_email
#         email["Subject"] = subject
#         email.attach(MIMEText(message, "plain"))

#         # Kirim email menggunakan SMTP Yahoo
#         try:
#             with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
#                 server.starttls()
#                 server.login(sender_email, password)
#                 server.sendmail(sender_email, receiver_email, email.as_string())
#             print("Email berhasil dikirim!")
# #         except Exception as e:
# #             print(f"Error: {e}")

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = EmailApp(root)
# #     root.mainloop()


# import schedule
# import time
# from twilio.rest import Client

# # Fungsi untuk mengirim pesan WhatsApp
# def send_whatsapp_message(to, body):
#     account_sid = 'your_twilio_account_sid'
#     auth_token = 'your_twilio_auth_token'
#     from_whatsapp_number='whatsapp:+14155238886'
#     to_whatsapp_number = f'whatsapp:{to}'

#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#                               from_=from_whatsapp_number,
#                               body=body,
#                               to=to_whatsapp_number
#                           )

#     print(f"WhatsApp message sent to {to}: {message.sid}")

# # Fungsi untuk menjalankan tugas harian
# def daily_task():
#     # Ubah nomor WhatsApp sesuai keinginan Anda
#     recipient_number = '082139948140'
    
#     # Ambil tanggal hari besok
#     tomorrow = (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday + 1,
#                 12, 0, 0, 0, 0, 0)
    
#     # Konversi tanggal ke timestamp
#     tomorrow_timestamp = time.mktime(tomorrow)

#     # Hitung selisih waktu antara sekarang dan hari besok
#     delay = tomorrow_timestamp - time.time()

#     # Jadwalkan pengiriman pesan pada pukul 12:00 hari besok
#     schedule.every().day.at("12:00").do(send_whatsapp_message, to=recipient_number, body="Ingat besok!")

#     # Mulai menjalankan tugas harian
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == "__main__":
#     daily_task()


# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime, timedelta
# import schedule
# import threading
# from twilio.rest import Client

# class WhatsAppReminderApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("WhatsApp Reminder App")
#         self.setup_gui()

#     def setup_gui(self):
#         # Label dan Entry untuk nomor WhatsApp penerima
#         ttk.Label(self.root, text="Nomor WhatsApp Penerima:").grid(row=0, column=0, padx=5, pady=5)
#         self.recipient_entry = ttk.Entry(self.root, width=30)
#         self.recipient_entry.grid(row=0, column=1, padx=5, pady=5)

#         # Label dan Entry untuk pesan
#         ttk.Label(self.root, text="Pesan:").grid(row=1, column=0, padx=5, pady=5)
#         self.message_entry = ttk.Entry(self.root, width=30)
#         self.message_entry.grid(row=1, column=1, padx=5, pady=5)

#         # Tombol untuk menjadwalkan pengiriman pesan
#         schedule_button = ttk.Button(self.root, text="Jadwalkan Pengiriman", command=self.schedule_message)
#         schedule_button.grid(row=2, column=0, columnspan=2, pady=10)

#     def schedule_message(self):
#         recipient_number = self.recipient_entry.get()
#         message = self.message_entry.get()

#         if not recipient_number or not message:
#             self.show_error("Mohon isi nomor penerima dan pesan.")
#             return

#         # Ambil waktu sekarang
#         now = datetime.now()

#         # Jadwalkan pengiriman pesan pada pukul 12:00 hari berikutnya
#         scheduled_time = now.replace(hour=12, minute=0, second=0, microsecond=0) + timedelta(days=1)

#         # Hitung selisih waktu antara sekarang dan waktu jadwal
#         delay = (scheduled_time - now).total_seconds()

#         # Jadwalkan pengiriman pesan menggunakan library schedule
#         schedule.every().seconds.do(self.send_whatsapp_message, recipient_number, message).tag('whatsapp')

#         # Buat thread terpisah untuk menjalankan schedule
#         threading.Thread(target=self.run_schedule).start()

#         self.show_info(f"Pesan akan dijadwalkan untuk dikirim pada pukul 12:00 hari berikutnya.")

#     def send_whatsapp_message(self, to, body):
#         # Ganti dengan informasi akun Twilio Anda
#         account_sid = 'your_twilio_account_sid'
#         auth_token = 'your_twilio_auth_token'
#         from_whatsapp_number = 'whatsapp:+14155238886'
#         to_whatsapp_number = f'whatsapp:{to}'

#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#             from_=from_whatsapp_number,
#             body=body,
#             to=to_whatsapp_number
#         )

#         print(f"WhatsApp message sent to {to}: {message.sid}")

#     def run_schedule(self):
#         while True:
#             schedule.run_pending()

#     def show_info(self, message):
#         tk.messagebox.showinfo("Info", message)

#     def show_error(self, message):
#         tk.messagebox.showerror("Error", message)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WhatsAppReminderApp(root)
#     root.mainloop()


# import tkinter as tk

# class ScrollingBannerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Pamflet Berjalan")
#         self.root.geometry("600x100")
#         self.setup_gui()

#     def setup_gui(self):
#         self.scroll_frame = tk.Frame(self.root, bg="white")
#         self.scroll_frame.pack(fill=tk.BOTH, expand=True)

#         self.label = tk.Label(self.scroll_frame, text="Selamat Datang di Aplikasi Pamflet Berjalan!", font=("Arial", 14), bg="white")
#         self.label.pack(side=tk.LEFT, padx=(600, 0))

#         self.scroll_text()

#     def scroll_text(self):
#         x = 600
#         while True:
#             x -= 1
#             self.label.place(x=x)
#             self.root.update()
#             self.root.after(10)
            
#             # Jika label mencapai batas kiri window, reset posisi ke kanan window
#             if x == -self.label.winfo_width():
#                 x = 600

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ScrollingBannerApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime, timedelta
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# class EmailSchedulerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Email Scheduler App")
#         self.setup_gui()

#     def setup_gui(self):
        # Label dan Entry untuk alamat email pengirim
#         ttk.Label(self.root, text="Email Pengirim:").grid(row=0, column=0, padx=5, pady=5)
#         self.sender_email_entry = ttk.Entry(self.root, width=30)
#         self.sender_email_entry.grid(row=0, column=1, padx=5, pady=5)

#         # Label dan Entry untuk kata sandi email pengirim
#         ttk.Label(self.root, text="Kata Sandi:").grid(row=1, column=0, padx=5, pady=5)
#         self.password_entry = ttk.Entry(self.root, show="*", width=30)
#         self.password_entry.grid(row=1, column=1, padx=5, pady=5)

#         # Label dan Entry untuk alamat email penerima
#         ttk.Label(self.root, text="Email Penerima:").grid(row=2, column=0, padx=5, pady=5)
#         self.receiver_email_entry = ttk.Entry(self.root, width=30)
#         self.receiver_email_entry.grid(row=2, column=1, padx=5, pady=5)

#         # Label dan Entry untuk subjek email
#         ttk.Label(self.root, text="Subjek:").grid(row=3, column=0, padx=5, pady=5)
#         self.subject_entry = ttk.Entry(self.root, width=30)
#         self.subject_entry.grid(row=3, column=1, padx=5, pady=5)

#         # Label dan Text untuk isi email
#         ttk.Label(self.root, text="Isi Email:").grid(row=4, column=0, padx=5, pady=5)
#         self.message_text = tk.Text(self.root, wrap="word", width=30, height=5)
#         self.message_text.grid(row=4, column=1, padx=5, pady=5)

# #         # Tombol untuk mengirim email hari ini
# #         send_now_button = ttk.Button(self.root, text="Kirim Hari Ini", command=self.send_email_now)
# #         send_now_button.grid(row=5, column=0, columnspan=2, pady=5)

# #         # Tombol untuk menjadwalkan pengiriman email 3 bulan kemudian
# #         schedule_button = ttk.Button(self.root, text="Jadwalkan Pengiriman 3 Bulan", command=self.schedule_email)
# #         schedule_button.grid(row=6, column=0, columnspan=2, pady=5)

# #     def send_email(self, sender_email, password, receiver_email, subject, message):
# #         email = MIMEMultipart()
# #         email["From"] = sender_email
# #         email["To"] = receiver_email
# #         email["Subject"] = subject
# #         email.attach(MIMEText(message, "plain"))

#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, email.as_string())

#     def send_email_now(self):
#         sender_email = self.sender_email_entry.get()
#         password = self.password_entry.get()
#         receiver_email = self.receiver_email_entry.get()
#         subject = self.subject_entry.get()
#         message = self.message_text.get("1.0", tk.END)

#         self.send_email(sender_email, password, receiver_email, subject, message)
#         self.show_info("Email berhasil dikirim hari ini!")

#     def schedule_email(self):
#         sender_email = self.sender_email_entry.get()
#         password = self.password_entry.get()
#         receiver_email = self.receiver_email_entry.get()
#         subject = self.subject_entry.get()
#         message = self.message_text.get("1.0", tk.END)

#         # Jadwalkan pengiriman email 3 bulan dari hari ini
#         scheduled_time = datetime.now() + timedelta(days=90)

#         # Buat thread terpisah untuk menjalankan schedule
#         threading.Thread(target=self.schedule_email_thread, args=(sender_email, password, receiver_email, subject, message, scheduled_time)).start()

#         self.show_info(f"Email akan dijadwalkan untuk dikirim pada {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}.")

#     def schedule_email_thread(self, sender_email, password, receiver_email, subject, message, scheduled_time):
#         now = datetime.now()

#         # Hitung selisih waktu antara sekarang dan waktu jadwal
#         delay = (scheduled_time - now).total_seconds()

#         # Tunggu sampai waktunya untuk mengirim email
#         time.sleep(delay)

#         # Kirim email sesuai jadwal
#         self.send_email(sender_email, password, receiver_email, subject, message)
#         self.show_info("Email berhasil dijadwalkan!")

#     def show_info(self, message):
#         tk.messagebox.showinfo("Info", message)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EmailSchedulerApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime, timedelta
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# class EmailSchedulerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Email Scheduler App")
#         self.setup_gui()

#     def setup_gui(self):
#         # ... (sama seperti sebelumnya)
#         # Label dan Entry untuk alamat email pengirim
#         ttk.Label(self.root, text="Email Pengirim:").grid(row=0, column=0, padx=5, pady=5)
#         self.sender_email_entry = ttk.Entry(self.root, width=30)
#         self.sender_email_entry.grid(row=0, column=1, padx=5, pady=5)

#         # Label dan Entry untuk kata sandi email pengirim
#         ttk.Label(self.root, text="Kata Sandi:").grid(row=1, column=0, padx=5, pady=5)
#         self.password_entry = ttk.Entry(self.root, show="*", width=30)
#         self.password_entry.grid(row=1, column=1, padx=5, pady=5)

#         # Label dan Entry untuk alamat email penerima
#         ttk.Label(self.root, text="Email Penerima:").grid(row=2, column=0, padx=5, pady=5)
#         self.receiver_email_entry = ttk.Entry(self.root, width=30)
#         self.receiver_email_entry.grid(row=2, column=1, padx=5, pady=5)

#         # Label dan Entry untuk subjek email
#         ttk.Label(self.root, text="Subjek:").grid(row=3, column=0, padx=5, pady=5)
#         self.subject_entry = ttk.Entry(self.root, width=30)
#         self.subject_entry.grid(row=3, column=1, padx=5, pady=5)

#         # Label dan Text untuk isi email
#         ttk.Label(self.root, text="Isi Email:").grid(row=4, column=0, padx=5, pady=5)
#         self.message_text = tk.Text(self.root, wrap="word", width=30, height=5)
#         self.message_text.grid(row=4, column=1, padx=5, pady=5)

#         # Tombol untuk mengirim email hari ini
#         send_now_button = ttk.Button(self.root, text="Kirim Hari Ini", command=self.send_email_now)
#         send_now_button.grid(row=5, column=0, columnspan=2, pady=5)

#         # Tombol untuk menjadwalkan pengiriman email 3 bulan kemudian
#         schedule_button = ttk.Button(self.root, text="Jadwalkan Pengiriman 3 Bulan", command=self.schedule_email)
#         schedule_button.grid(row=6, column=0, columnspan=2, pady=5)

#     def send_email(self, sender_email, password, receiver_email, subject, message):
#         email = MIMEMultipart()
#         email["From"] = sender_email
#         email["To"] = receiver_email
#         email["Subject"] = subject
#         email.attach(MIMEText(message, "plain"))

#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, email.as_string())

#     def send_email_now(self):
#         sender_email = self.sender_email_entry.get()
#         password = self.password_entry.get()
#         receiver_email = self.receiver_email_entry.get()
#         subject = self.subject_entry.get()
#         message = self.message_text.get("1.0", tk.END)

#         self.send_email(sender_email, password, receiver_email, subject, message)
#         self.show_info("Email berhasil dikirim hari ini!")

#     def schedule_email(self):
#         sender_email = self.sender_email_entry.get()
#         password = self.password_entry.get()
#         receiver_email = self.receiver_email_entry.get()
#         subject = self.subject_entry.get()
#         message = self.message_text.get("1.0", tk.END)

#         # Jadwalkan pengiriman email 3 bulan dari hari ini
#         scheduled_time = datetime.now() + timedelta(days=90)

#         # Jadwalkan operasi untuk menjalankan thread di dalam event loop utama
#         self.root.after(1, self.schedule_email_thread, sender_email, password, receiver_email, subject, message, scheduled_time)

#         self.show_info(f"Email akan dijadwalkan untuk dikirim pada {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}.")

#     def schedule_email_thread(self, sender_email, password, receiver_email, subject, message, scheduled_time):
#         now = datetime.now()

#         # Hitung selisih waktu antara sekarang dan waktu jadwal
#         delay = (scheduled_time - now).total_seconds()

#         # Tunggu sampai waktunya untuk mengirim email
#         self.root.after(int(delay * 1000), lambda: self.send_email(sender_email, password, receiver_email, subject, message))
#         self.show_info("Email berhasil dijadwalkan!")

#     def show_info(self, message):
#         tk.messagebox.showinfo("Info", message)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EmailSchedulerApp(root)
#     root.mainloop()
# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime, timedelta
# from tkcalendar import DateEntry
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# class EmailSchedulerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Email Scheduler App")
#         self.setup_gui()

#     def setup_gui(self):
#         # Label dan Entry untuk alamat email pengirim
#         ttk.Label(self.root, text="Email Pengirim:").grid(row=0, column=0, padx=5, pady=5)
#         self.sender_email_entry = ttk.Entry(self.root, width=30)
#         self.sender_email_entry.grid(row=0, column=1, padx=5, pady=5)

#         # Label dan Entry untuk kata sandi email pengirim
#         ttk.Label(self.root, text="Kata Sandi:").grid(row=1, column=0, padx=5, pady=5)
#         self.password_entry = ttk.Entry(self.root, show="*", width=30)
#         self.password_entry.grid(row=1, column=1, padx=5, pady=5)

#         # Label dan Entry untuk alamat email penerima
#         ttk.Label(self.root, text="Email Penerima:").grid(row=2, column=0, padx=5, pady=5)
#         self.receiver_email_entry = ttk.Entry(self.root, width=30)
#         self.receiver_email_entry.grid(row=2, column=1, padx=5, pady=5)

#         # Label dan Entry untuk subjek email
#         ttk.Label(self.root, text="Subjek:").grid(row=3, column=0, padx=5, pady=5)
#         self.subject_entry = ttk.Entry(self.root, width=30)
#         self.subject_entry.grid(row=3, column=1, padx=5, pady=5)

#         # Label dan Text untuk isi email
#         ttk.Label(self.root, text="Isi Email:").grid(row=4, column=0, padx=5, pady=5)
#         self.message_text = tk.Text(self.root, wrap="word", width=30, height=5)
#         self.message_text.grid(row=4, column=1, padx=5, pady=5)

#         # Widget kalender untuk memilih tanggal
#         ttk.Label(self.root, text="Pilih Tanggal Jadwal:").grid(row=5, column=0, padx=5, pady=5)
#         self.calendar = DateEntry(self.root, width=30, background='darkblue', foreground='white', borderwidth=2, year=2022)
#         self.calendar.grid(row=5, column=1, padx=5, pady=5)

#         # Tombol untuk mengirim email
#         send_button = ttk.Button(self.root, text="Kirim Email", command=self.send_scheduled_email)
#         send_button.grid(row=6, column=0, columnspan=2, pady=10)

#     def send_email(self, sender_email, password, receiver_email, subject, message):
#         email = MIMEMultipart()
#         email["From"] = sender_email
#         email["To"] = receiver_email
#         email["Subject"] = subject
#         email.attach(MIMEText(message, "plain"))

#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, email.as_string())

#     def send_scheduled_email(self):
#         sender_email = self.sender_email_entry.get()
#         password = self.password_entry.get()
#         receiver_email = self.receiver_email_entry.get()
#         subject = self.subject_entry.get()
#         message = self.message_text.get("1.0", tk.END)

#         selected_date = self.calendar.get_date()
#         scheduled_time = datetime(selected_date.year, selected_date.month, selected_date.day) + timedelta(days=90)

#         # Jadwalkan operasi untuk menjalankan thread di dalam event loop utama
#         self.root.after(1, self.schedule_email_thread, sender_email, password, receiver_email, subject, message, scheduled_time)

#         self.show_info(f"Email akan dijadwalkan untuk dikirim pada {scheduled_time.strftime('%Y-%m-%d')}.")

#     def schedule_email_thread(self, sender_email, password, receiver_email, subject, message, scheduled_time):
#         now = datetime.now()

#         # Hitung selisih waktu antara sekarang dan waktu jadwal
#         delay = (scheduled_time - now).total_seconds()

#         # Tunggu sampai waktunya untuk mengirim email
#         self.root.after(int(delay * 1000), lambda: self.send_email(sender_email, password, receiver_email, subject, message))
#         self.show_info("Email berhasil dijadwalkan!")

#     def show_info(self, message):
#         tk.messagebox.showinfo("Info", message)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EmailSchedulerApp(root)
#     root.mainloop()


# import csv
# from datetime import datetime, timedelta 
# import smtplib

# def read_last_line(csv_file):
#     with open(csv_file, 'r', newline='') as file:
#         # Membuka file CSV
#         reader = csv.reader(file)

#         # Membaca setiap baris
#         rows = list(reader)

#         # Mengembalikan baris terakhir
#         if rows:
#             a = rows[-1]
#             for row in a:
#                 present = datetime.now()
#                 formatted_date = present.strftime('%d/%m/%y')
# #                 if  row[-1] == formatted_date:
#                     gmail_user = "s.techcorpss@gmail.com"
#                     gmail_app_password = "jmob eqfu ilta hhgf"
                    

#                     sent_from = gmail_user
#                     sent_to = "dealishah@gmail.com"
#                     sent_subject = "kukukaka"
#                     sent_body = f"Dear customer, Please service your AC ASAP! thank you for using our apps, your last service is {self.mydate}, reminder has sucessfully set, we'll remind you to service your AC three months after your last service \n\nwith note: {self.noteRemind.get()}"


#                     email_text = f"""\
#                     From : {sent_from}
#                     To: {sent_to}
#                     Subject: {sent_subject}

#                     {sent_body}
#                     """

#                     try:
#                         server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#                         server.ehlo()
#                         server.login(gmail_user, gmail_app_password)
#                         server.sendmail(sent_from,sent_to, email_text)
#                         print("email 22 berhasil dikirim")
#                         print("Info", "Reminder berhasil di set")
#                         break
#                     except Exception as exception:
#                         print("Error: %s!\n\n" % exception)           
                    

# import csv
# from datetime import datetime, timedelta 
# import smtplib


# def read_last_row_columns(csv_file):
#     with open(csv_file, 'r', newline='') as file:
#         # Membuka file CSV
#         reader = csv.reader(file)

#         # Membaca setiap baris dan menyimpannya
#         rows = list(reader)

#         # Mengembalikan kolom-kolom dari baris terakhir
#         if rows:
#             last_row = rows[-1]
#             return last_row
#         else:
#             return None

# # Contoh penggunaan
# csv_file_path = 'dataremind.csv'
# last_row_columns = read_last_row_columns(csv_file_path)
# present = datetime.now()
# formatted_date = present.strftime('%d/%m/%y')
# if last_row_columns[-1]== formatted_date:
#                     print("Kolom-kolom dalam baris terakhir dari file CSV:")
#                     print(last_row_columns[-1])
#                     gmail_user = "s.techcorpss@gmail.com"
#                     gmail_app_password = "jmob eqfu ilta hhgf"
                    

#                     sent_from = gmail_user
#                     sent_to = "dealishah@gmail.com"
#                     sent_subject = "kukukaka"
#                     sent_body = f"Dear customer, Please service your AC ASAP! thank you for using our apps, your last service is , reminder has sucessfully set, we'll remind you to service your AC three months after your last service \n\nwith note: "


#                     email_text = f"""\
#                     From : {sent_from}
#                     To: {sent_to}
#                     Subject: {sent_subject}

#                     {sent_body}
#                     """

#                     try:
#                         server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#                         server.ehlo()
#                         server.login(gmail_user, gmail_app_password)
#                         server.sendmail(sent_from,sent_to, email_text)
#                         print("email 22 berhasil dikirim")
#                         print("Info", "Reminder berhasil di set")
                        
#                     except Exception as exception:
#                         print("Error: %s!\n\n" % exception)           
                    
# else:
#     print("File CSV kosong atau tidak dapat dibaca.")

    


    

            
    




        


# #         else:
# #             return None

# # # Contoh penggunaan
# # csv_file_path = 'dataremind.csv'
# # last_line = read_last_line(csv_file_path)

# # if last_line:
# #     print("Data terakhir dalam file CSV:")
# #     print(last_line)
# # else:
# #     print("File CSV kosong atau tidak dapat dibaca.")





# import tkinter as tk
# from tkinter import messagebox
# import os

# def save():
#     bill_no.set(str(x))
#     op = messagebox.askyesno("Save bill", "Do you want to save the Bill?")
#     if op > 0:
#         bill_details = text_struk.get('1.0', tk.END)
        
        
#         if not os.path.exists("bills"):
#             os.makedirs("bills")
        
#         file_path = os.path.join("bills", str(bill_no.get()) + ".txt")
        
        
#         with open(file_path, "w") as f1:
#             f1.write(bill_details)
        
#         messagebox.showinfo("Saved", f"Bill no. : {bill_no.get()} Saved Successfully")
#     else:
#         return


# def save_button_clicked():
#     save()


# root = tk.Tk()
# root.title("Bill Saving App")


# x = 1
# bill_no = tk.StringVar()


# label_bill_no = tk.Label(root, text="Bill Number:")
# label_bill_no.pack()


# entry_bill_no = tk.Entry(root, textvariable=bill_no, state="readonly")
# entry_bill_no.pack()


# text_struk = tk.Text(root, height=10, width=40)
# text_struk.pack()


# save_button = tk.Button(root, text="Save", command=save_button_clicked)
# save_button.pack()

# root.mainloop()


# import tkinter as tk
# from tkinter import StringVar

# class JasaACRecommendationApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Rekomendasi Layanan Jasa AC")

#         self.frame_konsul = tk.Frame(root, bg="#f8f8f8")
#         self.frame_konsul.pack(padx=20, pady=20)

#         self.konsultasi_vars = []
#         self.masalah_ac = []

#         for i in range(1, 8):
#             konsultasi_var = StringVar()
#             konsultasi_var.set("Tidak")
#             self.konsultasi_vars.append(konsultasi_var)

#             tk.Radiobutton(
#                 self.frame_konsul,
#                 text="Ya",
#                 value="Ya",
#                 variable=konsultasi_var,
#                 bg="#f8f8f8"
#             ).place(x=60, y=130 + 50 * (i - 1))

#             tk.Radiobutton(
#                 self.frame_konsul,
#                 text="Tidak",
#                 value="Tidak",
#                 variable=konsultasi_var,
#                 bg="#f8f8f8"
#             ).place(x=120, y=130 + 50 * (i - 1))

#         booking_button = tk.Button(self.frame_konsul, width=100, text="Result", command=self.konsul2)
#         booking_button.place(x=340, y=470)
#         close_button = tk.Button(self.frame_konsul, width=100, text="Close", command=root.destroy)
#         close_button.place(x=80, y=470)

#     def konsul2(self):
#         self.masalah_ac = []

#         for i in range(1, 8):
#             if self.konsultasi_vars[i - 1].get() == "Ya":
#                 masalah = f"✼Masalah {i}:\nAnda bisa pilih layanan jasa yang sesuai.\n"
#                 self.masalah_ac.append(masalah)

#         if self.masalah_ac:
#             result_text = "\n".join(self.masalah_ac)
#             result_window = tk.Toplevel(self.root)
#             result_window.title("Hasil Rekomendasi")
#             result_label = tk.Label(result_window, text=result_text, padx=20, pady=20)
#             result_label.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = JasaACRecommendationApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import StringVar

# class JasaACRecommendationApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Rekomendasi Layanan Jasa AC")

#         self.frame_konsul = tk.Frame(root, bg="#f8f8f8")
#         self.frame_konsul.pack(padx=20, pady=20)

#         self.konsultasi_vars = []
#         self.masalah_ac = []

#         for i in range(1, 8):
#             konsultasi_var = StringVar()
#             konsultasi_var.set("Tidak")
#             self.konsultasi_vars.append(konsultasi_var)

#             tk.Radiobutton(
#                 self.frame_konsul,
#                 text="Ya",
#                 value="Ya",
#                 variable=konsultasi_var,
#                 bg="#f8f8f8"
#             ).place(x=60, y=130 + 50 * (i - 1))

#             tk.Radiobutton(
#                 self.frame_konsul,
#                 text="Tidak",
#                 value="Tidak",
#                 variable=konsultasi_var,
#                 bg="#f8f8f8"
#             ).place(x=120, y=130 + 50 * (i - 1))

#         booking_button = tk.Button(self.frame_konsul, width=100, text="Result", command=self.konsul2)
#         booking_button.place(x=340, y=470)
#         close_button = tk.Button(self.frame_konsul, width=100, text="Close", command=root.destroy)
#         close_button.place(x=80, y=470)

#     def konsul2(self):
#         self.masalah_ac = []

#         for i in range(1, 8):
#             if self.konsultasi_vars[i - 1].get() == "Ya":
#                 masalah = f"✼Masalah {i}:\nAnda bisa pilih layanan jasa yang sesuai.\n"
#                 self.masalah_ac.append(masalah)

#         if self.masalah_ac:
#             result_text = "\n".join(self.masalah_ac)
#             result_window = tk.Toplevel(self.root)
#             result_window.title("Hasil Rekomendasi")
#             result_label = tk.Label(result_window, text=result_text, padx=20, pady=20)
#             result_label.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = JasaACRecommendationApp(root)
#     root.mainloop()
# import tkinter as tk

# class PurchaseRecommendationApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Quiz dan Pembelian Recommendation")

#         # Frame untuk Quiz
#         self.frame_quiz = tk.Frame(root, bg="#f8f8f8")
#         self.frame_quiz.pack(padx=20, pady=20)

#         self.quiz_a_var = tk.StringVar()
#         self.quiz_a_var.set("Tidak")
#         quiz_a_label = tk.Label(self.frame_quiz, text="Quiz A: Merekomendasikan untuk membeli sayur", bg="#f8f8f8")
#         quiz_a_label.pack()

#         quiz_a_checkbox = tk.Checkbutton(self.frame_quiz, text="Centang jika ingin membeli sayur", variable=self.quiz_a_var, bg="#f8f8f8")
#         quiz_a_checkbox.pack()

#         self.quiz_b_var = tk.StringVar()
#         self.quiz_b_var.set("Tidak")
#         quiz_b_label = tk.Label(self.frame_quiz, text="Quiz B: Merekomendasikan untuk membeli buah", bg="#f8f8f8")
#         quiz_b_label.pack()

#         quiz_b_checkbox = tk.Checkbutton(self.frame_quiz, text="Centang jika ingin membeli buah", variable=self.quiz_b_var, bg="#f8f8f8")
#         quiz_b_checkbox.pack()

#         # Frame untuk Pembelian
#         self.frame_pembelian = tk.Frame(root, bg="#f8f8f8")
#         self.frame_pembelian.pack(padx=20, pady=20)

#         purchase_label = tk.Label(self.frame_pembelian, text="Pembelian", bg="#f8f8f8")
#         purchase_label.pack()

#         self.purchase_var = tk.StringVar()
#         purchase_checkbox = tk.Checkbutton(self.frame_pembelian, text="Beli", variable=self.purchase_var, bg="#f8f8f8")
#         purchase_checkbox.pack()

#         result_button = tk.Button(root, text="Lihat Rekomendasi", command=self.lihat_rekomendasi)
#         result_button.pack()

#     def lihat_rekomendasi(self):
#         if self.quiz_a_var.get() == "Ya":
#             print("Rekomendasi: Beli sayur")
#         elif self.quiz_b_var.get() == "Ya":
#             print("Rekomendasi: Beli buah")
#         else:
#             print("Tidak ada rekomendasi pembelian")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PurchaseRecommendationApp(root)
#     root.mainloop()



# import tkinter as tk

# class PurchaseRecommendationApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Quiz dan Pembelian Recommendation")

#         # Frame untuk Quiz
#         self.frame_quiz = tk.Frame(root, bg="#f8f8f8")
#         self.frame_quiz.pack(padx=20, pady=20)

#         self.quiz_a_var = tk.StringVar()
#         self.quiz_a_var.set("Tidak")
#         quiz_a_label = tk.Label(self.frame_quiz, text="Quiz A: Merekomendasikan untuk membeli sayur", bg="#f8f8f8")
#         quiz_a_label.pack()

#         quiz_a_checkbox = tk.Checkbutton(self.frame_quiz, text="Centang jika ingin membeli sayur", variable=self.quiz_a_var, bg="#f8f8f8", command=self.update_purchase_checkbox)
#         quiz_a_checkbox.pack()

#         self.quiz_b_var = tk.StringVar()
#         self.quiz_b_var.set("Tidak")
#         quiz_b_label = tk.Label(self.frame_quiz, text="Quiz B: Merekomendasikan untuk membeli buah", bg="#f8f8f8")
#         quiz_b_label.pack()

#         quiz_b_checkbox = tk.Checkbutton(self.frame_quiz, text="Centang jika ingin membeli buah", variable=self.quiz_b_var, bg="#f8f8f8", command=self.update_purchase_checkbox)
#         quiz_b_checkbox.pack()

#         # Frame untuk Pembelian
#         self.frame_pembelian = tk.Frame(root, bg="#f8f8f8")
#         self.frame_pembelian.pack(padx=20, pady=20)

#         purchase_label = tk.Label(self.frame_pembelian, text="Pembelian", bg="#f8f8f8")
#         purchase_label.pack()

#         self.purchase_var = tk.StringVar()
#         purchase_checkbox = tk.Checkbutton(self.frame_pembelian, text="Beli", variable=self.purchase_var, bg="#f8f8f8")
#         purchase_checkbox.pack()

#         result_button = tk.Button(root, text="Lihat Rekomendasi", command=self.lihat_rekomendasi)
#         result_button.pack()

#     def update_purchase_checkbox(self):
#         # Jika quiz A atau quiz B dicentang, checkbox pembelian otomatis dicentang
#         if self.quiz_a_var.get() == "Ya" or self.quiz_b_var.get() == "Ya":
#             self.purchase_var.set("Ya")
#         else:
#             self.purchase_var.set("Tidak")

#     def lihat_rekomendasi(self):
#         if self.quiz_a_var.get() == "Ya":
#             print("Rekomendasi: Beli sayur")
#         elif self.quiz_b_var.get() == "Ya":
#             print("Rekomendasi: Beli buah")
#         else:
#             print("Tidak ada rekomendasi pembelian")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PurchaseRecommendationApp(root)
#     root.mainloop()


import tkinter as tk

class CheckButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Check Button Berkaitan")

        self.checkbutton_var1 = tk.IntVar()
        self.checkbutton_var2 = tk.IntVar()

        checkbutton1 = tk.Checkbutton(root, text="Check Button 1", variable=self.checkbutton_var1, command=self.update_checkbutton2)
        checkbutton1.pack(pady=10)

        checkbutton2 = tk.Checkbutton(root, text="Check Button 2", variable=self.checkbutton_var2)
        checkbutton2.pack(pady=10)

    def update_checkbutton2(self):
        # Fungsi ini dipanggil saat check button pertama dicentang
        if self.checkbutton_var1.get() == 1:
            self.checkbutton_var2.set(1)
        else:
            self.checkbutton_var2.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckButtonApp(root)
    root.mainloop()

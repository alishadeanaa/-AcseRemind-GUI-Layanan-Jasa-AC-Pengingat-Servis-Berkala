from tkinter import *
import tkinter as tk
from tkinter import messagebox,scrolledtext
from PIL import Image,ImageTk
import customtkinter as ctk
import csv
from tkcalendar import *
import smtplib
from datetime import datetime, timedelta 



window = Tk()

class ACseRemind:

    def __init__ (self,window):
        self.username = StringVar()
        self.password = StringVar()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.phone_number= IntVar()
        self.address = StringVar()

        #============ background ==========#

        self.window = window  
        window.title("AC seRemind")
        window.state('zoomed')
        window.resizable(0,0)
        self.bg = PhotoImage(file="loginn2.png")
        self.a_label1=Label(window, image=self.bg)
        self.a_label1.place(x=0,y=0, relheight=1,relwidth=1)

        #======= LOG IN =======#

        self.label_username = Label(window, text="Username", bg = "#75bfd5", font=("sans serif",10,"bold"),fg="#0370a9").place(x=250,y=270)
        self.entry_username = Entry(window, textvariable=self.username,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",13),bg="white",fg="#0370a9").place(x=250, y=300)


        self.label_password = Label(window, text="Password", bg = "#75bfd5", font=("sans serif",10,"bold"),fg="#0370a9").place(x=250,y=345)
        self.entry_password = Entry(window, textvariable=self.password,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",13),bg="white",fg="#0370a9",show='*')
        self.entry_password.place(x=250, y=375)

        self.button_lupapsw = Button(window,text="Forgot Password?",bg = "#75bfd5", font=("sans serif",8),fg="black",command=self.forgot_password,
                                     highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=500,y=410)
        
        self.label_gapunya_akun = Label(window,text="Don't have a account?",bg = "#8ec8d9", font=("sans serif",8),fg="black").place(x=250,y=480)
        self.button_sign_in = Button(window,text="Sign in",bg = "#94cddf", font=("sans serif",8,"bold underline"),fg="blue",command=self.show_sign_in_window,
                                     highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=366,y=480)
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.button_login = ctk.CTkButton(window,command=self.login,text="LOGIN",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#92bee0",width=350)
        self.button_login.place(x=250,y=450)
        

        showpsw = Checkbutton(window, bg="#75bfd5", command=self.show_psw, text="show password",font=("sans serif",8))
        showpsw.place(x=250,y=410)

    #=========Show Password=========#

    def show_psw(self):
        if self.entry_password.cget("show") == "*":
            self.entry_password.config(show='')
        else:
            self.entry_password.config(show="*")

    #===================CHECK LOG IN===============#
    def login(self):
        username = self.username.get()
        password = self.password.get()

        with open('dataservice.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username and row['Password'] == password:
                    messagebox.showinfo("Login", "Login berhasil!")   
                    self.dashboard() 
                    return

        messagebox.showerror("Login", "Username atau password Invalid!")

        
#=========== LUPA PASSWORD ===========#
    def forgot_password(self):
        window = Toplevel()
        window.geometry('500x500')
        window.title('Forgot Password')
        window.configure(background='#f8f8f8')
        window.resizable(0, 0)

        self.new_password_label = Label(window, text="New Password", bg="#f8f8f8", font=("sans serif", 10, "bold"), fg="#0370a9").place(x=50, y=125)
        self.new_password_entry = Entry(window, show='*', border=0, highlightthickness=2, highlightcolor="#0370a9",
                                        relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.new_password_entry.place(x=50, y=155)

        self.confirm_password_label = Label(window, text="Confirm Password", bg="#f8f8f8",
                                        font=("sans serif", 10, "bold"), fg="#0370a9").place(x=50, y=200)
        self.confirm_password_entry = Entry(window, show='*', border=0, highlightthickness=2, highlightcolor="#0370a9",
                                        relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.confirm_password_entry.place(x=50, y=230)

        self.submit_button = ctk.CTkButton(window, text="Submit", font=("sans serif", 12, "bold"), width=350,
                                                command=self.submit_new_password)
        self.submit_button.place(x=50, y=260)

#=============== CHECK NEW PASSWORD =============#
    def submit_new_password(self):
        
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password == confirm_password:
            username = self.username.get()
            with open('dataservice.csv', 'r') as file:
                reader = csv.DictReader(file)
                rows = list(reader)


            ada_username = False
            for row in rows:
                if row['Username'] == username:
                    ada_username = True
                    row['Password'] = new_password

            if ada_username:
                with open('dataservice.csv', 'w', newline='') as file:
                    fieldnames = ['First Name', 'Last Name', 'Phone Number', 'Address', 'Username', 'Password']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                messagebox.showinfo("Password Updated", "Password updated successfully!")
            else:
                messagebox.showerror("Error", "Username tidak terdaftar")
        else:
            messagebox.showerror("Error", "Periksa confirm password Anda")
        
#===================SIGN IN==============#
    def show_sign_in_window(self):
        sign_in_window = Toplevel()
        sign_in_window.geometry('500x600')
        sign_in_window.title('Sign In')
        sign_in_window.configure(background='#f8f8f8')
        sign_in_window.resizable(0, 0)
        self.username = StringVar()
        self.password = StringVar()

        self.sign_in_label = Label(sign_in_window, text="Sign In", font=("sans serif", 16, "bold"), fg="#0370a9",
                              bg="#f8f8f8").place(x=150, y=10)

        self.first_name_label = Label(sign_in_window, text="First Name", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                                 fg="#0370a9").place(x=50, y=50)
        self.first_name_entry = Entry(sign_in_window, textvariable=self.firstname,border=0, highlightthickness=2, highlightcolor="#0370a9",
                                      relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.first_name_entry.place(x=50, y=80)


        self.last_name_label = Label(sign_in_window, text="Last Name", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                                fg="#0370a9").place(x=50, y=125)
        self.last_name_entry = Entry(sign_in_window, textvariable=self.lastname,border=0, highlightthickness=2, highlightcolor="#0370a9",
                                     relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.last_name_entry.place(x=50, y=155)


        self.phone_number_label = Label(sign_in_window, text="Phone Number", bg="#f8f8f8",
                                   font=("sans serif", 10, "bold"), fg="#0370a9").place(x=50, y=200)
        self.phone_number_entry = Entry(sign_in_window, textvariable=self.phone_number,border=0, highlightthickness=2, highlightcolor="#0370a9",
                                        relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.phone_number_entry.place(x=50, y=230)


        self.address_label = Label(sign_in_window, text="Address", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                              fg="#0370a9").place(x=50, y=275)
        self.address_entry = Entry(sign_in_window,textvariable=self.address, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                   relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.address_entry.place(x=50, y=305)


        self.username_label = Label(sign_in_window, text="Username", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                               fg="#0370a9").place(x=50, y=350)
        self.username_entry = Entry(sign_in_window, border=0, textvariable=self.username,highlightthickness=2, highlightcolor="#0370a9",
                                    relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.username_entry.place(x=50, y=380)


        self.password_label = Label(sign_in_window, text="Password", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                               fg="#0370a9").place(x=50, y=425)
        self.password_entry = Entry(sign_in_window,textvariable=self.password, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                    relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black",
                                    show='*')
        self.password_entry.place(x=50, y=455)


        sign_in_button = ctk.CTkButton(sign_in_window,command=self.signup, text="Sign In", font=("sans serif", 12, "bold"),
                                                 width=350)
        sign_in_button.place(x=50, y=500)

    #+======================SIGN UP==========#
    def signup(self):
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        phonenumber = self.phone_number_entry.get()
        address = self.address_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not all([firstname, lastname, phonenumber, address, username, password]):
            messagebox.showerror("Signup", "Harap isi semua kolom untuk melakukan sign in.")
            return

        with open('dataservice.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username:
                    messagebox.showerror("Signup", "Username sudah ada!")
                    return

        with open('dataservice.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([firstname, lastname, phonenumber, address, username, password])
        messagebox.showinfo("Signup", "Signup berhasil!")

#===========DASHBOARD========#

    def dashboard(self):

        self.a_label1.destroy()
        self.window = window  
        self.bg = PhotoImage(file="dashboard.png")
        self.a_label2 = Label(window, image=self.bg)
        self.a_label2.place(x=0, y=0, relheight=1, relwidth=1)
        username = self.username.get()
        # self.nama_dashboard = ctk.CTkFrame(window,width=350,height=200,bg_color='transparent')
        # self.nama_dashboard.place(x=150, y=90)

        with open('dataservice.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Username'] == username:
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    # self.nama_label_dshbrd = Label(self.nama_dashboard, text=f"WELCOME {first_name} {last_name} \nTO S.TECH \nAC SERVICE REMINDER", font=("Roboto", 25, "bold"))
                    # self.nama_label_dshbrd.place(x=0, y=10)
                    self.nama_label_dshbrd = ctk.CTkLabel(window,corner_radius=20,text=f"WELCOME, {first_name} {last_name}\nTO S.TECH\nAC SERVICE REMINDER!",font=("Hack",30,"bold"),fg_color='#1679ad',bg_color="#1679ad",text_color='white')
                    self.nama_label_dshbrd.place(x=350, y=220,anchor='center')
                    break
 
        # self.button_tentang=Button(window, command=self.reminder,text="Reminder",bg="#0370a9",foreground="white" ,font=("gothic",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        # self.button_tentang.place(x=920,y=600)

    #==================JASA SERVICE===============#
        # self.label_jasa_service = ctk.CTkLabel(window,corner_radius=20,text="Jasa Service AC",font=("Hack",30,"bold"),fg_color='white',bg_color='#97bad5',text_color='black')
        # self.label_jasa_service.place(x=820,y=120)
        self.fotoA=PhotoImage(file="jasa a.png")
        self.fotoB= PhotoImage(file="jasa b.png")
        self.fotoC= PhotoImage(file="jasa c.png")
        self.fotoD= PhotoImage(file="jasa d.png")

        # value = IntVar()
        self.button_jasa_A = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoA,hover_color='#adbec8',bg_color="#8fc5d7",fg_color="white",compound=TOP,anchor=N,text="Rp. 80.000,-\n Botania Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768", command=self.jasa_A)
        self.button_jasa_A.place(x=780,y=200)

        self.button_jasa_B = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoB,hover_color='#adbec8',bg_color="#8fc5d7",fg_color="white",compound=TOP,anchor=N,text="Rp. 70.000,- \n ACTECH Service", font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768", command=self.jasa_B)
        self.button_jasa_B.place(x=1020,y=200)

        self.button_jasa_C = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoC,hover_color='#adbec8',bg_color="#8fc5d7",fg_color="white",compound=TOP,anchor=N, text="Rp. 60.000,- \n BORCHELE Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=self.jasa_C)
        self.button_jasa_C.place(x=780,y=430)

        self.button_jasa_D = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoD,hover_color='#adbec8',bg_color="#8fc5d7",fg_color="white",compound=TOP,anchor=N,text="Rp. 50.000,- \n JAYA service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=self.jasa_D)
        self.button_jasa_D.place(x=1020,y=430)
        # if self.button_jasa_A > 1:
    #  self.button_reminder=Button(window, command=self.reminder,text="Reminder",bg='#8cc6d7',fg="white", font=("Tw Cen MT Condensed Extra Bold",20),relief="flat")
        # self.button_reminder.place(x=930,y=50)

        self.button_reminder=Button(window, command=self.reminder,text="Reminder",bg="#8cc6d7",foreground="white" ,font=("gothic",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        self.button_reminder.place(x=1000,y=55)

        # self.button_booking=Button(window, command=self.booking,text="Booking",bg="#8cc6d7",foreground="white" ,font=("gothic",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        # self.button_booking.place(x=850,y=55)
        

    
    def jasa_A(self):
        global jasa_A_frame
        jasa_A_frame = ctk.CTkFrame(window,corner_radius=20,bg_color='#97bad5',border_width=3,border_color='black',fg_color='#f8f8f8',width=500,height=500)
        jasa_A_frame.place(x=750, y=140)

        Servis_Cuci = Label(jasa_A_frame,text="BOTANIA Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
        Servis_Cuci.place(x=35,y=15)

        Servis_Cuci = Label(jasa_A_frame,text="-Service Cuci\nAC\n-Tambah Freon\n-IsiFreon",font=("Consolas",11),bg='#f8f8f8',justify='left')
        Servis_Cuci.place(x=35,y=360)
        
        self.image_paths = [r"jasa a.png",r"jasaa1.png",r"jasaa2.png"]
        self.images = [Image.open(path) for path in self.image_paths]

        self.current_image_index = 0
        
        self.image_label = Label(jasa_A_frame, bg="#f8f8f8")
        self.image_label.place(x=35,y=150)

        self.scroll_images()

        deskripsi = scrolledtext.ScrolledText(jasa_A_frame,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
        deskripsi.insert(tk.END, "Service Cuci: Proses membersihkan \nkomponen-komponen dalam unit AC\n untuk menghilangkan debu, \nkotoran, dan potensi pembentukan\n jamur atau bakteri.\
                        \nTujuannya Menjaga kualitas udara \nyang keluar dari AC, meningkatkan\n efisiensi operasional, dan mencegah\n masalah kesehatan terkait udara.\n\nTambah Freon: Menambahkan refrigeran\n (biasanya Freon) ke dalam sistem AC\n untuk menjaga atau meningkatkan \ntingkat pendinginan.\
                        \nTujuannya Memastikan bahwa\n AC memiliki jumlah refrigeran \nyang tepat untuk berfungsi \nsecara efisien. Refrigeran digunakan \ndalam proses pendinginan dan\n mengubah fase gas-ke-cair \nuntuk menciptakan efek pendinginan.\n\nIsi Freon adalah Pemeriksaan dan Identifikasi Kebocoran: Sebelum mengisi \
                         \nfreon, teknisi AC biasanya melakukan\n pemeriksaan untuk mengidentifikasi kemungkinan\n kebocoran dalam sistem. Kebocoran dapat\n menyebabkan kehilangan refrigeran secara berkelanjutan.\
                        \nPengisian Refrigeran yang Hilang: Setelah \nkebocoran diidentifikasi dan diperbaiki, \nteknisi akan mengisi freon kembali ke dalam\n sistem untuk mengembalikan tingkat \nrefrigeran ke level yang direkomendasikan.\
                         \n\nAlamat: Jalan Mangga No.1,RT 01 RW 02,Kelurahan Besi Muda,\nKecamatan Wert,Kab.Brunei,\nSumatera Bawah.\
                         \n\n\nNo. WA : 082139948140")
        deskripsi.config(state=tk.DISABLED)
        deskripsi.place(x=250,y=15)

        def click():
            self.booking(1)
        booking_button = ctk.CTkButton(jasa_A_frame,width=100,text="Booking",command=click)
        booking_button.place(x=340,y=450)
        close_button = ctk.CTkButton(jasa_A_frame,width=100, text="Close", command=jasa_A_frame.destroy)
        close_button.place(x=50,y=450)

    def scroll_images(self):
        # Menampilkan gambar saat ini
        current_image = self.images[self.current_image_index]
        photo = ImageTk.PhotoImage(current_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Mengganti indeks gambar untuk menggulir ke gambar berikutnya
        self.current_image_index = (self.current_image_index + 1) % len(self.images)

        # Memanggil fungsi rekursif untuk menggulir gambar berikutnya setelah 2000 milidetik (2 detik)
        jasa_A_frame.after(2000, self.scroll_images)
        
    def jasa_B(self):
        global jasa_B_frame
        jasa_B_frame = ctk.CTkFrame(window,corner_radius=20,bg_color='#97bad5',border_width=3,border_color='black',fg_color='#f8f8f8',width=500,height=500)
        jasa_B_frame.place(x=740, y=140)

        Servis_Cuci = Label(jasa_B_frame,text="ACTECH Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
        Servis_Cuci.place(x=35,y=15)

        Servis_Cuci = Label(jasa_B_frame,text="-Service Cuci AC\n-Bongkar pasang AC",font=("Consolas",11),bg='#f8f8f8',justify='left')
        Servis_Cuci.place(x=35,y=330)

        # Daftar gambar yang akan digunakan
        self.image_paths = [r"jasa b.png",r"jasab1.png",r"jasab2.png"]
        self.images = [Image.open(path) for path in self.image_paths]

        # Indeks gambar saat ini
        self.current_image_index = 0

        # Tampilkan gambar pertama di dalam frame utama
        self.image_label = Label(jasa_B_frame, bg="#f8f8f8")
        self.image_label.place(x=35,y=150)

        # Memulai fungsi pengguliran otomatis

        deskripsi = scrolledtext.ScrolledText(jasa_B_frame,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
        deskripsi.insert(tk.END, "Service Cuci: Proses membersihkan \nkomponen-komponen dalam unit AC\n untuk menghilangkan debu, \nkotoran, dan potensi pembentukan\n jamur atau bakteri.\
                        \nTujuannya Menjaga kualitas udara \nyang keluar dari AC, meningkatkan\n efisiensi operasional, dan mencegah\n masalah kesehatan terkait udara.\n\nBongkar pasang AC\
                          adalah proses umum yang sering dilakukan untuk berbagai keperluan, seperti pemindahan AC ke lokasi baru, perbaikan, atau renovasi. Namun, sering muncul pertanyaan apakah bongkar pasang AC bisa merusak AC dengan cepat.\
                         Bongkar pasang AC memberikan peluang untuk \nmelakukan pemeliharaan dan perbaikan \nyang diperlukan. Membersihkan komponen AC, \nmengganti bagian yang aus, atau memperbaiki \nkerusakan dapat membantu mengembalikan \nperforma AC ke kondisi optimal.\
                         \n\nAlamat: Jalan Mangga No.1,RT 01 RW 02,Kelurahan Besi Muda,\nKecamatan Wert,Kab.Brunei,\nSumatera Bawah.\
                         \n\n\nNo. WA : 082139948140")
        deskripsi.config(state=tk.DISABLED)
        deskripsi.place(x=250,y=15)

        def click():
            self.booking(2)
        booking_button = ctk.CTkButton(jasa_B_frame,width=100,text="Booking",command=click)
        booking_button.place(x=340,y=450)

        close_button = ctk.CTkButton(jasa_B_frame,width=100, text="Close", command=jasa_B_frame.destroy)
        close_button.place(x=50,y=450)

        self.scroll_images2()

    def scroll_images2(self):
        # Menampilkan gambar saat ini
        current_image = self.images[self.current_image_index]
        photo = ImageTk.PhotoImage(current_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Mengganti indeks gambar untuk menggulir ke gambar berikutnya
        self.current_image_index = (self.current_image_index + 1) % len(self.images)

        # Memanggil fungsi rekursif untuk menggulir gambar berikutnya setelah 2000 milidetik (2 detik)
        jasa_B_frame.after(2000,self.scroll_images2)

    def jasa_C(self):
        global jasa_C_frame
        jasa_C_frame = ctk.CTkFrame(window,corner_radius=20,bg_color='#97bad5',border_width=3,border_color='black',fg_color='#f8f8f8',width=500,height=500)
        jasa_C_frame.place(x=740, y=140)

        Servis_Cuci = Label(jasa_C_frame,text="BORCELLE Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
        Servis_Cuci.place(x=35,y=15)

        Servis_Cuci = Label(jasa_C_frame,text="-Service Cuci AC\n-Penggantian kapasitor AC",font=("Consolas",11),bg='#f8f8f8',justify='left')
        Servis_Cuci.place(x=35,y=330)

        # Daftar gambar yang akan digunakan
        self.image_paths = [r"jasa c.png",r"jasac1.png",r"jasac2.png"]
        self.images = [Image.open(path) for path in self.image_paths]

        # Indeks gambar saat ini
        self.current_image_index = 0

        # Tampilkan gambar pertama di dalam frame utama
        self.image_label = Label(jasa_C_frame, bg="#f8f8f8")
        self.image_label.place(x=35,y=150)

        # Memulai fungsi pengguliran otomatis

        deskripsi = scrolledtext.ScrolledText(jasa_C_frame,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
        deskripsi.insert(tk.END, "Service Cuci: Proses membersihkan \nkomponen-komponen dalam unit AC\n untuk menghilangkan debu, \nkotoran, dan potensi pembentukan\n jamur atau bakteri.\
                        \nTujuannya Menjaga kualitas udara \nyang keluar dari AC, meningkatkan\n efisiensi operasional, dan mencegah\n masalah kesehatan terkait udara.\n\nperan kapasitor sangat \
                         penting dalam mendukung kinerja AC.\n Kerusakan kapasitor tak boleh\n dibiarkan begitu saja karena dapat mengganggu \nperforma AC secara keseluruhan. \
                         \nSetidaknya Anda harus memahami penyebab \nkapasitor AC rusak, ciri-ciri, serta \ncara mengatasinya supaya sigap mengantisipasi \ngangguan tersebut.\
                         \n\nAlamat: Jalan Mangga No.1,RT 01 RW 02,Kelurahan Besi Muda,\nKecamatan Wert,Kab.Brunei,\nSumatera Bawah.\
                         \n\n\nNo. WA : 082139948140")
        deskripsi.config(state=tk.DISABLED)
        deskripsi.place(x=250,y=15)

        def click():
            self.booking(3)
        booking_button = ctk.CTkButton(jasa_C_frame,width=100,text="Booking",command=click)
        booking_button.place(x=340,y=450)

        close_button = ctk.CTkButton(jasa_C_frame,width=100, text="Close", command=jasa_C_frame.destroy)
        close_button.place(x=50,y=450)

        self.scroll_images3()

    def scroll_images3(self):
        # Menampilkan gambar saat ini
        current_image = self.images[self.current_image_index]
        photo = ImageTk.PhotoImage(current_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Mengganti indeks gambar untuk menggulir ke gambar berikutnya
        self.current_image_index = (self.current_image_index + 1) % len(self.images)

        # Memanggil fungsi rekursif untuk menggulir gambar berikutnya setelah 2000 milidetik (2 detik)
        jasa_C_frame.after(2000,self.scroll_images3)

    def jasa_D(self):
        global jasa_D_frame
        jasa_D_frame = ctk.CTkFrame(window,corner_radius=20,bg_color='#97bad5',border_width=3,border_color='black',fg_color='#f8f8f8',width=500,height=500)
        jasa_D_frame.place(x=740, y=140)

        Servis_Cuci = Label(jasa_D_frame,text="Jaya Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
        Servis_Cuci.place(x=35,y=15)

        Servis_Cuci = Label(jasa_D_frame,text="-Service Cuci AC\n-Vacuum AC dan\nFlushing AC",font=("Consolas",11),bg='#f8f8f8',justify='left')
        Servis_Cuci.place(x=35,y=330)

        # Daftar gambar yang akan digunakan
        self.image_paths = [r"jasa d.png",r"jasad1.png",r"jasad2.png"]
        self.images = [Image.open(path) for path in self.image_paths]
        
        # Indeks gambar saat ini
        self.current_image_index = 0

        # Tampilkan gambar pertama di dalam frame utama
        self.image_label = Label(jasa_D_frame, bg="#f8f8f8")
        self.image_label.place(x=35,y=150)


        deskripsi = scrolledtext.ScrolledText(jasa_D_frame,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
        deskripsi.insert(tk.END, "Service Cuci: Proses membersihkan \nkomponen-komponen dalam unit AC\n untuk menghilangkan debu, \nkotoran, dan potensi pembentukan\n jamur atau bakteri.\
                        \nTujuannya Menjaga kualitas udara \nyang keluar dari AC, meningkatkan\n efisiensi operasional, dan mencegah\n masalah kesehatan terkait udara.\n\nTeknik flushing \
                         merupakan cara menanggulangi kondisi AC \nyang tersumbat akibat adanya tumpukan \nkotoran pada saluran AC. Jika ini terjadi, \nmaka akan menghambat kinerja AC dan memperpendek \
                         usia AC Anda. Tim Sejasa telah menyediakan jasa vacuum dan flushing AC.\
                         \n\nAlamat: Jalan Mangga No.1,RT 01 RW 02,Kelurahan Besi Muda,\nKecamatan Wert,Kab.Brunei,\nSumatera Bawah.\
                         \n\n\nNo. WA : 082139948140")
        deskripsi.config(state=tk.DISABLED)
        deskripsi.place(x=250,y=15)

        def click():
            self.booking(4)
        booking_button = ctk.CTkButton(jasa_D_frame,width=100,text="Booking",command=click)
        booking_button.place(x=340,y=450)
        close_button = ctk.CTkButton(jasa_D_frame,width=100, text="Close", command=jasa_D_frame.destroy)
        close_button.place(x=50,y=450)

        self.scroll_images4()
    
    def scroll_images4(self):
        # Menampilkan gambar saat ini
        current_image = self.images[self.current_image_index]
        photo = ImageTk.PhotoImage(current_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Mengganti indeks gambar untuk menggulir ke gambar berikutnya
        self.current_image_index = (self.current_image_index + 1) % len(self.images)

        # Memanggil fungsi rekursif untuk menggulir gambar berikutnya setelah 2000 milidetik (2 detik)
        jasa_D_frame.after(2000,self.scroll_images4)

    #========= BOOKING ========#

# class BookingForm:
    def booking(self,button_id):
        
        self.window = window
        self.nama = StringVar()
        self.alamat = StringVar()
        self.no_Hp = StringVar()
        self.nama_jasa = StringVar()
        self.tanggal_booking = StringVar()

        service_AC = IntVar()
        isi_Freon = IntVar()
        tambah_Freon = IntVar()
        ganti_kapasitor_AC = IntVar()
        ganti_komponen = IntVar()
        vacuum = IntVar()
        flushing_AC = IntVar()

        global frame_booking
        frame_booking = ctk.CTkFrame(window, corner_radius=20, bg_color='#94c9d7', fg_color='#1679ad', width=500, height=530)
        frame_booking.place(x=740, y=140)

        ctk.CTkLabel(frame_booking, corner_radius=20, text='Booking Form', text_color='white', font=('Helvetica', 30, 'bold'), fg_color='#99c9db', bg_color='#1679ad').place(x=140, y=15)

        self.label_nama_booking = ctk.CTkLabel(frame_booking, text='Name Booking', font=("Times", 15, "bold"), bg_color="#1679ad", text_color='white')
        self.label_nama_booking.place(x=60, y=75)

        self.entry_nama_booking = ctk.CTkEntry(frame_booking, width=250, corner_radius=20, textvariable=self.nama, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_nama_booking.place(x=50, y=100)

        self.label_alamat_booking = ctk.CTkLabel(frame_booking, text='Addres Home', font=("Times", 15, "bold"), bg_color="#1679ad", text_color='white')
        self.label_alamat_booking.place(x=60, y=145)

        self.entry_alamat_booking = ctk.CTkEntry(frame_booking, width=250, corner_radius=20, textvariable=self.alamat, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_alamat_booking.place(x=50, y=170)

        self.label_no_hp_booking = ctk.CTkLabel(frame_booking, text='No. Whatsapp', font=("Times", 15, "bold"), bg_color="#1679ad", text_color='white')
        self.label_no_hp_booking.place(x=60, y=215)

        self.entry_no_hp_booking = ctk.CTkEntry(frame_booking, width=250, corner_radius=20, textvariable=self.no_Hp, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_no_hp_booking.place(x=50, y=240)

        self.label_tanggal_booking = ctk.CTkLabel(frame_booking, text='Tanggal Booking', font=("Times", 15, "bold"), bg_color="#1679ad", text_color='white')
        self.label_tanggal_booking.place(x=60, y=285)

        self.entry_tanggal_booking = ctk.CTkLabel(frame_booking, width=250, corner_radius=20, textvariable=self.tanggal_booking, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_tanggal_booking.place(x=50, y=310)
        
        self.label_nama_jasa = ctk.CTkLabel(frame_booking, text='Nama Jasa', font=("Times", 15, "bold"), bg_color="#1679ad", text_color='white')
        self.label_nama_jasa.place(x=60, y=345)

        self.harga_jasa = IntVar()
        global service_prices
        service_prices = {}
        if button_id == 1:
            self.nama_jasa = "BOTANIA Service"
            self.harga_jasa = 80000
            entry_nama_jasa = ctk.CTkLabel(frame_booking, text="BOTANIA Service", width=250, corner_radius=20, textvariable=self.nama_jasa, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
            entry_nama_jasa.place(x=50, y=370)
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp.75.000,-", variable=isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp.50.000,-", variable=tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp.120.000,-", variable=ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp.200.000,-", variable=ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp.150.000", variable=vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp.180.000,-", variable=flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Isi Freon": 75000,
                "Tambah Freon": 50000,
                "Ganti Kapasitor AC": 120000,
                "Ganti Komponen": 200000,
                "Vacuum AC": 150000,
                "Flushing AC": 180000
            }
        elif button_id == 2:
            self.nama_jasa = "ACTECH Service"
            self.harga_jasa = 70000
            entry_nama_jasa = ctk.CTkLabel(frame_booking, text="ACTECH Service", width=250, corner_radius=20, textvariable=self.nama_jasa, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
            entry_nama_jasa.place(x=50, y=370)
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp.80.000,-", variable=isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp.60.000,-", variable=tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp.110.000,-", variable=ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp.180.000,-", variable=ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp.160.000", variable=vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp.190.000,-", variable=flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Isi Freon": 80000,
                "Tambah Freon": 60000,
                "Ganti Kapasitor AC": 110000,
                "Ganti Komponen": 180000,
                "Vacuum AC": 160000,
                "Flushing AC": 190000
            }
        elif button_id == 3:
            self.nama_jasa = "BORCHELLE Service"
            self.harga_jasa = 60000
            entry_nama_jasa = ctk.CTkLabel(frame_booking, text="BORCHELLE Service", width=250, corner_radius=20, textvariable=self.nama_jasa, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
            entry_nama_jasa.place(x=50, y=370)
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp.70.000,-", variable=isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp 65.000,-", variable=tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp.110.000,-", variable=ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp.190.000,-", variable=ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp.180.000", variable=vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp.200.000,-", variable=flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Isi Freon": 70000,
                "Tambah Freon": 65000,
                "Ganti Kapasitor AC": 110000,
                "Ganti Komponen": 190000,
                "Vacuum AC": 180000,
                "Flushing AC": 200000
            }
        elif button_id == 4:
            self.nama_jasa = "JAYA Service"
            self.harga_jasa = 50000
            entry_nama_jasa = ctk.CTkLabel(frame_booking, text="JAYA Service", width=250, corner_radius=20, textvariable=self.nama_jasa, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
            entry_nama_jasa.place(x=50, y=370)
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp. 80.000,-", variable=isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp. 70.000,-", variable=tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp. 100.000,-", variable=ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp. 140.000,-", variable=ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp. 115.000", variable=vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp. 160.000,-", variable=flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Isi Freon": 80000,
                "Tambah Freon": 70000,
                "Ganti Kapasitor AC": 100000,
                "Ganti Komponen": 140000,
                "Vacuum AC": 115000,
                "Flushing AC": 160000
            }
        self.label_payment = ctk.CTkLabel(frame_booking, text='Payment', font=("Times", 15, "bold"), bg_color="#1679ad", text_color='white')
        self.label_payment.place(x=60, y=405)

#===============Calendar=========#
        cal = Calendar(frame_booking, selectmode='day', year=2023, month=12, day=5, date_pattern='yyyy-mm-dd', font=("Times", 5), foreground='black', background='white')
        cal.place(x=315, y=285)   

        self.radio_values = {1: "CASH", 2: "QRIS"}
        self.pemilihanpay = IntVar()

        def show_selected_value():
            global selected_value
            selected_value = self.pemilihanpay.get()
            if selected_value in self.radio_values:
                self.pemilihanpayyy =  self.radio_values[selected_value]

        checkbutton_A = Radiobutton(frame_booking, text="CASH", value = 1, variable = self.pemilihanpay, bg="#1679ad",command= show_selected_value)
        checkbutton_A.place(x=50, y=425)
       
        
        checkbutton_B = Radiobutton(frame_booking, text="QRIS",value=2, variable = self.pemilihanpay, bg="#1679ad",command= show_selected_value)
        checkbutton_B.place(x=170, y=425)
        
        def get_date():
            date = cal.get_date()
            self.tanggal_booking.set(date)
            # cal.destroy()
        
        btn = ctk.CTkButton(frame_booking, text="Select Date", command=get_date, corner_radius=20, bg_color='#1679ad',border_width=1,border_color='black', font=("Times", 15, "bold"))
        btn.place(x=310, y=440)

       
# Function to calculate the total price based on the selected services
        def calculate_price():
            if not all([self.nama.get(), self.alamat.get(), self.no_Hp.get(), self.tanggal_booking.get(), self.nama_jasa]):
                messagebox.showerror("Error", "Harus mengisi semua kolom booking form")
            elif not service_AC.get() and not isi_Freon.get() and not tambah_Freon.get() and not ganti_kapasitor_AC.get() and not ganti_komponen.get() and not vacuum.get() and not flushing_AC.get():
                messagebox.showerror("Error", "Anda harus memilih setidaknya satu layanan")
            elif not self.pemilihanpay.get():
                messagebox.showerror("Error","Silahkan pilih metode pembayaran")
            else:
                global total_price,harga_jasa
                harga_jasa = self.harga_jasa
                total_price = harga_jasa
                selected_services = []
                for service, price in service_prices.items():
                    if service == "Service AC" and service_AC.get() == 1:
                        selected_services.append(("Service AC")), total_price
                    elif service == "Isi Freon" and isi_Freon.get() == 1:
                        # total_price += harga_jasa
                        total_price += price
                        selected_services.append("Isi Freon"), total_price
                    elif service == "Tambah Freon" and tambah_Freon.get() == 1:
                        # total_price += harga_jasa
                        total_price += price
                        selected_services.append("Tambah Freon"), total_price
                    elif service == "Ganti Kapasitor AC" and ganti_kapasitor_AC.get() == 1:
                        # total_price += harga_jasa
                        total_price += price
                        selected_services.append("Ganti Kapasitor AC"), total_price
                    elif service == "Ganti Komponen" and ganti_komponen.get() == 1:
                        # total_price += harga_jasa
                        total_price += price
                        selected_services.append("Ganti Komponen"), total_price
                    elif service == "Vacuum AC" and vacuum.get() == 1:
                        # total_price += harga_jasa
                        total_price += price
                        selected_services.append("Vacuum AC"), total_price
                    elif service == "Flushing AC" and flushing_AC.get() == 1:
                        # total_price += harga_jasa
                        total_price += price
                        selected_services.append("Flushing AC"), total_price

            # jasa = self.nama_jasa
            # if jasa in jasa_prices:
            #     jasa_price = jasa_prices[jasa]
            #     total_price += jasa_price
            #     selected_services.append(f"Jasa:{jasa}")

            #     # Display or use the total_price as needed
            #     print("Total Price: $", total_price)


        # Write booking_data to a CSV file
                with open('booking_data.csv', mode='a', newline='') as file:
                    row = ['Name', 'Address', 'Phone Number', 'Booking Date', 'Service Name', 'Selected Services', 'Service Price', 'Payment Methode']
                    writer = csv.DictWriter(file, fieldnames=row)
                    writer.writerow({
                        'Name': self.nama.get(),
                        'Address': self.alamat.get(),
                        'Phone Number': self.no_Hp.get(),
                        'Booking Date': self.tanggal_booking.get(),
                        'Service Name': self.nama_jasa,
                        'Selected Services': ', '.join([service[0:] for service in selected_services]),
                        'Service Price': total_price,
                        'Payment Methode' : self.pemilihanpayyy
                        })


                messagebox.showinfo("Booking","Lakukan Pembayaran")

                frame_booking.destroy()
                self.payment_methode()
            
        btn1 = ctk.CTkButton(frame_booking, text="Back", command=frame_booking.destroy, corner_radius=20, bg_color='#1679ad',border_width=1,border_color='black',hover_color="red", font=("Times", 15, "bold"))
        btn1.place(x=70, y=480)
            
        btn = ctk.CTkButton(frame_booking, text="Payment", command=calculate_price, corner_radius=20, bg_color='#1679ad',border_width=1, border_color='black', font=("Times" , 15, "bold")) 
        btn.place(x=310, y=480)


    def payment_methode(self):
        try:
            jasa_A_frame.destroy()
        except:
            pass
        try:
            jasa_B_frame.destroy()
        except:
            pass
        try:
            jasa_C_frame.destroy()
        except:
            pass
        try:
            jasa_D_frame.destroy()
        except:
            pass
        window_payment = ctk.CTkFrame(window,corner_radius=20,bg_color='#97bad5',border_width=3,border_color='black',fg_color='#f8f8f8',width=500,height=500)
        window_payment.place(x=740, y=140)

        ctk.CTkLabel(window_payment, corner_radius=20, text='Payment', text_color='black', font=('Helvetica', 30, 'bold'), fg_color='#99c9db', bg_color='white').place(x=150, y=15)
        # window_payment.geometry('500x500')
        # window_payment.title('Payment')
        # window_payment.configure(background='#f8f8f8')
        # # window_payment.resizable(0, 0)
        
        self.pemilihanpayyy =  self.radio_values[selected_value]

        if self.pemilihanpayyy == "CASH":
            a=ctk.CTkLabel(window_payment, text=f'Terima kasih, \nsilahkan melakukan pembayaran ditempat sebesar \nRp. {total_price} ,-')
            a.place(x=150,y=150)

        elif self.pemilihanpayyy == "QRIS":
               
                image = PhotoImage(file="jasa a.png")
                ctk.CTkLabel(window_payment, image=image).place(x=20,y=20)
                ctk.CTkLabel(window_payment, text=f'anda harus bayar sebesar {total_price}').place(x=150,y=150)

    def calendar(self):
            self.mycal=Calendar(window,setmode="day", date_pattern = "d/mm/yy").pack()
            self.set_date_button= Button(window, command=self.set_date_entry, text="set")

#====================REMINDER=========================#
    def reminder(self):
        self.emailRemind = StringVar()
        self.noteRemind = StringVar()
        self.emailSubject = "[S.Tech] AC Reminder Service"
    

        self.frame_reminder = Frame(window,bg='white') 
        self.frame_reminder.pack(fill='both',expand=True) 
        self.frame_reminder.place(x=280, y=100, width=800, height=500)

        self.reminder_label = Label(self.frame_reminder, text="Reminder", font=("sans serif", 16, "bold"), fg="#0370a9",
                              bg="#f8f8f8").place(x=100, y=10)

        self.calendar = Calendar(self.frame_reminder, setmode="day", date_pattern="d/mm/yy")
        self.calendar.place(x = 500, y=100)

        self.set_date_button = ctk.CTkButton(self.frame_reminder, text="Select date", width=20,command = self.Selectdate)
        self.set_date_button.place(x=600, y = 300)

        
        self.last_service  = Label(self.frame_reminder, text="Last service", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                                fg="#0370a9").place(x=50, y=60)
        self.last_services__ket= Label(self.frame_reminder, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                      relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.last_services__ket.place(x=50, y=90)


        self.email_label = Label(self.frame_reminder, text="Email", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                                fg="#0370a9").place(x=50, y=125)
        self.email_entry = Entry(self.frame_reminder, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                     relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black", textvariable=self.emailRemind)
        self.email_entry.place(x=50, y=155)


        self.note_label = Label(self.frame_reminder, text="Note", bg="#f8f8f8",
                                   font=("sans serif", 10, "bold"), fg="#0370a9").place(x=50, y=200)
        self.note_entry = Entry(self.frame_reminder, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                        relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black", textvariable=self.noteRemind)
        self.note_entry.place(x=50, y=230)

        self.set_reminder_button = ctk.CTkButton(self.frame_reminder, text="Set reminder",hover_color='green', width=350, command=self.atur_tanggal_kirim_email)
        self.set_reminder_button.place(x=50,y=320)

        cancel_reminder_button = ctk.CTkButton(self.frame_reminder, text="Cancel reminder",hover_color='red',command=self.cancel)
        cancel_reminder_button.place(x=50, y=360)   
        
    def cancel(self):
        self.frame_reminder.destroy()

    def Selectdate(self):
             self.mydate = self.calendar.get_date()
             self.last_services__ket.config(text=self.mydate)






    def atur_tanggal_kirim_email(self):
        Username = self.username.get()
        email_user = self.emailRemind.get()
        input_date = self.mydate
        note = self.noteRemind.get()

        if not all([Username, email_user, input_date,note]):
            messagebox.showerror("Set Reminder", "Harap isi semua kolom untuk melakukan set reminder.")
            return
        
        with open('dataremind.csv', 'r') as file:
            csv.DictReader(file)
        with open('dataremind.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            def add_three_months(input_date):
                    # Konversi input_date ke objek datetime
                    date_object = datetime.strptime(input_date, '%d/%m/%y')

                    # Tambahkan 3 bulan menggunakan timedelta
                    new_date = date_object + timedelta(days=3*30)

                    # Format ulang tanggal baru ke format dd/mm/yy
                    new_date_formatted = new_date.strftime('%d/%m/%y')

                    return new_date_formatted
            global reminder_date
            reminder_date = add_three_months(input_date)
            writer.writerow([Username, email_user, input_date, note,reminder_date])
        messagebox.showinfo("csv", "Berhasil masuk csv")
        gmail_user = "alishadeana.23244@mhs.unesa.ac.id"
        gmail_app_password = "pluwvhhi"
        

        sent_from = gmail_user
        sent_to = self.emailRemind.get()
        sent_subject = self.emailSubject
        sent_body = f" Dear customer, thank you for using our apps, your last service is {self.mydate}, reminder has sucessfully set, we'll remind you to service your AC three months after your last service \n\nwith note: {self.noteRemind.get()}"


        email_text = f"""\
        From : {sent_from}
        To: {sent_to}
        Subject: {sent_subject}

        {sent_body}
        """

        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.ehlo()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(sent_from,sent_to, email_text)
            print("email berhasil dikirim")
            tk.messagebox.showinfo("Info", "Reminder berhasil di set")
            self.send_email_after_three()
        except Exception as exception:
            print("Error: %s!\n\n" % exception)
        
    

    def send_email_after_three(self):
        present = datetime.now()
        formatted_date = present.strftime('%d/%m/%y')
        with open('dataremind.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                if row['Reminder Date'] == formatted_date:

                    gmail_user = "alishadeana.23244@mhs.unesa.ac.id"
                    gmail_app_password = "pluwvhhi"
                    

                    sent_from = gmail_user
                    sent_to = self.emailRemind.get()
                    sent_subject = self.emailSubject
                    sent_body = f"Dear customer, Please service your AC ASAP! thank you for using our apps, your last service is {self.mydate}, reminder has sucessfully set, we'll remind you to service your AC three months after your last service \n\nwith note: {self.noteRemind.get()}"


                    email_text = f"""\
                    From : {sent_from}
                    To: {sent_to}
                    Subject: {sent_subject}

                    {sent_body}
                    """

                    try:
                        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
                        server.ehlo()
                        server.login(gmail_user, gmail_app_password)
                        server.sendmail(sent_from,sent_to, email_text)
                        print("email 22 berhasil dikirim")
                        tk.messagebox.showinfo("Info", "Reminder berhasil di set")
                    except Exception as exception:
                        print("Error: %s!\n\n" % exception)

 

gui = ACseRemind(window)
window.mainloop()
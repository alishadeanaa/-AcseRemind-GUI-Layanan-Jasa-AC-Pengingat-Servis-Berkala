from tkinter import *
import tkinter as tk
from tkinter import messagebox,scrolledtext,ttk
from PIL import Image,ImageTk
import webbrowser
import customtkinter as ctk
import csv
from tkcalendar import *
import smtplib
from datetime import datetime, timedelta 
import smtplib
from datetime import datetime, timedelta

window = Tk()
#=======================AcSeRemind=========================#
class ACseRemind:

    def __init__ (self,window):
        self.username = StringVar()
        self.password = StringVar()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.phone_number= IntVar()
        self.address = StringVar()

        self.service_AC = IntVar()
        self.isi_Freon = IntVar()
        self.tambah_Freon = IntVar()
        self.ganti_kapasitor_AC = IntVar()
        self.ganti_komponen = IntVar()
        self.vacuum = IntVar()
        self.flushing_AC = IntVar()
        
        #============ Background ==========#
        self.window = window  
        window.title("AC seRemind")
        window.state('zoomed')
        window.resizable(0,0)
        self.bg = PhotoImage(file="login.png")
        self.loginlayar=Label(window, image=self.bg)
        self.loginlayar.place(x=0,y=0, relheight=1,relwidth=1)

        #=========== Login Role ===========#
        def gas():
            self.window.destroy
            self.layarlogin(1)
        user_button = ctk.CTkButton(window, text="Login as User",corner_radius=10, border_width=3, border_color='black', bg_color="#d2d5d8", width=200, height=50, command=gas)
        user_button.place(x=540, y=400)  

        def gas2():
            self.window.destroy
            self.layarlogin(2)
        owner_button = ctk.CTkButton(window, text="Login as Owner",corner_radius=10, border_width=3, border_color='black', bg_color="#d2d5d8", width=200, height=50, command=gas2)
        owner_button.place(x=540, y=500)
        
    #================ Login As User or Owner ===================#    
    def layarlogin(self,user_or_owner):

        self.window = window  
        window.title("AC seRemind")
        window.state('zoomed')
        window.resizable(0,0)
        self.bg = PhotoImage(file="login.png")
        self.loginlayar=Label(window, image=self.bg)
        self.loginlayar.place(x=0,y=0, relheight=1,relwidth=1)

        #============= Login As User ===========#
        if user_or_owner == 1:

            self.label_username = Label(self.window, text="Username", bg = "#ecf0f3", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=360)
            self.entry_username = Entry(self.window, textvariable=self.username,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
            self.entry_username.place(x=360, y=390)

            self.label_password = Label(self.window, text="Password", bg = "#ecf0f3", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=460)
            self.entry_password = Entry(self.window, show='*',textvariable=self.password,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
            self.entry_password.place(x=360, y=490)
            

            self.button_lupapsw = Button(self.window,text="Forgot Password?",bg = "#ecf0f3", font=("sans serif",10,"underline"),fg="blue",command=self.forgot_password,
                                        highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=790,y=550)
            
            self.label_gapunya_akun = Label(self.window,text="Don't have a account?",bg = "#ecf0f3", font=("sans serif",10),fg="black").place(x=360,y=580)
            self.button_sign_in = Button(self.window,text="Sign in",bg = "#ecf0f3", font=("sans serif",10,"bold underline"),fg="blue",command=self.show_sign_in_window,
                                        highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=490,y=580)
            
            showpsw = Checkbutton(self.window, bg="#ecf0f3", command=self.show_psw, text="show password",font=("sans serif",10))
            showpsw.place(x=360,y=550)

            def next1():
                self.login(1)
            self.button_login = ctk.CTkButton(self.window,text="LOGIN",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#ecf0f3",width=480,height=40,command=next1)
            self.button_login.place(x=395,y=610)
            self.button_logout=Button(window,text="Back",bg = "#ecf0f3", font=("sans serif",10,"bold underline"),fg="red",command=self.back,
                                     activebackground='red',highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=60,y=70)

        #============== Login As Owner ============#
        if user_or_owner == 2:

            self.label_username = Label(self.window, text="Username", bg = "#ecf0f3", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=360)
            self.entry_username = Entry(self.window, textvariable=self.username,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
            self.entry_username.place(x=360, y=390)

            self.label_password = Label(self.window, text="Password", bg = "#ecf0f3", font=("sans serif",12,"bold"),fg="#0370a9").place(x=360,y=460)
            self.entry_password = Entry(self.window, show='*',textvariable=self.password,border=0,highlightthickness=2,highlightcolor="#0370a9",relief="groove", width=38, font=("Sans serif",19),bg="white",fg="#0370a9")
            self.entry_password.place(x=360, y=490)
            

            self.button_lupapsw = Button(self.window,text="Forgot Password?",bg = "#ecf0f3", font=("sans serif",10,"underline"),fg="blue",command=self.forgot_password,
                                        highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=790,y=550)
            
            self.label_gapunya_akun = Label(self.window,text="Don't have a account?",bg = "#ecf0f3", font=("sans serif",10),fg="black").place(x=360,y=580)
            self.button_sign_in = Button(self.window,text="Sign in",bg = "#ecf0f3", font=("sans serif",10,"bold underline"),fg="blue",command=self.show_sign_in_window,
                                        highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=490,y=580)
            
            showpsw = Checkbutton(self.window, bg="#ecf0f3", command=self.show_psw, text="show password",font=("sans serif",10))
            showpsw.place(x=360,y=550)
            
            def next2():
                self.login(2)
            self.button_login = ctk.CTkButton(self.window,text="LOGIN",corner_radius=20,hover_color='green',fg_color='#0370a9',bg_color="#ecf0f3",width=480,height=40,command=next2)
            self.button_login.place(x=395,y=610)
            self.button_logout=Button(window,text="Back",bg = "#ecf0f3", font=("sans serif",10,"bold underline"),fg="red",command=self.back,
                                     activebackground='red',highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=60,y=70)
    
    #======== Show Password =========#
    def show_psw(self):
        if self.entry_password.cget("show") == "*":
            self.entry_password.config(show='')
        else:
            self.entry_password.config(show="*")

    #=================== CHECK LOG IN ===============#
    def login(self,role):
        username = self.username.get()
        password = self.password.get()

        if 6 <= len(password) <= 20:
            with open('dataservice.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Check if the entered username and password match the ones in the CSV
                    if row['Username'] == username and row['Password'] == password:
                        if role == 2:
                            if row['Role'] == 'Owner BOTANIA' or row['Role'] == 'Owner ACTECH' or row['Role'] == 'Owner BORCELLE' or row['Role'] == 'Owner JAYA':
                                messagebox.showinfo("Login", "Owner login berhasil!")
                                self.owner_dashboard() 
                            else:
                                messagebox.showwarning("Warning","Anda bukan owner") 

                        elif role == 1:
                            if row['Role'] == 'User':
                                messagebox.showinfo("Login", "User login berhasil!")
                                self.dashboard()
                            else:
                                messagebox.showwarning("Warning","Anda bukan user")

                        return
                        
            messagebox.showerror("Login", "Username atau password Invalid!")

        else:
            messagebox.showerror("Login", "Password must be between 6 and 20 characters.")

        
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
        
    #===================SIGN IN===================#
    def show_sign_in_window(self):
        sign_in_window = Toplevel()
        sign_in_window.geometry('500x650')
        sign_in_window.title('Sign In')
        sign_in_window.configure(background='#f8f8f8')
        sign_in_window.resizable(0, 0)
        self.username = StringVar()
        self.password = StringVar()
        self.role = StringVar()


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


        self.password_label = Label(sign_in_window, text="Password(6-20 karakter)", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                               fg="#0370a9").place(x=50, y=425)
        self.password_entry = Entry(sign_in_window,textvariable=self.password, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                    relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black",
                                    )
        self.password_entry.place(x=50, y=455)

        self.role_label = Label(sign_in_window, text="Role", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                                fg="#0370a9").place(x=50, y=500)

        roles = ["User", "Owner BOTANIA", "Owner ACTECH", "Owner BORCELLE", "Owner JAYA"]
        self.role_combobox = ttk.Combobox(sign_in_window, textvariable=self.role, values=roles,
                                          state="readonly", width=36, font=("Sans serif", 13), background="white", foreground="black")
        self.role_combobox.place(x=50, y=530)

        sign_in_button = ctk.CTkButton(sign_in_window, command=self.signup, text="Sign In",
                                       font=("sans serif", 12, "bold"), width=350)
        sign_in_button.place(x=50, y=570)


    #+================CHECK SIGN UP===============#
    def signup(self):
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        phonenumber = self.phone_number_entry.get()
        address = self.address_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role.get()

        if not all([firstname, lastname, phonenumber, address, username, password,role]):
            messagebox.showerror("Signup", "Harap isi semua kolom untuk melakukan sign in.")
            return
        elif 6 <= len(password) <= 20:
            with open('dataservice.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Username'] == username and row['Password'] == password and row['Address'] == address:
                        messagebox.showerror("Signup", "Username terdaftar!")
                        return
                    
            with open('dataservice.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([firstname, lastname, phonenumber, address, username, password,role])
            messagebox.showinfo("Signup", "Signup berhasil!")

        else:
            messagebox.showerror("Sign Up", "Password must be between 6 and 20 characters.")

    #==========ADMIN DASHBOARD=======#
    def owner_dashboard(self):
        self.loginlayar.destroy()
        self.window = window  
        self.bg = PhotoImage(file="Owner Dashboard.png")
        self.layardash = Label(window, image=self.bg)
        self.layardash.place(x=0, y=0, relheight=1, relwidth=1)
        self.fotoA= PhotoImage(file="jasa a.png")
        self.fotoB= PhotoImage(file="jasa b.png")
        self.fotoC= PhotoImage(file="jasa c.png")
        self.fotoD= PhotoImage(file="jasa d.png")
        self.setting = PhotoImage(file="setting.png")
        username = self.username.get()

        with open('dataservice.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Username'] == username:
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    self.nama_label_dshbrd = Label(window,text=f"Welcome {first_name} {last_name}!\nto S.TECH\nAC Service Reminder", font=("sans serif", 20, "bold"),bg='#ecf0f3',justify='center',fg='#74818a')
                    self.nama_label_dshbrd.place(x=140,y=170)
                    break

        def set1():
            X = messagebox.askyesno("Anda","Apakah anda owner jasa Service Botania?")
            if X:
                self.owner(1)

        def set2():
            X = messagebox.askyesno("Anda","Apakah anda owner jasa Service AcTech?")
            if  X:
                self.owner(2)

        def set3():
            X = messagebox.askyesno("Anda","Apakah anda owner jasa Service Borcelle?")
            if  X:
                self.owner(3)

        def set4():
            X = messagebox.askyesno("Anda","Apakah anda owner jasa Service Jaya?")
            if  X:
                self.owner(4)
        
        def about1():
            self.about_service_owner(1)
        def about2():
            self.about_service_owner(2)
        def about3():
            self.about_service_owner(3)
        def about4():
            self.about_service_owner(4)

        with open ('dataservice.csv',mode='r') as Owner1 :
            csv_reader = csv.DictReader(Owner1)
            for row in csv_reader:

                if row['Username'] == username and row['Role'] == 'Owner BOTANIA' :

                    self.button_jasa_A = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.fotoA,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="Botania Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=set1)
                    self.button_jasa_A.place(x=700,y=230)
                    self.button_jasa_A = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.setting,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="About Botania Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=about1)
                    self.button_jasa_A.place(x=700,y=460)
                    break

                elif row['Username'] == username and row['Role'] == 'Owner ACTECH':
                    self.button_jasa_B = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.fotoB,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="ACTECH Service", font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768", command=set2)
                    self.button_jasa_B.place(x=700,y=230)
                    self.button_jasa_A = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.setting,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="About ACTECH Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=about2)
                    self.button_jasa_A.place(x=700,y=460)
                    break
        
                elif row['Username'] == username and row['Role'] == 'Owner BORCELLE':
                    
                    self.button_jasa_C = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.fotoC,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N, text="BORCELLE Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768", command=set3)
                    self.button_jasa_C.place(x=700,y=230)
                    self.button_jasa_A = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.setting,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="About BORCELLE Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=about3)
                    self.button_jasa_A.place(x=700,y=460)
                    break

                elif row['Username'] == username and row['Role'] == 'Owner JAYA':
                    
                    self.button_jasa_D = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.fotoD,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="JAYA service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768", command=set4)
                    self.button_jasa_D.place(x=700,y=230)
                    self.button_jasa_A = ctk.CTkButton(window,width=500,height=120,corner_radius=20,image=self.setting,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="About JAYA Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=about4)
                    self.button_jasa_A.place(x=700,y=460)
                    break

        self.button_logout=Button(window,text="Log out",bg = "#ecf0f3", font=("sans serif",10,"bold underline"),fg="red",command=self.logout,
                                     activebackground='red',highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=60,y=70)
    #========= Back to Login Layar ======#
    def back(self):
        back = messagebox.askyesno("Back","Apakah anda ingin keluar?")

        if back:
            self.reset_gui2()

    def reset_gui2(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.__init__(self.window)

    def about_service_owner(self,no):
        self.frame_owner= ctk.CTkFrame(window, corner_radius=20, bg_color='#ecf0f3', fg_color='#f8f8f8', width=500, height=530)
        self.frame_owner.place(x=720, y=160)

        self.image = PhotoImage(file="service.png")
        Label(self.frame_owner,image=self.image).place(x=2,y=8)

        if no == 1:
            Servis_Cuci = Label(self.frame_owner,text="BOTANIA",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)

            self.image_paths = [r"jasa a.png",r"jasaa1.png",r"jasaa2.png"]
            self.images = [Image.open(path) for path in self.image_paths]

            self.current_image_index = 0
            
            self.image_label = Label(self.frame_owner, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            self.scroll_images2()

            deskripsi = scrolledtext.ScrolledText(self.frame_owner,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Botania Service \nperusahaan terkemuka di bidang layanan perawatan dan perbaikan sistem pendingin udara (AC). Dengan komitmen untuk memberikan kualitas terbaik kepada pelanggan, Botania Service telah menjadi pilihan utama dalam menjaga performa optimal AC.
                                    Tenaga kerja kita memiliki:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\n4.Pelayanan pelanggan ramah dan responsif.\n5. Jaminan kepuasan pelanggan.
                                    Informasi Kami:
                                    Alamat: \nJalan Mangga No.1, RT 01 RW 02, Kelurahan Besi Muda, Kecamatan Genteng, Kota Surabaya, Jawa Timur.
                                    "Berikan yang terbaik untuk para pelanggan.Kepuasan mereka adalah kebahagiaan kita."
                                    NO HP: 081111222333
                                    [BOTANIA Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)
            close_button = ctk.CTkButton(self.frame_owner,width=100, text="Close", command=self.frame_owner.destroy)
            close_button.place(x=20,y=450)

        if no == 2:
            Servis_Cuci = Label(self.frame_owner,text="ACTECH",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)

            self.image_paths = [r"jasa b.png",r"jasab1.png",r"jasab2.png"]
            self.images = [Image.open(path) for path in self.image_paths]

            # Indeks gambar saat ini
            self.current_image_index = 0

            # Tampilkan gambar pertama di dalam frame utama
            self.image_label = Label(self.frame_owner, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            self.scroll_images2()
            # Memulai fungsi pengguliran otomatis

            deskripsi = scrolledtext.ScrolledText(self.frame_owner,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Actech Service  \nperusahaan yang berdedikasi dalam menyediakan layanan unggul di bidang perawatan dan perbaikan sistem pendingin udara (AC). Dengan fokus utama pada kualitas, keandalan, dan kepuasan pelanggan, Actech Service telah menjadi pilihan utama bagi individu dan bisnis yang membutuhkan solusi profesional untuk kebutuhan AC mereka.
                                    Tenaga kerja kita:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\n4.Pelayanan pelanggan ramah dan responsif.\n5. Jaminan kepuasan pelanggan.
                                    Informasi Kami:
                                    Alamat: \nJalan Anggrek No. 15, RT 05 RW 03, Kelurahan Bambu Kuning, Kecamatan Gubeng, Kota Surabaya, Jawa Timur.
                                    "Prioritaskan pelanggan. ingat AC ingat kami."
                                    NO HP: 081123456789
                                    [ACTECH Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)
            close_button = ctk.CTkButton(self.frame_owner,width=100, text="Close", command=self.frame_owner.destroy)
            close_button.place(x=20,y=450)
        
        if no == 3:
            Servis_Cuci = Label(self.frame_owner,text="BORCHELLE",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)

            self.image_paths = [r"jasa c.png",r"jasac1.png",r"jasac2.png"]
            self.images = [Image.open(path) for path in self.image_paths]

            # Indeks gambar saat ini
            self.current_image_index = 0

            # Tampilkan gambar pertama di dalam frame utama
            self.image_label = Label(self.frame_owner, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            # Memulai fungsi pengguliran otomatis
            self.scroll_images2()

            deskripsi = scrolledtext.ScrolledText(self.frame_owner,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Borcelle Service \nperusahaan yang bergerak di bidang layanan perbaikan dan pemeliharaan sistem pendingin udara (AC). Dengan komitmen untuk memberikan pelayanan terbaik kepada pelanggan, Borcelle Service telah menjadi pilihan utama bagi mereka yang membutuhkan solusi profesional untuk masalah AC
                                    Tenaga kerja kita:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\n4.Pelayanan pelanggan ramah dan responsif.\n5. Jaminan kepuasan pelanggan.
                                    Informasi Kami:
                                    Alamat: \nJalan Dahlia No. 10A, RT 07 RW 04, Kelurahan Mawar Biru, Kecamatan Simokerto, Kota Surabaya, Jawa Timur.
                                    "Layanan cepat dan terpecaya"
                                    NO HP: 081234432567
                                    [BORCELLE Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)
            close_button = ctk.CTkButton(self.frame_owner,width=100, text="Close", command=self.frame_owner.destroy)
            close_button.place(x=20,y=450)
        
        if no == 4:
            Servis_Cuci = Label(self.frame_owner,text="JAYA",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)

            self.image_paths = [r"jasa d.png",r"jasad1.png",r"jasad2.png"]
            self.images = [Image.open(path) for path in self.image_paths]
            
            # Indeks gambar saat ini
            self.current_image_index = 0

            # Tampilkan gambar pertama di dalam frame utama
            self.image_label = Label(self.frame_owner, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            self.scroll_images2()

            deskripsi = scrolledtext.ScrolledText(self.frame_owner,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Jaya Service \nperusahaan yang berdedikasi dalam memberikan layanan profesional dan terpercaya di bidang service AC. Dengan pengalaman yang telah teruji dan tenaga kerja yang ahli, Jaya Service menjadi pilihan utama bagi pelanggan yang mengutamakan kualitas dan kehandalan dalam perawatan dan perbaikan perangkat pendingin udara.
                                    Tenaga kerja kita:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\nPelayanan pelanggan ramah dan responsif.\n4. Jaminan kepuasan pelanggan.
                                    Informasi Kami:
                                    Alamat: \nJalan Mawar Indah No. 15, RT 10 RW 02, Kelurahan Kenanga, Kecamatan Wonocolo, Kota Surabaya, Jawa Timur.
                                    "Ada kendala AC? Ingat JAYA"
                                    NO HP: 081987456432
                                    [Jaya Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)
            close_button = ctk.CTkButton(self.frame_owner,width=100, text="Close", command=self.frame_owner.destroy)
            close_button.place(x=20,y=450)

    #=========== Pop Up Frame Owner Jasa ===========#

    def save_checkbox_states(self,jasa):
        if jasa == 1:
            with open('Botania booking.txt', 'w') as file:
                for var in self.checkbox_vars:
                    state = var.get()
                    file.write(f"{state}\n")
        if jasa == 2:
            with open('ACTECH booking.txt', 'w') as file:
                for var in self.checkbox_vars:
                    state = var.get()
                    file.write(f"{state}\n")
        if jasa == 3:
            with open('Borcelle booking.txt', 'w') as file:
                for var in self.checkbox_vars:
                    state = var.get()
                    file.write(f"{state}\n")
        if jasa == 4:
            with open('Jaya booking.txt', 'w') as file:
                for var in self.checkbox_vars:
                    state = var.get()
                    file.write(f"{state}\n")
        

    def load_checkbox_states(self,jasa):
        
        if jasa == 1:
            with open('Botania booking.txt', 'r') as file:
                for index, line in enumerate(file):
                    if index < len(self.checkbox_vars):
                        state = int(line.strip())
                        self.checkbox_vars[index].set(state)
        if jasa == 2:
            with open('ACTECH booking.txt', 'r') as file:
                for index, line in enumerate(file):
                    if index < len(self.checkbox_vars):
                        state = int(line.strip())
                        self.checkbox_vars[index].set(state)
        if jasa == 3:
            with open('Borcelle booking.txt', 'r') as file:
                for index, line in enumerate(file):
                    if index < len(self.checkbox_vars):
                        state = int(line.strip())
                        self.checkbox_vars[index].set(state)
        if jasa == 4:
            with open('Jaya booking.txt', 'r') as file:
                for index, line in enumerate(file):
                    if index < len(self.checkbox_vars):
                        state = int(line.strip())
                        self.checkbox_vars[index].set(state)
        

    def owner(self,owner_id):
        
        self.frame_owner= ctk.CTkFrame(window, corner_radius=20, bg_color='#ecf0f3', fg_color='#f8f8f8', width=500, height=530)
        self.frame_owner.place(x=720, y=160)

        self.image = PhotoImage(file="service.png")
        Label(self.frame_owner,image=self.image).place(x=2,y=8)
    

        if owner_id == 1:
            Servis_Cuci = Label(self.frame_owner,justify='center',text="BOTANIA Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=175,y=80)

            list_booking = []  
            with open('booking_data.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['Service Name'] == 'BOTANIA Service':
                        list_booking.append(row)

            text_widget = scrolledtext.ScrolledText(self.frame_owner, wrap='word', width=60, height=20, font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
            text_widget.place(x=35, y=110)

            if not list_booking:
                no_booking_label = Label(self.frame_owner, text="Tidak ada orang yang menggunakan jasa anda", font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
                no_booking_label.place(x=80, y=170)
            else:
                
                self.checkbox_vars = []
                for booking in list_booking:
                    var = tk.IntVar()
                    checkbox = tk.Checkbutton(self.frame_owner, variable=var)
                    self.checkbox_vars.append(var)

                    booking_text = (
                        f"• Username = {booking['Username']},\n• Date = {booking['Booking Date']},"
                        f"\n• Lokasi = {booking['Address']},\n• Service = {booking['Selected Services']},"
                        f"\n• Harga = {booking['Service Price']},Payment = {booking['Payment']},"
                        f"\n• No.Hp = {booking['Phone Number']}\n\n============================================\n\n"
                    )
                    text_widget.window_create(tk.END, window=checkbox)
                    text_widget.insert(tk.END, booking_text)
                    self.load_checkbox_states(1)
            def savebox():
                messagebox.showinfo("Check","Berhasil Checklist")
                self.save_checkbox_states(1)
            ctk.CTkButton(self.frame_owner, text="Save Checklist", corner_radius=20,
                       bg_color='#f8f8f8', hover_color='green', fg_color='#1679ad',
                       width=150, height=30, command=savebox).place(x=200, y=460)

                    
            ctk.CTkButton(self.frame_owner,text="Back",corner_radius=20,bg_color='#f8f8f8',hover_color='red',fg_color='#1679ad',width=100,height=30,command=self.frame_owner.destroy).place(x=50,y=460)

        if owner_id == 2:
            Servis_Cuci = Label(self.frame_owner,justify='center',text="ACTECH Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=175,y=80)

            list_booking = []  
            with open('booking_data.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['Service Name'] == 'ACTECH Service':
                        list_booking.append(row)

            text_widget = scrolledtext.ScrolledText(self.frame_owner, wrap='word', width=60, height=20, font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
            text_widget.place(x=35, y=110)

            if not list_booking:
                no_booking_label = Label(self.frame_owner, text="Tidak ada orang yang menggunakan jasa anda", font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
                no_booking_label.place(x=80, y=170)
            else:
                self.checkbox_vars = []
                for booking in list_booking:
                    var = tk.IntVar()
                    checkbox = tk.Checkbutton(self.frame_owner, variable=var)
                    self.checkbox_vars.append(var)

                    booking_text = (
                        f"• Username = {booking['Username']},\n• Date = {booking['Booking Date']},"
                        f"\n• Lokasi = {booking['Address']},\n• Service = {booking['Selected Services']},"
                        f"\n• Harga = {booking['Service Price']},Payment = {booking['Payment']},"
                        f"\n• No.Hp = {booking['Phone Number']}\n\n============================================\n\n"
                    )
                    text_widget.window_create(tk.END, window=checkbox)
                    text_widget.insert(tk.END, booking_text)
                    self.load_checkbox_states(2)
            def savebox():
                messagebox.showinfo("Check","Berhasil Checklist")
                self.save_checkbox_states(2)
            ctk.CTkButton(self.frame_owner, text="Save Checklist", corner_radius=20,
                       bg_color='#f8f8f8', hover_color='green', fg_color='#1679ad',
                       width=150, height=30, command=savebox).place(x=200, y=460)

            ctk.CTkButton(self.frame_owner,text="Back",corner_radius=20,bg_color='#f8f8f8',hover_color='red',fg_color='#1679ad',width=100,height=30,command=self.frame_owner.destroy).place(x=50,y=460)

        if owner_id == 3:
            Servis_Cuci = Label(self.frame_owner,justify='center',text="BORCELLE Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=175,y=80)

            list_booking = []  
            with open('booking_data.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['Service Name'] == 'BORCELLE Service':
                        list_booking.append(row)

            text_widget = scrolledtext.ScrolledText(self.frame_owner, wrap='word', width=60, height=20, font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
            text_widget.place(x=35, y=110)

            if not list_booking:
                no_booking_label = Label(self.frame_owner, text="Tidak ada orang yang menggunakan jasa anda", font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
                no_booking_label.place(x=80, y=170)
            else:
                self.checkbox_vars = []
                for booking in list_booking:
                    var = tk.IntVar()
                    checkbox = tk.Checkbutton(self.frame_owner, variable=var)
                    self.checkbox_vars.append(var)

                    booking_text = (
                        f"• Username = {booking['Username']},\n• Date = {booking['Booking Date']},"
                        f"\n• Lokasi = {booking['Address']},\n• Service = {booking['Selected Services']},"
                        f"\n• Harga = {booking['Service Price']},Payment = {booking['Payment']},"
                        f"\n• No.Hp = {booking['Phone Number']}\n\n============================================\n\n"
                    )
                    text_widget.window_create(tk.END, window=checkbox)
                    text_widget.insert(tk.END, booking_text)
                    self.load_checkbox_states(3)
            def savebox():
                messagebox.showinfo("Check","Berhasil Checklist")
                self.save_checkbox_states(3)
            ctk.CTkButton(self.frame_owner, text="Save Checklist", corner_radius=20,
                       bg_color='#f8f8f8', hover_color='green', fg_color='#1679ad',
                       width=150, height=30, command=savebox).place(x=200, y=460)

            ctk.CTkButton(self.frame_owner,text="Back",corner_radius=20,bg_color='#f8f8f8',hover_color='red',fg_color='#1679ad',width=100,height=30,command=self.frame_owner.destroy).place(x=50,y=460)

        if owner_id == 4:
            Servis_Cuci = Label(self.frame_owner,justify='center',text="JAYA Service",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=175,y=80)

            list_booking = []  
            with open('booking_data.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['Service Name'] == 'JAYA Service':
                        list_booking.append(row)

            text_widget = scrolledtext.ScrolledText(self.frame_owner, wrap='word', width=60, height=20, font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
            text_widget.place(x=35, y=110)

            if not list_booking:
                no_booking_label = Label(self.frame_owner, text="Tidak ada orang yang menggunakan jasa anda", font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
                no_booking_label.place(x=80, y=170)
            else:
                self.checkbox_vars = []
                for booking in list_booking:
                    var = tk.IntVar()
                    checkbox = tk.Checkbutton(self.frame_owner, variable=var)
                    self.checkbox_vars.append(var)

                    booking_text = (
                        f"• Username = {booking['Username']},\n• Date = {booking['Booking Date']},"
                        f"\n• Lokasi = {booking['Address']},\n• Service = {booking['Selected Services']},"
                        f"\n• Harga = {booking['Service Price']},Payment = {booking['Payment']},"
                        f"\n• No.Hp = {booking['Phone Number']}\n\n============================================\n\n"
                    )
                    text_widget.window_create(tk.END, window=checkbox)
                    text_widget.insert(tk.END, booking_text)
                    self.load_checkbox_states(4)
            def savebox():
                messagebox.showinfo("Check","Berhasil Checklist")
                self.save_checkbox_states(4)
            ctk.CTkButton(self.frame_owner, text="Save Checklist", corner_radius=20,
                       bg_color='#f8f8f8', hover_color='green', fg_color='#1679ad',
                       width=150, height=30, command=savebox).place(x=200, y=460)

            ctk.CTkButton(self.frame_owner,text="Back",corner_radius=20,bg_color='#f8f8f8',hover_color='red',fg_color='#1679ad',width=100,height=30,command=self.frame_owner.destroy).place(x=50,y=460)


#=========== DASHBOARD USER ========#

    def dashboard(self):

        self.loginlayar.destroy()
        self.window = window  
        self.bg = PhotoImage(file="dashboard.png")
        self.layardash = Label(window, image=self.bg)
        self.layardash.place(x=0, y=0, relheight=1, relwidth=1)
        username = self.username.get()

        with open('dataservice.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Username'] == username:
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    self.nama_label_dshbrd = Label(window,text=f"Welcome {first_name} {last_name}!\nto S.TECH\nAC Service Reminder", font=("sans serif", 20, "bold"),bg='#ecf0f3',justify='center',fg='#74818a')
                    self.nama_label_dshbrd.place(x=140,y=170)
                    break
 
    #==================JASA SERVICE===============#
        self.fotoA= PhotoImage(file="jasa a.png")
        self.fotoB= PhotoImage(file="jasa b.png")
        self.fotoC= PhotoImage(file="jasa c.png")
        self.fotoD= PhotoImage(file="jasa d.png")


        def click1():
            self.jasa(1)
        self.button_jasa_A = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoA,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="Rp. 80.000,-\n Botania Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768", command=click1)
        self.button_jasa_A.place(x=740,y=230)

        def click2():
            self.jasa(2)
        self.button_jasa_B = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoB,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="Rp. 70.000,- \n ACTECH Service", font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768", command=click2)
        self.button_jasa_B.place(x=980,y=230)

        def click3():
            self.jasa(3)
        self.button_jasa_C = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoC,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N, text="Rp. 60.000,- \n BORCHELE Service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=click3)
        self.button_jasa_C.place(x=740,y=460)

        def click4():
            self.jasa(4)
        self.button_jasa_D = ctk.CTkButton(window,width=100,height=120,corner_radius=20,image=self.fotoD,hover_color='#adbec8',bg_color="#ecf0f3",fg_color="white",compound=TOP,anchor=N,text="Rp. 50.000,- \n JAYA service",font=("Tw Cen MT Condensed Extra Bold",20), text_color="#2b5768",command=click4)
        self.button_jasa_D.place(x=980,y=460)

        self.button_reminder=Button(window, command=self.reminder,text="Reminder",bg="#ecf0f3",foreground="blue" ,font=("Arial MT Rounded",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        self.button_reminder.place(x=975,y=90)

        self.button_riwayat_booking=Button(window, command=self.riwayat_booking,text="Booking\nHistory",bg="#ecf0f3",foreground="blue" ,font=("Arial MT Rounded",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        self.button_riwayat_booking.place(x=765,y=90)

        self.button_konsul=Button(window,command=self.konsul,text="AC\nConsultation",bg="#ecf0f3",foreground="blue" ,font=("Arial MT Rounded",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        self.button_konsul.place(x=530,y=90)

        self.button_logout=Button(window,text="Log out",bg = "#ecf0f3", font=("sans serif",10,"bold underline"),fg="red",command=self.logout,
                                     activebackground='red',highlightbackground="#75bfd5",highlightcolor="#75bfd5",highlightthickness=0,border=0,borderwidth=0).place(x=60,y=70)
    #============ Logout ===========#
    def logout(self):
        logout = messagebox.askyesno("Logout","Apakah anda ingin logout?")

        if logout:
            # self.window.destroy()
            self.reset_gui()

    def reset_gui(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.__init__(self.window)
    
    #============== Perlakuan khusus ketika salah satu button di tekan ===========#
    def disable_button(self):
        self.button_reminder.config(state="disabled")
        self.button_riwayat_booking.config(state="disabled")
        self.button_konsul.config(state="disabled")
    
    def active_button(self):
        try:
            # self.frame_jasa.destroy()
            # self.frame_reminder.destroy()
            self.button_reminder.config(state="normal")
            self.button_riwayat_booking.config(state="normal")
            self.button_konsul.config(state="normal")
        except:
            pass
        try:
            # self.frame_jasa.destroy()
            # self.frame_riwayat.destroy()
            self.button_reminder.config(state="normal")
            self.button_riwayat_booking.config(state="normal")
            self.button_konsul.config(state="normal")
        except:
            pass
        try:
            # self.frame_jasa.destroy()
            # self.frame_konsul.destroy()
            self.button_reminder.config(state="normal")
            self.button_riwayat_booking.config(state="normal")
            self.button_konsul.config(state="normal")
        except:
            pass
        try:
            self.frame_jasa.destroy()
        except:
            pass
        try:
            self.frame_reminder.destroy()
        except:
            pass
        try:
            self.frame_riwayat.destroy()
        except:
            pass
        try:
            self.frame_konsul.destroy()
        except:
            pass
        try:
            frame_konsul1.destroy()
        except:
            pass
        try:
            self.frame_reminder.destroy()
        except:
            pass


    #=============== Konsultasi AC ================#
    def konsul(self):
        self.disable_button()
        self.frame_konsul= ctk.CTkFrame(window, border_width=3,border_color='black', corner_radius=20, bg_color='#ecf0f3', fg_color='#f8f8f8', width=520, height=510)
        self.frame_konsul.place(x=720, y=180)

    
        self.image = PhotoImage(file="konsul.png")
        Label(self.frame_konsul,image=self.image).place(x=7,y=7)

        self.konsultasi1=StringVar()
        self.konsultasi2=StringVar()
        self.konsultasi3=StringVar()
        self.konsultasi4=StringVar()
        self.konsultasi5=StringVar()
        self.konsultasi6=StringVar()
        self.konsultasi7=StringVar()

        self.konsultasi1.set("Tidak")
        checkbutton_A = Radiobutton(self.frame_konsul, text="Ya", value = "Ya", variable = self.konsultasi1, bg="#f8f8f8")
        checkbutton_A.place(x=60, y=130)
        checkbutton_B = Radiobutton(self.frame_konsul, text="Tidak",value="Tidak", variable = self.konsultasi1, bg="#f8f8f8")
        checkbutton_B.place(x=120, y=130)

        self.konsultasi2.set("Tidak")
        checkbutton_A = Radiobutton(self.frame_konsul, text="Ya", value = "Ya", variable = self.konsultasi2, bg="#f8f8f8")
        checkbutton_A.place(x=60, y=180)
        checkbutton_B = Radiobutton(self.frame_konsul, text="Tidak",value="Tidak", variable = self.konsultasi2, bg="#f8f8f8")
        checkbutton_B.place(x=120, y=180)

        self.konsultasi3.set("Tidak")
        checkbutton_A = Radiobutton(self.frame_konsul, text="Ya", value = "Ya", variable = self.konsultasi3, bg="#f8f8f8")
        checkbutton_A.place(x=60, y=230)
        checkbutton_B = Radiobutton(self.frame_konsul, text="Tidak",value="Tidak", variable = self.konsultasi3, bg="#f8f8f8")
        checkbutton_B.place(x=120, y=230)

        self.konsultasi4.set("Tidak")
        checkbutton_A = Radiobutton(self.frame_konsul, text="Ya", value = "Ya", variable = self.konsultasi4, bg="#f8f8f8")
        checkbutton_A.place(x=60, y=280)
        checkbutton_B = Radiobutton(self.frame_konsul, text="Tidak",value="Tidak", variable = self.konsultasi4, bg="#f8f8f8")
        checkbutton_B.place(x=120, y=280)

        self.konsultasi5.set("Tidak")
        checkbutton_A = Radiobutton(self.frame_konsul, text="Ya", value = "Ya", variable = self.konsultasi5, bg="#f8f8f8")
        checkbutton_A.place(x=60, y=330)
        checkbutton_B = Radiobutton(self.frame_konsul, text="Tidak",value="Tidak", variable = self.konsultasi5, bg="#f8f8f8")
        checkbutton_B.place(x=120, y=330)
        
        self.konsultasi6.set("Tidak")
        checkbutton_A = Radiobutton(self.frame_konsul, text="Ya", value = "Ya", variable = self.konsultasi6, bg="#f8f8f8")
        checkbutton_A.place(x=60, y=380)
        checkbutton_B = Radiobutton(self.frame_konsul, text="Tidak",value="Tidak", variable = self.konsultasi6, bg="#f8f8f8")
        checkbutton_B.place(x=120, y=380)

        self.konsultasi7.set("Tidak")
        checkbutton_A = Radiobutton(self.frame_konsul, text="Ya", value = "Ya", variable = self.konsultasi7, bg="#f8f8f8")
        checkbutton_A.place(x=60, y=430)
        checkbutton_B = Radiobutton(self.frame_konsul, text="Tidak",value="Tidak", variable = self.konsultasi7, bg="#f8f8f8")
        checkbutton_B.place(x=120, y=430)

        booking_button = ctk.CTkButton(self.frame_konsul,width=100,text="Result",command=self.konsul2)
        booking_button.place(x=340,y=470)
        close_button = ctk.CTkButton(self.frame_konsul,width=100, text="Close", command=self.active_button)
        close_button.place(x=80,y=470)


    
        
    def konsul2(self): 
        self.frame_konsul.destroy()
        global frame_konsul1
        frame_konsul1= ctk.CTkFrame(window, corner_radius=20, bg_color='#ecf0f3', fg_color='white', width=500, height=530)
        frame_konsul1.place(x=740, y=180)

        
        ctk.CTkLabel(frame_konsul1, corner_radius=20, text='result', text_color='white', font=('Helvetica', 30, 'bold'), fg_color='#99c9db', bg_color='#f8f8f8').place(x=210, y=15)
        # self.image = PhotoImage(file="konsul.png")
        # Label(frame_konsul1,image=self.image).place(x=10,y=10)
        masalah_ac = []
        if self.konsultasi1.get() == "Ya":
            # Label(frame_konsul1, text="halo").pack()
            masalah = "✼AC Tidak dingin:\nAda beberapa faktor yang bisa menyebabkan udara yang dikeluarkan AC menjadi tidak dingin. Beberapa di antaranya yaitu daya kerja AC yang tidak sesuai dengan luas ruangan, pengaturan remote AC yang tidak sesuai, hingga kondisi ruangan yang sering terpapar sinar matahari.\n pilih layanan jasa: service ac\n "
            masalah_ac.append(masalah)
            self.service_AC.set(1)
        if self.konsultasi2.get() =="Ya":
            masalah = "✼Udara AC panas: \nPenyebabnya bisa karena ada komponen AC yang rusak, seperti bocornya sistem AC, atau tekanan pada freon yang terlalu tinggi.\npilih layanan jasa: service ac dan ganti komponen\n"
            masalah_ac.append(masalah)
            self.service_AC.set(1)
            self.ganti_komponen.set(1)
            
        if self.konsultasi3.get()=="Ya":
            masalah="✼AC mendadak mati:\nKemungkinan ada komponen AC yang rusak. Masalah AC mati biasanya terjadi saat AC sudah lama tidak dinyalakan. Untuk masalah yang satu ini, Anda juga sebaiknya memanggil jasa servis AC.\n pilih layanan jasa: service ac dan ganti komponen\n"
            masalah_ac.append(masalah)
            self.service_AC.set(1)
            self.ganti_komponen.set(1)
        if self.konsultasi4.get()=="Ya":
            masalah="✼AC / Air Ac bocor:\nBiasanya, hal ini berhubungan dengan adanya kebocoran pada pemasangan rangkaian jalur gas freon yang diselimuti oleh pipa sanitasi. Freon yang bocor bisa membahayakan kesehatan, seperti iritasi pada mata, hidung, lidah, tenggorokan, dan lain-lain. Bila Anda curiga freon bocor, segera panggil teknisi servis AC ke rumah Anda.\n pilih layanan jasa: service ac dan isi freon\n"
            masalah_ac.append(masalah)
            self.service_AC.set(1)
            self.isi_Freon.set(1)
        if self.konsultasi5.get()=="Ya":
            masalah="✼AC mengeluarkan bau tidak sedap:\nBiasanya, hal ini disebabkan oleh adanya bangkai binatang kecil yang mati di dalam AC. Anda bisa membuka penutup AC untuk mengecek apakah ada bangkai binatang di dalamnya atau menempel pada filter AC.\n pilih layanan jasa: service ac dan vacuum ac\n"
            masalah_ac.append(masalah)
            self.service_AC.set(1)
            self.vacuum.set(1)

        if self.konsultasi6.get()=="Ya":
            masalah="✼AC menghembuskan angin lemah:\nMasalah ini bisa disebabkan oleh saluran duct yang bocor, penyumbatan ventilasi, dan tingkat refrigeran yang rendah.\n pilih layanan jasa: service ac\n"
            masalah_ac.append(masalah)
            self.service_AC.set(1)

        if self.konsultasi7.get()=="Ya":
            masalah="✼AC berbunyi tidak normal:\nMasalah tersebut dapat berasal dari kompresor atau motor yang mengalami kerusakan. Bisa juga ada sesuatu yang menyangkut pada kipas AC ataupun masalah pada kapasitor.\n pilih layanan jasa: service ac dan ganti kapasitor \n"
            masalah_ac.append(masalah) 
            self.service_AC.set(1)
            self.ganti_kapasitor_AC.set(1)
        
        if masalah_ac:
            desc = "\n".join(masalah_ac)
        text_widget = Text(frame_konsul1, wrap=WORD, bg='#f8f8f8', fg='black', font=("Sans serif", 12))
        text_widget.insert(END, ''.join(desc))
        text_widget.config(state=DISABLED)  # Membuat teks tidak dapat diedit
        text_widget.place(x=50, y=60, width=400, height=400)


        scrollbar = Scrollbar(frame_konsul1, command=text_widget.yview)
        scrollbar.place(x=450, y=50, height=400)
        text_widget.config(yscrollcommand=scrollbar.set)

        close_button = ctk.CTkButton(frame_konsul1,width=100, text="Close", command=self.active_button)
        close_button.place(x=220,y=480)
    
    #============= Jasa User ============#
    def jasa(self,button_id):

        self.frame_jasa= ctk.CTkFrame(window, corner_radius=20, bg_color='#ecf0f3', fg_color='#f8f8f8', width=500, height=530)
        self.frame_jasa.place(x=720, y=160)

    
        self.image = PhotoImage(file="service.png")
        Label(self.frame_jasa,image=self.image).place(x=2,y=8)

        if button_id == 1: 
            self.disable_button()

            no_hp = Label(self.frame_jasa,text="Owner : 085852188805",font=("sans serif",10),bg='#f8f8f8',fg="#072D44")
            no_hp.place(x=20,y=505)

            Servis_Cuci = Label(self.frame_jasa,text="BOTANIA",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)
            
            #=============== Animasi Gambar ===========#
            self.image_paths = [r"jasa a.png",r"jasaa1.png",r"jasaa2.png"]
            self.images = [Image.open(path) for path in self.image_paths]

            self.current_image_index = 0
            
            self.image_label = Label(self.frame_jasa, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            self.scroll_images()

            deskripsi = scrolledtext.ScrolledText(self.frame_jasa,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Botania Service \nperusahaan terkemuka di bidang layanan perawatan dan perbaikan sistem pendingin udara (AC). Dengan komitmen untuk memberikan kualitas terbaik kepada pelanggan, Botania Service telah menjadi pilihan utama dalam menjaga performa optimal AC.
                                    Kenapa Memilih Layanan Kami:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\nPelayanan pelanggan ramah dan responsif.\n4. Jaminan kepuasan pelanggan.
                                    Hubungi Kami:
                                    Alamat: \nJalan Mangga No.1, RT 01 RW 02, Kelurahan Besi Muda, Kecamatan Genteng, Kota Surabaya, Jawa Timur.
                                    Jangan biarkan AC Anda beroperasi di bawah performa optimal. Percayakan perawatan AC Anda kepada kami dan rasakan perbedaannya! Terima kasih telah memilih kami sebagai mitra perawatan AC Anda.
                                    NO HP: 081111222333
                                    [BOTANIA Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)

            def click():
                self.booking(1)
            booking_button = ctk.CTkButton(self.frame_jasa,width=100,text="Booking",command=click)
            booking_button.place(x=140,y=450)
            close_button = ctk.CTkButton(self.frame_jasa,width=100, text="Close", command=self.active_button)
            close_button.place(x=20,y=450)
            
        elif button_id == 2: 
            self.disable_button()

            no_hp = Label(self.frame_jasa,text="Owner : 085852188805",font=("sans serif",10),bg='#f8f8f8',fg="#072D44")
            no_hp.place(x=20,y=505)

            Servis_Cuci = Label(self.frame_jasa,text="ACTECH",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)

            #===========Animasi Gambar============
            self.image_paths = [r"jasa b.png",r"jasab1.png",r"jasab2.png"]
            self.images = [Image.open(path) for path in self.image_paths]

            self.current_image_index = 0

            # Tampilkan gambar pertama di dalam frame utama
            self.image_label = Label(self.frame_jasa, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            self.scroll_images()
            # Memulai fungsi pengguliran otomatis

            deskripsi = scrolledtext.ScrolledText(self.frame_jasa,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Actech Service  \nperusahaan yang berdedikasi dalam menyediakan layanan unggul di bidang perawatan dan perbaikan sistem pendingin udara (AC). Dengan fokus utama pada kualitas, keandalan, dan kepuasan pelanggan, Actech Service telah menjadi pilihan utama bagi individu dan bisnis yang membutuhkan solusi profesional untuk kebutuhan AC mereka.
                                    Kenapa Memilih Layanan Kami:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\nPelayanan pelanggan ramah dan responsif.\n4. Jaminan kepuasan pelanggan.
                                    Hubungi Kami:
                                    Alamat: \nJalan Anggrek No. 15, RT 05 RW 03, Kelurahan Bambu Kuning, Kecamatan Gubeng, Kota Surabaya, Jawa Timur.
                                    NO HP: 081123456789
                                    [ACTECH Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)

            def click():
                self.booking(2)
            booking_button = ctk.CTkButton(self.frame_jasa,width=100,text="Booking",command=click)
            booking_button.place(x=140,y=450)
            close_button = ctk.CTkButton(self.frame_jasa,width=100, text="Close", command=self.active_button)
            close_button.place(x=20,y=450)

        elif button_id ==3:
            self.disable_button()

            no_hp = Label(self.frame_jasa,text="Owner : 082139948140",font=("sans serif",10),bg='#f8f8f8',fg="#072D44")
            no_hp.place(x=20,y=505)

            Servis_Cuci = Label(self.frame_jasa,text="BORCHELLE",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)

            #============ Animasi Gambar =============#
            self.image_paths = [r"jasa c.png",r"jasac1.png",r"jasac2.png"]
            self.images = [Image.open(path) for path in self.image_paths]

            # Indeks gambar saat ini
            self.current_image_index = 0

            # Tampilkan gambar pertama di dalam frame utama
            self.image_label = Label(self.frame_jasa, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            # Memulai fungsi pengguliran otomatis
            self.scroll_images()

            deskripsi = scrolledtext.ScrolledText(self.frame_jasa,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Borcelle Service \nperusahaan yang bergerak di bidang layanan perbaikan dan pemeliharaan sistem pendingin udara (AC). Dengan komitmen untuk memberikan pelayanan terbaik kepada pelanggan, Borcelle Service telah menjadi pilihan utama bagi mereka yang membutuhkan solusi profesional untuk masalah AC
                                    Kenapa Memilih Layanan Kami:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\nPelayanan pelanggan ramah dan responsif.\n4. Jaminan kepuasan pelanggan.
                                    Hubungi Kami:
                                    Alamat: \nJalan Dahlia No. 10A, RT 07 RW 04, Kelurahan Mawar Biru, Kecamatan Simokerto, Kota Surabaya, Jawa Timur.
                                    NO HP: 081234432567
                                    [BORCELLE Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)

            def click():
                self.booking(3)
            booking_button = ctk.CTkButton(self.frame_jasa,width=100,text="Booking",command=click)
            booking_button.place(x=140,y=450)
            close_button = ctk.CTkButton(self.frame_jasa,width=100, text="Close", command=self.active_button)
            close_button.place(x=20,y=450)

        elif button_id ==4:
            self.disable_button()

            no_hp = Label(self.frame_jasa,text="Owner : 082132656248",font=("sans serif",10),bg='#f8f8f8',fg="#072D44")
            no_hp.place(x=20,y=505)

            Servis_Cuci = Label(self.frame_jasa,text="JAYA",font=("Arial Rounded MT Bold",11,"bold"),bg='#f8f8f8',fg="#072D44")
            Servis_Cuci.place(x=35,y=80)

            #============= Animasi Gambar =============#
            self.image_paths = [r"jasa d.png",r"jasad1.png",r"jasad2.png"]
            self.images = [Image.open(path) for path in self.image_paths]
            
            # Indeks gambar saat ini
            self.current_image_index = 0

            # Tampilkan gambar pertama di dalam frame utama
            self.image_label = Label(self.frame_jasa, bg="#f8f8f8")
            self.image_label.place(x=35,y=210)

            self.scroll_images()

            deskripsi = scrolledtext.ScrolledText(self.frame_jasa,width=27,height=25,wrap=tk.WORD,bg='#D0D7E1')
            deskripsi.insert(tk.END,"""Jaya Service \nperusahaan yang berdedikasi dalam memberikan layanan profesional dan terpercaya di bidang service AC. Dengan pengalaman yang telah teruji dan tenaga kerja yang ahli, Jaya Service menjadi pilihan utama bagi pelanggan yang mengutamakan kualitas dan kehandalan dalam perawatan dan perbaikan perangkat pendingin udara.
                                    Kenapa Memilih Layanan Kami:\n1. Teknisi berpengalaman dan terlatih.\n2. Peralatan mutakhir untuk diagnosis dan perbaikan.\n3. Harga yang terjangkau dan transparan.\nPelayanan pelanggan ramah dan responsif.\n4. Jaminan kepuasan pelanggan.
                                    Hubungi Kami:
                                    Alamat: \nJalan Mawar Indah No. 15, RT 10 RW 02, Kelurahan Kenanga, Kecamatan Wonocolo, Kota Surabaya, Jawa Timur.
                                    NO HP: 081987456432
                                    [Jaya Service]""")
            deskripsi.config(state=tk.DISABLED)
            deskripsi.place(x=250,y=75)

            def click():
                self.booking(4)
            booking_button = ctk.CTkButton(self.frame_jasa,width=100,text="Booking",command=click)
            booking_button.place(x=140,y=450)
            close_button = ctk.CTkButton(self.frame_jasa,width=100, text="Close", command=self.active_button)
            close_button.place(x=20,y=450)
     
    def scroll_images2(self):
        
        current_image = self.images[self.current_image_index]
        photo = ImageTk.PhotoImage(current_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Mengganti indeks gambar untuk menggulir ke gambar berikutnya
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.frame_owner.after(2000,self.scroll_images2)

    def scroll_images(self):
        # Menampilkan gambar saat ini
        current_image = self.images[self.current_image_index]
        photo = ImageTk.PhotoImage(current_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Mengganti indeks gambar untuk menggulir ke gambar berikutnya
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.frame_jasa.after(2000, self.scroll_images)
        

    #========= BOOKING ========#
    def booking(self,button_id):
        
        self.alamat = tk.StringVar()
        self.no_Hp = tk.StringVar()
        self.nama_jasa = tk.StringVar()
        self.tanggal_booking = tk.StringVar()
        self.total_price = tk.StringVar()

        service_AC = IntVar()
        isi_Freon = IntVar()
        tambah_Freon = IntVar()
        ganti_kapasitor_AC = IntVar()
        ganti_komponen = IntVar()
        vacuum = IntVar()
        flushing_AC = IntVar()

        global frame_booking
        frame_booking= ctk.CTkFrame(window, corner_radius=20, bg_color='#ecf0f3', fg_color='white', width=530, height=550)
        frame_booking.place(x=700, y=120)

        self.image_boform = PhotoImage(file="booking form.png")
        Label(frame_booking,image=self.image_boform).place(x=2,y=8)

        frame_kecil =ctk.CTkFrame(frame_booking,corner_radius=20, bg_color="white", fg_color="#acafb1", width=200, height=375)
        frame_kecil.place(x=285,y=115)
        
        self.label_nama_booking = ctk.CTkLabel(frame_booking, text='Username', font=("Times", 15, "bold"), bg_color="white", text_color='black')
        self.label_nama_booking.place(x=30, y=115)

        self.entry_nama_booking = ctk.CTkEntry(frame_booking, state='readonly',width=250, corner_radius=20, textvariable=self.username, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_nama_booking.place(x=20, y=145)

        self.label_alamat_booking = ctk.CTkLabel(frame_booking, text='Addres Home', font=("Times", 15, "bold"), bg_color="white", text_color='black')
        self.label_alamat_booking.place(x=30, y=175)

        self.entry_alamat_booking = ctk.CTkEntry(frame_booking, width=250, corner_radius=20, textvariable=self.alamat, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_alamat_booking.place(x=20, y=205)

        self.label_no_hp_booking = ctk.CTkLabel(frame_booking, text='No. Whatsapp', font=("Times", 15, "bold"), bg_color="white", text_color='black')
        self.label_no_hp_booking.place(x=30, y=235)

        self.entry_no_hp_booking = ctk.CTkEntry(frame_booking, width=250, corner_radius=20, textvariable=self.no_Hp, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_no_hp_booking.place(x=20, y=265)

        self.label_tanggal_booking = ctk.CTkLabel(frame_booking, text='Tanggal Booking', font=("Times", 15, "bold"), bg_color="white", text_color='black')
        self.label_tanggal_booking.place(x=30, y=295)

        self.entry_tanggal_booking = ctk.CTkEntry(frame_booking, state='readonly',width=250, corner_radius=20, textvariable=self.tanggal_booking, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
        self.entry_tanggal_booking.place(x=20, y=325)
        
        self.label_nama_jasa = ctk.CTkLabel(frame_booking, text='Nama Jasa', font=("Times", 15, "bold"), bg_color="white", text_color='black')
        self.label_nama_jasa.place(x=30, y=355)

        self.harga_jasa = IntVar()
        global service_prices
        service_prices = {}
        if button_id == 1:
            self.nama_jasa = "BOTANIA Service"
            self.harga_jasa = 80000
            entry_nama_jasa = ctk.CTkLabel(frame_booking, text="BOTANIA Service", width=250, corner_radius=20, textvariable=self.nama_jasa, font=("Times", 20), fg_color="#f8f8f8", text_color="black")
            entry_nama_jasa.place(x=50, y=370)
        
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=self.service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp.75.000,-", variable=self.isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp.50.000,-", variable=self.tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp.120.000,-", variable=self.ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp.200.000,-", variable=self.ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp.150.000", variable=self.vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp.180.000,-", variable=self.flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Service AC":self.harga_jasa,
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
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=self.service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp.80.000,-", variable=self.isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp.60.000,-", variable=self.tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp.110.000,-", variable=self.ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp.180.000,-", variable=self.ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp.160.000", variable=self.vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp.190.000,-", variable=self.flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Service AC":self.harga_jasa,
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
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=self.service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp.70.000,-", variable=self.isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp 65.000,-", variable=self.tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp.110.000,-", variable=self.ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp.190.000,-", variable=self.ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp.180.000", variable=self.vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp.200.000,-", variable=self.flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Service AC":self.harga_jasa,
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
            Checkbutton(frame_booking, text=f"Service AC, Rp.{self.harga_jasa},-", variable=self.service_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=75)
            Checkbutton(frame_booking, text="Isi Freon, Rp. 80.000,-", variable=self.isi_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=105)
            Checkbutton(frame_booking, text="Tambah Freon, Rp. 70.000,-", variable=self.tambah_Freon, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=135)
            Checkbutton(frame_booking, text="Ganti Kapasitor AC, Rp. 100.000,-", variable=self.ganti_kapasitor_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=165)
            Checkbutton(frame_booking, text="Ganti Komponen, Rp. 140.000,-", variable=self.ganti_komponen, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=195)
            Checkbutton(frame_booking, text="Vacuum AC, Rp. 115.000", variable=self.vacuum, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=225)
            Checkbutton(frame_booking, text="Flushing AC, Rp. 160.000,-", variable=self.flushing_AC, bg='#1679ad', activebackground='#8bc3d3').place(x=310, y=255)
            service_prices = {
                "Service AC":self.harga_jasa,
                "Isi Freon": 80000,
                "Tambah Freon": 70000,
                "Ganti Kapasitor AC": 100000,
                "Ganti Komponen": 140000,
                "Vacuum AC": 115000,
                "Flushing AC": 160000
            }
        self.label_payment = ctk.CTkLabel(frame_booking, text='Payment', font=("Times", 15, "bold"), bg_color="white", text_color='black')
        self.label_payment.place(x=30, y=415)

        #========Calendar=========#
        cal = Calendar(frame_booking, selectmode='day', date_pattern='yyyy-mm-dd', font=("Times", 5), foreground='black', background='white')
        cal.place(x=305, y=300)   

        self.radio_values = {1: "CASH", 2: "QRIS"}
        self.pemilihanpay = IntVar()

        def show_selected_value():
            global selected_value
            selected_value = self.pemilihanpay.get()
            if selected_value in self.radio_values:
                self.pemilihanpayyy =  self.radio_values[selected_value]

        checkbutton_A = Radiobutton(frame_booking, text="CASH", value = 1, variable = self.pemilihanpay, bg="white",command= show_selected_value)
        checkbutton_A.place(x=50, y=450)
       
        
        checkbutton_B = Radiobutton(frame_booking, text="QRIS",value=2, variable = self.pemilihanpay, bg="white",command= show_selected_value)
        checkbutton_B.place(x=170, y=450)
        
        def get_date():
            date = cal.get_date()
            self.tanggal_booking.set(date)
        
        btn = ctk.CTkButton(frame_booking, text="Select Date", command=get_date, corner_radius=20, bg_color='#acafb1', font=("Times", 15, "bold"))
        btn.place(x=315, y=450)

        def check_username_limit():
                csv_file="booking_data.csv"
                tgl_booking = self.tanggal_booking.get()
                nama_servis = self.nama_jasa
                with open(csv_file, mode='r') as file:
                    reader = csv.DictReader(file)
                    booking_count = sum(1 for row in reader if row['Booking Date'] == tgl_booking and row['Service Name'] == nama_servis)
                    return booking_count >= 3
        
        def calculate_price():

            if not all([self.alamat.get(), self.no_Hp.get(), self.tanggal_booking.get(), self.nama_jasa]):
                messagebox.showerror("Error", "Harus mengisi semua kolom booking form")
            elif not self.service_AC.get() and not self.isi_Freon.get() and not self.tambah_Freon.get() and not self.ganti_kapasitor_AC.get() and not self.ganti_komponen.get() and not self.vacuum.get() and not self.flushing_AC.get():
                messagebox.showerror("Error", "Anda harus memilih setidaknya satu layanan")
            elif not self.pemilihanpay.get():
                messagebox.showerror("Error","Silahkan pilih metode pembayaran")
            elif check_username_limit():
                messagebox.showerror("Booking", "Booking pada hari yang anda pilih sudah penuh!")
            else:
                global harga_jasa,selected_services
                harga_jasa = self.harga_jasa
                self.total_price = harga_jasa
                selected_services = []
                for service, price in service_prices.items():
                    if service == "Service AC" and self.service_AC.get() == 1:
                        selected_services.append(("Service AC")), self.total_price
                    elif service == "Tambah Freon" and self.tambah_Freon.get() == 1:
                        self.total_price += price
                        selected_services.append("Tambah Freon"), self.total_price
                    elif service == "Ganti Kapasitor AC" and self.ganti_kapasitor_AC.get() == 1:
                        self.total_price += price
                        selected_services.append("Ganti Kapasitor AC"), self.total_price
                    elif service == "Ganti Komponen" and self.ganti_komponen.get() == 1:
                        self.total_price += price
                        selected_services.append("Ganti Komponen"), self.total_price
                    elif service == "Vacuum AC" and self.vacuum.get() == 1:
                        self.total_price += price
                        selected_services.append("Vacuum AC"), self.total_price
                    elif service == "Flushing AC" and self.flushing_AC.get() == 1:
                        self.total_price += price
                        selected_services.append("Flushing AC"), self.total_price

                messagebox.showinfo("Booking","Lakukan Pembayaran")
                self.payment_methode()

        button_back = ctk.CTkButton(frame_booking, text="Back", command=frame_booking.destroy, corner_radius=20, bg_color='white', font=("Times" , 15, "bold")) 
        button_back.place(x=50, y=510)

        btn = ctk.CTkButton(frame_booking, text="Payment",command=calculate_price, corner_radius=20,bg_color='white', font=("Times" , 15, "bold")) 
        btn.place(x=325, y=510)
           
    def simpan_info(self,button_id):
            with open('booking_data.csv', mode='a', newline='') as file:
                    row = ['Name', 'Address', 'Phone Number', 'Booking Date', 'Service Name', 'Selected Services', 'Service Price', 'Payment Methode']
                    writer = csv.DictWriter(file, fieldnames=row)
                    writer.writerow({
                        'Name': self.username.get(),
                        'Address': self.alamat.get(),
                        'Phone Number': self.no_Hp.get(),
                        'Booking Date': self.tanggal_booking.get(),
                        'Service Name': self.nama_jasa,
                        'Selected Services': ', '.join([service[0:] for service in selected_services]),
                        'Service Price': self.total_price,
                        'Payment Methode' : self.pemilihanpayyy
                        })
            if button_id == 1:
                messagebox.showinfo("Confirm Payment","Terimakasih telah menggunakan jasa kami\nIngat AC, Ingat kami ^_^")
            elif button_id == 2:
                Y = messagebox.showinfo("Confirm Payment","Mohon mengisi google form terlebih dahulu")
                if Y:
                    webbrowser.open('https://forms.gle/CeT5tAKySecCuKzQ9')
                    messagebox.showinfo("Confirm Payment","Terimakasih telah menggunakan jasa kami\nIngat AC, Ingat kami ^_^")
                    

            window_payment.destroy()
            frame_booking.destroy()
            self.active_button()
    #==========Payment========#
    def payment_methode(self):
            
            self.frame_jasa.destroy()
            frame_booking.destroy()
            global window_payment
            window_payment = ctk.CTkFrame(window,corner_radius=20,bg_color='white',border_width=3,border_color='black',fg_color='#f8f8f8',width=530,height=530)
            window_payment.place(x=740, y=140)
            self.image2=PhotoImage(file="payment.png")
            Label(window_payment,image=self.image2).place(x=5,y=5)
            # ctk.CTkLabel(window_payment, corner_radius=20, text='Payment', text_color='black', font=('Helvetica', 30, 'bold'), fg_color='#99c9db', bg_color='white').place(x=200, y=15)
            self.pemilihanpayyy =  self.radio_values[selected_value]

            if self.pemilihanpayyy == "CASH":
                self.image3=PhotoImage(file="cash.png")
                Label(window_payment,image=self.image3).place(x=150,y=130)
                a=ctk.CTkLabel(window_payment, text=f'Terima kasih! \nsilahkan melakukan pembayaran ditempat sebesar \nRp. {self.total_price} ,-',font=('Helvetica',15, 'bold'), text_color='black')
                a.place(x=90,y=400)

                def cash():
                    self.simpan_info(1)
                btn = ctk.CTkButton(window_payment, width=130,height=50, text="Confirm Payment",command=cash, corner_radius=20, bg_color='#f8f8f8', font=("Times" , 15, "bold")) 
                btn.place(x=187, y=470)    

            elif self.pemilihanpayyy == "QRIS":
                self.image1=PhotoImage(file="qr.png")
                Label(window_payment,image=self.image1).place(x=150,y=130)
                ctk.CTkLabel(window_payment, text=f'Anda harus bayar sebesar\nRp.{self.total_price},-',font=('Helvetica',20, 'bold'),text_color='black').place(x=140,y=400)
                
                def payyy():
                    self.simpan_info(2)
                
                btn = ctk.CTkButton(window_payment, width=130,height=50, text="Confirm Payment",command=payyy, corner_radius=20, bg_color='#f8f8f8', font=("Times" , 15, "bold")) 
                btn.place(x=187, y=470)

    def riwayat_booking(self):
        self.disable_button()
        self.frame_riwayat= ctk.CTkFrame(window, corner_radius=20, bg_color='#ecf0f3', fg_color='#f8f8f8', width=500, height=530)
        self.frame_riwayat.place(x=740, y=180)

        self.image = PhotoImage(file="booking.png")
        Label(self.frame_riwayat,image=self.image).place(x=2,y=8)

        username = self.username.get()

        booking_history = []  
        with open('booking_data.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Username'] == username:
                    booking_history.append(row)

        text_widget = scrolledtext.ScrolledText(self.frame_riwayat, wrap='word', width=60, height=20, font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
        text_widget.place(x=35, y=110)

        if not booking_history:
            no_booking_label = Label(self.frame_riwayat, text="Anda belum pernah booking.", font=("Arial", 10), bg='#f8f8f8', fg="#072D44")
            no_booking_label.place(x=80, y=170)
        else:
            for booking in booking_history:
                booking_text = (
                    f"• Username = {booking['Username']},\n• Date = {booking['Booking Date']},"
                    f"\n• Jasa = {booking['Service Name']},\n• Service = {booking['Selected Services']},"
                    f"\n• Harga = {booking['Service Price']}\n\n============================================\n\n"
                )
                text_widget.insert('end', booking_text)

        ctk.CTkButton(self.frame_riwayat,text="Back",corner_radius=20,bg_color='#f8f8f8',hover_color='red',fg_color='#1679ad',width=100,height=30,command=self.active_button).place(x=50,y=460)

#===========Calendar For Reminder==============#
    def calendar(self):
            self.mycal=Calendar(window,setmode="day", date_pattern = "d/mm/yy").pack()
            self.set_date_button= Button(window, command=self.set_date_entry, text="set")

#====================REMINDER=========================#
    
    def reminder(self):
        self.disable_button()
        self.emailRemind = StringVar()
        self.noteRemind = StringVar()
        self.emailSubject = "[S.Tech] AC Reminder Service"

        self.frame_reminder = ctk.CTkFrame(window,corner_radius=20,bg_color='#ecf0f3',border_width=3,border_color='white',fg_color='#f8f8f8',width=530,height=460)
        self.frame_reminder.place(x=660, y=215)

        self.image = PhotoImage(file="reminder.png")
        Label(self.frame_reminder,image=self.image).place(x=20,y=10)

        self.calendar = Calendar(self.frame_reminder, setmode="day", date_pattern="d/mm/yy")
        self.calendar.place(x=235, y=105)

        self.set_date_button = ctk.CTkButton(self.frame_reminder, text="Select date", width=20,command = self.Selectdate)
        self.set_date_button.place(x=320, y =310)

        self.last_service  = Label(self.frame_reminder, text="Last service", bg="#f8f8f8", font=("sans serif", 10, "bold"),fg="#0370a9").place(x=25, y=100)
        self.last_services__ket= Label(self.frame_reminder, border=0, highlightthickness=2, highlightcolor="#0370a9",relief="groove", width=19, font=("Sans serif", 13), bg="white", fg="black")
        self.last_services__ket.place(x=25, y=130)

        self.email_label = Label(self.frame_reminder, text="Email", bg="#f8f8f8", font=("sans serif", 10, "bold"),fg="#0370a9").place(x=25, y=160)
        self.email_entry = Entry(self.frame_reminder, border=0, highlightthickness=2, highlightcolor="#0370a9",relief="groove", width=19, font=("Sans serif", 13), bg="white", fg="black", textvariable=self.emailRemind)
        self.email_entry.place(x=25, y=200)

        self.note_label = Label(self.frame_reminder, text="Note", bg="#f8f8f8",font=("sans serif", 10, "bold"), fg="#0370a9").place(x=25, y=237)
        self.note_entry = Entry(self.frame_reminder, border=0, highlightthickness=2, highlightcolor="#0370a9",relief="groove", width=19, font=("Sans serif", 13), bg="white", fg="black", textvariable=self.noteRemind)
        self.note_entry.place(x=25, y=267)

        self.set_reminder_button = ctk.CTkButton(self.frame_reminder, text="Set reminder",hover_color='green', width=20, command=self.atur_tanggal_kirim_email)
        self.set_reminder_button.place(x=75,y=310)

        cancel_reminder_button = ctk.CTkButton(self.frame_reminder, text="Cancel reminder",hover_color='red',width=350,command=self.active_button)
        cancel_reminder_button.place(x=85, y=420)  

    def Selectdate(self):
             self.mydate = self.calendar.get_date()
             self.last_services__ket.config(text=self.mydate)

    #=============== Set tanggal reminder ===========#
    def atur_tanggal_kirim_email(self):
        Username = self.username.get()
        # global email_user
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
        gmail_user = "s.techcorpss@gmail.com"
        gmail_app_password = "jmob eqfu ilta hhgf"
        

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
        except Exception as exception:
            print("Error: %s!\n\n" % exception)
        
        self.send_email_after_three()

    #============ Pengiriman setelah 3 bulan ==========#
    def send_email_after_three(self):
        def read_last_row_columns(csv_file):
            with open(csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if rows:
                    last_row = rows[-1]
                    return last_row
                else:
                    return None
        csv_file_path = 'dataremind.csv'
        last_row_columns = read_last_row_columns(csv_file_path)
        present = datetime.now()
        formatted_date = present.strftime('%d/%m/%y')
        if last_row_columns[-1]== formatted_date:

                    gmail_user = "s.techcorpss@gmail.com"
                    gmail_app_password = "jmob eqfu ilta hhgf"
                    

                    sent_from = gmail_user
                    sent_to = self.emailRemind.get()
                    sent_subject = "Reminder Ac Service"
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




                            #================= TERIMAKASIH DARI KAMI S.TECH ======================#
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter
import csv
from tkcalendar import *
import smtplib
import pandas as pd
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
        
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.button_login = customtkinter.CTkButton(window,command=self.dashboard ,text="LOGIN",font=("sans serif",12,"bold"),width=350,)
        self.button_login.place(x=250,y=450)

        showpsw = Checkbutton(window, bg="#75bfd5", command=self.show_psw, text="show password",font=("sans serif",8))
        showpsw.place(x=250,y=410)

    #=========Show Password=========#

    def show_psw(self):
        if self.entry_password.cget("show") == "*":
            self.entry_password.config(show='')
        else:
            self.entry_password.config(show="*")

    # ===================CHECK LOG IN===============#
    def login(self):
        username = self.username.get()
        password = self.password.get()

        with open('dataservice.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username and row['Password'] == password:
                    messagebox.showinfo("Login", "Login berhasil!")   
                    self.dashboard(window) 
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

        self.submit_button = customtkinter.CTkButton(window, text="Submit", font=("sans serif", 12, "bold"), width=350,
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


        sign_in_button = customtkinter.CTkButton(sign_in_window,command=self.signup, text="Sign In", font=("sans serif", 12, "bold"),
                                                 width=350)
        sign_in_button.place(x=50, y=500)

    #+======================SIGN UP==========#
    def signup(self):
        global firstname
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
        self.nama_dashboard = Frame(window)
        # self.nama_dashboard.attributes("-alpha",0.8)
        self.nama_dashboard.place(x=190, y=90, width=600, height=200)

        with open('dataservice.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Username'] == username:
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    self.nama_label_dshbrd = Label(self.nama_dashboard, text=f"WELCOME {first_name} {last_name} \nTO S.TECH \nAC SERVICE REMINDER", font=("Roboto", 25, "bold"))
                    self.nama_label_dshbrd.place(x=0, y=10)
        # self.nama_label_dshbrd.config(bg="systemTransparent")
                    break

        self.button_tentang=Button(window, command=self.reminder,text="Reminder",bg="#012554",foreground="white" ,font=("gothic",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        self.button_tentang.place(x=1200,y=30)
        

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

        self.set_date_button = customtkinter.CTkButton(self.frame_reminder, text="Select date", width=20,command = self.Selectdate)
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

        self.set_reminder_button = customtkinter.CTkButton(self.frame_reminder, text="Set reminder",hover_color='green', width=350, command=self.atur_tanggal_kirim_email)
        self.set_reminder_button.place(x=50,y=320)

        cancel_reminder_button = customtkinter.CTkButton(self.frame_reminder, text="Cancel reminder",hover_color='red',command=self.cancel)
        cancel_reminder_button.place(x=50, y=360)   
        
    def cancel(self):
        self.frame_reminder.destroy()

    def Selectdate(self):
             self.mydate = self.calendar.get_date()
             self.last_services__ket.config(text=self.mydate)






    def atur_tanggal_kirim_email(self):
        Username = self.username.get()
        global email_user
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
        gmail_user = "s.techcorpss@gmail.com"
        gmail_app_password = "jmob eqfu ilta hhgf"
        

        sent_from = gmail_user
        sent_to = self.emailRemind.get()
        sent_subject = "Reminder Ac Service"
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
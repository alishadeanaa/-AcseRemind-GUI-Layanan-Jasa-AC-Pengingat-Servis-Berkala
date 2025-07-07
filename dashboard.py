from tkinter import *
import tkinter as tk 
import customtkinter as ct
from tkcalendar import *
import smtplib

window = Tk()




class Dashboard:

    def __init__(self,window):
        self.window = window  
        window.title("AC seRemind")
        window.state('zoomed')
        window.resizable(0,0)
        self.bg = PhotoImage(file="dashboard.png")
        self.a_label1=Label(window, image=self.bg)
        self.a_label1.place(x=0,y=0, relheight=1,relwidth=1)
    
        
        self.button_tentang=Button(window, command=self.reminder,text="Reminder",bg="#012554",foreground="white" ,font=("gothic",12,"bold underline"), relief="flat",activebackground="#012554", activeforeground="light blue", border = 0)
        self.button_tentang.place(x=1200,y=30)

       

    def calendar(self):
            self.mycal=Calendar(window,setmode="day", date_pattern = "d/mm/yy").pack()
            self.set_date_button= Button(window, command=self.set_date_entry, text="set")

    def reminder(self):
        self.emailRemind = StringVar()
        self.noteRemind = StringVar()
        self.emailSubject = "[S.Tech] AC Reminder Service"
        reminder_window = Toplevel()
        reminder_window.geometry('1000x600')
        reminder_window.title('Reminder')
        reminder_window.configure(background='#f8f8f8')
        reminder_window.resizable(0, 0)

        self.reminder_label = Label(reminder_window, text="Reminder", font=("sans serif", 16, "bold"), fg="#0370a9",
                              bg="#f8f8f8").place(x=150, y=10)

        self.calendar = Calendar(reminder_window, setmode="day", date_pattern="d/mm/yy")
        self.calendar.place(x = 500, y=100)

        self.set_date_button = ct.CTkButton(reminder_window, text="select date", width=20,command = self.Selectdate)
        self.set_date_button.place(x=600, y = 300)

        self.last_services__ket = Label(reminder_window, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                      relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.last_services__ket.place(x=50, y=90)

        
        self.last_service  = Label(reminder_window, text="last service", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                                fg="#0370a9").place(x=50, y=60)
        self.last_services__ket= Label(reminder_window, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                      relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black")
        self.last_services__ket.place(x=50, y=90)


        self.email_label = Label(reminder_window, text="email", bg="#f8f8f8", font=("sans serif", 10, "bold"),
                                fg="#0370a9").place(x=50, y=125)
        self.email_entry = Entry(reminder_window, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                     relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black", textvariable=self.emailRemind)
        self.email_entry.place(x=50, y=155)


        self.note_label = Label(reminder_window, text="Note", bg="#f8f8f8",
                                   font=("sans serif", 10, "bold"), fg="#0370a9").place(x=50, y=200)
        self.note_entry = Entry(reminder_window, border=0, highlightthickness=2, highlightcolor="#0370a9",
                                        relief="groove", width=38, font=("Sans serif", 13), bg="white", fg="black", textvariable=self.noteRemind)
        self.note_entry.place(x=50, y=230)

        self.set_reminder_button = ct.CTkButton(reminder_window, text="set reminder", width=350, command=self.sent_email)
        self.set_reminder_button.place(x=50,y=320)

    def Selectdate(self):
             self.mydate = self.calendar.get_date()
             self.last_services__ket.config(text=self.mydate)
    
    def sent_email(self):
        gmail_user = "alishadeana.23244@mhs.unesa.ac.id"
        gmail_app_password = "pluwvhhi"


        sent_from = gmail_user
        sent_to = self.emailRemind.get()
        sent_subject = f"S.Tech Ac Service Reminder"
        sent_body = f" Dear customer, thank you for using our apps, your last service is {self.mydate}, please service your AC ASAP! \n\nwith note: {self.noteRemind.get()}"


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

             
        
    # def calendar(self):
    #         self.mycal=Calendar(window,setmode="day", date_pattern = "d/m/yy").pack
    #         self.set_date_button= Button(window, command=self.set_date_entry, text="set")

    # def tentang(self):

            
    




        









gui = Dashboard(window)
window.mainloop()


import customtkinter
import oracledb
from operations import opreation_form

oracledb.init_oracle_client()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("database_connection")
app.geometry("500x500")

label = customtkinter.CTkLabel(app,text="LOG IN")
label.place(relx=0.5, rely=0.1, anchor="center")

label = customtkinter.CTkLabel(app, text=" welcome",text_color="blue")
label.place(relx=0.5, rely=0.9, anchor="center" )


entry_username = customtkinter.CTkEntry(app, placeholder_text="database_username", width=200, height=30)
entry_username.place(relx=.5, rely=.2 , anchor="center")

entry_password = customtkinter.CTkEntry(app, placeholder_text="database_password", width=200, height=30,show="*")
entry_password.place(relx=.5, rely=.3 , anchor="center")

def connect_to_database():
    global app
    try:
        label1.configure(text="Connecting.....")

        p_username = entry_username.get()
        p_password = entry_password.get()
        p_dns = "192.168.96.128/orcl"
        p_port = "1521"
        conn = oracledb.connect(user=p_username, password=p_password, dsn=p_dns, port=p_port)
        label1.configure(text="Connection successful!")
        opreation_form(conn)
    
    except Exception as e:
        label1.configure(text="Invalid username or password")
        print("Error:", e)

connect_button = customtkinter.CTkButton(app, text="Connect", fg_color="green", command=connect_to_database)
connect_button.place(relx=.5, rely=.4 ,anchor="center")

label1 = customtkinter.CTkLabel(app, text="",text_color='red')
label1.place(relx=.4, rely=.5, anchor="center")





app.mainloop()
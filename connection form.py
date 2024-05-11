import customtkinter
import oracledb

oracledb.init_oracle_client()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.title("database_connection")
app.geometry("300x400")

entry_username = customtkinter.CTkEntry(app, placeholder_text="database_username", width=200, height=30)
entry_username.place(relx=.1, rely=.1)

entry_password = customtkinter.CTkEntry(app, placeholder_text="database_password", width=200, height=30,show="*")
entry_password.place(relx=.1, rely=.2)

def connect_to_database():
    try:
        label1.configure(text="Connecting.....")

        p_username = entry_username.get()
        p_password = entry_password.get()
        p_dns = "192.168.96.128/orcl"
        p_port = "1521"
        conn = oracledb.connect(user=p_username, password=p_password, dsn=p_dns, port=p_port)
        label1.configure(text="Connection successful!")

    except Exception as e:
        label1.configure(text="Invalid username or password")
        print("Error:", e)

connect_button = customtkinter.CTkButton(app, text="Connect", fg_color="green", command=connect_to_database)
connect_button.place(relx=.2, rely=.3)

label1 = customtkinter.CTkLabel(app, text="")
label1.place(relx=.2, rely=.4)

app.mainloop()

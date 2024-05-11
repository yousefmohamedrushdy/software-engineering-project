import tkinter as tk
from tkinter import ttk
import customtkinter

def select(conn):
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("600x400")
    app.title('SELECT OPERATION')

    label = customtkinter.CTkLabel(app, text_color="#1E90FF", text="SELECT OPERATION")
    label.place(relx=0.5, rely=0.1, anchor="center")
  
    def get_table_names(conn):
        c = conn.cursor()
        c.execute("SELECT table_name FROM user_tables")
        tables = c.fetchall()
        return [table[0] for table in tables]

    def fetch_table_data(conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        cursor.close()
        return data

    table_names = get_table_names(conn)
    my_option = customtkinter.CTkOptionMenu(app, values=table_names)
    my_option.place(relx=0.1, rely=0.2)

    tree = ttk.Treeview(app, columns=("column1", "column2", "column3"), show='headings')
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Column 1")
    tree.heading("#3", text="Column 2")
    tree.place(relx=0.1, rely=0.3)

    def select():
        table_name = my_option.get()
        data = fetch_table_data(conn, table_name)
        if data:
            # Clearing existing data
            tree.delete(*tree.get_children())
            for row in data:
                tree.insert("", "end", values=row)

    select_button = customtkinter.CTkButton(app, text_color="#F0EAD6", text='SELECT', command=select, fg_color="#AB4B52")
    select_button.place(relx=0.5, rely=0.2)

    app.mainloop()

# Example of usage
# select(conn)

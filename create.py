


import customtkinter
import tkinter

def creat_t(conn):
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("500x500")
    app.title('create tables')


    label = customtkinter.CTkLabel(app, text_color="#BF00FF", text="TABLE CREATION",)
    label.place(relx=0.5, rely=0.1, anchor="center")

    entry_table_name = customtkinter.CTkEntry(app, placeholder_text="TABLE NAME", width=190)
    entry_table_name.place(relx=0.1, rely=0.2)

    entry_column1 = customtkinter.CTkEntry(app, placeholder_text="column1", width=190)
    entry_column1.place(relx=0.1, rely=0.3)
    radio_var_col1 = tkinter.StringVar(value="")
    col1_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                    text="varchar2(50)",
                                                    variable=radio_var_col1,
                                                    value="varchar2(50)")
    col1_rd_varchar50.place(relx=0.5, rely=0.3)

    col1_rd_int = customtkinter.CTkRadioButton(app,
                                            text="number",
                                            variable=radio_var_col1,
                                            value="number")
    col1_rd_int.place(relx=0.7, rely=0.3)

    entry_column2 = customtkinter.CTkEntry(app, placeholder_text="column2", width=190)
    entry_column2.place(relx=0.1, rely=0.4)

    radio_var_col2 = tkinter.StringVar(value="")
    col2_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                    text="varchar2(50)",
                                                    variable=radio_var_col2,
                                                    value="varchar2(50)")
    col2_rd_varchar50.place(relx=0.5, rely=0.4)

    col2_rd_int = customtkinter.CTkRadioButton(app,
                                            text="number",
                                            variable=radio_var_col2,
                                            value="number")
    col2_rd_int.place(relx=0.7, rely=0.4)

    entry_column3 = customtkinter.CTkEntry(app, placeholder_text="column3", width=190)
    entry_column3.place(relx=0.1, rely=0.5)

    radio_var_col3 = tkinter.StringVar(value="")
    col3_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                    text="varchar2(50)",
                                                    variable=radio_var_col3,
                                                    value="varchar2(50)")
    col3_rd_varchar50.place(relx=0.5, rely=0.5)

    col3_rd_int = customtkinter.CTkRadioButton(app,
                                            text="number",
                                            variable=radio_var_col3,
                                            value="number")
    col3_rd_int.place(relx=0.7, rely=0.5)
    label1 = customtkinter.CTkLabel(app, text="",text_color='red')
    label1.place(relx=.5, rely=.7, anchor="center")
    def create_db():
        table_name = entry_table_name.get()
        column1_name = entry_column1.get()
        column1_type = radio_var_col1.get()
        column2_name = entry_column2.get()
        column2_type = radio_var_col2.get()
        column3_name = entry_column3.get()
        column3_type = radio_var_col3.get()

        c = conn.cursor()
        try:
            c.execute(f'''CREATE TABLE {table_name} 
                    ({column1_name} {column1_type}, 
                    {column2_name} {column2_type}, 
                    {column3_name} {column3_type})''')

            conn.commit()
            conn.close()
            label1.configure(text="creation successful!")

        except:
               label1.configure(text="creation failed")

            
        
    create_button = customtkinter.CTkButton(app, text_color="#36454F", text='CREATE', command=create_db, fg_color="#FFB200")
    create_button.place(relx=0.1, rely=0.6)

    app.mainloop()

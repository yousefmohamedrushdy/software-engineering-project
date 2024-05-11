import customtkinter


def insert_db(conn):
  customtkinter.set_appearance_mode("system")
  customtkinter.set_default_color_theme("blue")
  app = customtkinter.CTk()
  app.geometry("500x500")
  app.title('INSERT OPERATION')

  label = customtkinter.CTkLabel(app, text_color="#BF00FF", text="INSERT")
  label.place(relx=0.5, rely=0.1, anchor="center")
  def get_table_names(conn):
    c = conn.cursor()

    c.execute("SELECT table_name FROM user_tables")
    tables = c.fetchall()
    
    return [table[0] for table in tables]

  table_names = get_table_names(conn)

  my_option = customtkinter.CTkOptionMenu(app, values=table_names,)
  my_option.place(relx=0.1, rely=0.2)
  table_names = my_option.get()
  
  entry_id = customtkinter.CTkEntry(app, placeholder_text="id", width=190)
  entry_id.place(relx=0.1, rely=0.3)

  entry_col1 = customtkinter.CTkEntry(app, placeholder_text="name", width=190)
  entry_col1.place(relx=0.1, rely=0.4)

  entry_col2 = customtkinter.CTkEntry(app, placeholder_text="age", width=190)
  entry_col2.place(relx=0.1, rely=0.5)

  def insert_data():
      table_name=my_option.get()
      id = entry_id.get()
      col1= entry_col1.get()
      col2 = entry_col2.get()

      c = conn.cursor()
      try:
        c.execute(f"INSERT INTO {table_name} (ID, NAME, AGE) VALUES ({id}, '{col1}', {col2})")

        conn.commit()
        conn.close()
        label_result.configure(text="insert sucess")

      except :
        label_result.configure(text="arledy exist")

  insert_button = customtkinter.CTkButton(app, text_color="#36454F", text='INSERT', command=insert_data, fg_color="#FFB200")
  insert_button.place(relx=0.1, rely=0.6)

  label_result = customtkinter.CTkLabel(app, text_color="#BF00FF", text="",)
  label_result.place(relx=0.5, rely=0.8, anchor="center")

  app.mainloop()

import customtkinter

def update_dp(conn):
  customtkinter.set_appearance_mode("system")
  customtkinter.set_default_color_theme("blue")
  app = customtkinter.CTk()
  app.geometry("500x500")
  app.title('UPDATE OPERATION')

  label = customtkinter.CTkLabel(app, text_color="#1E90FF", text="UPDATE OPERATION")
  label.place(relx=0.5, rely=0.1, anchor="center")

  def get_table_names(conn):
    c = conn.cursor()

    c.execute("SELECT table_name FROM user_tables")
    tables = c.fetchall()
    
    return [table[0] for table in tables]

  table_names = get_table_names(conn)
  my_option = customtkinter.CTkOptionMenu(app, values=table_names,)
  my_option.place(relx=0.1, rely=0.2)

  entry_id = customtkinter.CTkEntry(app, placeholder_text="id", width=190)
  entry_id.place(relx=0.1, rely=0.3)

  entry_name= customtkinter.CTkEntry(app, placeholder_text="name", width=190)
  entry_name.place(relx=0.1, rely=0.4)

  entry_age = customtkinter.CTkEntry(app, placeholder_text="age", width=190)
  entry_age.place(relx=0.1, rely=0.5)
  
  label_result = customtkinter.CTkLabel(app, text_color="#BF00FF", text="",)
  label_result.place(relx=0.1, rely=0.6)
  def update():
      table_name =my_option.get()
      id = entry_id.get()
      name = entry_name.get()
      age = entry_age.get()
      cursor = conn.cursor()
      try :
        query = f"UPDATE {table_name} SET name = {name}, age = '{age}' WHERE id = '{id}'"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        label_result.configure(text="updated sucssfully")

      except: 
                label_result.configure(text="invaild id")


  create_button = customtkinter.CTkButton(app, text_color="#FFBF00", text='UPDATE', command=update, fg_color="#79443B")
  create_button.place(relx=0.1, rely=0.6)
  
  app.mainloop()

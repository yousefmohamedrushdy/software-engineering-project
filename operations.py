import customtkinter
from create import creat_t
from insert import insert_db
from delete import delete
from update import update_dp
from select_dp import select
def opreation_form(conn):
  customtkinter.set_appearance_mode("dark")
  customtkinter.set_default_color_theme("blue")
  app = customtkinter.CTk()
  app.geometry("500x500")
  app.title('Operations')
  def click_create():
    creat_t(conn)

  def click_insert():
      insert_db(conn)
  def click_delet():
      delete(conn)
  def click_updata():
      update_dp(conn)
  def click_select():
      select(conn)
  create_button = customtkinter.CTkButton(app, text_color="#EED9C4",text='Create New Table', command=click_create)
  create_button.place(relx=0.5, rely=0.2, anchor="center",)


  insert_button = customtkinter.CTkButton(app, text_color="black",text='Insert', command=click_insert)
  insert_button.place(relx=0.5, rely=0.3, anchor="center")


  update_button = customtkinter.CTkButton(app,text_color="orange", text='Update', command=click_updata)
  update_button.place(relx=0.5, rely=0.5, anchor="center")


  delete_button = customtkinter.CTkButton(app,text_color="#EED9C4", text='Delete', command=click_delet)
  delete_button.place(relx=0.5, rely=0.4,anchor="center")



  label = customtkinter.CTkLabel(app, text_color="#EED9C4",text="chose an operation to do on database",)
  label.place(relx=0.5, rely=0.1, anchor="center")
  select_button = customtkinter.CTkButton(app,text_color="#EED9C4", text='SELECT', command=click_select)
  select_button.place(relx=0.5, rely=0.6,anchor="center")


  app.mainloop()
  
  

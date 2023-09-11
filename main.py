import tkinter.messagebox
from tkinter import *
import random
import pandas as pd
import subprocess


#Alphabet List, Character List, Number List
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7,","8","9","0"]
special_char = ["!","@","#","$","%","^","&","*","(",")"]
dict = {"Websites":[],"Passwords":[]}
file_path = ("passwords.txt")
password = []
#Password Generator Function
def password_generate():
    global password_button
    website = input.get()
    if len(website) == 0:
        input.insert(0,"Error, Enter Website")
        input.after(3000, lambda: input.delete(0,END))
    else:
        print(website)
        initial_password = []
        global password
        password2 = []
        for _ in range(0, 8):
            letter = random.choice(alphabet)
            initial_password.append(letter)
        for _ in range(0, 4):
            num = random.choice(numbers)
            initial_password.append(num)
        for _ in range(0, 4):
            char = random.choice(special_char)
            initial_password.append(char)
        for _ in range(0, 16):
            char = random.choice(initial_password)
            password2.append(char)
            initial_password.remove(char)

        for _ in range(0, 16):
            char = random.choice(password2)
            password.append(char)
            password2.remove(char)

        seperator = " "
        password = seperator.join(password)
        password = password.replace(" ", "")
        password_output.delete(0,END)
        password_output.insert(0,password)

        password_button.destroy()
        save_button = Button(text="Save", command=save, bg="#27005D", highlightbackground="#27005D")
        save_button.place(x=210,y=265)

def save():
    global password
    global password_button
    dict["Passwords"].append(password)
    password = []
    website = input.get()
    dict["Websites"].append(website)
    input.delete(0, END)
    df = pd.DataFrame(dict)
    df.to_csv("passwords.txt", mode="a", index=False, header=False)
    tkinter.messagebox.showinfo(Title=None, message="Your information has been succesfully saved")
    save_button.destroy()
    password_button = Button(text="Generate", width=5, command=password_generate, highlightbackground="#27005D" )
    password_output.delete(0,END)
    password_button.place(x=205, y=265)



def open_file():
    try:
        subprocess.run(['open',file_path],check=True)
    except subprocess.CalledProcessError:
        print("Failed to open file")






#Create GUI
window = Tk()
window.config()
window.minsize(500,350)
window.maxsize(500,350)
window.title("Password Generator")
window.config(bg="#27005D")
window.resizable(False,False)



#Title
title = Label(text="Password Generator",font=("Georgia",24,"bold"),bg="#27005D", fg="#AED2FF")
title.grid(column=1,row=0,pady=50,padx=(115,0))
#Website input field
website_text = Label(text="Enter the Website",bg="#27005D", fg="#AED2FF")
website_text.grid(column=1,row=1,padx=(115,0))

input = Entry(justify=CENTER,bg="#27005D", fg="#AED2FF")
input.grid(column=1,row=2,padx=(115,0))

#Generate Password button
password_text = Label(text="Password Output",bg="#27005D", fg="#AED2FF")
password_text.grid(column=1,row=3,pady=(30,0),padx=(115,0))

password_button = Button(text="Generate",width=5,command=password_generate,bg="#27005D", highlightbackground="#27005D")
password_button.place(x=205,y=265)


password_output = Entry(justify=CENTER,bg="#27005D", fg="#AED2FF")
password_output.insert(0,"Password")
password_output.grid(column=1,row=4,padx=(115,0))

version = Label(text="Version Alpha 0.4",bg="#27005D", fg="#AED2FF")
version.place(x=385,y=325)

dev_note = Label(text="Dev Note: Fix password list format",bg="#27005D", fg="#AED2FF")
dev_note.place(x=0,y=325)

open_button = Button(text="Password List", command=open_file,bg="#27005D", highlightbackground="#27005D")
open_button.place(x=0,y=0)

save_button = Button(text= "Save", command=save,bg="#27005D",highlightbackground="#27005D")




window.mainloop()
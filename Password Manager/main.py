import json
import random
from tkinter import *
from tkinter import messagebox
import os
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)
    password_list=[]
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)#listeye ekledigimiz karakterleri karistyirdik

    pasword=""
    password=pasword.join(password_list)#listeyi stringe cevirdik
    content=password_entry.get()
    if content=="":
        password_entry.insert(0,password)#password entry mizin 0.indeksinden baslayip icine olusturdugumuz paswordu yazicak
    else:
        password_entry.delete(0,END)
        password_entry.insert(0,password)

def save():
    website=website_entry.get()
    email=username_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json","r") as datafile:
                data=json.load(datafile)

        except FileNotFoundError:
            with open("data.json","w") as datafile:
                json.dump(new_data,datafile,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w")as datafile:
                json.dump(data,datafile,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():

    website=website_entry.get()
    try:
        with open("data.json") as datafile:

            if os.path.getsize("data.json") > 0: #dosya ici bos mu degil mi diye baktik
                data=json.load(datafile)
            else:
                messagebox.showinfo(title="Error", message="Empty File")

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")

    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"{website}\nEmail:{email}\nPassword:{password}")

        else:
            messagebox.showinfo(title="Not Saving Data",message=f"{website} Unsaved")
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,background="white")

canvas=Canvas(width=300,height=300,highlightthickness=0)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(150,150,image=lock_image)
canvas.grid(column=1,row=0)
canvas.config(background="white")

#labels
website=Label(text="Website:",background="white",fg="red",font=("Arial",12,"bold"))
username=Label(text="Username/Email:",background="white",fg="red",font=("Arial",12,"bold"))
password=Label(text="Password:",background="white",fg="red",font=("Arial",12,"bold"))
website.grid(row=1,column=0)
username.grid(row=2,column=0)
password.grid(row=3,column=0)

#enries
website_entry=Entry(width=21,fg="red",font=("Arial",12))
username_entry=Entry(width=35,fg="red",font=("Arial",12))
password_entry=Entry(width=21,fg="red",font=("Arial",12))
website_entry.focus()
website_entry.grid(row=1,column=1,sticky="we")
username_entry.grid(row=2,column=1,sticky="we",columnspan=3)
password_entry.grid(row=3,column=1,sticky="we")

#buttons
search_button=Button(text="Search",width=14,background="red",fg="white",highlightthickness=2,bd=3,relief="groove",command=find_password)
password_generate_button=Button(text="Password",width=14,background="red",fg="white",command=generate_password,highlightthickness=2,bd=3,relief="groove")
search_button.grid(row=1,column=2)
password_generate_button.grid(row=3,column=2)
add_button=Button(text="Add", width=14,background="red",fg="white",command=save)
add_button.grid(row=5, column=1, pady=10,sticky='we')  # Örneğin alt düğmeye biraz daha fazla dolgu ekledik
add_button.config(highlightthickness=2,bd=10,relief="groove")



window.mainloop()

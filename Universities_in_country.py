from tkinter.constants import BOTH, END, RIGHT, Y
import requests
import tkinter as tk
from tkinter import ttk
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
response = []


def clear():
    mylist.delete(0, 'end')
    university.config(text="")
    for i in range(len(textfield.get())):
        textfield.delete(0, last=None)


def Go_to_University_website(canvas):
    college = mylist.curselection()
    college_id = college[0]
    url = response[college_id]["web_pages"][0]
    webbrowser.get(chrome_path).open(url)


def getWeather(canvas):
    country = textfield.get()
    clear()
    global response
    api = "	http://universities.hipolabs.com/search?country=" + country
    response = requests.get(api).json()

    total_university = len(response)
    university.config(text="Total number of Universities / Colleges: " + str(total_university))
    for i in range(len(response)):
        data = response[i]["name"]
        mylist.insert(END, data)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("University List app")
icon = tk.PhotoImage(file='static/mortarboard.png')

# Setting icon of master window
canvas.iconphoto(False, icon)
detail_font = ("Times", 15, "bold")
font = ("Times", 20, "bold")

label = tk.Label(canvas, font=detail_font)
label.config(text="Enter country name: ")
label.pack(pady=15)
textfield = tk.Entry(canvas, justify='center', fg='green', font=font)
textfield.pack()
textfield.focus()
textfield.bind('<Return>', getWeather)

university = tk.Label(canvas, font=detail_font)
university.pack()

button = tk.Button(canvas, text="Clear", command=clear)
button.place(x=500, y=59)

sb = tk.Scrollbar(canvas)
sb.pack(side=RIGHT, fill=BOTH)

mylist = tk.Listbox(canvas, bg="lightblue", width=15, yscrollcommand=sb.set)

mylist.pack(padx=80, pady=20, fill=BOTH, expand=True)
mylist.bind('<Double-1>', Go_to_University_website)
sb.config(command=mylist.yview)

canvas.mainloop()
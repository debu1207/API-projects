from tkinter.constants import BOTH, BOTTOM, CENTER, END, LEFT, RIGHT, Y
import requests
import time
import tkinter as tk
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
    print(college_id)
    url = response[college_id]["web_pages"][0]
    webbrowser.get(chrome_path).open(url)


def getWeather(canvas):
    country = textfield.get()
    clear()
    global response
    api = "	http://universities.hipolabs.com/search?country=" + country
    response = requests.get(api).json()
    print(type(response))
    total_university = len(response)
    university.config(text="Total number of Universities / Colleges: " + str(total_university))
    for i in range(len(response)):
        data = response[i]["name"]
        mylist.insert(END, data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("University List app")

detail_font = ("poppins", 10, "bold")
font = ("poppins", 20, "bold")

label = tk.Label(canvas, font=detail_font)
label.config(text="Enter country name: ")
label.pack(pady=20)
textfield = tk.Entry(canvas, justify='center', fg='blue', font=font)
textfield.pack()
textfield.focus()
textfield.bind('<Return>', getWeather)

university = tk.Label(canvas, font=detail_font)
university.pack()

button = tk.Button(canvas, text="clear", command=clear)
button.place(x=500, y=65)

sb = tk.Scrollbar(canvas)
sb.pack(side=RIGHT, fill=BOTH)

mylist = tk.Listbox(canvas, bg="lightblue", width=15, yscrollcommand=sb.set)

mylist.pack(padx=80, pady=20, fill=BOTH, expand=True)
mylist.bind('<Double-1>', Go_to_University_website)
sb.config(command=mylist.yview)

canvas.mainloop()
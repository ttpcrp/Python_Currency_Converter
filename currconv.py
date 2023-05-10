import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import json

root = tk.Tk()

root.geometry('400x400')
root.title('Currency Converter')
root.resizable(False, False)

def currconvert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    curr1 = combo1.get()
    curr2 = combo2.get()
    amount = value.get()

    querystring = {"from":curr1,"to":curr2,"amount":amount}

    headers = {
        "X-RapidAPI-Key": "5edf344e87mshd8fb06d5a7986cap178654jsnebd988df4e66",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)
    convert_amount = data["result"]["convertedAmount"]

    result['text'] = convert_amount

top = Frame(root, width=400, height=60, bg="#FF700D")
top.grid(row=0, column=0)

icon = tk.PhotoImage(file='D:\Python\Python Project\Final Project\pic\exchange.png')

app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", padx=20, pady=3, anchor=CENTER, font=('Comic Sans MS', 20), bg="#FF700D")
app_name.place(x=0, y=0)

main = Frame(root, width=400, height=360, bg="#6CF8FF")
main.grid(row=1, column=0)

result = Label(main, text=" ", anchor=CENTER, font=('Comic Sans MS', 20), width=20, height=2, fg="black", relief="solid")
result.place(x=40, y=10)

currcode = []
with open('D:\Python\Python Project\Final Project\\currcode.json') as json_file:
    data = json.load(json_file)
    for key in data:
        currcode += [key['symbol']]

_from = Label(main, text="From", anchor=NW, font=('Comic Sans MS', 16), width=8, height=1, bg="#6CF8FF", fg="black", relief="flat")
_from.place(x=40, y=100)
combo1 = ttk.Combobox(main, width=9, justify=CENTER, font=('Comic Sans MS', 16))
combo1['value'] = (currcode)
combo1.place(x=40, y=140)

to = Label(main, text="To", anchor=NW, font=('Comic Sans MS', 16), width=8, height=1, bg="#6CF8FF", fg="black", relief="flat")
to.place(x=220, y=100)
combo2 = ttk.Combobox(main, width=9, justify=CENTER, font=('Comic Sans MS', 16))
combo2['value'] = (currcode)
combo2.place(x=230, y=140)

amount = Label(main, text="Amount", anchor=NW, font=('Comic Sans MS', 16), width=8, height=1, bg="#6CF8FF", fg="black", relief="flat")
amount.place(x=40, y=180)
value = ttk.Entry(main, width=25, justify=CENTER, font=('Comic Sans MS', 16))
value.place(x=40, y=220)

button = Button(main, text="Convert", width=20, height=1, font=('Comic Sans MS', 16), bg="#FF700D", foreground="black", command=currconvert)
button.place(x=70, y=270)

root.mainloop()
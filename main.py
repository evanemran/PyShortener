import pyshorteners
import pyperclip
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL SHORTENER")
root.configure(bg='#49A')
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_add = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_add)

def copyurl():
    url_add = url_address.get()
    pyperclip.copy(url_add)

Label(root, text="URL SHORTENER", font="calibri 20 bold").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root, text="Generate Short Url", command=urlshortener).pack(pady=7)
Entry(root, textvariable = url_address).pack(pady=5)
Button(root, text="Copy",command=copyurl).pack()

root.mainloop()
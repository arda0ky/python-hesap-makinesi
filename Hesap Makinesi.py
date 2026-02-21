from tkinter import *
from tkinter import font

islemYazi = ""
sonuc_gosterildi = False

gecmis1 = ""
gecmis2 = ""
gecmis3 = ""
gecmis4 = ""
gecmis5 = ""
birinci = ""
ikinci = ""
islemdeg = ""
sonuc = ""

tk = Tk()
tk.title("Hesap Makinesi")
tk.geometry("300x550")

def command1():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"1")

def command2():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"2")

def command3():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"3")

def command4():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"4")

def command5():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"5")

def command6():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"6")

def command7():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"7")

def command8():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"8")

def command9():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"9")

def command0():
    global islemYazi, sonuc_gosterildi
    if sonuc_gosterildi:
        islem.config(text="")
        sonuc_gosterildi = False
    islemYazi = islem.cget("text")
    islem.config(text=islemYazi+"0")

def commandesit():
    global islemYazi, gecmis1, gecmis2, gecmis3, gecmis4, gecmis5, sonuc, sonuc_gosterildi

    islemYazi = islem.cget("text")

    if islemYazi != "":
        try:
            hesap = islemYazi.replace("x", "*")

            sonuc = str(eval(hesap))

            gecmis5 = gecmis4
            gecmis4 = gecmis3
            gecmis3 = gecmis2
            gecmis2 = gecmis1
            gecmis1 = islemYazi + " = " + sonuc

            gecmis.config(text="·" + gecmis1 + "\n·" + gecmis2 + "\n·" + gecmis3 + "\n·" + gecmis4 + "\n·" + gecmis5)

            islem.config(text=sonuc)
            sonuc_gosterildi = True

        except:
            islem.config(text="Hata")
            sonuc_gosterildi = True

def commandtop():
    global islemYazi, sonuc_gosterildi
    sonuc_gosterildi = False
    islemYazi = islem.cget("text")

    if any(harf in islemYazi[-2:] for harf in "+-x/"):
        islemYazi = islemYazi[:-3]

    if islemYazi != "":
        islem.config(text=islemYazi + " + ")

def commandcik():
    global islemYazi, sonuc_gosterildi
    sonuc_gosterildi = False
    islemYazi = islem.cget("text")

    if any(harf in islemYazi[-2:] for harf in "+-x/"):
        islemYazi = islemYazi[:-3]

    if islemYazi != "":
        islem.config(text=islemYazi + " - ")

def commandcarp():
    global islemYazi, sonuc_gosterildi
    sonuc_gosterildi = False
    islemYazi = islem.cget("text")

    if any(harf in islemYazi[-2:] for harf in "+-x/"):
        islemYazi = islemYazi[:-3]

    if islemYazi != "":
        islem.config(text=islemYazi + " x ")

def commandbol():
    global islemYazi, sonuc_gosterildi
    sonuc_gosterildi = False
    islemYazi = islem.cget("text")

    if any(harf in islemYazi[-2:] for harf in "+-x/"):
        islemYazi = islemYazi[:-3]

    if islemYazi != "":
        islem.config(text=islemYazi + " / ")

def commandsil():
    global sonuc_gosterildi
    islem.config(text="")
    sonuc_gosterildi = False

buyukfont = font.Font(size=20)

islem = Label(tk, text="", width=20, font=buyukfont, anchor="w")
islem.pack(fill="x")

cizgi = Label(tk, text="_________________________________________________________")
cizgi.pack()

gecmisYazi = Label(tk, text="GEÇMİŞ", font=font.Font(size=15))
gecmisYazi.pack()

cizgi1 = Label(tk, text="_________________________________________________________")
cizgi1.pack()

gecmis = Label(tk, text="·" + gecmis1 + "\n·" + gecmis2 + "\n·" + gecmis3 + "\n·" + gecmis4 + "\n·" + gecmis5, anchor="w", justify="left")
gecmis.pack(fill="x")

cizgi2 = Label(tk, text="_________________________________________________________")
cizgi2.pack()

button1 = Button(tk, text="1", padx="10", pady="6", command=command1, font=buyukfont)
button1.place(x=10, y=380)

button2 = Button(tk, text="2", padx="10", pady="6", command=command2, font=buyukfont)
button2.place(x=80, y=380)

button3 = Button(tk, text="3", padx="10", pady="6", command=command3, font=buyukfont)
button3.place(x=150, y=380)

button4 = Button(tk, text="4", padx="10", pady="6", command=command4, font=buyukfont)
button4.place(x=10, y=300)

button5 = Button(tk, text="5", padx="10", pady="6", command=command5, font=buyukfont)
button5.place(x=80, y=300)

button6 = Button(tk, text="6", padx="10", pady="6", command=command6, font=buyukfont)
button6.place(x=150, y=300)

button7 = Button(tk, text="7", padx="10", pady="6", command=command7, font=buyukfont)
button7.place(x=10, y=220)

button8 = Button(tk, text="8", padx="10", pady="6", command=command8, font=buyukfont)
button8.place(x=80, y=220)

button9 = Button(tk, text="9", padx="10", pady="6", command=command9, font=buyukfont)
button9.place(x=150, y=220)

button0 = Button(tk, text="0", padx="10", pady="6", command=command0, font=buyukfont)
button0.place(x=80, y=460)

buttonesit = Button(tk, text="=", padx="10", pady="6", command=commandesit, font=buyukfont)
buttonesit.place(x=150, y=460)

buttontop = Button(tk, text="+", padx="10", pady="6", command=commandtop, font=buyukfont)
buttontop.place(x=220, y=300)

buttoncik = Button(tk, text="-", padx="14", pady="6", command=commandcik, font=buyukfont)
buttoncik.place(x=220, y=220)

buttoncarp = Button(tk, text="x", padx="12", pady="6", command=commandcarp, font=buyukfont)
buttoncarp.place(x=220, y=380)

buttonbol = Button(tk, text="/", padx="14", pady="6", command=commandbol, font=buyukfont)
buttonbol.place(x=220, y=460)

buttonsil = Button(tk, text="C", padx="14", pady="15", command=commandsil, font=font.Font(size=15))
buttonsil.place(x=10, y=460)

tk.mainloop()
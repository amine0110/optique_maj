from tkinter import *
from PIL import Image
from PIL import ImageTk

bg='#00CC99'
app = Tk()
app.geometry('700x500')
app.title('Optique')
app.configure(bg=bg)

def taille_objet():
    taille_image = taille_box.get()
    focale_cal = focale_box.get()
    bague_allonge = bague_box.get()
    taille_obj = 0

    if taille_image and focale_cal and bague_allonge:
        taille_obj = float(focale_cal) * float(taille_image) / float(bague_allonge)
    return taille_obj

def distance_lent_planImage():
    taille_image = taille_box.get()
    focale_cal = focale_box.get()
    bague_allonge = bague_box.get()
    taille_obj = taille_objet()
    p_prime = 0
    if taille_image and focale_cal and bague_allonge:
        agrr = float(taille_image) / taille_obj

        p_prime = (agrr + 1) * float(focale_cal)
    return p_prime

def distance_lent_obj():
    taille_image = taille_box.get()
    taille_obj = taille_objet()
    p_prime = distance_lent_planImage()
    p = 0
    if taille_image:
        agrr = float(taille_image) / taille_obj
        p = p_prime/agrr
    return p

def distance_obj_CCD():
    p = distance_lent_obj()
    p_prime = distance_lent_planImage()
    return p + p_prime

def hyperfocale():
    focale_cal = focale_box.get()
    ouver_num = ouver_box.get()
    cercle_moindre = cercle_box.get()
    h = 0
    if focale_cal and ouver_num and cercle_moindre:
        h = float(focale_cal)**2 / (float(ouver_num) * float(cercle_moindre))
    return h

def d_1():
    p = distance_lent_obj()
    focale_cal = focale_box.get()
    h = hyperfocale()
    d1 = 0
    if focale_cal:
        d1 = (h*p)/(h+(p-float(focale_cal)))
    return d1

def d_2():
    p = distance_lent_obj()
    focale_cal = focale_box.get()
    h = hyperfocale()
    d2 = 0
    if focale_cal:
        d2 = (h*p)/(h-(p-float(focale_cal)))
    return d2

def prof_champ():
    d1 = d_1()
    d2 = d_2()
    return d2 - d1

def affiche():
    taille_obj = taille_objet()
    dist_obj_ccd = distance_obj_CCD()
    p = distance_lent_obj()
    p_prime = distance_lent_planImage()
    pr_champ = prof_champ()

    affiche1 = "La taille de l'objet est: " + str(taille_obj) + " mm"
    affiche2 = "la distance entre l'objet et le capteur CCD: " + str(dist_obj_ccd) + " mm"
    affiche3 = "La distance entre la lentille et l'objet: " + str(p) + " mm"
    affiche4 = "La distance entre la lentille et le plan image: " + str(p_prime) + " mm"
    affiche5 = "La profondeur de champ: " + str(pr_champ) + " mm"

    for item in fra3.winfo_children():
        item.destroy()

    lab1 = Label(fra3, text=affiche1, bg=bg, font='agencyFB 10 bold')
    lab2 = Label(fra3, text=affiche2, bg=bg, font='agencyFB 10 bold')
    lab3 = Label(fra3, text=affiche3, bg=bg, font='agencyFB 10 bold')
    lab4 = Label(fra3, text=affiche4, bg=bg, font='agencyFB 10 bold')
    lab5 = Label(fra3, text=affiche5, bg=bg, font='agencyFB 10 bold')

    lab1.grid()
    lab2.grid()
    lab3.grid()
    lab4.grid()
    lab5.grid()

def clear():
    for item in fra3.winfo_children():
        item.destroy()
    focale_box.delete(0, END)
    bague_box.delete(0, END)
    taille_box.delete(0, END)



image = Image.open('Distance_focale.png')
image = image.resize((650,200), Image.ANTIALIAS)
image_printed = ImageTk.PhotoImage(image=image)

lab = Label(app, image=image_printed)
lab.pack()

fra = Frame(app, bg=bg)
fra.pack(pady=(20,0))

focale = Label(fra, text='Focale', bg=bg, font='agencyFB 10 bold')
focale.grid(row=0, column=0)
focale_box = Entry(fra, w=10, font='agencyFB 10')
focale_box.grid(row=0, column=1)

bague = Label(fra, text='Bague Allonge', bg=bg, font='agencyFB 10 bold')
bague.grid(row=0, column=2, padx=(20,0))
bague_box = Entry(fra, w=10, font='agencyFB 10')
bague_box.grid(row=0, column=3)

taille = Label(fra, text='Taille_CCD', bg=bg, font='agencyFB 10 bold')
taille.grid(row=0, column=4, padx=(20,0))
taille_box = Entry(fra, w=10, font='agencyFB 10')
taille_box.grid(row=0, column=5)

ouvert_num = Label(fra, text='Ouverture numérique', bg=bg, font='agencyFB 10 bold')
ouvert_num.grid(row=1, column=0, padx=(20,0), pady=(10,0))
ouver_box = Entry(fra, w=10, font='agencyFB 10')
ouver_box.grid(row=1, column=1, pady=(10,0))

cercle = Label(fra, text='Cercle de moindre confusion', bg=bg, font='agencyFB 10 bold')
cercle.grid(row=1, column=2, padx=(20,0), pady=(10,0))
cercle_box = Entry(fra, w=10, font='agencyFB 10')
cercle_box.grid(row=1, column=3, pady=(10,0))

fra2 = Frame(app, bg=bg)
fra2.pack(pady=(20,0))

calculer = Button(fra2, text='Calculer', width=30, command=affiche)
calculer.grid()

clear = Button(fra2, text='Clear', width=30, command=clear)
clear.grid(pady=(10,0))

fra3 = Frame(app, bg=bg)
fra3.pack(pady=(10,0))








app.mainloop()
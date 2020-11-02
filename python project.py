# Bitwise OPeration program


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Bitwise operation')
f = tk.Canvas(root, height=1920, width=1080, bg='pink')


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((1210, 1000))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


image = Image.open('image.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=photo)
label.bind('<Configure>', resize_image)
label.pack()  # fill=BOTH, expand = YES
L1 = tk.Label(text="Enter Number 1:", font=("Arial", 14, "bold"), fg='white', bg='gray13')
E1 = tk.Entry(root, width=10, fg='black', font=("Arial", 14))
L2 = tk.Label(text="Enter Number 2:", font=("Arial", 14, "bold"), fg='white', bg='gray13')
E2 = tk.Entry(root, width=10, fg='black', font=("Arial", 14))
lbls = tk.Label(text="Bitwise Operations", font=("Arial", 17, "bold"), fg='white', bg='black').place(x=500, y=10)
Btn = tk.Button(root, text="EXIT", bg='paleturquoise1', activebackground='turquoise1', command=root.destroy, height=2,
                font=('ComicSansMS', 10, 'bold'), width=17)
Btn.place(x=300, y=600)

var = tk.IntVar()


# for new window to open

def opennewwindow():
    def conver(a):
        le = tk.Label(newwindow, text='', font=('Arial', 14, "bold"), fg='white', bg='black', width=300).place(x=500,
                                                                                                               y=560)
        b = a[::-1]
        s = 0
        j = 0
        for i in b:
            s += int(i) * pow(2, j)
            j += 1
        op = "Decimal equivalent of " + a + " is " + str(s)
        le = tk.Label(newwindow, text=op, font=('Arial', 14, "bold"), fg='white', bg='black').place(x=500, y=560)

    newwindow = tk.Toplevel(root)
    newwindow.title("Explanation")
    c = tk.Canvas(newwindow, height=800, width=1200, bg='tomato2')
    c.propagate(0)
    c.pack()
    load = Image.open("br (1).png")
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = tk.Label(c, image=render)
    img.image = render
    img.place(x=0, y=0)
    num1 = int(E1.get())
    num2 = int(E2.get())

    x = var.get()
    a = num1
    ab = num2

    # To convert decimal value to binary

    s = ' '
    while (a > 0):
        rem = a % 2
        a = a // 2
        s += str(rem)
    sn = s[::-1]
    g = ' '
    while (ab > 0):
        rem = ab % 2
        ab = ab // 2
        g += str(rem)
    gn = g[::-1]
    if (len(s) != len(g)):
        if (len(s) > len(g)):
            diff = len(s) - len(g)
            for i in range(diff):
                g += '0'
        else:
            diff = len(g) - len(s)
            for i in range(diff):
                s += '0'
    s = s[::-1]
    g = g[::-1]
    h = ''
    for i in range(len(g) - 1):
        if (s[i] == '1' and g[i] == '1'):
            h += '1'
        else:
            h += '0'
    ANDOperation = h
    h = ''
    for i in range(len(g) - 1):
        if (s[i] == '1' or g[i] == '1'):
            h += '1'
        else:
            h += '0'
    OROperation = h

    h = ''
    for i in range(len(g) - 1):
        if (s[i] == g[i]):
            h += '0'
        else:
            h += '1'
    XOROperation = h
    snot = ''
    for i in range(len(sn) - 1):
        if (sn[i] == '1'):
            snot += '0'
        else:
            snot += '1'
    gnot = ''
    for i in range(len(gn) - 1):
        if (gn[i] == '1'):
            gnot += '0'
        else:
            gnot += '1'
    t1 = "➤ Decimal Equivalent of " + str(num1) + " : " + s
    t2 = "➤ Decimal Equivalent of " + str(num2) + " : " + g

    p1 = tk.Label(newwindow, text=t1, fg='white', font=('MSSerif', 14, ''), bg='black').place(x=50, y=250)
    p2 = tk.Label(newwindow, text=t2, fg='white', font=('MSSerif', 14, ''), bg='black').place(x=50, y=300)

    # These labels are for displaying the truth table of the corresponding gate selected

    if x == 1:
        txt = s + " . " + g + " = " + ANDOperation
        y1 = "'AND' gate"
        sym = "➤ Symbol : A . B"
        lod = Image.open("And.PNG")
        conver(ANDOperation)
    elif x == 2:
        txt = s + " + " + g + " = " + OROperation
        y1 = "'OR' gate"
        sym = "➤ Symbol : A + B"
        lod = Image.open("OR.PNG")
        conver(OROperation)
    elif x == 3:
        txt = "~ " + s + " = " + snot + " and  ~ " + g + " = " + gnot
        y1 = "'NOT' gate"
        sym = "➤ Symbol : ~ A"
        lod = Image.open("NOT.PNG")
        conver(snot)
        conver(gnot)
    else:
        txt = s + "  ⊕ " + g + " = " + XOROperation
        y1 = "'XOR' gate"
        sym = "➤ Symbol : A ⊕ B"
        lod = Image.open("XOR.PNG")
        conver(XOROperation)

    r = ImageTk.PhotoImage(lod)
    ex = "➤ Start Solving from the last bit "
    ex1 = "according to the table."
    lab = tk.Label(newwindow, text=ex, fg='white', font=('MSSerif', 14, ''), bg='black').place(x=50, y=400)
    lab1 = tk.Label(newwindow, text=ex1, fg='white', font=('MSSerif', 14, ''), bg='black').place(x=56, y=430)
    lab2 = tk.Label(newwindow, text="EXPLANATION", fg='white', font=('MSSerif', 20, 'bold'), bg='black').place(x=280,
                                                                                                               y=100)
    # labels can be text or images
    img = tk.Label(c, image=r)
    img.image = r
    img.place(x=390, y=270)

    o = tk.Label(newwindow, text=y1, fg='white', font=('MSSerif', 14, ''), bg='black').place(x=440, y=190)
    la = tk.Label(newwindow, text=txt, fg='white', font=('MSSerif', 18, ''), bg='black').place(x=100, y=550)

    p4 = tk.Label(newwindow, text=sym, fg='white', font=('MSSerif', 14, ''), bg='black').place(x=50, y=350)
    B2 = tk.Button(newwindow, text="EXIT", bg='paleturquoise1', activebackground='turquoise1',
                   command=newwindow.destroy, height=2, font=('ComicSansMS', 10, 'bold'), width=17)
    B2.place(x=300, y=600)

    # To let the user now which gate they have selected


def dis():
    lb = tk.Label(text="", fg="gold", bg='gray13', font=('Times', 14, 'bold italic')).place(x=100, y=500, width=350,
                                                                                            height=30)
    x = var.get()
    s = ''
    if (x == 1):
        s += 'You selected AND operation'
    elif (x == 2):
        s += 'You selected OR operation'
    elif (x == 3):
        s += 'You selected NOT operation'
    else:
        s += 'You selected XOR operation'
    lbl = tk.Label(text=s, font=('MSSerif', 14, ''), fg='gold', bg='gray13').place(x=200, y=500)

    # For the main root window


def display():
    lbl = tk.Label(text="", fg="gold", bg='gray13', font=('Times', 14, 'bold italic')).place(x=100, y=550, width=700,
                                                                                             height=30)
    num1 = int(E1.get())
    num2 = int(E2.get())
    x = var.get()
    a = num1
    ab = num2
    s = ' '
    while (a > 0):
        rem = a % 2
        a = a // 2
        s += str(rem)
    sn = s[::-1]
    g = ' '
    while (ab > 0):
        rem = ab % 2
        ab = ab // 2
        g += str(rem)
    gn = g[::-1]
    if (len(s) != len(g)):
        if (len(s) > len(g)):
            diff = len(s) - len(g)
            for i in range(diff):
                g += '0'
        else:
            diff = len(g) - len(s)
            for i in range(diff):
                s += '0'
    s = s[::-1]
    g = g[::-1]
    h = ''
    for i in range(len(g) - 1):
        if (s[i] == '1' and g[i] == '1'):
            h += '1'
        else:
            h += '0'
    ANDOperation = h
    h = ''
    for i in range(len(g) - 1):
        if (s[i] == '1' or g[i] == '1'):
            h += '1'
        else:
            h += '0'
    OROperation = h

    h = ''
    for i in range(len(g) - 1):
        if (s[i] == g[i]):
            h += '0'
        else:
            h += '1'
    XOROperation = h
    snot = ''
    for i in range(len(sn) - 1):
        if (sn[i] == '1'):
            snot += '0'
        else:
            snot += '1'
    gnot = ''
    for i in range(len(gn) - 1):
        if (gn[i] == '1'):
            gnot += '0'
        else:
            gnot += '1'
    if x == 1:
        txt = "AND Operation Of " + str(num1) + " and " + str(num2) + " is " + ANDOperation

    elif x == 2:
        txt = "OR Operation of " + str(num1) + " and " + str(num2) + " is " + OROperation
    elif x == 3:
        txt = "NOT operation on " + str(num1) + " is " + snot + " and on " + str(num2) + " is " + gnot
    else:
        txt = "XOR operation on  " + str(num1) + " and " + str(num2) + " is " + XOROperation
    la = tk.Label(text=txt, font=('MSSerif', 14, ''), fg='gold', bg='gray13').place(x=200, y=550)

    # To dsplay the radio buttons


R1 = tk.Radiobutton(root, text="AND", variable=var, command=dis, fg="lime", selectcolor="gray10", bg='gray13', value=1,
                    font=("Arial", 14), activebackground='gray13')

R2 = tk.Radiobutton(root, text="OR", variable=var, command=dis, fg="lime", bg='gray13', value=2, selectcolor='gray10',
                    font=("Arial", 14), activebackground='gray13')

R3 = tk.Radiobutton(root, text="NOT", variable=var, command=dis, fg="lime", bg='gray13', value=3, selectcolor='gray10',
                    font=("Arial", 14), activebackground='gray13')

R4 = tk.Radiobutton(root, text="XOR", variable=var, command=dis, fg='lime', bg="gray13", value=4, selectcolor='gray10',
                    font=("Arial", 14), activebackground='gray13')

B1 = tk.Button(root, text="RESULT", bg='paleturquoise1', activebackground='turquoise1', font=('Verdana', 10, 'bold'),
               height=2, width=15, command=display)
B2 = tk.Button(root, text="EXPLANATION", bg='paleturquoise1', activebackground='turquoise1', command=opennewwindow,
               height=2, font=('ComicSansMS', 10, 'bold'), width=17)

# To position all the labels, radiobuttons and buttons.

L1.place(x=100, y=150)
E1.place(x=260, y=150)
L2.place(x=500, y=150)
E2.place(x=660, y=150)
R1.place(x=100, y=250)
R2.place(x=200, y=250)
R3.place(x=100, y=350)
R4.place(x=200, y=350)
B1.place(x=450, y=250)
B2.place(x=450, y=350)
E1.bind('<Return>', display)
E2.bind('<Return>', display)

f.propagate(0)
f.pack()
root.mainloop()
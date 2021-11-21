from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("IMAGE VIEWER")
root.geometry("645x520")


def fowd(img_num):

    global l1
    global bb
    global bf

    l1.grid_forget()
    l1 = Label(image=img_lst[img_num - 1])
    l1.grid(row=0, column=0, columnspan=3)

    bb = Button(root, text="<<", command=lambda: bak(img_num - 1))
    bb.grid(row=1, column=0)

    if (img_num == 4):
        bf = Button(root, text=">>", state=DISABLED)
        bf.grid(row=1, column=2)

        bb = Button(root, text="<<", command=lambda: bak(2))
        bb.grid(row=1, column=0)

    else:
        bf = Button(root, text=">>", command=lambda: fowd(img_num + 1))
        bf.grid(row=1, column=2)


def bak(img_num):

    global l1
    global bb
    global bf

    l1.grid_forget()
    l1 = Label(image=img_lst[img_num])
    l1.grid(row=0, column=0, columnspan=3)

    bf = Button(root, text=">>", command=lambda: fowd(img_num + 2))
    bf.grid(row=1, column=2)

    if (img_num == 0):
        bb = Button(root, text="<<", state=DISABLED)
        bb.grid(row=1, column=0)

    else:
        bb = Button(root, text="<<", command=lambda: bak(img_num - 1))
        bb.grid(row=1, column=0)


img1 = ImageTk.PhotoImage(Image.open("k1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("k2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("k3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("k4.jpg"))


img_lst = [img1, img2, img3, img4]

l1 = Label(image=img1)
bb = Button(root, text="<<", state=DISABLED)
be = Button(root, text="EXIT", command=root.quit)
bf = Button(root, text=">>", command=lambda: fowd(2))

l1.grid(row=0, column=0, columnspan=3)
bb.grid(row=1, column=0)
be.grid(row=1, column=1)
bf.grid(row=1, column=2)


root.mainloop()

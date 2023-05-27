from tkinter import*
root=Tk()

root.title("dictionary")
root.geometry("400x400")
root.configure(background="green")

mutable_label=Label(root,fg="pink")
mutable_label.place(relx=0.5,rely=0.3,anchor=CENTER)

immutable_label=Label(root,fg="orange")
immutable_label.place(relx=0.5,rely=0.6,anchor=CENTER)

tkinter_label=Label(root,fg="brown")
tkinter_label.place(relx=0.5,rely=0.9,anchor=CENTER)

means={
       "mutable":"Values that can be changed just like lists",
       "immutable":"Values that cannot be changed just like tuple",
       "tkinter":"It is a GUI library of python"
       }

def mutable():
    mutable_label["text"]=means["mutable"]
    
btn_mu=Button(root,text="Meaning of mutable",bg="yellow",command=mutable)
btn_mu.place(relx=0.5,rely=0.2,anchor=CENTER)

def immutable():
    immutable_label["text"]=means["immutable"]
    
btn_im=Button(root,text="Meaning of immutable",bg="lightblue",command=immutable)
btn_im.place(relx=0.5,rely=0.5,anchor=CENTER)

def tkinter():
    tkinter_label["text"]=means["tkinter"]

btn_tk=Button(root,text="Meaning of tkinter",bg="purple",command=tkinter)
btn_tk.place(relx=0.5,rely=0.8,anchor=CENTER)





root.mainloop()


from tkinter import *

def clicou_botao():
    print(btn)

app = Tk()

btn = Button(app,text="Clique",command=clicou_botao,name='leel')
btn.pack()



app.mainloop()
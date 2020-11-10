import tkinter as tk
from PIL import Image ,ImageTk
HEIGHT = 700
WIDTH = 700
screen = tk.Tk()
screen.title('Income tax Calculation in India')
screen.iconbitmap(r'web.ico')

def test(entry1,entry2):
    income = int(entry1)
    age = int(entry2)
    tax = 0
    cess = 0
    if age <= 18:
        y="your age is less than 18 so you are not eligible to pay tax \n"
        text.insert(tk.END, y)

    elif age <= 60:
        if income <= 250000:
            tax = 0
        elif income <= 500000:
            tax = (income - 250000) * 0.05
        elif income <= 1000000:
            tax = 12500 + (income - 500000) * 0.2
        else:
            tax = 12500 + 100000 + (income - 1000000) * 0.3
        z= "your age is more than 18 \n"
        text.insert(tk.END, z)

    elif age <= 80:
        if income <= 300000:
            tax = 0
        elif income <= 500000:
            tax = (income - 300000) * 0.05
        elif income <= 1000000:
            tax = 10000 + (income - 500000) * 0.2
        else:
            tax = 10000 + 100000 + (income - 1000000) * 0.3
        b= "your age is more than 60 and you are senior citizen \n"
        text.insert(tk.END, b)
    else:
        if income <= 500000:
            tax = 0
        elif income <= 1000000:
            tax = (income - 500000) * 0.2

        else:
            tax = 100000 + (income - 1000000) * 0.3
        a="your age is more than 80 and you are super senior citizen \n"
        text.insert(tk.END, a)

    cess = tax * .04
    ttax = tax + cess
    l="your income tax = "+str(tax)+"\n"
    m="your health and education tax = "+str(cess)+"\n"
    n="your total tax to be paid = "+str(ttax)+"\n"
    text.insert(tk.END, l)
    text.insert(tk.END, m)
    text.insert(tk.END, n)






canvas = tk.Canvas(screen,height=HEIGHT,width=WIDTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("incttt.jpg"))
panel = tk.Label(canvas, image = img)
panel.place(x=0,y=0,relwidth=1,relheight=1)

frame = tk.Frame(screen,bg='#659EC7',bd=5)
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.10)

frame2 = tk.Frame(screen,bg='#659EC7',bd=5)
frame2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.10)


entry1 = tk.Entry(frame,fg='#e2440f',font=('Courier',18))
entry1.place(relx=0,rely=0,relwidth=0.40,relheight=1)
entry1.insert(0, 'income:')


entry2 = tk.Entry(frame2,fg='#e2440f',font=('Courier',18))
entry2.place(relx=0,rely=0,relwidth=0.40,relheight=1)
entry2.insert(0, 'age:')



button = tk.Button(frame2,text= "Calculate",bg ='#33EEFF',font=('Courier',10),fg='#ea1253',command=lambda:test(entry1.get(),entry2.get()))
button.place(relx=0.75,rely=0,relwidth=0.25,relheight=1)



lower_frame = tk.Frame(screen,bg='#659EC7',bd=5)
lower_frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.60)



text = tk.Text(screen,width=20,height=10,padx=10,pady=10,bg ='#659EC7',font=('Courier',18),wrap=tk.WORD)
text.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.60)



screen.mainloop()
